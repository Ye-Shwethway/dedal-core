
const VERSION = "0.1.0";
const REDIRECT_URI = "https://youtube.drthorne.uk/oauth/google/callback";
const GOOGLE_SCOPES = [
  "https://www.googleapis.com/auth/youtube.upload",
  "https://www.googleapis.com/auth/youtube",
  "https://www.googleapis.com/auth/yt-analytics.readonly",
];

export default {
  async fetch(request, env, ctx) {
    const requestId = crypto.randomUUID();
    try {
      return await route(request, env, requestId);
    } catch (error) {
      const status = Number.isInteger(error?.status) ? error.status : 500;
      const code = error?.code || "internal_error";
      console.error(JSON.stringify({ requestId, event: "request_error", status, code }));
      return reply({ error: code, request_id: requestId }, status);
    }
  },
};

async function route(request, env, requestId) {
  const url = new URL(request.url);
  const path = url.pathname.replace(/\/+$/, "") || "/";
  if (request.method === "GET" && path === "/health") {
    return reply({
      status: "ok",
      service: "dedal-youtube-gateway",
      version: VERSION,
      configured: Boolean(env.DB && env.GOOGLE_CLIENT_ID && env.GOOGLE_CLIENT_SECRET &&
        env.TOKEN_ENCRYPTION_KEY_B64 && env.ADMIN_API_TOKEN && env.RUNNER_API_TOKEN),
    });
  }

  if (request.method === "POST" && path === "/v1/channels") {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin");
    const body = await bodyJson(request);
    const alias = validAlias(body.alias);
    const channelId = validChannelId(body.channel_id);
    const now = isoNow();
    const existing = await env.DB.prepare(
      "SELECT alias, channel_id, credential_ref FROM channel_profiles WHERE alias = ?"
    ).bind(alias).first();
    if (existing && existing.channel_id !== channelId) {
      throw httpError(409, "alias_identity_locked", "Alias already belongs to a different channel_id.");
    }
    if (existing) {
      return reply({ alias, channel_id: channelId, connected: Boolean(existing.credential_ref), unchanged: true });
    }
    await env.DB.prepare(
      "INSERT INTO channel_profiles(alias,channel_id,display_name,default_privacy,enabled,credential_ref,created_at,updated_at) VALUES(?,?,?,?,0,NULL,?,?)"
    ).bind(alias, channelId, null, "private", now, now).run();
    await audit(env, "admin", "channel_profile.create_expected", alias, channelId, null, "success", {});
    return reply({ alias, channel_id: channelId, connected: false, enabled: false }, 201);
  }

  if (request.method === "GET" && path === "/v1/channels") {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin");
    const rows = await env.DB.prepare(
      "SELECT alias,channel_id,display_name,default_privacy,enabled,credential_ref IS NOT NULL AS connected,created_at,updated_at FROM channel_profiles ORDER BY alias"
    ).all();
    return reply({ channels: rows.results || [] });
  }

  const channelMatch = path.match(/^\/v1\/channels\/([^/]+)$/);
  if (request.method === "GET" && channelMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin");
    const alias = validAlias(decodeURIComponent(channelMatch[1]));
    const row = await env.DB.prepare(
      "SELECT alias,channel_id,display_name,default_privacy,enabled,credential_ref IS NOT NULL AS connected,created_at,updated_at FROM channel_profiles WHERE alias=?"
    ).bind(alias).first();
    if (!row) throw httpError(404, "profile_not_found");
    return reply({ channel: row });
  }

  const ticketMatch = path.match(/^\/v1\/channels\/([^/]+)\/connect-ticket$/);
  if (request.method === "POST" && ticketMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin");
    requireCryptoConfig(env);
    const alias = validAlias(decodeURIComponent(ticketMatch[1]));
    const profile = await getProfile(env, alias);
    const ticket = randomToken(32);
    const ticketHash = await sha256(ticket);
    const now = new Date();
    const expires = new Date(now.getTime() + 30 * 60 * 1000).toISOString();
    await env.DB.prepare(
      "INSERT INTO connect_tickets(ticket_hash,profile_alias,expires_at,consumed_at,created_at) VALUES(?,?,?,NULL,?)"
    ).bind(ticketHash, alias, expires, now.toISOString()).run();
    return reply({
      alias,
      expected_channel_id: profile.channel_id,
      connect_url: `https://youtube.drthorne.uk/oauth/connect/${encodeURIComponent(alias)}?ticket=${encodeURIComponent(ticket)}`,
      expires_at: expires,
    }, 201);
  }

  const connectMatch = path.match(/^\/oauth\/connect\/([^/]+)$/);
  if (request.method === "GET" && connectMatch) {
    requireOAuthConfig(env);
    const alias = validAlias(decodeURIComponent(connectMatch[1]));
    const ticket = url.searchParams.get("ticket") || "";
    if (!ticket) throw httpError(401, "connect_ticket_required");
    const ticketHash = await sha256(ticket);
    const row = await env.DB.prepare(
      "SELECT profile_alias,expires_at,consumed_at FROM connect_tickets WHERE ticket_hash=?"
    ).bind(ticketHash).first();
    if (!row || row.profile_alias !== alias || row.expires_at <= isoNow()) {
      throw httpError(401, "invalid_or_expired_connect_ticket");
    }

    // The ticket is time-bounded but intentionally reusable. Link previewers and
    // browser prefetchers may issue a GET before the Creator opens the page.
    // The OAuth state remains browser-bound, short-lived, and single-use.
    const profile = await getProfile(env, alias);
    const state = randomToken(32);
    const browser = randomToken(32);
    const verifier = randomToken(64);
    const challenge = base64url(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(verifier)));
    const stateHash = await sha256(state);
    const browserHash = await sha256(browser);
    const sealed = await seal(env, verifier, `oauth-state:${alias}`);
    const created = new Date();
    const expires = new Date(created.getTime() + 10 * 60 * 1000).toISOString();
    await env.DB.prepare(
      "INSERT INTO oauth_states(state_hash,profile_alias,browser_hash,pkce_ciphertext,pkce_iv,expires_at,consumed_at,created_at) VALUES(?,?,?,?,?,?,NULL,?)"
    ).bind(stateHash, alias, browserHash, sealed.ciphertext, sealed.iv, expires, created.toISOString()).run();

    const auth = new URL("https://accounts.google.com/o/oauth2/v2/auth");
    auth.searchParams.set("client_id", env.GOOGLE_CLIENT_ID);
    auth.searchParams.set("redirect_uri", REDIRECT_URI);
    auth.searchParams.set("response_type", "code");
    auth.searchParams.set("scope", GOOGLE_SCOPES.join(" "));
    auth.searchParams.set("access_type", "offline");
    auth.searchParams.set("prompt", "consent");
    auth.searchParams.set("include_granted_scopes", "true");
    auth.searchParams.set("state", state);
    auth.searchParams.set("code_challenge", challenge);
    auth.searchParams.set("code_challenge_method", "S256");
    const headers = new Headers({ Location: auth.toString(), "Cache-Control": "no-store" });
    headers.append("Set-Cookie", `dedal_oauth_browser=${browser}; Path=/oauth/google/callback; Secure; HttpOnly; SameSite=Lax; Max-Age=600`);
    return new Response(null, { status: 302, headers });
  }

  if (request.method === "GET" && path === "/oauth/google/callback") {
    requireOAuthConfig(env);
    if (url.searchParams.get("error")) {
      return html(`Authorization was not completed: ${escapeHtml(url.searchParams.get("error"))}`, 400);
    }
    const code = url.searchParams.get("code") || "";
    const state = url.searchParams.get("state") || "";
    const browser = cookie(request, "dedal_oauth_browser");
    if (!code || !state || !browser) throw httpError(400, "invalid_oauth_callback");
    const stateHash = await sha256(state);
    const stateRow = await env.DB.prepare(
      "SELECT * FROM oauth_states WHERE state_hash=?"
    ).bind(stateHash).first();
    if (!stateRow || stateRow.consumed_at || stateRow.expires_at <= isoNow() ||
        !(await secureEqual(stateRow.browser_hash, await sha256(browser)))) {
      throw httpError(400, "invalid_or_expired_oauth_state");
    }
    const consumed = await env.DB.prepare(
      "UPDATE oauth_states SET consumed_at=? WHERE state_hash=? AND consumed_at IS NULL AND expires_at>?"
    ).bind(isoNow(), stateHash, isoNow()).run();
    if (!consumed.meta || consumed.meta.changes !== 1) throw httpError(409, "oauth_state_already_used");

    const alias = stateRow.profile_alias;
    const verifier = await unseal(env, stateRow.pkce_ciphertext, stateRow.pkce_iv, `oauth-state:${alias}`);
    const tokenResponse = await fetch("https://oauth2.googleapis.com/token", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({
        code,
        client_id: env.GOOGLE_CLIENT_ID,
        client_secret: env.GOOGLE_CLIENT_SECRET,
        redirect_uri: REDIRECT_URI,
        grant_type: "authorization_code",
        code_verifier: verifier,
      }),
    });
    const token = await tokenResponse.json();
    if (!tokenResponse.ok || !token.access_token || !token.refresh_token) {
      await audit(env, "oauth", "channel_profile.bind", alias, null, null, "failed", { reason: "token_exchange_failed" });
      throw httpError(502, "oauth_token_exchange_failed", "Google did not return a usable refresh token.");
    }
    const identity = await youtubeIdentity(token.access_token);
    const profile = await getProfile(env, alias);
    if (identity.id !== profile.channel_id) {
      await audit(env, "oauth", "channel_profile.bind", alias, identity.id, null, "denied", {
        reason: "channel_id_mismatch", expected_channel_id: profile.channel_id,
      });
      return html(`FAIL-CLOSED: authenticated YouTube channel ID did not match the pre-registered profile. Expected ${escapeHtml(profile.channel_id)}; received ${escapeHtml(identity.id)}. No credential was stored.`, 409);
    }
    const credentialRef = `yt:${alias}`;
    const sealed = await seal(env, token.refresh_token, `credential:${alias}:${identity.id}`);
    const now = isoNow();
    await env.DB.batch([
      env.DB.prepare(
        "INSERT INTO oauth_credentials(credential_ref,profile_alias,channel_id,ciphertext,iv,scopes,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(credential_ref) DO UPDATE SET channel_id=excluded.channel_id,ciphertext=excluded.ciphertext,iv=excluded.iv,scopes=excluded.scopes,updated_at=excluded.updated_at"
      ).bind(credentialRef, alias, identity.id, sealed.ciphertext, sealed.iv, GOOGLE_SCOPES.join(" "), now, now),
      env.DB.prepare(
        "UPDATE channel_profiles SET display_name=?,enabled=1,credential_ref=?,updated_at=? WHERE alias=? AND channel_id=?"
      ).bind(identity.title, credentialRef, now, alias, identity.id),
    ]);
    await audit(env, "oauth", "channel_profile.bind", alias, identity.id, null, "success", {});
    return html(`Connected profile “${escapeHtml(alias)}” to verified YouTube channel “${escapeHtml(identity.title)}” (${escapeHtml(identity.id)}). You may close this page.`, 200);
  }

  if (request.method === "POST" && path === "/v1/upload-jobs") {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin");
    const body = await bodyJson(request);
    const alias = validAlias(body.profile_alias);
    const profile = await getConnectedProfile(env, alias);
    const sourceType = body.source_type;
    if (!["direct_url", "local_file", "google_drive"].includes(sourceType)) throw httpError(400, "invalid_source_type");
    if (typeof body.source_locator !== "string" || !body.source_locator.trim()) throw httpError(400, "source_locator_required");
    if (sourceType === "direct_url") {
      const sourceUrl = new URL(body.source_locator);
      if (!["https:", "http:"].includes(sourceUrl.protocol)) throw httpError(400, "invalid_source_url");
    }
    if (sourceType === "google_drive" && !/^[A-Za-z0-9_-]{10,100}$/.test(body.source_locator.trim())) {
      throw httpError(400, "invalid_drive_file_id");
    }
    if (typeof body.title !== "string" || !body.title.trim() || body.title.length > 100) throw httpError(400, "invalid_title");
    const privacy = body.requested_privacy || "private";
    if (!["private", "unlisted", "public"].includes(privacy)) throw httpError(400, "invalid_privacy");
    if (privacy !== "private" && body.explicit_visibility_intent !== true) throw httpError(409, "explicit_visibility_intent_required");
    if (body.publish_at && body.explicit_publication_intent !== true) throw httpError(409, "explicit_publication_intent_required");
    if (body.publish_at && privacy !== "private") throw httpError(400, "publish_at_requires_private");
    const idempotencyKey = String(body.idempotency_key || "").trim();
    if (!idempotencyKey || idempotencyKey.length > 200) throw httpError(400, "idempotency_key_required");
    const existing = await env.DB.prepare("SELECT * FROM upload_jobs WHERE idempotency_key=?").bind(idempotencyKey).first();
    if (existing) return reply({ job: publicJob(existing), deduplicated: true }, 200);
    const id = crypto.randomUUID();
    const now = isoNow();
    const tags = Array.isArray(body.tags) ? body.tags.map(String).slice(0, 50) : [];
    await env.DB.prepare(
      "INSERT INTO upload_jobs(id,idempotency_key,profile_alias,channel_id,source_type,source_locator,source_fingerprint,title,description,tags_json,category_id,made_for_kids,playlist_id,thumbnail_locator,requested_privacy,publish_at,status,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    ).bind(id,idempotencyKey,alias,profile.channel_id,sourceType,body.source_locator.trim(),body.source_fingerprint || null,
      body.title.trim(),String(body.description || ""),JSON.stringify(tags),String(body.category_id || "22"),
      body.made_for_kids === true ? 1 : 0,body.playlist_id || null,body.thumbnail_locator || null,privacy,
      body.publish_at || null,"queued",now,now).run();
    const job = await getJob(env, id);
    await audit(env, "admin", "upload_job.create", alias, profile.channel_id, id, "success", { privacy });
    return reply({ job: publicJob(job) }, 201);
  }

  const jobGet = path.match(/^\/v1\/upload-jobs\/([^/]+)$/);
  if (request.method === "GET" && jobGet) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin");
    return reply({ job: publicJob(await getJob(env, jobGet[1])) });
  }

  const claim = path.match(/^\/v1\/upload-jobs\/([^/]+)\/claim$/);
  if (request.method === "POST" && claim) {
    await requireActor(request, env.RUNNER_API_TOKEN, "runner");
    requireOAuthConfig(env);
    const body = await bodyJson(request);
    const job = await getJob(env, claim[1]);
    if (body.inspect_only === true) {
      return reply({ job: runnerJob(job), upload: null });
    }
    const contentLength = Number(body.content_length);
    const contentType = String(body.content_type || "application/octet-stream");
    if (!Number.isSafeInteger(contentLength) || contentLength <= 0) throw httpError(400, "invalid_content_length");
    if (!/^(video\/[-+.\w]+|application\/octet-stream)$/.test(contentType)) throw httpError(400, "invalid_content_type");
    if (["verified","failed","cancelled"].includes(job.status)) throw httpError(409, "job_not_claimable");
    const profile = await getConnectedProfile(env, job.profile_alias);
    if (profile.channel_id !== job.channel_id) throw httpError(409, "profile_job_channel_mismatch");

    const existingSession = await env.DB.prepare("SELECT * FROM upload_sessions WHERE job_id=?").bind(job.id).first();
    if (existingSession) {
      if (Number(existingSession.content_length) !== contentLength || existingSession.content_type !== contentType) {
        throw httpError(409, "source_shape_changed");
      }
      const sessionUrl = await unseal(env, existingSession.session_ciphertext, existingSession.session_iv, `upload-session:${job.id}:${job.channel_id}`);
      return reply({ job: runnerJob(job), upload: { session_url: sessionUrl, content_length: contentLength, content_type: contentType, resumed: true } });
    }

    const now = new Date();
    const lease = new Date(now.getTime() + 15 * 60 * 1000).toISOString();
    const claimed = await env.DB.prepare(
      "UPDATE upload_jobs SET status='claimed',claimed_at=COALESCE(claimed_at,?),lease_expires_at=?,bytes_total=?,updated_at=? WHERE id=? AND status IN ('queued','claimed','uploading')"
    ).bind(now.toISOString(), lease, contentLength, now.toISOString(), job.id).run();
    if (!claimed.meta || claimed.meta.changes !== 1) throw httpError(409, "job_claim_race");

    const accessToken = await profileAccessToken(env, profile);
    await assertChannel(accessToken, job.channel_id);
    const metadata = {
      snippet: { title: job.title, description: job.description, categoryId: job.category_id },
      status: { privacyStatus: job.requested_privacy, selfDeclaredMadeForKids: Boolean(job.made_for_kids) },
    };
    const tags = JSON.parse(job.tags_json || "[]");
    if (tags.length) metadata.snippet.tags = tags;
    if (job.publish_at) metadata.status.publishAt = job.publish_at;
    const init = await fetch("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json; charset=UTF-8",
        "X-Upload-Content-Length": String(contentLength),
        "X-Upload-Content-Type": contentType,
      },
      body: JSON.stringify(metadata),
    });
    const sessionUrl = init.headers.get("Location");
    if (!init.ok || !sessionUrl) {
      const detail = await safeGoogleError(init);
      await failJob(env, job.id, "resumable_session_init_failed");
      throw httpError(502, "resumable_session_init_failed", detail);
    }
    const sealed = await seal(env, sessionUrl, `upload-session:${job.id}:${job.channel_id}`);
    const stamp = isoNow();
    await env.DB.batch([
      env.DB.prepare(
        "INSERT INTO upload_sessions(job_id,session_ciphertext,session_iv,content_type,content_length,created_at,updated_at) VALUES(?,?,?,?,?,?,?)"
      ).bind(job.id,sealed.ciphertext,sealed.iv,contentType,contentLength,stamp,stamp),
      env.DB.prepare("UPDATE upload_jobs SET status='uploading',updated_at=? WHERE id=?").bind(stamp,job.id),
    ]);
    await audit(env, "runner", "upload_job.claim", job.profile_alias, job.channel_id, job.id, "success", {});
    return reply({ job: runnerJob(await getJob(env, job.id)), upload: { session_url: sessionUrl, content_length: contentLength, content_type: contentType, resumed: false } });
  }

  const progress = path.match(/^\/v1\/upload-jobs\/([^/]+)\/progress$/);
  if (request.method === "POST" && progress) {
    await requireActor(request, env.RUNNER_API_TOKEN, "runner");
    const body = await bodyJson(request);
    const bytes = Number(body.bytes_uploaded);
    const job = await getJob(env, progress[1]);
    if (!Number.isSafeInteger(bytes) || bytes < Number(job.bytes_uploaded) || bytes > Number(job.bytes_total || 0)) {
      throw httpError(400, "invalid_progress");
    }
    await env.DB.prepare(
      "UPDATE upload_jobs SET bytes_uploaded=?,lease_expires_at=?,updated_at=? WHERE id=? AND status='uploading'"
    ).bind(bytes,new Date(Date.now()+15*60*1000).toISOString(),isoNow(),job.id).run();
    return reply({ job_id: job.id, bytes_uploaded: bytes, bytes_total: Number(job.bytes_total) });
  }

  const complete = path.match(/^\/v1\/upload-jobs\/([^/]+)\/complete$/);
  if (request.method === "POST" && complete) {
    await requireActor(request, env.RUNNER_API_TOKEN, "runner");
    requireOAuthConfig(env);
    const body = await bodyJson(request);
    const videoId = String(body.youtube_video_id || "");
    if (!/^[A-Za-z0-9_-]{6,20}$/.test(videoId)) throw httpError(400, "invalid_video_id");
    const job = await getJob(env, complete[1]);
    if (job.youtube_video_id && job.youtube_video_id !== videoId) throw httpError(409, "video_identity_locked");
    const profile = await getConnectedProfile(env, job.profile_alias);
    if (profile.channel_id !== job.channel_id) throw httpError(409, "profile_job_channel_mismatch");
    await env.DB.prepare(
      "UPDATE upload_jobs SET status='verifying',youtube_video_id=?,updated_at=? WHERE id=? AND status IN ('uploading','verifying')"
    ).bind(videoId,isoNow(),job.id).run();
    const accessToken = await profileAccessToken(env, profile);
    await assertChannel(accessToken, job.channel_id);
    const response = await fetch(`https://www.googleapis.com/youtube/v3/videos?part=id,snippet,status,processingDetails&id=${encodeURIComponent(videoId)}`, {
      headers: { Authorization: `Bearer ${accessToken}` },
    });
    const data = await response.json();
    const remote = data.items && data.items.length === 1 ? data.items[0] : null;
    const mismatch = !response.ok || !remote || remote.snippet.channelId !== job.channel_id ||
      remote.snippet.title !== job.title || remote.status.privacyStatus !== job.requested_privacy;
    if (mismatch) {
      await failJob(env, job.id, "remote_readback_mismatch");
      await audit(env, "gateway", "upload_job.verify", job.profile_alias, job.channel_id, job.id, "failed", {
        video_id: videoId, reason: "remote_readback_mismatch",
      });
      throw httpError(409, "remote_readback_mismatch");
    }
    const stamp = isoNow();
    const summary = JSON.stringify({
      video_id: videoId,
      channel_id: remote.snippet.channelId,
      title: remote.snippet.title,
      privacy: remote.status.privacyStatus,
      upload_status: remote.status.uploadStatus || null,
      processing_status: remote.processingDetails ? remote.processingDetails.processingStatus : null,
    });
    await env.DB.prepare(
      "UPDATE upload_jobs SET status='verified',bytes_uploaded=COALESCE(bytes_total,bytes_uploaded),result_summary=?,error_summary=NULL,updated_at=?,completed_at=? WHERE id=?"
    ).bind(summary,stamp,stamp,job.id).run();
    await audit(env, "gateway", "upload_job.verify", job.profile_alias, job.channel_id, job.id, "success", { video_id: videoId });
    return reply({ job: publicJob(await getJob(env, job.id)), verified_remote: JSON.parse(summary) });
  }

  throw httpError(404, "not_found");
}

async function profileAccessToken(env, profile) {
  if (!profile.credential_ref) throw httpError(409, "profile_not_connected");
  const credential = await env.DB.prepare("SELECT * FROM oauth_credentials WHERE credential_ref=? AND profile_alias=? AND channel_id=?")
    .bind(profile.credential_ref, profile.alias, profile.channel_id).first();
  if (!credential) throw httpError(409, "credential_binding_missing");
  const refreshToken = await unseal(env, credential.ciphertext, credential.iv, `credential:${profile.alias}:${profile.channel_id}`);
  const response = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: env.GOOGLE_CLIENT_ID,
      client_secret: env.GOOGLE_CLIENT_SECRET,
      refresh_token: refreshToken,
      grant_type: "refresh_token",
    }),
  });
  const data = await response.json();
  if (!response.ok || !data.access_token) throw httpError(502, "google_token_refresh_failed");
  return data.access_token;
}

async function youtubeIdentity(accessToken) {
  const response = await fetch("https://www.googleapis.com/youtube/v3/channels?part=id,snippet&mine=true", {
    headers: { Authorization: `Bearer ${accessToken}` },
  });
  const data = await response.json();
  if (!response.ok || !data.items || data.items.length !== 1) throw httpError(409, "ambiguous_youtube_identity");
  return { id: data.items[0].id, title: data.items[0].snippet?.title || "" };
}

async function assertChannel(accessToken, expected) {
  const actual = await youtubeIdentity(accessToken);
  if (actual.id !== expected) throw httpError(409, "authenticated_channel_mismatch");
  return actual;
}

async function getProfile(env, alias) {
  const row = await env.DB.prepare("SELECT * FROM channel_profiles WHERE alias=?").bind(alias).first();
  if (!row) throw httpError(404, "profile_not_found");
  return row;
}

async function getConnectedProfile(env, alias) {
  const row = await getProfile(env, alias);
  if (!row.enabled || !row.credential_ref) throw httpError(409, "profile_not_connected");
  return row;
}

async function getJob(env, id) {
  const row = await env.DB.prepare("SELECT * FROM upload_jobs WHERE id=?").bind(id).first();
  if (!row) throw httpError(404, "job_not_found");
  return row;
}

function publicJob(job) {
  return {
    id: job.id,
    profile_alias: job.profile_alias,
    channel_id: job.channel_id,
    source_type: job.source_type,
    source_fingerprint: job.source_fingerprint,
    title: job.title,
    requested_privacy: job.requested_privacy,
    publish_at: job.publish_at,
    status: job.status,
    bytes_total: job.bytes_total == null ? null : Number(job.bytes_total),
    bytes_uploaded: Number(job.bytes_uploaded || 0),
    youtube_video_id: job.youtube_video_id,
    error_summary: job.error_summary,
    result_summary: parseJson(job.result_summary),
    created_at: job.created_at,
    updated_at: job.updated_at,
    completed_at: job.completed_at,
  };
}

function runnerJob(job) {
  return {
    ...publicJob(job),
    source: { type: job.source_type, locator: job.source_locator },
  };
}

async function failJob(env, id, summary) {
  await env.DB.prepare("UPDATE upload_jobs SET status='failed',error_summary=?,updated_at=? WHERE id=?")
    .bind(summary,isoNow(),id).run();
}

async function audit(env, actor, action, alias, channelId, jobId, outcome, details) {
  await env.DB.prepare(
    "INSERT INTO mutation_audit(id,actor_type,action,profile_alias,channel_id,job_id,outcome,details_json,created_at) VALUES(?,?,?,?,?,?,?,?,?)"
  ).bind(crypto.randomUUID(),actor,action,alias,channelId,jobId,outcome,JSON.stringify(details || {}),isoNow()).run();
}

async function requireActor(request, secret, actor) {
  if (!secret) throw httpError(503, "gateway_not_configured");
  const header = request.headers.get("Authorization") || "";
  const presented = header.startsWith("Bearer ") ? header.slice(7) : "";
  if (!presented || !(await secureEqual(presented, secret))) throw httpError(401, `${actor}_authentication_required`);
}

function requireOAuthConfig(env) {
  requireCryptoConfig(env);
  if (!env.GOOGLE_CLIENT_ID || !env.GOOGLE_CLIENT_SECRET) throw httpError(503, "oauth_not_configured");
}

function requireCryptoConfig(env) {
  if (!env.DB || !env.TOKEN_ENCRYPTION_KEY_B64) throw httpError(503, "secure_storage_not_configured");
}

async function seal(env, plaintext, aad) {
  const key = await encryptionKey(env);
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const encoded = new TextEncoder();
  const ciphertext = await crypto.subtle.encrypt({ name: "AES-GCM", iv, additionalData: encoded.encode(aad) }, key, encoded.encode(plaintext));
  return { ciphertext: base64url(ciphertext), iv: base64url(iv) };
}

async function unseal(env, ciphertext, iv, aad) {
  const key = await encryptionKey(env);
  const encoded = new TextEncoder();
  try {
    const plaintext = await crypto.subtle.decrypt(
      { name: "AES-GCM", iv: fromBase64url(iv), additionalData: encoded.encode(aad) },
      key,
      fromBase64url(ciphertext),
    );
    return new TextDecoder().decode(plaintext);
  } catch {
    throw httpError(500, "credential_decryption_failed");
  }
}

async function encryptionKey(env) {
  const raw = fromBase64url(env.TOKEN_ENCRYPTION_KEY_B64);
  if (raw.byteLength !== 32) throw httpError(503, "invalid_encryption_key");
  return crypto.subtle.importKey("raw", raw, "AES-GCM", false, ["encrypt","decrypt"]);
}

async function sha256(value) {
  return base64url(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(value)));
}

async function secureEqual(a, b) {
  const [ha,hb] = await Promise.all([sha256(String(a)),sha256(String(b))]);
  if (ha.length !== hb.length) return false;
  let diff = 0;
  for (let i=0;i<ha.length;i++) diff |= ha.charCodeAt(i) ^ hb.charCodeAt(i);
  return diff === 0;
}

function randomToken(bytes) {
  return base64url(crypto.getRandomValues(new Uint8Array(bytes)));
}

function base64url(input) {
  const bytes = input instanceof ArrayBuffer ? new Uint8Array(input) : new Uint8Array(input.buffer || input);
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replace(/\+/g,"-").replace(/\//g,"_").replace(/=+$/,"");
}

function fromBase64url(value) {
  const base = String(value).replace(/-/g,"+").replace(/_/g,"/");
  const padded = base + "=".repeat((4 - base.length % 4) % 4);
  const binary = atob(padded);
  return Uint8Array.from(binary, c => c.charCodeAt(0));
}

function validAlias(value) {
  const alias = String(value || "");
  if (!/^[a-z][a-z0-9_-]{1,31}$/.test(alias)) throw httpError(400, "invalid_alias");
  return alias;
}

function validChannelId(value) {
  const id = String(value || "");
  if (!/^UC[A-Za-z0-9_-]{20,30}$/.test(id)) throw httpError(400, "invalid_channel_id");
  return id;
}

async function bodyJson(request) {
  const length = Number(request.headers.get("Content-Length") || 0);
  if (length > 64 * 1024) throw httpError(413, "request_too_large");
  try { return await request.json(); } catch { throw httpError(400, "invalid_json"); }
}

function cookie(request, name) {
  const match = (request.headers.get("Cookie") || "").match(new RegExp("(?:^|;\\s*)" + name + "=([^;]+)"));
  return match ? match[1] : "";
}

function reply(payload, status=200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" },
  });
}

function html(message, status=200) {
  return new Response(`<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>DEDAL YouTube Gateway</title><body><main><h1>DEDAL YouTube Gateway</h1><p>${message}</p></main></body>`, {
    status,
    headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff", "Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; frame-ancestors 'none'" },
  });
}

function httpError(status, code, message) {
  const error = new Error(message || code);
  error.status = status;
  error.code = code;
  return error;
}

function safeError(error) {
  return error && error.code ? error.code : "internal_error";
}

async function safeGoogleError(response) {
  try {
    const data = await response.json();
    return data?.error?.message || `Google API HTTP ${response.status}`;
  } catch {
    return `Google API HTTP ${response.status}`;
  }
}

function isoNow() { return new Date().toISOString(); }
function parseJson(value) { try { return value ? JSON.parse(value) : null; } catch { return null; } }
function escapeHtml(value) { return String(value || "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c])); }
