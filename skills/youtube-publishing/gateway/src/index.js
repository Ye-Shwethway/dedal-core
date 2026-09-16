
const VERSION = "0.4.7";
const REDIRECT_URI = "https://youtube.drthorne.uk/oauth/google/callback";
const GOOGLE_SCOPES = [
  "https://www.googleapis.com/auth/youtube.upload",
  "https://www.googleapis.com/auth/youtube",
  "https://www.googleapis.com/auth/youtube.force-ssl",
  "https://www.googleapis.com/auth/yt-analytics.readonly",
  "https://www.googleapis.com/auth/yt-analytics-monetary.readonly",
  "https://www.googleapis.com/auth/youtube.channel-memberships.creator",
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
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const rows = await env.DB.prepare(
      "SELECT alias,channel_id,display_name,default_privacy,enabled,credential_ref IS NOT NULL AS connected,created_at,updated_at FROM channel_profiles ORDER BY alias"
    ).all();
    return reply({ channels: rows.results || [] });
  }

  const channelMatch = path.match(/^\/v1\/channels\/([^/]+)$/);
  if (request.method === "GET" && channelMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
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

  const videosMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos$/);
  if (request.method === "GET" && videosMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(videosMatch[1]));
    const { profile, accessToken } = await channelContext(env, alias);
    const maxResults = boundedInt(url.searchParams.get("max_results"), 10, 1, 50);
    const channel = await googleJson(`https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=${encodeURIComponent(profile.channel_id)}`, accessToken, "channel_content_lookup_failed");
    const uploadsId = channel.items?.[0]?.contentDetails?.relatedPlaylists?.uploads;
    if (!uploadsId) throw httpError(502, "uploads_playlist_missing");
    const items = await googleJson(`https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&playlistId=${encodeURIComponent(uploadsId)}&maxResults=${maxResults}`, accessToken, "video_list_failed");
    return reply({ profile_alias: alias, channel_id: profile.channel_id, videos: (items.items || []).map(publicPlaylistVideo) });
  }

  const videoMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos\/([^/]+)$/);
  if (request.method === "GET" && videoMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(videoMatch[1]));
    const videoId = validVideoId(decodeURIComponent(videoMatch[2]));
    const { profile, accessToken } = await channelContext(env, alias);
    return reply({ video: publicVideo(await ownedVideo(accessToken, profile.channel_id, videoId)) });
  }

  if (request.method === "PATCH" && videoMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(videoMatch[1]));
    const videoId = validVideoId(decodeURIComponent(videoMatch[2]));
    const body = await bodyJson(request);
    const { profile, accessToken } = await channelContext(env, alias);
    const current = await ownedVideo(accessToken, profile.channel_id, videoId);
    const snippet = { ...current.snippet };
    delete snippet.channelId; delete snippet.channelTitle; delete snippet.publishedAt; delete snippet.thumbnails; delete snippet.liveBroadcastContent; delete snippet.localized;
    if (body.title !== undefined) snippet.title = validTitle(body.title);
    if (body.description !== undefined) snippet.description = String(body.description).slice(0, 5000);
    if (body.tags !== undefined) snippet.tags = validTags(body.tags);
    if (body.category_id !== undefined) snippet.categoryId = validCategory(body.category_id);
    const updated = await googleJson("https://www.googleapis.com/youtube/v3/videos?part=snippet", accessToken, "video_update_failed", {
      method: "PUT", body: { id: videoId, snippet },
    });
    const verified = await verifyVideoMetadataEventually(accessToken, profile.channel_id, videoId, body);
    if (!videoMetadataMatches(verified, body)) throw httpError(409, "video_update_readback_mismatch");
    await audit(env, "admin", "video.update", alias, profile.channel_id, null, "success", { video_id: videoId, fields: Object.keys(body).filter(k => ["title","description","tags","category_id"].includes(k)) });
    return reply({ video: publicVideo(verified), google_id: updated.id || videoId });
  }


  if (request.method === "POST" && path === "/v1/media/stage") {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    if (!env.MEDIA_STAGING_URL || !env.MEDIA_STAGING_TOKEN) throw httpError(503, "media_staging_not_configured");
    const endpoint = String(env.MEDIA_STAGING_URL).replace(/\/+$/, "") + "/v1/stage";
    const upstream = await fetch(endpoint, { method: "POST", headers: { Authorization: "Bearer " + env.MEDIA_STAGING_TOKEN, "Content-Type": "application/json" }, body: JSON.stringify({ content_base64: body.content_base64, content_type: body.content_type, ttl_seconds: body.ttl_seconds }) });
    const text = await upstream.text();
    let data = {};
    try { data = text ? JSON.parse(text) : {}; } catch { data = { upstream_message: text.slice(0, 500) }; }
    if (!upstream.ok) throw httpError(upstream.status >= 400 && upstream.status < 500 ? upstream.status : 502, data.error || "media_staging_failed");
    return reply(data, upstream.status === 201 ? 201 : 200);
  }

  if (request.method === "POST" && path === "/v1/media/stage/chunk") {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    if (!env.MEDIA_STAGING_URL || !env.MEDIA_STAGING_TOKEN) throw httpError(503, "media_staging_not_configured");
    const endpoint = String(env.MEDIA_STAGING_URL).replace(/\/+$/, "") + "/v1/stage/chunk";
    const upstream = await fetch(endpoint, { method: "POST", headers: { Authorization: "Bearer " + env.MEDIA_STAGING_TOKEN, "Content-Type": "application/json" }, body: JSON.stringify({ upload_id: body.upload_id, chunk_index: body.chunk_index, chunk_base64: body.chunk_base64, content_type: body.content_type, ttl_seconds: body.ttl_seconds }) });
    const text = await upstream.text(); let data = {}; try { data = text ? JSON.parse(text) : {}; } catch { data = { upstream_message: text.slice(0, 500) }; }
    if (!upstream.ok) throw httpError(upstream.status >= 400 && upstream.status < 500 ? upstream.status : 502, data.error || "media_staging_chunk_failed");
    return reply(data, upstream.status === 201 ? 201 : 200);
  }

  if (request.method === "POST" && path === "/v1/media/stage/finalize") {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    if (!env.MEDIA_STAGING_URL || !env.MEDIA_STAGING_TOKEN) throw httpError(503, "media_staging_not_configured");
    const endpoint = String(env.MEDIA_STAGING_URL).replace(/\/+$/, "") + "/v1/stage/finalize";
    const upstream = await fetch(endpoint, { method: "POST", headers: { Authorization: "Bearer " + env.MEDIA_STAGING_TOKEN, "Content-Type": "application/json" }, body: JSON.stringify({ upload_id: body.upload_id, total_chunks: body.total_chunks }) });
    const text = await upstream.text(); let data = {}; try { data = text ? JSON.parse(text) : {}; } catch { data = { upstream_message: text.slice(0, 500) }; }
    if (!upstream.ok) throw httpError(upstream.status >= 400 && upstream.status < 500 ? upstream.status : 502, data.error || "media_staging_finalize_failed");
    return reply(data, upstream.status === 201 ? 201 : 200);
  }

  const mediaUnstageMatch = path.match(/^\/v1\/media\/stage\/([0-9a-f-]{36})$/i);
  if (request.method === "DELETE" && mediaUnstageMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    if (!env.MEDIA_STAGING_URL || !env.MEDIA_STAGING_TOKEN) throw httpError(503, "media_staging_not_configured");
    const endpoint = String(env.MEDIA_STAGING_URL).replace(/\/+$/, "") + "/v1/stage/" + encodeURIComponent(mediaUnstageMatch[1]);
    const upstream = await fetch(endpoint, { method: "DELETE", headers: { Authorization: "Bearer " + env.MEDIA_STAGING_TOKEN } });
    const text = await upstream.text();
    let data = {};
    try { data = text ? JSON.parse(text) : {}; } catch { data = { upstream_message: text.slice(0, 500) }; }
    if (!upstream.ok) throw httpError(upstream.status >= 400 && upstream.status < 500 ? upstream.status : 502, data.error || "media_unstage_failed");
    return reply(data);
  }

  const thumbnailMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos\/([^/]+)\/thumbnail$/);
  if (request.method === "POST" && thumbnailMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(thumbnailMatch[1]));
    const videoId = validVideoId(decodeURIComponent(thumbnailMatch[2]));
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    let media;
    try {
      media = await fetchExternalMedia(body.source_url, 50 * 1024 * 1024, ["image/jpeg", "image/png", "application/octet-stream"]);
    } catch (error) {
      await audit(env, "admin", "video.thumbnail_set", alias, profile.channel_id, null, "failed", { video_id: videoId, stage: "media", error_code: error?.code || "media_fetch_failed", error_status: Number.isInteger(error?.status) ? error.status : null, error_message: String(error?.message || error?.code || "media_fetch_failed").slice(0, 300) });
      throw error;
    }
    let data;
    try {
      data = await googleRawMedia("POST", "https://www.googleapis.com/upload/youtube/v3/thumbnails/set?uploadType=media&videoId=" + encodeURIComponent(videoId), accessToken, media, "thumbnail_set_failed");
    } catch (error) {
      const d = error?.diagnostic || {};
      await audit(env, "admin", "video.thumbnail_set", alias, profile.channel_id, null, "failed", { video_id: videoId, stage: "upload", error_code: error?.code || "thumbnail_set_failed", google_status: d.google_status ?? null, google_reason: d.google_reason ?? null, google_message: String(d.google_message || error?.message || "thumbnail_set_failed").slice(0, 500) });
      throw error;
    }
    await audit(env, "admin", "video.thumbnail_set", alias, profile.channel_id, null, "success", { video_id: videoId, bytes: media.bytes.byteLength, content_type: media.contentType });
    return reply({ video_id: videoId, thumbnail_set: true, thumbnails: data.items || [] });
  }

  const captionListMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos\/([^/]+)\/captions$/);
  if (request.method === "GET" && captionListMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(captionListMatch[1]));
    const videoId = validVideoId(decodeURIComponent(captionListMatch[2]));
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    const data = await googleJson("https://www.googleapis.com/youtube/v3/captions?part=id,snippet&videoId=" + encodeURIComponent(videoId), accessToken, "captions_list_failed");
    return reply({ video_id: videoId, captions: data.items || [] });
  }

  if (request.method === "POST" && captionListMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(captionListMatch[1]));
    const videoId = validVideoId(decodeURIComponent(captionListMatch[2]));
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    const language = String(body.language || "").trim();
    const name = String(body.name || "").trim();
    if (!language || !name || language.length > 150 || name.length > 150) throw httpError(400, "invalid_caption_metadata");
    let profile;
    try {
      const context = await channelContext(env, alias);
      profile = context.profile;
      await ownedVideo(context.accessToken, profile.channel_id, videoId);
      const media = await fetchExternalMedia(body.source_url, 100 * 1024 * 1024, ["text/xml", "application/octet-stream", "text/plain", "application/x-subrip", "text/vtt"]);
      const metadata = { snippet: { videoId, language, name, isDraft: body.is_draft === true } };
      const data = await googleMultipartUpload("POST", "https://www.googleapis.com/upload/youtube/v3/captions?uploadType=multipart&part=snippet", context.accessToken, metadata, media, "caption_insert_failed");
      await audit(env, "admin", "caption.insert", alias, profile.channel_id, null, "success", { video_id: videoId, caption_id: data.id || null, language });
      return reply({ video_id: videoId, caption: data });
    } catch (error) {
      const d = error?.diagnostic || {};
      await audit(env, "admin", "caption.insert", alias, profile?.channel_id || null, null, "failed", { video_id: videoId, language, error_code: error?.code || "caption_insert_failed", google_status: d.google_status || null, google_reason: d.google_reason || null, google_message: d.google_message || null, stage: d.stage || null });
      throw error;
    }
  }

  const captionItemMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos\/([^/]+)\/captions\/([^/]+)$/);
  if (request.method === "PATCH" && captionItemMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(captionItemMatch[1]));
    const videoId = validVideoId(decodeURIComponent(captionItemMatch[2]));
    const captionId = String(decodeURIComponent(captionItemMatch[3]));
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    await assertCaptionOwned(accessToken, videoId, captionId);
    const metadata = { id: captionId, snippet: {} };
    if (body.is_draft !== undefined) metadata.snippet.isDraft = body.is_draft === true;
    let data;
    if (body.source_url) {
      const media = await fetchExternalMedia(body.source_url, 100 * 1024 * 1024, ["text/xml", "application/octet-stream", "text/plain", "application/x-subrip", "text/vtt"]);
      data = await googleMultipartUpload("PUT", "https://www.googleapis.com/upload/youtube/v3/captions?uploadType=multipart&part=snippet", accessToken, metadata, media, "caption_update_failed");
    } else {
      data = await googleJson("https://www.googleapis.com/youtube/v3/captions?part=snippet", accessToken, "caption_update_failed", { method: "PUT", body: metadata });
    }
    await audit(env, "admin", "caption.update", alias, profile.channel_id, null, "success", { video_id: videoId, caption_id: captionId, replaced_file: Boolean(body.source_url), is_draft: body.is_draft === undefined ? null : body.is_draft === true });
    return reply({ video_id: videoId, caption: data });
  }

  if (request.method === "DELETE" && captionItemMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(captionItemMatch[1]));
    const videoId = validVideoId(decodeURIComponent(captionItemMatch[2]));
    const captionId = String(decodeURIComponent(captionItemMatch[3]));
    const body = await bodyJson(request);
    if (body.explicit_destructive_intent !== true) throw httpError(409, "explicit_destructive_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    await assertCaptionOwned(accessToken, videoId, captionId);
    await googleJson("https://www.googleapis.com/youtube/v3/captions?id=" + encodeURIComponent(captionId), accessToken, "caption_delete_failed", { method: "DELETE", expectEmpty: true });
    await audit(env, "admin", "caption.delete", alias, profile.channel_id, null, "success", { video_id: videoId, caption_id: captionId });
    return reply({ deleted: true, video_id: videoId, caption_id: captionId });
  }

  const captionDownloadMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos\/([^/]+)\/captions\/([^/]+)\/download$/);
  if (request.method === "GET" && captionDownloadMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(captionDownloadMatch[1]));
    const videoId = validVideoId(decodeURIComponent(captionDownloadMatch[2]));
    const captionId = String(decodeURIComponent(captionDownloadMatch[3]));
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    await assertCaptionOwned(accessToken, videoId, captionId);
    const query = new URLSearchParams();
    if (url.searchParams.get("tfmt")) query.set("tfmt", url.searchParams.get("tfmt"));
    if (url.searchParams.get("tlang")) query.set("tlang", url.searchParams.get("tlang"));
    const response = await fetch("https://www.googleapis.com/youtube/v3/captions/" + encodeURIComponent(captionId) + (query.toString() ? "?" + query.toString() : ""), { headers: { Authorization: "Bearer " + accessToken } });
    if (!response.ok) throw httpError(response.status === 404 ? 404 : 502, "caption_download_failed", await safeGoogleError(response));
    const text = await response.text();
    if (text.length > 5 * 1024 * 1024) throw httpError(413, "caption_download_too_large");
    return reply({ video_id: videoId, caption_id: captionId, format: url.searchParams.get("tfmt") || null, language: url.searchParams.get("tlang") || null, content: text });
  }

  const playlistImageMatch = path.match(/^\/v1\/channels\/([^/]+)\/playlists\/([^/]+)\/image$/);
  if (request.method === "GET" && playlistImageMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(playlistImageMatch[1]));
    const playlistId = validPlaylistId(decodeURIComponent(playlistImageMatch[2]));
    let profile;
    try {
      const context = await channelContext(env, alias);
      profile = context.profile;
      await ownedPlaylist(context.accessToken, profile.channel_id, playlistId);
      const listed = await playlistImagesList(context.accessToken, playlistId);
      await audit(env, "admin", "playlist.image_list", alias, profile.channel_id, null, "success", { playlist_id: playlistId, filter_variant: listed.filter });
      return reply({ playlist_id: playlistId, images: listed.data.items || [], filter_variant: listed.filter });
    } catch (error) {
      const d = error?.diagnostic || {};
      await audit(env, "admin", "playlist.image_list", alias, profile?.channel_id || null, null, "failed", { playlist_id: playlistId, error_code: error?.code || "playlist_images_list_failed", google_status: d.google_status || null, google_reason: d.google_reason || null, google_message: d.google_message || null });
      throw error;
    }
  }

  if (request.method === "POST" && playlistImageMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(playlistImageMatch[1]));
    const playlistId = validPlaylistId(decodeURIComponent(playlistImageMatch[2]));
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    let profile;
    let stage = "context";
    try {
      const context = await channelContext(env, alias);
      profile = context.profile;
      const accessToken = context.accessToken;
      stage = "ownership";
      await ownedPlaylist(accessToken, profile.channel_id, playlistId);
      stage = "media";
      const media = await fetchExternalMedia(body.source_url, 50 * 1024 * 1024, ["image/jpeg", "image/png"]);
      stage = "list";
      const listed = await playlistImagesList(accessToken, playlistId);
      const current = listed.data.items?.[0];
      stage = "upload";
      let data;
      let operation;
      if (current) {
        data = await managedPlaylistImageReplace(env, alias, profile, accessToken, playlistId, current, String(body.source_url || ""), media);
        operation = "replaced";
      } else {
        data = await googleMultipartUpload("POST", "https://www.googleapis.com/upload/youtube/v3/playlistImages?uploadType=multipart&part=snippet", accessToken, { snippet: { playlistId, type: "hero" } }, media, "playlist_image_set_failed");
        operation = "inserted";
      }
      stage = "readback";
      const verifiedList = await playlistImagesList(accessToken, playlistId);
      const verified = verifiedList.data.items?.[0];
      if (!verified) throw httpError(409, "playlist_image_readback_missing");
      await env.DB.prepare("INSERT INTO playlist_image_state(playlist_id,profile_alias,image_id,source_url,updated_at) VALUES(?,?,?,?,?) ON CONFLICT(playlist_id) DO UPDATE SET profile_alias=excluded.profile_alias,image_id=excluded.image_id,source_url=excluded.source_url,updated_at=excluded.updated_at").bind(playlistId, alias, verified.id || data.id || null, String(body.source_url || ""), isoNow()).run();
      await audit(env, "admin", "playlist.image_set", alias, profile.channel_id, null, "success", { playlist_id: playlistId, image_id: verified.id || data.id || null, operation, filter_variant: verifiedList.filter });
      return reply({ playlist_id: playlistId, image: verified, operation });
    } catch (error) {
      const d = error?.diagnostic || {};
      await audit(env, "admin", "playlist.image_set", alias, profile?.channel_id || null, null, "failed", { playlist_id: playlistId, stage: d.stage || stage, error_code: error?.code || "playlist_image_set_failed", google_status: d.google_status || null, google_reason: d.google_reason || null, google_message: d.google_message || null, google_location: d.google_location || null, google_location_type: d.google_location_type || null });
      throw error;
    }
  }

  if (request.method === "DELETE" && playlistImageMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(playlistImageMatch[1]));
    const playlistId = validPlaylistId(decodeURIComponent(playlistImageMatch[2]));
    const body = await bodyJson(request);
    if (body.explicit_destructive_intent !== true) throw httpError(409, "explicit_destructive_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedPlaylist(accessToken, profile.channel_id, playlistId);
    const listed = await playlistImagesList(accessToken, playlistId);
    const id = listed.data.items?.[0]?.id;
    if (!id) return reply({ playlist_id: playlistId, deleted: false, already_absent: true });
    await googleJson("https://www.googleapis.com/youtube/v3/playlistImages?id=" + encodeURIComponent(id), accessToken, "playlist_image_delete_failed", { method: "DELETE", expectEmpty: true });
    await env.DB.prepare("DELETE FROM playlist_image_state WHERE playlist_id=? AND profile_alias=?").bind(playlistId, alias).run();
    await audit(env, "admin", "playlist.image_delete", alias, profile.channel_id, null, "success", { playlist_id: playlistId, image_id: id });
    return reply({ playlist_id: playlistId, image_id: id, deleted: true });
  }

  const bannerMatch = path.match(/^\/v1\/channels\/([^/]+)\/banner$/);
  if (request.method === "POST" && bannerMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(bannerMatch[1]));
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    let profile;
    let stage = "context";
    try {
      const context = await channelContext(env, alias);
      profile = context.profile;
      const accessToken = context.accessToken;
      stage = "media";
      const media = await fetchExternalMedia(body.source_url, 6 * 1024 * 1024, ["image/jpeg", "image/png", "application/octet-stream"]);
      stage = "upload";
      const upload = await googleRawMedia("POST", "https://www.googleapis.com/upload/youtube/v3/channelBanners/insert?uploadType=media&channelId=" + encodeURIComponent(profile.channel_id), accessToken, media, "banner_upload_failed");
      if (!upload.url) throw httpError(502, "banner_url_missing");
      stage = "branding_lookup";
      const current = await googleJson("https://www.googleapis.com/youtube/v3/channels?part=brandingSettings&id=" + encodeURIComponent(profile.channel_id), accessToken, "channel_branding_lookup_failed");
      const branding = current.items?.[0]?.brandingSettings || {};
      branding.image = { ...(branding.image || {}), bannerExternalUrl: upload.url };
      stage = "apply";
      await googleJson("https://www.googleapis.com/youtube/v3/channels?part=brandingSettings", accessToken, "banner_apply_failed", { method: "PUT", body: { id: profile.channel_id, brandingSettings: branding } });
      await audit(env, "admin", "channel.banner_set", alias, profile.channel_id, null, "success", { bytes: media.bytes.byteLength });
      return reply({ channel_id: profile.channel_id, banner_set: true, banner_url: upload.url });
    } catch (error) {
      const d = error?.diagnostic || {};
      await audit(env, "admin", "channel.banner_set", alias, profile?.channel_id || null, null, "failed", { stage: d.stage || stage, error_code: error?.code || "banner_set_failed", google_status: d.google_status || null, google_reason: d.google_reason || null, google_message: d.google_message || null });
      throw error;
    }
  }

  const watermarkMatch = path.match(/^\/v1\/channels\/([^/]+)\/watermark$/);
  if (request.method === "POST" && watermarkMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(watermarkMatch[1]));
    const body = await bodyJson(request);
    if (body.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    const media = await fetchExternalMedia(body.source_url, 10 * 1024 * 1024, ["image/jpeg", "image/png", "application/octet-stream"]);
    const timingType = ["offsetFromStart", "offsetFromEnd"].includes(body.timing_type) ? body.timing_type : "offsetFromStart";
    const metadata = { timing: { type: timingType, offsetMs: Number.isSafeInteger(body.offset_ms) ? body.offset_ms : 0, durationMs: Number.isSafeInteger(body.duration_ms) ? body.duration_ms : 315360000000 }, position: { type: "corner", cornerPosition: "topRight" }, targetChannelId: profile.channel_id };
    await googleMultipartUpload("POST", "https://www.googleapis.com/upload/youtube/v3/watermarks/set?uploadType=multipart&channelId=" + encodeURIComponent(profile.channel_id), accessToken, metadata, media, "watermark_set_failed", true);
    await audit(env, "admin", "channel.watermark_set", alias, profile.channel_id, null, "success", { bytes: media.bytes.byteLength });
    return reply({ channel_id: profile.channel_id, watermark_set: true });
  }

  if (request.method === "DELETE" && watermarkMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(watermarkMatch[1]));
    const body = await bodyJson(request);
    if (body.explicit_destructive_intent !== true) throw httpError(409, "explicit_destructive_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    await googleJson("https://www.googleapis.com/youtube/v3/watermarks/unset?channelId=" + encodeURIComponent(profile.channel_id), accessToken, "watermark_unset_failed", { method: "POST", expectEmpty: true });
    await audit(env, "admin", "channel.watermark_unset", alias, profile.channel_id, null, "success", {});
    return reply({ channel_id: profile.channel_id, watermark_unset: true });
  }

  const privacyMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos\/([^/]+)\/privacy$/);
  if (request.method === "POST" && privacyMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(privacyMatch[1]));
    const videoId = validVideoId(decodeURIComponent(privacyMatch[2]));
    const body = await bodyJson(request);
    const privacy = validPrivacy(body.privacy);
    if (privacy !== "private" && body.explicit_visibility_intent !== true) throw httpError(409, "explicit_visibility_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    const current = await ownedVideo(accessToken, profile.channel_id, videoId);
    const status = writableStatus(current.status, { privacyStatus: privacy, publishAt: null });
    await googleJson("https://www.googleapis.com/youtube/v3/videos?part=status", accessToken, "video_privacy_update_failed", { method: "PUT", body: { id: videoId, status } });
    const verified = await verifyVideoStatusEventually(accessToken, profile.channel_id, videoId, status => status.privacyStatus === privacy && !status.publishAt);
    if (verified.status.privacyStatus !== privacy || verified.status.publishAt) throw httpError(409, "video_privacy_readback_mismatch");
    await audit(env, "admin", "video.set_privacy", alias, profile.channel_id, null, "success", { video_id: videoId, privacy });
    return reply({ video: publicVideo(verified) });
  }

  const scheduleMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos\/([^/]+)\/schedule$/);
  if (request.method === "POST" && scheduleMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(scheduleMatch[1]));
    const videoId = validVideoId(decodeURIComponent(scheduleMatch[2]));
    const body = await bodyJson(request);
    if (body.explicit_publication_intent !== true) throw httpError(409, "explicit_publication_intent_required");
    const publishAt = validFutureTime(body.publish_at);
    const { profile, accessToken } = await channelContext(env, alias);
    const current = await ownedVideo(accessToken, profile.channel_id, videoId);
    const status = writableStatus(current.status, { privacyStatus: "private", publishAt });
    const updated = await googleJson("https://www.googleapis.com/youtube/v3/videos?part=status", accessToken, "video_schedule_failed", { method: "PUT", body: { id: videoId, status } });
    const verified = await verifyVideoStatusEventually(accessToken, profile.channel_id, videoId, status => status.privacyStatus === "private" && status.publishAt === publishAt);
    const readbackConfirmed = verified?.status?.privacyStatus === "private" && verified?.status?.publishAt === publishAt;
    const resultVideo = readbackConfirmed ? verified : { ...current, status: { ...(current.status || {}), ...(updated.status || {}) } };
    await audit(env, "admin", "video.schedule", alias, profile.channel_id, null, "success", { video_id: videoId, publish_at: publishAt, readback_confirmed: readbackConfirmed });
    return reply({ video: publicVideo(resultVideo), verification: readbackConfirmed ? "confirmed" : "accepted_pending_readback" });
  }

  const playlistsMatch = path.match(/^\/v1\/channels\/([^/]+)\/playlists$/);
  if (request.method === "GET" && playlistsMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(playlistsMatch[1]));
    const { profile, accessToken } = await channelContext(env, alias);
    const maxResults = boundedInt(url.searchParams.get("max_results"), 25, 1, 50);
    const data = await googleJson(`https://www.googleapis.com/youtube/v3/playlists?part=id,snippet,contentDetails&mine=true&maxResults=${maxResults}`, accessToken, "playlist_list_failed");
    const playlists = (data.items || []).filter(x => x.snippet?.channelId === profile.channel_id).map(publicPlaylist);
    return reply({ profile_alias: alias, channel_id: profile.channel_id, playlists });
  }

  if (request.method === "POST" && playlistsMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(playlistsMatch[1]));
    const body = await bodyJson(request);
    const title = validTitle(body.title);
    const privacy = validPrivacy(body.privacy || "private");
    if (privacy !== "private" && body.explicit_visibility_intent !== true) throw httpError(409, "explicit_visibility_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    const created = await googleJson("https://www.googleapis.com/youtube/v3/playlists?part=snippet,status", accessToken, "playlist_create_failed", {
      method: "POST", body: { snippet: { title, description: String(body.description || "").slice(0, 5000) }, status: { privacyStatus: privacy } },
    });
    if (created.snippet?.channelId !== profile.channel_id) throw httpError(409, "playlist_create_channel_mismatch");
    await audit(env, "admin", "playlist.create", alias, profile.channel_id, null, "success", { playlist_id: created.id, privacy });
    return reply({ playlist: publicPlaylist(created) }, 201);
  }

  const playlistItemMatch = path.match(/^\/v1\/channels\/([^/]+)\/playlists\/([^/]+)\/videos\/([^/]+)$/);
  if (request.method === "POST" && playlistItemMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(playlistItemMatch[1]));
    const playlistId = validPlaylistId(decodeURIComponent(playlistItemMatch[2]));
    const videoId = validVideoId(decodeURIComponent(playlistItemMatch[3]));
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    const result = await ensurePlaylistMembership(accessToken, profile.channel_id, playlistId, videoId);
    await audit(env, "admin", "playlist.add_video", alias, profile.channel_id, null, "success", { playlist_id: playlistId, video_id: videoId, status: result.status });
    return reply({ operation: result });
  }

  if (request.method === "DELETE" && playlistItemMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(playlistItemMatch[1]));
    const playlistId = validPlaylistId(decodeURIComponent(playlistItemMatch[2]));
    const videoId = validVideoId(decodeURIComponent(playlistItemMatch[3]));
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedPlaylist(accessToken, profile.channel_id, playlistId);
    const found = await playlistMembership(accessToken, playlistId, videoId);
    if (found) await googleJson(`https://www.googleapis.com/youtube/v3/playlistItems?id=${encodeURIComponent(found.id)}`, accessToken, "playlist_remove_failed", { method: "DELETE", expectEmpty: true });
    const verified = await playlistMembership(accessToken, playlistId, videoId);
    if (verified) throw httpError(409, "playlist_remove_readback_mismatch");
    await audit(env, "admin", "playlist.remove_video", alias, profile.channel_id, null, "success", { playlist_id: playlistId, video_id: videoId, status: found ? "removed" : "already_absent" });
    return reply({ operation: { type: "playlist", playlist_id: playlistId, video_id: videoId, status: found ? "removed" : "already_absent" } });
  }

  const analyticsMatch = path.match(/^\/v1\/channels\/([^/]+)\/analytics\/summary$/);
  if (request.method === "GET" && analyticsMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(analyticsMatch[1]));
    const { profile, accessToken } = await channelContext(env, alias);
    const { startDate, endDate } = analyticsDates(url);
    const qs = new URLSearchParams({ ids: "channel==MINE", startDate, endDate, metrics: "views,estimatedMinutesWatched,averageViewDuration,subscribersGained,subscribersLost" });
    const data = await googleJson(`https://youtubeanalytics.googleapis.com/v2/reports?${qs}`, accessToken, "analytics_summary_failed");
    return reply({ profile_alias: alias, channel_id: profile.channel_id, start_date: startDate, end_date: endDate, analytics: analyticsRows(data) });
  }

  const searchTermsMatch = path.match(/^\/v1\/channels\/([^/]+)\/analytics\/search-terms$/);
  if (request.method === "GET" && searchTermsMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(searchTermsMatch[1]));
    const { profile, accessToken } = await channelContext(env, alias);
    const { startDate, endDate } = analyticsDates(url);
    const maxResults = boundedInt(url.searchParams.get("max_results"), 25, 1, 50);
    const qs = new URLSearchParams({ ids: "channel==MINE", startDate, endDate, dimensions: "insightTrafficSourceDetail", filters: "insightTrafficSourceType==YT_SEARCH", metrics: "views,estimatedMinutesWatched", sort: "-views", maxResults: String(maxResults) });
    const data = await googleJson(`https://youtubeanalytics.googleapis.com/v2/reports?${qs}`, accessToken, "analytics_search_terms_failed");
    return reply({ profile_alias: alias, channel_id: profile.channel_id, start_date: startDate, end_date: endDate, search_terms: analyticsRows(data) });
  }


  const videoTrafficMatch = path.match(/^\/v1\/channels\/([^/]+)\/analytics\/videos\/([^/]+)\/traffic-sources$/);
  if (request.method === "GET" && videoTrafficMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(videoTrafficMatch[1]));
    const videoId = validVideoId(decodeURIComponent(videoTrafficMatch[2]));
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    const { startDate, endDate } = analyticsDates(url);
    const maxResults = boundedInt(url.searchParams.get("max_results"), 25, 1, 50);
    const qs = new URLSearchParams({ ids: "channel==MINE", startDate, endDate, dimensions: "insightTrafficSourceType", filters: `video==${videoId}`, metrics: "views,estimatedMinutesWatched", sort: "-views", maxResults: String(maxResults) });
    const data = await googleJson(`https://youtubeanalytics.googleapis.com/v2/reports?${qs}`, accessToken, "analytics_video_traffic_sources_failed");
    return reply({ profile_alias: alias, channel_id: profile.channel_id, video_id: videoId, start_date: startDate, end_date: endDate, traffic_sources: analyticsRows(data) });
  }

  const videoSearchTermsMatch = path.match(/^\/v1\/channels\/([^/]+)\/analytics\/videos\/([^/]+)\/search-terms$/);
  if (request.method === "GET" && videoSearchTermsMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(videoSearchTermsMatch[1]));
    const videoId = validVideoId(decodeURIComponent(videoSearchTermsMatch[2]));
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    const { startDate, endDate } = analyticsDates(url);
    const maxResults = boundedInt(url.searchParams.get("max_results"), 25, 1, 50);
    const qs = new URLSearchParams({ ids: "channel==MINE", startDate, endDate, dimensions: "insightTrafficSourceDetail", filters: `video==${videoId};insightTrafficSourceType==YT_SEARCH`, metrics: "views,estimatedMinutesWatched", sort: "-views", maxResults: String(maxResults) });
    const data = await googleJson(`https://youtubeanalytics.googleapis.com/v2/reports?${qs}`, accessToken, "analytics_video_search_terms_failed");
    return reply({ profile_alias: alias, channel_id: profile.channel_id, video_id: videoId, start_date: startDate, end_date: endDate, search_terms: analyticsRows(data) });
  }

  const videoRetentionMatch = path.match(/^\/v1\/channels\/([^/]+)\/analytics\/videos\/([^/]+)\/retention$/);
  if (request.method === "GET" && videoRetentionMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(videoRetentionMatch[1]));
    const videoId = validVideoId(decodeURIComponent(videoRetentionMatch[2]));
    const { profile, accessToken } = await channelContext(env, alias);
    await ownedVideo(accessToken, profile.channel_id, videoId);
    const { startDate, endDate } = analyticsDates(url);
    const qs = new URLSearchParams({ ids: "channel==MINE", startDate, endDate, dimensions: "elapsedVideoTimeRatio", filters: `video==${videoId}`, metrics: "audienceWatchRatio,relativeRetentionPerformance" });
    const data = await googleJson(`https://youtubeanalytics.googleapis.com/v2/reports?${qs}`, accessToken, "analytics_video_retention_failed");
    return reply({ profile_alias: alias, channel_id: profile.channel_id, video_id: videoId, start_date: startDate, end_date: endDate, retention: analyticsRows(data) });
  }

  const videoDeleteMatch = path.match(/^\/v1\/channels\/([^/]+)\/videos\/([^/]+)\/delete$/);
  if (request.method === "POST" && videoDeleteMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(videoDeleteMatch[1]));
    const videoId = validVideoId(decodeURIComponent(videoDeleteMatch[2]));
    const body = await bodyJson(request);
    if (body.explicit_delete_intent !== true) throw httpError(409, "explicit_delete_intent_required");
    const { profile, accessToken } = await channelContext(env, alias);
    const before = await ownedVideo(accessToken, profile.channel_id, videoId);
    await googleJson(`https://www.googleapis.com/youtube/v3/videos?id=${encodeURIComponent(videoId)}`, accessToken, "video_delete_failed", { method: "DELETE", expectEmpty: true });
    await audit(env, "admin", "video.delete", alias, profile.channel_id, null, "success", { video_id: videoId, title: before.snippet?.title || null });
    return reply({ deleted: true, video_id: videoId, verification: "caller_readback_recommended" });
  }

  const dataApiMatch = path.match(/^\/v1\/channels\/([^/]+)\/data-api$/);
  if (request.method === "POST" && dataApiMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(dataApiMatch[1]));
    const body = await bodyJson(request);
    const { profile, accessToken } = await channelContext(env, alias);
    try {
      const result = await youtubeDataApi(accessToken, profile, body);
      await audit(env, "admin", "youtube.data_api", alias, profile.channel_id, null, "success", { resource: body.resource, operation: body.operation });
      return reply({ profile_alias: alias, channel_id: profile.channel_id, resource: body.resource, operation: body.operation, result });
    } catch (error) {
      const d = error?.diagnostic || {};
      await audit(env, "admin", "youtube.data_api", alias, profile.channel_id, null, "failed", { resource: body.resource, operation: body.operation, error_code: error?.code || "youtube_data_api_failed", google_status: d.google_status || null, google_reason: d.google_reason || null, google_message: d.google_message || null });
      throw error;
    }
  }

  const reportingApiMatch = path.match(/^\/v1\/channels\/([^/]+)\/reporting-api$/);
  if (request.method === "POST" && reportingApiMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(reportingApiMatch[1]));
    const body = await bodyJson(request);
    let profile;
    try {
      const context = await channelContext(env, alias);
      profile = context.profile;
      const result = await youtubeReportingApi(context.accessToken, body);
      await audit(env, "admin", "youtube.reporting_api", alias, profile.channel_id, null, "success", { resource: body.resource, operation: body.operation });
      return reply({ profile_alias: alias, channel_id: profile.channel_id, resource: body.resource, operation: body.operation, result });
    } catch (error) {
      const d = error?.diagnostic || {};
      await audit(env, "admin", "youtube.reporting_api", alias, profile?.channel_id || null, null, "failed", { resource: body.resource, operation: body.operation, error_code: error?.code || "youtube_reporting_api_failed", google_status: d.google_status || null, google_reason: d.google_reason || null, google_message: d.google_message || null });
      throw error;
    }
  }

  const analyticsApiMatch = path.match(/^\/v1\/channels\/([^/]+)\/analytics-api$/);
  if (request.method === "POST" && analyticsApiMatch) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
    const alias = validAlias(decodeURIComponent(analyticsApiMatch[1]));
    const body = await bodyJson(request);
    const { profile, accessToken } = await channelContext(env, alias);
    const result = await youtubeAnalyticsApi(accessToken, profile, body);
    await audit(env, "admin", "youtube.analytics_api", alias, profile.channel_id, null, "success", { resource: body.resource, operation: body.operation });
    return reply({ profile_alias: alias, channel_id: profile.channel_id, resource: body.resource, operation: body.operation, result });
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
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
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
    const playlistId = body.playlist_id == null ? null : String(body.playlist_id).trim();
    if (playlistId && !/^[A-Za-z0-9_-]{10,100}$/.test(playlistId)) throw httpError(400, "invalid_playlist_id");
    const idempotencyKey = String(body.idempotency_key || "").trim();
    if (!idempotencyKey || idempotencyKey.length > 200) throw httpError(400, "idempotency_key_required");
    const requestedFingerprint = body.source_fingerprint == null ? null : String(body.source_fingerprint).toLowerCase();
    if (requestedFingerprint && !/^sha256:[a-f0-9]{64}$/.test(requestedFingerprint)) throw httpError(400, "invalid_source_fingerprint");
    const existing = await env.DB.prepare("SELECT * FROM upload_jobs WHERE idempotency_key=?").bind(idempotencyKey).first();
    if (existing) {
      const sameRequest = existing.profile_alias === alias && existing.channel_id === profile.channel_id &&
        existing.source_type === sourceType && existing.source_locator === body.source_locator.trim() &&
        existing.title === body.title.trim() && existing.requested_privacy === privacy &&
        (existing.playlist_id || null) === playlistId &&
        (!requestedFingerprint || !existing.source_fingerprint || existing.source_fingerprint.toLowerCase() === requestedFingerprint);
      if (!sameRequest) throw httpError(409, "idempotency_key_manifest_mismatch");
      return reply({ job: publicJob(existing), deduplicated: true }, 200);
    }
    const id = crypto.randomUUID();
    const now = isoNow();
    const tags = Array.isArray(body.tags) ? body.tags.map(String).slice(0, 50) : [];
    await env.DB.prepare(
      "INSERT INTO upload_jobs(id,idempotency_key,profile_alias,channel_id,source_type,source_locator,source_fingerprint,title,description,tags_json,category_id,made_for_kids,playlist_id,thumbnail_locator,requested_privacy,publish_at,status,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    ).bind(id,idempotencyKey,alias,profile.channel_id,sourceType,body.source_locator.trim(),requestedFingerprint,
      body.title.trim(),String(body.description || ""),JSON.stringify(tags),String(body.category_id || "22"),
      body.made_for_kids === true ? 1 : 0,playlistId,body.thumbnail_locator || null,privacy,
      body.publish_at || null,"queued",now,now).run();
    const job = await getJob(env, id);
    await audit(env, "admin", "upload_job.create", alias, profile.channel_id, id, "success", { privacy });
    return reply({ job: publicJob(job) }, 201);
  }

  const jobGet = path.match(/^\/v1\/upload-jobs\/([^/]+)$/);
  if (request.method === "GET" && jobGet) {
    await requireActor(request, env.ADMIN_API_TOKEN, "admin", env.MCP_API_TOKEN);
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
    const sourceFingerprint = String(body.source_fingerprint || "").toLowerCase();
    if (!Number.isSafeInteger(contentLength) || contentLength <= 0) throw httpError(400, "invalid_content_length");
    if (!/^(video\/[-+.\w]+|application\/octet-stream)$/.test(contentType)) throw httpError(400, "invalid_content_type");
    if (!/^sha256:[a-f0-9]{64}$/.test(sourceFingerprint)) throw httpError(400, "invalid_source_fingerprint");
    if (job.source_fingerprint && job.source_fingerprint.toLowerCase() !== sourceFingerprint) {
      throw httpError(409, "source_fingerprint_mismatch");
    }
    if (!job.source_fingerprint) {
      await env.DB.prepare("UPDATE upload_jobs SET source_fingerprint=?,updated_at=? WHERE id=? AND source_fingerprint IS NULL")
        .bind(sourceFingerprint,isoNow(),job.id).run();
      job.source_fingerprint = sourceFingerprint;
    }
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

    let secondaryOperation = null;
    if (job.playlist_id) {
      try {
        secondaryOperation = await ensurePlaylistMembership(accessToken, job.channel_id, job.playlist_id, videoId);
        await audit(env, "gateway", "upload_job.playlist", job.profile_alias, job.channel_id, job.id, "success", secondaryOperation);
      } catch (error) {
        const code = safeError(error);
        await env.DB.prepare("UPDATE upload_jobs SET error_summary=?,updated_at=? WHERE id=?")
          .bind(code,isoNow(),job.id).run();
        await audit(env, "gateway", "upload_job.playlist", job.profile_alias, job.channel_id, job.id, "failed", {
          video_id: videoId, playlist_id: job.playlist_id, reason: code,
        });
        throw error;
      }
    }

    const stamp = isoNow();
    const summary = JSON.stringify({
      video_id: videoId,
      channel_id: remote.snippet.channelId,
      title: remote.snippet.title,
      privacy: remote.status.privacyStatus,
      upload_status: remote.status.uploadStatus || null,
      processing_status: remote.processingDetails ? remote.processingDetails.processingStatus : null,
      secondary_operation: secondaryOperation,
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

async function ensurePlaylistMembership(accessToken, expectedChannelId, playlistId, videoId) {
  const authHeaders = { Authorization: `Bearer ${accessToken}` };
  const playlistResponse = await fetch(
    `https://www.googleapis.com/youtube/v3/playlists?part=id,snippet&id=${encodeURIComponent(playlistId)}`,
    { headers: authHeaders },
  );
  const playlistData = await playlistResponse.json();
  if (!playlistResponse.ok) {
    throw httpError(502, "playlist_lookup_failed", playlistData?.error?.message || `Google API HTTP ${playlistResponse.status}`);
  }
  const playlist = playlistData.items && playlistData.items.length === 1 ? playlistData.items[0] : null;
  if (!playlist) throw httpError(409, "playlist_not_found_or_inaccessible");
  if (playlist.snippet?.channelId !== expectedChannelId) throw httpError(409, "playlist_channel_mismatch");

  const membershipUrl = `https://www.googleapis.com/youtube/v3/playlistItems?part=id,snippet&playlistId=${encodeURIComponent(playlistId)}&videoId=${encodeURIComponent(videoId)}&maxResults=50`;
  const existingResponse = await fetch(membershipUrl, { headers: authHeaders });
  const existingData = await existingResponse.json();
  if (!existingResponse.ok) {
    throw httpError(502, "playlist_membership_lookup_failed", existingData?.error?.message || `Google API HTTP ${existingResponse.status}`);
  }
  const existingMatches = (existingData.items || []).filter(item => item.snippet?.resourceId?.videoId === videoId);
  if (existingMatches.length > 1) throw httpError(409, "duplicate_playlist_membership_detected");
  const existing = existingMatches[0];
  if (existing) {
    return { type: "playlist", playlist_id: playlistId, status: "already_present", playlist_item_id: existing.id || null, membership_count: 1 };
  }

  const insertResponse = await fetch("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet", {
    method: "POST",
    headers: { ...authHeaders, "Content-Type": "application/json; charset=UTF-8" },
    body: JSON.stringify({
      snippet: {
        playlistId,
        resourceId: { kind: "youtube#video", videoId },
      },
    }),
  });
  const inserted = await insertResponse.json();
  if (!insertResponse.ok) {
    throw httpError(502, "playlist_insert_failed", inserted?.error?.message || `Google API HTTP ${insertResponse.status}`);
  }

  const verifyResponse = await fetch(membershipUrl, { headers: authHeaders });
  const verifyData = await verifyResponse.json();
  if (!verifyResponse.ok) {
    throw httpError(502, "playlist_readback_failed", verifyData?.error?.message || `Google API HTTP ${verifyResponse.status}`);
  }
  const verifiedMatches = (verifyData.items || []).filter(item => item.snippet?.resourceId?.videoId === videoId);
  if (verifiedMatches.length !== 1) throw httpError(502, "playlist_readback_mismatch");
  const verified = verifiedMatches[0];
  return {
    type: "playlist",
    playlist_id: playlistId,
    status: "inserted",
    playlist_item_id: verified.id || inserted.id || null,
    membership_count: 1,
  };
}

async function channelContext(env, alias) {
  const profile = await getConnectedProfile(env, alias);
  const accessToken = await profileAccessToken(env, profile);
  await assertChannel(accessToken, profile.channel_id);
  return { profile, accessToken };
}

async function googleMultipartUpload(method, endpoint, accessToken, metadata, media, errorCode, expectEmpty = false) {
  const boundary = "dedal-" + crypto.randomUUID();
  const enc = new TextEncoder();
  const prefix = enc.encode(`--${boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n${JSON.stringify(metadata)}\r\n--${boundary}\r\nContent-Type: ${media.contentType}\r\n\r\n`);
  const suffix = enc.encode(`\r\n--${boundary}--\r\n`);
  const body = new Uint8Array(prefix.byteLength + media.bytes.byteLength + suffix.byteLength);
  body.set(prefix, 0); body.set(new Uint8Array(media.bytes), prefix.byteLength); body.set(suffix, prefix.byteLength + media.bytes.byteLength);
  const response = await fetch(endpoint, { method, headers: { Authorization: `Bearer ${accessToken}`, "Content-Type": `multipart/related; boundary=${boundary}` }, body });
  if (expectEmpty && response.ok) return null;
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw googleHttpError(response.status, errorCode, data);
  return data;
}

async function googleRawMedia(method, endpoint, accessToken, media, errorCode) {
  const response = await fetch(endpoint, { method, headers: { Authorization: `Bearer ${accessToken}`, "Content-Type": media.contentType, "Content-Length": String(media.bytes.byteLength) }, body: media.bytes });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw googleHttpError(response.status, errorCode, data);
  return data;
}

async function googleResumableMediaUpload(method, endpoint, accessToken, metadata, media, errorCode) {
  const init = await fetch(endpoint, { method, headers: { Authorization: `Bearer ${accessToken}`, "Content-Type": "application/json; charset=UTF-8", "X-Upload-Content-Type": media.contentType, "X-Upload-Content-Length": String(media.bytes.byteLength) }, body: JSON.stringify(metadata) });
  if (!init.ok) {
    const data = await init.json().catch(() => ({}));
    const error = googleHttpError(init.status, errorCode, data);
    error.diagnostic = { ...(error.diagnostic || {}), stage: "resumable_init" };
    throw error;
  }
  const location = init.headers.get("Location");
  if (!location) {
    const error = httpError(502, errorCode, "Google resumable upload session missing Location header");
    error.diagnostic = { google_status: init.status, google_reason: "missingUploadLocation", google_message: "Google resumable upload session missing Location header", stage: "resumable_init" };
    throw error;
  }
  const locationUrl = new URL(location);
  const sessionPart = locationUrl.searchParams.get("part");
  const sessionQueryKeys = Array.from(locationUrl.searchParams.keys()).sort().join(",");
  locationUrl.searchParams.delete("part");
  const upload = await fetch(locationUrl.toString(), { method: "PUT", headers: { "Content-Type": media.contentType, "Content-Length": String(media.bytes.byteLength) }, body: media.bytes });
  const data = await upload.json().catch(() => ({}));
  if (!upload.ok) {
    const error = googleHttpError(upload.status, errorCode, data);
    error.diagnostic = { ...(error.diagnostic || {}), session_part: sessionPart, session_query_keys: sessionQueryKeys, stage: "resumable_media" };
    throw error;
  }
  return data;
}

function googleHttpError(status, errorCode, data) {
  const googleMessage = String(data?.error?.message || `Google API HTTP ${status}`).slice(0, 500);
  const googleReason = String(data?.error?.errors?.[0]?.reason || data?.error?.status || "unknown").slice(0, 120);
  const error = httpError(status === 404 ? 404 : 502, errorCode, googleMessage);
  error.diagnostic = { google_status: status, google_reason: googleReason, google_message: googleMessage, google_location: data?.error?.errors?.[0]?.location || null, google_location_type: data?.error?.errors?.[0]?.locationType || null, google_error_json: JSON.stringify(data?.error || {}).slice(0, 1000) };
  return error;
}

async function fetchExternalMedia(sourceUrl, maxBytes, allowedTypes) {
  let current;
  try { current = new URL(String(sourceUrl || "")); } catch { throw httpError(400, "invalid_media_url"); }
  for (let hop = 0; hop < 4; hop++) {
    validateExternalHttpsUrl(current);
    const response = await fetch(current.toString(), { redirect: "manual" });
    if ([301, 302, 303, 307, 308].includes(response.status)) {
      const location = response.headers.get("Location");
      if (!location) throw httpError(502, "media_redirect_invalid");
      current = new URL(location, current);
      continue;
    }
    if (!response.ok) throw httpError(502, "media_fetch_failed");
    const declared = Number(response.headers.get("Content-Length") || 0);
    if (declared && declared > maxBytes) throw httpError(413, "media_too_large");
    const contentType = String(response.headers.get("Content-Type") || "application/octet-stream").split(";")[0].trim().toLowerCase();
    if (!allowedTypes.includes(contentType)) throw httpError(415, "unsupported_media_type");
    const bytes = await response.arrayBuffer();
    if (!bytes.byteLength || bytes.byteLength > maxBytes) throw httpError(413, "media_too_large");
    return { bytes, contentType, sourceUrl: current.toString() };
  }
  throw httpError(400, "too_many_media_redirects");
}

function validateExternalHttpsUrl(url) {
  if (url.protocol !== "https:" || url.username || url.password) throw httpError(400, "invalid_media_url");
  const host = url.hostname.toLowerCase();
  const naked = host.replace(/^\[|\]$/g, "");
  if (host === "localhost" || host.endsWith(".localhost") || host.endsWith(".local") || host === "metadata.google.internal") throw httpError(400, "media_host_not_allowed");
  if (/^(?:127|10|0)\./.test(host) || /^169\.254\./.test(host) || /^192\.168\./.test(host) || /^172\.(?:1[6-9]|2\d|3[01])\./.test(host) || /^(?:fc|fd|fe80):/i.test(naked)) throw httpError(400, "media_host_not_allowed");
}

async function assertCaptionOwned(accessToken, videoId, captionId) {
  const data = await googleJson(`https://www.googleapis.com/youtube/v3/captions?part=id,snippet&videoId=${encodeURIComponent(videoId)}&id=${encodeURIComponent(captionId)}`, accessToken, "caption_lookup_failed");
  const item = data.items?.[0];
  if (!item || item.id !== captionId || item.snippet?.videoId !== videoId) throw httpError(404, "caption_not_found");
  return item;
}

async function playlistImagesList(accessToken, playlistId) {
  const attempts = [
    { filter: "playlistId", url: "https://www.googleapis.com/youtube/v3/playlistImages?part=snippet&playlistId=" + encodeURIComponent(playlistId) },
    { filter: "parent_raw", url: "https://www.googleapis.com/youtube/v3/playlistImages?part=snippet&parent=" + encodeURIComponent(playlistId) },
    { filter: "parent_resource", url: "https://www.googleapis.com/youtube/v3/playlistImages?part=snippet&parent=" + encodeURIComponent("playlists/" + playlistId) },
  ];
  let lastError;
  for (const attempt of attempts) {
    try { return { data: await googleJson(attempt.url, accessToken, "playlist_images_list_failed"), filter: attempt.filter }; }
    catch (error) { lastError = error; if (error?.diagnostic?.google_status !== 400) throw error; }
  }
  throw lastError || httpError(502, "playlist_images_list_failed");
}

async function managedPlaylistImageReplace(env, alias, profile, accessToken, playlistId, current, sourceUrl, media) {
  const managed = await env.DB.prepare("SELECT source_url FROM playlist_image_state WHERE playlist_id=? AND profile_alias=?").bind(playlistId, alias).first();
  if (!managed?.source_url) throw httpError(409, "playlist_image_replace_requires_managed_baseline");
  const oldSourceUrl = String(managed.source_url);
  const rollbackMedia = oldSourceUrl === sourceUrl ? media : await fetchExternalMedia(oldSourceUrl, 50 * 1024 * 1024, ["image/jpeg", "image/png"]);
  await googleJson("https://www.googleapis.com/youtube/v3/playlistImages?id=" + encodeURIComponent(current.id), accessToken, "playlist_image_delete_failed", { method: "DELETE", expectEmpty: true });
  const endpoint = "https://www.googleapis.com/upload/youtube/v3/playlistImages?uploadType=multipart&part=snippet";
  try {
    return await googleMultipartUpload("POST", endpoint, accessToken, { snippet: { playlistId, type: "hero" } }, media, "playlist_image_set_failed");
  } catch (insertError) {
    try {
      const restored = await googleMultipartUpload("POST", endpoint, accessToken, { snippet: { playlistId, type: "hero" } }, rollbackMedia, "playlist_image_rollback_failed");
      await audit(env, "admin", "playlist.image_rollback", alias, profile.channel_id, null, "success", { playlist_id: playlistId, image_id: restored.id || null });
    } catch (rollbackError) {
      await audit(env, "admin", "playlist.image_rollback", alias, profile.channel_id, null, "failed", { playlist_id: playlistId, error_code: rollbackError?.code || "playlist_image_rollback_failed", error_message: String(rollbackError?.message || "").slice(0, 500) });
    }
    throw insertError;
  }
}

async function googleJson(url, accessToken, errorCode, options = {}) {
  const headers = { Authorization: `Bearer ${accessToken}`, ...(options.headers || {}) };
  if (options.body !== undefined) headers["Content-Type"] = "application/json; charset=UTF-8";
  const response = await fetch(url, { method: options.method || "GET", headers, body: options.body === undefined ? undefined : JSON.stringify(options.body) });
  if (options.expectEmpty && response.ok) return null;
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw googleHttpError(response.status, errorCode, data);
  return data;
}

async function ownedVideo(accessToken, expectedChannelId, videoId) {
  const data = await googleJson(`https://www.googleapis.com/youtube/v3/videos?part=id,snippet,status,contentDetails,statistics&id=${encodeURIComponent(videoId)}`, accessToken, "video_lookup_failed");
  const video = data.items?.length === 1 ? data.items[0] : null;
  if (!video) throw httpError(404, "video_not_found");
  if (video.snippet?.channelId !== expectedChannelId) throw httpError(409, "video_channel_mismatch");
  return video;
}

async function ownedPlaylist(accessToken, expectedChannelId, playlistId) {
  const data = await googleJson(`https://www.googleapis.com/youtube/v3/playlists?part=id,snippet,status,contentDetails&id=${encodeURIComponent(playlistId)}`, accessToken, "playlist_lookup_failed");
  const playlist = data.items?.length === 1 ? data.items[0] : null;
  if (!playlist) throw httpError(404, "playlist_not_found");
  if (playlist.snippet?.channelId !== expectedChannelId) throw httpError(409, "playlist_channel_mismatch");
  return playlist;
}

async function playlistMembership(accessToken, playlistId, videoId) {
  const data = await googleJson(`https://www.googleapis.com/youtube/v3/playlistItems?part=id,snippet&playlistId=${encodeURIComponent(playlistId)}&videoId=${encodeURIComponent(videoId)}&maxResults=50`, accessToken, "playlist_membership_lookup_failed");
  return (data.items || []).find(item => item.snippet?.resourceId?.videoId === videoId) || null;
}

function publicPlaylistVideo(item) {
  return { video_id: item.contentDetails?.videoId || item.snippet?.resourceId?.videoId || null, title: item.snippet?.title || "", published_at: item.contentDetails?.videoPublishedAt || item.snippet?.publishedAt || null };
}

function publicVideo(video) {
  return {
    video_id: video.id,
    channel_id: video.snippet?.channelId || null,
    title: video.snippet?.title || "",
    description: video.snippet?.description || "",
    tags: video.snippet?.tags || [],
    category_id: video.snippet?.categoryId || null,
    published_at: video.snippet?.publishedAt || null,
    privacy: video.status?.privacyStatus || null,
    publish_at: video.status?.publishAt || null,
    made_for_kids: video.status?.madeForKids ?? video.status?.selfDeclaredMadeForKids ?? null,
    duration: video.contentDetails?.duration || null,
    statistics: video.statistics || {},
  };
}

function publicPlaylist(playlist) {
  return { playlist_id: playlist.id, channel_id: playlist.snippet?.channelId || null, title: playlist.snippet?.title || "", description: playlist.snippet?.description || "", privacy: playlist.status?.privacyStatus || null, item_count: Number(playlist.contentDetails?.itemCount || 0) };
}

function videoMetadataMatches(video, body) {
  const snippet = video?.snippet || {};
  if (body.title !== undefined && snippet.title !== validTitle(body.title)) return false;
  if (body.description !== undefined && snippet.description !== String(body.description).slice(0, 5000)) return false;
  if (body.category_id !== undefined && snippet.categoryId !== validCategory(body.category_id)) return false;
  if (body.tags !== undefined) {
    const expected = validTags(body.tags).slice().sort();
    const actual = (snippet.tags || []).map(x => String(x)).slice().sort();
    if (expected.length !== actual.length || expected.some((tag, i) => tag !== actual[i])) return false;
  }
  return true;
}

async function verifyVideoMetadataEventually(accessToken, channelId, videoId, body) {
  const delays = [0, 200, 500, 1000, 2000, 5000];
  let video = null;
  for (const delay of delays) {
    if (delay) await new Promise(resolve => setTimeout(resolve, delay));
    video = await ownedVideo(accessToken, channelId, videoId);
    if (videoMetadataMatches(video, body)) return video;
  }
  return video;
}

async function verifyVideoStatusEventually(accessToken, channelId, videoId, predicate) {
  const delays = [0, 200, 500, 1000, 2000, 5000];
  let video = null;
  for (const delay of delays) {
    if (delay) await new Promise(resolve => setTimeout(resolve, delay));
    video = await ownedVideo(accessToken, channelId, videoId);
    if (predicate(video.status || {})) return video;
  }
  return video;
}

function writableStatus(current, overrides) {
  const status = {
    privacyStatus: overrides.privacyStatus || current.privacyStatus,
    selfDeclaredMadeForKids: Boolean(current.selfDeclaredMadeForKids),
  };
  for (const key of ["embeddable", "license", "publicStatsViewable"]) {
    if (current[key] !== undefined) status[key] = current[key];
  }
  if (overrides.publishAt) status.publishAt = overrides.publishAt;
  return status;
}

function analyticsDates(url) {
  const endDate = validDate(url.searchParams.get("end_date") || new Date(Date.now() - 86400000).toISOString().slice(0, 10));
  const startDate = validDate(url.searchParams.get("start_date") || new Date(Date.parse(`${endDate}T00:00:00Z`) - 27 * 86400000).toISOString().slice(0, 10));
  if (startDate > endDate) throw httpError(400, "invalid_analytics_range");
  if (Date.parse(`${endDate}T00:00:00Z`) - Date.parse(`${startDate}T00:00:00Z`) > 366 * 86400000) throw httpError(400, "analytics_range_too_large");
  return { startDate, endDate };
}

function analyticsRows(data) {
  const headers = (data.columnHeaders || []).map(x => x.name);
  return (data.rows || []).map(row => Object.fromEntries(headers.map((name, i) => [name, row[i]])));
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
    playlist_id: job.playlist_id,
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

async function requireActor(request, secret, actor, alternateSecret = null) {
  if (!secret) throw httpError(503, "gateway_not_configured");
  const header = request.headers.get("Authorization") || "";
  const presented = header.startsWith("Bearer ") ? header.slice(7) : "";
  const accepted = presented && ((await secureEqual(presented, secret)) || (alternateSecret && await secureEqual(presented, alternateSecret)));
  if (!accepted) throw httpError(401, `${actor}_authentication_required`);
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

async function youtubeReportingApi(accessToken, input) {
  const resource = String(input.resource || "reportTypes");
  const operation = String(input.operation || "list");
  const params = input.params && typeof input.params === "object" && !Array.isArray(input.params) ? { ...input.params } : {};
  let body = input.body && typeof input.body === "object" && !Array.isArray(input.body) ? input.body : undefined;
  let method = "GET", path = "";
  if (resource === "reportTypes" && operation === "list") path = "/v1/reportTypes";
  else if (resource === "jobs" && operation === "list") path = "/v1/jobs";
  else if (resource === "jobs" && operation === "get") { if (!input.job_id) throw httpError(400, "job_id_required"); path = "/v1/jobs/" + encodeURIComponent(String(input.job_id)); }
  else if (resource === "jobs" && operation === "create") { if (input.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required"); method = "POST"; path = "/v1/jobs"; }
  else if (resource === "jobs" && operation === "delete") { if (input.explicit_destructive_intent !== true) throw httpError(409, "explicit_destructive_intent_required"); if (!input.job_id) throw httpError(400, "job_id_required"); method = "DELETE"; path = "/v1/jobs/" + encodeURIComponent(String(input.job_id)); }
  else if (resource === "reports" && operation === "list") { if (!input.job_id) throw httpError(400, "job_id_required"); path = "/v1/jobs/" + encodeURIComponent(String(input.job_id)) + "/reports"; }
  else if (resource === "reports" && operation === "get") { if (!input.job_id || !input.report_id) throw httpError(400, "report_ids_required"); path = "/v1/jobs/" + encodeURIComponent(String(input.job_id)) + "/reports/" + encodeURIComponent(String(input.report_id)); }
  else throw httpError(400, "reporting_operation_not_allowed");
  const query = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) if (value !== undefined && value !== null) query.set(key, Array.isArray(value) ? value.join(",") : String(value));
  return googleJson("https://youtubereporting.googleapis.com" + path + (query.toString() ? "?" + query.toString() : ""), accessToken, "youtube_reporting_api_failed", { method, body: method === "POST" ? body : undefined, expectEmpty: method === "DELETE" });
}

async function youtubeAnalyticsApi(accessToken, profile, input) {
  const resource = String(input.resource || "reports");
  const operation = String(input.operation || (resource === "reports" ? "query" : "list"));
  const params = input.params && typeof input.params === "object" && !Array.isArray(input.params) ? { ...input.params } : {};
  const body = input.body && typeof input.body === "object" && !Array.isArray(input.body) ? input.body : undefined;
  if (resource === "reports") {
    if (operation !== "query") throw httpError(400, "analytics_operation_not_allowed");
    params.ids = "channel==MINE";
    if (!params.startDate || !params.endDate || !params.metrics) throw httpError(400, "analytics_query_params_required");
    const query = new URLSearchParams(Object.entries(params).filter(([,value]) => value !== undefined && value !== null).map(([key,value]) => [key, Array.isArray(value) ? value.join(",") : String(value)]));
    const data = await googleJson(`https://youtubeanalytics.googleapis.com/v2/reports?${query}`, accessToken, "analytics_query_failed");
    return { columnHeaders: data.columnHeaders || [], rows: analyticsRows(data) };
  }
  if (!["groups", "groupItems"].includes(resource)) throw httpError(400, "analytics_resource_not_allowed");
  const allowed = resource === "groups" ? ["list", "insert", "update", "delete"] : ["list", "insert", "delete"];
  if (!allowed.includes(operation)) throw httpError(400, "analytics_operation_not_allowed");
  if (["insert", "update"].includes(operation) && input.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
  if (operation === "delete" && input.explicit_destructive_intent !== true) throw httpError(409, "explicit_destructive_intent_required");
  const method = { list: "GET", insert: "POST", update: "PUT", delete: "DELETE" }[operation];
  const query = new URLSearchParams();
  for (const [key,value] of Object.entries(params)) if (value !== undefined && value !== null) query.set(key, Array.isArray(value) ? value.join(",") : String(value));
  return googleJson(`https://youtubeanalytics.googleapis.com/v2/${resource}${query.toString() ? "?" + query.toString() : ""}`, accessToken, "analytics_group_api_failed", { method, body: ["POST", "PUT"].includes(method) ? body : undefined, expectEmpty: operation === "delete" });
}

const DATA_API_ALLOW = {
  activities: ["list"], channels: ["list", "update"], channelSections: ["list", "insert", "update", "delete"],
  commentThreads: ["list", "insert"], comments: ["list", "insert", "update", "delete", "setModerationStatus"],
  captions: ["list", "delete"], i18nLanguages: ["list"], i18nRegions: ["list"], members: ["list"], membershipsLevels: ["list"],
  playlistImages: ["list", "delete"], playlistItems: ["list", "insert", "update", "delete"], playlists: ["list", "insert", "update", "delete"], search: ["list"],
  subscriptions: ["list", "insert", "delete"], videoCategories: ["list"], videos: ["list", "update", "delete", "getRating", "rate"],
  liveBroadcasts: ["list", "insert", "update", "delete", "bind", "transition"], liveStreams: ["list", "insert", "update", "delete"],
  liveChatBans: ["list", "insert", "delete"], liveChatMessages: ["list", "insert", "delete"], liveChatModerators: ["list", "insert", "delete"], superChatEvents: ["list"], videoAbuseReportReasons: ["list"], watermarks: ["unset"]
};

async function youtubeDataApi(accessToken, profile, input) {
  const resource = String(input.resource || "");
  const operation = String(input.operation || "");
  if (!DATA_API_ALLOW[resource]?.includes(operation)) throw httpError(400, "youtube_api_operation_not_allowed");
  const params = input.params && typeof input.params === "object" && !Array.isArray(input.params) ? { ...input.params } : {};
  const body = input.body && typeof input.body === "object" && !Array.isArray(input.body) ? input.body : undefined;
  const moderationDestructive = resource === "comments" && operation === "setModerationStatus" && (String(params.moderationStatus || "") === "rejected" || params.banAuthor === true || String(params.banAuthor || "") === "true");
  const destructive = operation === "delete" || operation === "unset" || moderationDestructive;
  const interactive = ["insert", "update", "rate", "setModerationStatus", "bind", "transition"].includes(operation);
  const publication = (resource === "liveBroadcasts" && operation === "transition") || (resource === "videos" && operation === "update" && Boolean(body?.status?.publishAt));
  if (destructive && input.explicit_destructive_intent !== true) throw httpError(409, "explicit_destructive_intent_required");
  if (interactive && input.explicit_action_intent !== true) throw httpError(409, "explicit_action_intent_required");
  if (publication && input.explicit_publication_intent !== true) throw httpError(409, "explicit_publication_intent_required");
  const privacy = body?.status?.privacyStatus;
  if ((privacy === "public" || privacy === "unlisted") && input.explicit_visibility_intent !== true) throw httpError(409, "explicit_visibility_intent_required");
  if (resource === "channels" && operation === "update" && body?.id !== profile.channel_id) throw httpError(409, "channel_identity_mismatch");
  if (resource === "videos" && ["update", "delete"].includes(operation)) { const id = String(body?.id || params.id || ""); if (!id) throw httpError(400, "video_id_required"); await ownedVideo(accessToken, profile.channel_id, validVideoId(id)); }
  if (resource === "playlists" && ["update", "delete"].includes(operation)) {
    const id = String(body?.id || params.id || "");
    if (!id) throw httpError(400, "playlist_id_required");
    const current = await ownedPlaylist(accessToken, profile.channel_id, validPlaylistId(id));
    if (operation === "update") {
      const requested = body || {};
      const snippetIn = requested.snippet && typeof requested.snippet === "object" && !Array.isArray(requested.snippet) ? requested.snippet : {};
      const nextSnippet = {
        title: snippetIn.title !== undefined ? String(snippetIn.title) : String(current.snippet?.title || ""),
        description: snippetIn.description !== undefined ? String(snippetIn.description) : String(current.snippet?.description || ""),
      };
      if (snippetIn.defaultLanguage !== undefined) nextSnippet.defaultLanguage = snippetIn.defaultLanguage;
      body = { ...requested, id, snippet: nextSnippet };
      const parts = new Set(String(params.part || "").split(",").map(x => x.trim()).filter(Boolean));
      parts.add("snippet");
      if (requested.status !== undefined) parts.add("status");
      params.part = Array.from(parts).join(",");
    }
  }
  if (resource === "playlistItems" && operation === "insert") { const playlistId = body?.snippet?.playlistId; if (!playlistId) throw httpError(400, "playlist_id_required"); await ownedPlaylist(accessToken, profile.channel_id, validPlaylistId(playlistId)); }
  const methodMap = { list: "GET", insert: "POST", update: "PUT", delete: "DELETE", getRating: "GET", rate: "POST", setModerationStatus: "POST", bind: "POST", transition: "POST", unset: "POST" };
  const suffixMap = { getRating: "getRating", rate: "rate", setModerationStatus: "setModerationStatus", bind: "bind", transition: "transition", unset: "unset" };
  const suffix = suffixMap[operation] ? "/" + suffixMap[operation] : "";
  const query = new URLSearchParams();
  for (const [key,value] of Object.entries(params)) if (value !== undefined && value !== null) query.set(key, Array.isArray(value) ? value.join(",") : String(value));
  const endpoint = `https://www.googleapis.com/youtube/v3/${resource}${suffix}${query.toString() ? "?" + query.toString() : ""}`;
  return googleJson(endpoint, accessToken, "youtube_data_api_failed", { method: methodMap[operation], body: ["POST", "PUT"].includes(methodMap[operation]) ? body : undefined, expectEmpty: destructive });
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

function validVideoId(value) {
  const id = String(value || "");
  if (!/^[A-Za-z0-9_-]{6,20}$/.test(id)) throw httpError(400, "invalid_video_id");
  return id;
}

function validPlaylistId(value) {
  const id = String(value || "");
  if (!/^[A-Za-z0-9_-]{10,100}$/.test(id)) throw httpError(400, "invalid_playlist_id");
  return id;
}

function validTitle(value) {
  const title = String(value || "").trim();
  if (!title || title.length > 100) throw httpError(400, "invalid_title");
  return title;
}

function validTags(value) {
  if (!Array.isArray(value) || value.length > 50) throw httpError(400, "invalid_tags");
  const tags = value.map(x => String(x).trim()).filter(Boolean);
  if (tags.some(x => x.length > 500) || tags.join(",").length > 500) throw httpError(400, "invalid_tags");
  return tags;
}

function validCategory(value) {
  const id = String(value || "");
  if (!/^\d{1,4}$/.test(id)) throw httpError(400, "invalid_category_id");
  return id;
}

function validPrivacy(value) {
  const privacy = String(value || "");
  if (!["private", "unlisted", "public"].includes(privacy)) throw httpError(400, "invalid_privacy");
  return privacy;
}

function validFutureTime(value) {
  const date = new Date(String(value || ""));
  if (!Number.isFinite(date.getTime()) || date.getTime() < Date.now() + 60_000) throw httpError(400, "invalid_publish_at");
  return date.toISOString();
}

function validDate(value) {
  const date = String(value || "");
  if (!/^\d{4}-\d{2}-\d{2}$/.test(date) || !Number.isFinite(Date.parse(`${date}T00:00:00Z`))) throw httpError(400, "invalid_date");
  return date;
}

function boundedInt(value, fallback, min, max) {
  const number = value == null ? fallback : Number(value);
  if (!Number.isSafeInteger(number) || number < min || number > max) throw httpError(400, "invalid_limit");
  return number;
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
