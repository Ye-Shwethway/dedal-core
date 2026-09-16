const VERSION = "0.2.2";
const ISSUER = "https://mcp.youtube.drthorne.uk";
const RESOURCE = `${ISSUER}/mcp`;
const GATEWAY = "https://youtube.drthorne.uk";
const SCOPE = "youtube:manage";

const TOOLS = [
  tool("youtube_channels", "List verified YouTube channel profiles.", {}, true),
  tool("youtube_videos_list", "List recent videos for a verified profile.", { profile_alias: str(), max_results: integer(1, 50) }, true, ["profile_alias"]),
  tool("youtube_video_get", "Get one video after exact channel ownership verification.", { profile_alias: str(), video_id: str() }, true, ["profile_alias", "video_id"]),
  tool("youtube_video_update", "Update bounded video metadata on the verified channel.", { profile_alias: str(), video_id: str(), title: str(), description: str(), tags: array(str()), category_id: str() }, false, ["profile_alias", "video_id"]),
  tool("youtube_video_delete", "Permanently delete a verified owned video. Requires explicit delete intent.", { profile_alias: str(), video_id: str(), explicit_delete_intent: bool() }, false, ["profile_alias", "video_id", "explicit_delete_intent"]),
  tool("youtube_data_api", "Advanced allowlisted YouTube Data API bridge for channel management. Mutating and destructive operations require explicit intent flags.", { profile_alias: str(), resource: { type: "string", enum: ["activities","channels","channelSections","commentThreads","comments","captions","i18nLanguages","i18nRegions","members","membershipsLevels","playlistImages","playlistItems","playlists","search","subscriptions","videoCategories","videos","liveBroadcasts","liveStreams","liveChatBans","liveChatMessages","liveChatModerators","superChatEvents","videoAbuseReportReasons","watermarks"] }, operation: str(), params: obj(), body: obj(), explicit_action_intent: bool(), explicit_destructive_intent: bool(), explicit_visibility_intent: bool(), explicit_publication_intent: bool() }, false, ["profile_alias", "resource", "operation"]),
  tool("youtube_playlist_create", "Create a playlist on the verified channel. Public or unlisted requires explicit visibility intent.", { profile_alias: str(), title: str(), description: str(), privacy: { type: "string", enum: ["private","unlisted","public"] }, explicit_visibility_intent: bool() }, false, ["profile_alias","title"]),
  tool("youtube_playlist_update", "Update an owned playlist title/description/privacy. Public or unlisted requires explicit visibility intent.", { profile_alias: str(), playlist_id: str(), title: str(), description: str(), privacy: { type: "string", enum: ["private","unlisted","public"] }, explicit_visibility_intent: bool() }, false, ["profile_alias","playlist_id"]),
  tool("youtube_playlist_delete", "Permanently delete an owned playlist. Requires explicit destructive intent.", { profile_alias: str(), playlist_id: str(), explicit_destructive_intent: bool() }, false, ["profile_alias","playlist_id","explicit_destructive_intent"]),
  tool("youtube_playlist_items_list", "List items in a playlist.", { profile_alias: str(), playlist_id: str(), max_results: integer(1, 50) }, true, ["profile_alias","playlist_id"]),
  tool("youtube_comments_list", "List top-level comment threads and replies for a video.", { profile_alias: str(), video_id: str(), max_results: integer(1,100), order: { type: "string", enum: ["time","relevance"] } }, true, ["profile_alias","video_id"]),
  tool("youtube_comment_reply", "Reply to an existing YouTube comment.", { profile_alias: str(), parent_id: str(), text: str() }, false, ["profile_alias","parent_id","text"]),
  tool("youtube_comment_update", "Edit a YouTube comment that the connected identity is allowed to edit.", { profile_alias: str(), comment_id: str(), text: str() }, false, ["profile_alias","comment_id","text"]),
  tool("youtube_comment_moderate", "Set comment moderation status. Rejecting or banning an author requires explicit destructive intent.", { profile_alias: str(), comment_id: str(), moderation_status: { type: "string", enum: ["heldForReview","published","rejected"] }, ban_author: bool(), explicit_destructive_intent: bool() }, false, ["profile_alias","comment_id","moderation_status"]),
  tool("youtube_comment_delete", "Permanently delete a comment. Requires explicit destructive intent.", { profile_alias: str(), comment_id: str(), explicit_destructive_intent: bool() }, false, ["profile_alias","comment_id","explicit_destructive_intent"]),
  tool("youtube_subscriptions_list", "List subscriptions for the connected YouTube identity.", { profile_alias: str(), max_results: integer(1,50) }, true, ["profile_alias"]),
  tool("youtube_subscribe", "Subscribe the connected YouTube identity to a channel.", { profile_alias: str(), channel_id: str() }, false, ["profile_alias","channel_id"]),
  tool("youtube_unsubscribe", "Remove a subscription by subscription resource id. Requires explicit destructive intent.", { profile_alias: str(), subscription_id: str(), explicit_destructive_intent: bool() }, false, ["profile_alias","subscription_id","explicit_destructive_intent"]),
  tool("youtube_channel_sections_list", "List channel sections for the verified channel.", { profile_alias: str() }, true, ["profile_alias"]),
  tool("youtube_search", "Search YouTube using the connected identity with bounded SEO research controls.", { profile_alias: str(), q: str(), type: { type: "string", enum: ["video","channel","playlist"] }, order: { type: "string", enum: ["date","rating","relevance","title","videoCount","viewCount"] }, max_results: integer(1,50), region_code: str(), relevance_language: str(), published_after: str(), published_before: str(), page_token: str(), safe_search: { type: "string", enum: ["moderate","none","strict"] } }, true, ["profile_alias","q"]),
  tool("youtube_activities_list", "List recent activities for the connected identity/channel.", { profile_alias: str(), max_results: integer(1,50) }, true, ["profile_alias"]),
  tool("youtube_members_list", "List channel members when memberships are available.", { profile_alias: str(), max_results: integer(1,100) }, true, ["profile_alias"]),
  tool("youtube_membership_levels_list", "List channel membership levels when available.", { profile_alias: str() }, true, ["profile_alias"]),
  tool("youtube_live_broadcasts_list", "List live broadcasts for the verified channel.", { profile_alias: str(), broadcast_status: { type: "string", enum: ["all","active","completed","upcoming"] }, max_results: integer(1,50) }, true, ["profile_alias"]),
  tool("youtube_live_streams_list", "List live streams for the verified channel.", { profile_alias: str(), max_results: integer(1,50) }, true, ["profile_alias"]),
  tool("youtube_live_chat_messages_list", "List messages from a live chat.", { profile_alias: str(), live_chat_id: str(), max_results: integer(1,200) }, true, ["profile_alias","live_chat_id"]),
  tool("youtube_thumbnail_set", "Upload and set a custom thumbnail for a verified owned video from an HTTPS source URL.", { profile_alias: str(), video_id: str(), source_url: str(), explicit_action_intent: bool() }, false, ["profile_alias","video_id","source_url","explicit_action_intent"]),
  tool("youtube_captions_list", "List caption tracks for a verified owned video.", { profile_alias: str(), video_id: str() }, true, ["profile_alias","video_id"]),
  tool("youtube_caption_insert", "Upload a caption track from an HTTPS source URL.", { profile_alias: str(), video_id: str(), source_url: str(), language: str(), name: str(), is_draft: bool(), explicit_action_intent: bool() }, false, ["profile_alias","video_id","source_url","language","name","explicit_action_intent"]),
  tool("youtube_caption_update", "Update a caption track metadata and optionally replace its file from an HTTPS source URL.", { profile_alias: str(), video_id: str(), caption_id: str(), source_url: str(), is_draft: bool(), explicit_action_intent: bool() }, false, ["profile_alias","video_id","caption_id","explicit_action_intent"]),
  tool("youtube_caption_download", "Download a caption track as text.", { profile_alias: str(), video_id: str(), caption_id: str(), tfmt: str(), tlang: str() }, true, ["profile_alias","video_id","caption_id"]),
  tool("youtube_caption_delete", "Permanently delete a caption track. Requires explicit destructive intent.", { profile_alias: str(), video_id: str(), caption_id: str(), explicit_destructive_intent: bool() }, false, ["profile_alias","video_id","caption_id","explicit_destructive_intent"]),
  tool("youtube_playlist_images_list", "List custom images for an owned playlist.", { profile_alias: str(), playlist_id: str() }, true, ["profile_alias","playlist_id"]),
  tool("youtube_playlist_image_set", "Set or replace the custom image of an owned playlist from a square JPEG/PNG HTTPS source URL.", { profile_alias: str(), playlist_id: str(), source_url: str(), explicit_action_intent: bool() }, false, ["profile_alias","playlist_id","source_url","explicit_action_intent"]),
  tool("youtube_playlist_image_delete", "Delete the custom image of an owned playlist. Requires explicit destructive intent.", { profile_alias: str(), playlist_id: str(), explicit_destructive_intent: bool() }, false, ["profile_alias","playlist_id","explicit_destructive_intent"]),
  tool("youtube_channel_banner_set", "Upload and apply a channel banner image from an HTTPS source URL.", { profile_alias: str(), source_url: str(), explicit_action_intent: bool() }, false, ["profile_alias","source_url","explicit_action_intent"]),
  tool("youtube_watermark_set", "Upload and set the channel watermark from an HTTPS image URL.", { profile_alias: str(), source_url: str(), timing_type: { type: "string", enum: ["offsetFromStart","offsetFromEnd"] }, offset_ms: integer(0,2147483647), duration_ms: integer(1,2147483647), explicit_action_intent: bool() }, false, ["profile_alias","source_url","explicit_action_intent"]),
  tool("youtube_watermark_unset", "Remove the channel watermark. Requires explicit destructive intent.", { profile_alias: str(), explicit_destructive_intent: bool() }, false, ["profile_alias","explicit_destructive_intent"]),
  tool("youtube_video_set_privacy", "Set video privacy. Public or unlisted requires explicit visibility intent.", { profile_alias: str(), video_id: str(), privacy: { type: "string", enum: ["private","unlisted","public"] }, explicit_visibility_intent: bool() }, false, ["profile_alias","video_id","privacy"]),
  tool("youtube_video_schedule", "Schedule a private video for publication with explicit publication intent.", { profile_alias: str(), video_id: str(), publish_at: str(), explicit_publication_intent: bool() }, false, ["profile_alias","video_id","publish_at","explicit_publication_intent"]),
  tool("youtube_playlists_list", "List playlists owned by the verified channel.", { profile_alias: str(), max_results: integer(1,50) }, true, ["profile_alias"]),
  tool("youtube_playlist_add", "Idempotently add an owned video to an owned playlist.", { profile_alias: str(), playlist_id: str(), video_id: str() }, false, ["profile_alias","playlist_id","video_id"], true),
  tool("youtube_playlist_remove", "Idempotently remove a video from an owned playlist.", { profile_alias: str(), playlist_id: str(), video_id: str() }, false, ["profile_alias","playlist_id","video_id"], true),
  tool("youtube_upload_create", "Create a private-first upload job. Media bytes never pass through MCP or Gateway.", { profile_alias: str(), source_type: { type: "string", enum: ["direct_url","local_file","google_drive"] }, source_locator: str(), source_fingerprint: str(), title: str(), description: str(), tags: array(str()), category_id: str(), made_for_kids: bool(), playlist_id: str(), requested_privacy: { type: "string", enum: ["private","unlisted","public"] }, publish_at: str(), explicit_visibility_intent: bool(), explicit_publication_intent: bool(), idempotency_key: str() }, false, ["profile_alias","source_type","source_locator","title","idempotency_key"], true),
  tool("youtube_upload_status", "Get an upload job status and verified result.", { job_id: str() }, true, ["job_id"]),
  tool("youtube_reporting_api", "YouTube Reporting API bridge for report types, scheduled jobs, and generated report metadata.", { profile_alias: str(), resource: { type: "string", enum: ["reportTypes","jobs","reports"] }, operation: str(), job_id: str(), report_id: str(), params: obj(), body: obj(), explicit_action_intent: bool(), explicit_destructive_intent: bool() }, false, ["profile_alias","resource","operation"]),
  tool("youtube_analytics_api", "Flexible YouTube Analytics API bridge for channel reports and analytics groups.", { profile_alias: str(), resource: { type: "string", enum: ["reports","groups","groupItems"] }, operation: str(), params: obj(), body: obj(), explicit_action_intent: bool(), explicit_destructive_intent: bool() }, false, ["profile_alias","resource","operation"]),
  tool("youtube_analytics_summary", "Get a bounded YouTube Analytics summary.", { profile_alias: str(), start_date: str(), end_date: str() }, true, ["profile_alias"]),
  tool("youtube_search_terms", "Get bounded YouTube search-term analytics where available.", { profile_alias: str(), start_date: str(), end_date: str(), max_results: integer(1,50) }, true, ["profile_alias"]),
  tool("youtube_video_traffic_sources", "Get bounded traffic-source analytics for one owned video.", { profile_alias: str(), video_id: str(), start_date: str(), end_date: str(), max_results: integer(1,50) }, true, ["profile_alias","video_id"]),
  tool("youtube_video_search_terms", "Get bounded YouTube search-term analytics for one owned video where available.", { profile_alias: str(), video_id: str(), start_date: str(), end_date: str(), max_results: integer(1,50) }, true, ["profile_alias","video_id"]),
  tool("youtube_video_retention", "Get audience-retention analytics for one owned video where available.", { profile_alias: str(), video_id: str(), start_date: str(), end_date: str() }, true, ["profile_alias","video_id"]),
];

export default {
  async fetch(request, env) {
    try { return await route(request, env); }
    catch (error) {
      console.error(JSON.stringify({ event: "mcp_error", code: error.code || "internal_error", status: error.status || 500 }));
      return json({ error: error.code || "internal_error" }, error.status || 500, error.headers || {});
    }
  },
};

async function route(request, env) {
  const url = new URL(request.url);
  if (request.method === "GET" && url.pathname === "/health") return json({ status: "ok", service: "dedal-youtube-mcp", version: VERSION, configured: Boolean(env.DB && env.GATEWAY_API_TOKEN) });
  if (request.method === "GET" && url.pathname === "/.well-known/oauth-protected-resource") return json({ resource: RESOURCE, authorization_servers: [ISSUER], scopes_supported: [SCOPE] });
  if (request.method === "GET" && url.pathname === "/.well-known/oauth-authorization-server") return json({ issuer: ISSUER, authorization_endpoint: `${ISSUER}/oauth/authorize`, token_endpoint: `${ISSUER}/oauth/token`, registration_endpoint: `${ISSUER}/oauth/register`, response_types_supported: ["code"], grant_types_supported: ["authorization_code", "refresh_token"], code_challenge_methods_supported: ["S256"], token_endpoint_auth_methods_supported: ["none"], scopes_supported: [SCOPE] });
  if (request.method === "POST" && url.pathname === "/oauth/register") return registerClient(request, env);
  if (request.method === "GET" && url.pathname === "/oauth/authorize") return authorizationForm(url, env);
  if (request.method === "POST" && url.pathname === "/oauth/authorize") return approveAuthorization(request, env);
  if (request.method === "POST" && url.pathname === "/oauth/token") return exchangeToken(request, env);
  if (url.pathname === "/mcp" && request.method === "POST") return mcp(request, env);
  throw failure(404, "not_found");
}

async function registerClient(request, env) {
  const body = await request.json();
  const redirects = Array.isArray(body.redirect_uris) ? body.redirect_uris.map(validRedirect) : [];
  if (!redirects.length) throw failure(400, "redirect_uris_required");
  const clientId = random(24), now = new Date().toISOString();
  await env.DB.prepare("INSERT INTO mcp_clients(client_id,redirect_uris_json,client_name,created_at) VALUES(?,?,?,?)").bind(clientId, JSON.stringify(redirects), String(body.client_name || "ChatGPT").slice(0, 100), now).run();
  return json({ client_id: clientId, client_id_issued_at: Math.floor(Date.now() / 1000), redirect_uris: redirects, token_endpoint_auth_method: "none", grant_types: ["authorization_code", "refresh_token"], response_types: ["code"] }, 201);
}

async function authorizationForm(url, env) {
  const auth = await validateAuthorization(url.searchParams, env);
  const hidden = Object.entries(auth).map(([k, v]) => `<input type="hidden" name="${escape(k)}" value="${escape(v)}">`).join("");
  return html(`<h1>Authorize DEDAL YouTube MCP</h1><p>This grants ChatGPT access only to the bounded DEDAL YouTube Gateway tools. Public/unlisted publication still requires explicit intent.</p><form method="post" action="/oauth/authorize">${hidden}<label>One-time approval code <input name="approval_ticket" required autocomplete="one-time-code"></label><button type="submit">Authorize</button></form>`);
}

async function approveAuthorization(request, env) {
  const form = await request.formData();
  const auth = await validateAuthorization(form, env);
  const ticket = String(form.get("approval_ticket") || ""), ticketHash = await sha256(ticket), now = new Date().toISOString();
  const consumed = await env.DB.prepare("UPDATE mcp_approval_tickets SET consumed_at=? WHERE ticket_hash=? AND consumed_at IS NULL AND expires_at>?").bind(now, ticketHash, now).run();
  if (consumed.meta?.changes !== 1) throw failure(401, "invalid_or_expired_approval_ticket");
  const code = random(32), codeHash = await sha256(code), expires = new Date(Date.now() + 5 * 60_000).toISOString();
  await env.DB.prepare("INSERT INTO mcp_auth_codes(code_hash,client_id,redirect_uri,code_challenge,resource,scope,expires_at,consumed_at,created_at) VALUES(?,?,?,?,?,?,?,NULL,?)").bind(codeHash, auth.client_id, auth.redirect_uri, auth.code_challenge, auth.resource, auth.scope, expires, now).run();
  const redirect = new URL(auth.redirect_uri); redirect.searchParams.set("code", code); redirect.searchParams.set("state", auth.state);
  return new Response(null, { status: 302, headers: { Location: redirect.toString(), "Cache-Control": "no-store" } });
}

async function exchangeToken(request, env) {
  const form = await request.formData(), grant = String(form.get("grant_type") || ""), now = new Date().toISOString();
  if (grant === "authorization_code") {
    const codeHash = await sha256(String(form.get("code") || ""));
    const row = await env.DB.prepare("SELECT * FROM mcp_auth_codes WHERE code_hash=?").bind(codeHash).first();
    if (!row || row.consumed_at || row.expires_at <= now || row.client_id !== form.get("client_id") || row.redirect_uri !== form.get("redirect_uri") || row.resource !== form.get("resource")) throw failure(400, "invalid_grant");
    const challenge = base64url(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(String(form.get("code_verifier") || ""))));
    if (!(await equal(challenge, row.code_challenge))) throw failure(400, "invalid_grant");
    await env.DB.prepare("UPDATE mcp_auth_codes SET consumed_at=? WHERE code_hash=? AND consumed_at IS NULL").bind(now, codeHash).run();
    return issueTokens(env, row.client_id, row.resource, row.scope);
  }
  if (grant === "refresh_token") {
    const hash = await sha256(String(form.get("refresh_token") || ""));
    const row = await env.DB.prepare("SELECT * FROM mcp_tokens WHERE token_hash=? AND token_type='refresh'").bind(hash).first();
    if (!row || row.revoked_at || row.expires_at <= now || row.client_id !== form.get("client_id") || row.resource !== form.get("resource")) throw failure(400, "invalid_grant");
    return issueTokens(env, row.client_id, row.resource, row.scope);
  }
  throw failure(400, "unsupported_grant_type");
}

async function issueTokens(env, clientId, resource, scope) {
  const access = random(32), refresh = random(40), now = new Date(), accessExpiry = new Date(now.getTime() + 3600_000), refreshExpiry = new Date(now.getTime() + 90 * 86400_000);
  await env.DB.batch([
    env.DB.prepare("INSERT INTO mcp_tokens(token_hash,token_type,client_id,resource,scope,expires_at,revoked_at,created_at) VALUES(?,'access',?,?,?,?,NULL,?)").bind(await sha256(access), clientId, resource, scope, accessExpiry.toISOString(), now.toISOString()),
    env.DB.prepare("INSERT INTO mcp_tokens(token_hash,token_type,client_id,resource,scope,expires_at,revoked_at,created_at) VALUES(?,'refresh',?,?,?,?,NULL,?)").bind(await sha256(refresh), clientId, resource, scope, refreshExpiry.toISOString(), now.toISOString()),
  ]);
  return json({ access_token: access, token_type: "Bearer", expires_in: 3600, refresh_token: refresh, scope, resource });
}

async function mcp(request, env) {
  await requireMcpToken(request, env);
  const rpc = await request.json();
  if (rpc.method === "notifications/initialized") return new Response(null, { status: 202 });
  if (rpc.method === "initialize") return rpcResult(rpc.id, { protocolVersion: "2025-06-18", capabilities: { tools: { listChanged: false } }, serverInfo: { name: "dedal-youtube", version: VERSION }, instructions: "Operate YouTube only through bounded Gateway tools. Default uploads private. Never infer channel identity; use verified aliases." });
  if (rpc.method === "tools/list") return rpcResult(rpc.id, { tools: TOOLS });
  if (rpc.method === "tools/call") {
    const result = await callGateway(rpc.params?.name, rpc.params?.arguments || {}, env);
    return rpcResult(rpc.id, { content: [{ type: "text", text: JSON.stringify(result) }], structuredContent: result, isError: false });
  }
  return rpcError(rpc.id, -32601, "Method not found");
}

async function callGateway(name, a, env) {
  const enc = encodeURIComponent;
  const clean = object => Object.fromEntries(Object.entries(object).filter(([, value]) => value !== undefined));
  const dataApi = (resource, operation, params = {}, body = undefined, flags = {}) => ["POST", `/v1/channels/${enc(a.profile_alias)}/data-api`, { resource, operation, params, ...(body === undefined ? {} : { body }), ...flags }];
  const playlistUpdatePart = () => [(a.title !== undefined || a.description !== undefined) ? "snippet" : null, a.privacy !== undefined ? "status" : null].filter(Boolean).join(",");
  const playlistUpdateBody = () => clean({ id: a.playlist_id, snippet: (a.title !== undefined || a.description !== undefined) ? clean({ title: a.title, description: a.description }) : undefined, status: a.privacy !== undefined ? { privacyStatus: a.privacy } : undefined });
  const routes = {
    youtube_channels: ["GET", "/v1/channels"],
    youtube_videos_list: ["GET", `/v1/channels/${enc(a.profile_alias)}/videos?max_results=${a.max_results || 10}`],
    youtube_video_get: ["GET", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}`],
    youtube_video_update: ["PATCH", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}`, pick(a, ["title", "description", "tags", "category_id"])],
    youtube_video_delete: ["POST", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/delete`, pick(a, ["explicit_delete_intent"])],
    youtube_data_api: ["POST", `/v1/channels/${enc(a.profile_alias)}/data-api`, pick(a, ["resource","operation","params","body","explicit_action_intent","explicit_destructive_intent","explicit_visibility_intent","explicit_publication_intent"])],
    youtube_playlist_create: ["POST", `/v1/channels/${enc(a.profile_alias)}/playlists`, pick(a, ["title","description","privacy","explicit_visibility_intent"])],
    youtube_playlist_update: dataApi("playlists", "update", { part: playlistUpdatePart() }, playlistUpdateBody(), { explicit_action_intent: true, explicit_visibility_intent: a.explicit_visibility_intent === true }),
    youtube_playlist_delete: dataApi("playlists", "delete", { id: a.playlist_id }, undefined, { explicit_destructive_intent: a.explicit_destructive_intent }),
    youtube_playlist_items_list: dataApi("playlistItems", "list", { part: "id,snippet,contentDetails", playlistId: a.playlist_id, maxResults: a.max_results || 50 }),
    youtube_comments_list: dataApi("commentThreads", "list", { part: "snippet,replies", videoId: a.video_id, maxResults: a.max_results || 50, order: a.order || "time" }),
    youtube_comment_reply: dataApi("comments", "insert", { part: "snippet" }, { snippet: { parentId: a.parent_id, textOriginal: a.text } }, { explicit_action_intent: true }),
    youtube_comment_update: dataApi("comments", "update", { part: "snippet" }, { id: a.comment_id, snippet: { textOriginal: a.text } }, { explicit_action_intent: true }),
    youtube_comment_moderate: dataApi("comments", "setModerationStatus", { id: a.comment_id, moderationStatus: a.moderation_status, ...(a.ban_author !== undefined ? { banAuthor: a.ban_author } : {}) }, undefined, { explicit_action_intent: true, explicit_destructive_intent: a.explicit_destructive_intent }),
    youtube_comment_delete: dataApi("comments", "delete", { id: a.comment_id }, undefined, { explicit_destructive_intent: a.explicit_destructive_intent }),
    youtube_subscriptions_list: dataApi("subscriptions", "list", { part: "snippet,contentDetails", mine: true, maxResults: a.max_results || 50 }),
    youtube_subscribe: dataApi("subscriptions", "insert", { part: "snippet" }, { snippet: { resourceId: { kind: "youtube#channel", channelId: a.channel_id } } }, { explicit_action_intent: true }),
    youtube_unsubscribe: dataApi("subscriptions", "delete", { id: a.subscription_id }, undefined, { explicit_destructive_intent: a.explicit_destructive_intent }),
    youtube_channel_sections_list: dataApi("channelSections", "list", { part: "id,snippet,contentDetails", mine: true }),
    youtube_search: dataApi("search", "list", { part: "snippet", q: a.q, type: a.type, order: a.order, maxResults: a.max_results || 25, forMine: a.type === "video" ? true : undefined, ...(a.region_code ? { regionCode: a.region_code } : {}), ...(a.relevance_language ? { relevanceLanguage: a.relevance_language } : {}), ...(a.published_after ? { publishedAfter: a.published_after } : {}), ...(a.published_before ? { publishedBefore: a.published_before } : {}), ...(a.page_token ? { pageToken: a.page_token } : {}), ...(a.safe_search ? { safeSearch: a.safe_search } : {}) }),
    youtube_activities_list: dataApi("activities", "list", { part: "snippet,contentDetails", mine: true, maxResults: a.max_results || 25 }),
    youtube_members_list: dataApi("members", "list", { part: "snippet", mode: "all_current", maxResults: a.max_results || 100 }),
    youtube_membership_levels_list: dataApi("membershipsLevels", "list", { part: "snippet" }),
    youtube_live_broadcasts_list: dataApi("liveBroadcasts", "list", { part: "id,snippet,status,contentDetails", broadcastStatus: a.broadcast_status || "all", maxResults: a.max_results || 25 }),
    youtube_live_streams_list: dataApi("liveStreams", "list", { part: "id,snippet,status,cdn,contentDetails", mine: true, maxResults: a.max_results || 25 }),
    youtube_live_chat_messages_list: dataApi("liveChatMessages", "list", { part: "id,snippet,authorDetails", liveChatId: a.live_chat_id, maxResults: a.max_results || 200 }),
    youtube_thumbnail_set: ["POST", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/thumbnail`, pick(a, ["source_url","explicit_action_intent"])],
    youtube_captions_list: ["GET", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/captions`],
    youtube_caption_insert: ["POST", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/captions`, pick(a, ["source_url","language","name","is_draft","explicit_action_intent"])],
    youtube_caption_update: ["PATCH", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/captions/${enc(a.caption_id)}`, pick(a, ["source_url","is_draft","explicit_action_intent"])],
    youtube_caption_download: ["GET", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/captions/${enc(a.caption_id)}/download?${query(pick(a, ["tfmt","tlang"]))}`],
    youtube_caption_delete: ["DELETE", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/captions/${enc(a.caption_id)}`, pick(a, ["explicit_destructive_intent"])],
    youtube_playlist_images_list: ["GET", `/v1/channels/${enc(a.profile_alias)}/playlists/${enc(a.playlist_id)}/image`],
    youtube_playlist_image_set: ["POST", `/v1/channels/${enc(a.profile_alias)}/playlists/${enc(a.playlist_id)}/image`, pick(a, ["source_url","explicit_action_intent"])],
    youtube_playlist_image_delete: ["DELETE", `/v1/channels/${enc(a.profile_alias)}/playlists/${enc(a.playlist_id)}/image`, pick(a, ["explicit_destructive_intent"])],
    youtube_channel_banner_set: ["POST", `/v1/channels/${enc(a.profile_alias)}/banner`, pick(a, ["source_url","explicit_action_intent"])],
    youtube_watermark_set: ["POST", `/v1/channels/${enc(a.profile_alias)}/watermark`, pick(a, ["source_url","timing_type","offset_ms","duration_ms","explicit_action_intent"])],
    youtube_watermark_unset: ["DELETE", `/v1/channels/${enc(a.profile_alias)}/watermark`, pick(a, ["explicit_destructive_intent"])],
    youtube_video_set_privacy: ["POST", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/privacy`, pick(a, ["privacy", "explicit_visibility_intent"])],
    youtube_video_schedule: ["POST", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/schedule`, pick(a, ["publish_at", "explicit_publication_intent"])],
    youtube_playlists_list: ["GET", `/v1/channels/${enc(a.profile_alias)}/playlists?max_results=${a.max_results || 25}`],
    youtube_playlist_add: ["POST", `/v1/channels/${enc(a.profile_alias)}/playlists/${enc(a.playlist_id)}/videos/${enc(a.video_id)}`],
    youtube_playlist_remove: ["DELETE", `/v1/channels/${enc(a.profile_alias)}/playlists/${enc(a.playlist_id)}/videos/${enc(a.video_id)}`],
    youtube_upload_create: ["POST", "/v1/upload-jobs", a],
    youtube_upload_status: ["GET", `/v1/upload-jobs/${enc(a.job_id)}`],
    youtube_reporting_api: ["POST", `/v1/channels/${enc(a.profile_alias)}/reporting-api`, pick(a, ["resource","operation","job_id","report_id","params","body","explicit_action_intent","explicit_destructive_intent"])],
    youtube_analytics_api: ["POST", `/v1/channels/${enc(a.profile_alias)}/analytics-api`, pick(a, ["resource","operation","params","body","explicit_action_intent","explicit_destructive_intent"])],
    youtube_analytics_summary: ["GET", `/v1/channels/${enc(a.profile_alias)}/analytics/summary?${query(pick(a, ["start_date", "end_date"]))}`],
    youtube_search_terms: ["GET", `/v1/channels/${enc(a.profile_alias)}/analytics/search-terms?${query(pick(a, ["start_date", "end_date", "max_results"]))}`],
    youtube_video_traffic_sources: ["GET", `/v1/channels/${enc(a.profile_alias)}/analytics/videos/${enc(a.video_id)}/traffic-sources?${query(pick(a, ["start_date", "end_date", "max_results"]))}`],
    youtube_video_search_terms: ["GET", `/v1/channels/${enc(a.profile_alias)}/analytics/videos/${enc(a.video_id)}/search-terms?${query(pick(a, ["start_date", "end_date", "max_results"]))}`],
    youtube_video_retention: ["GET", `/v1/channels/${enc(a.profile_alias)}/analytics/videos/${enc(a.video_id)}/retention?${query(pick(a, ["start_date", "end_date"]))}`],
  };
  const route = routes[name]; if (!route) throw failure(400, "unknown_tool");
  const response = await fetch(GATEWAY + route[1], { method: route[0], headers: { Authorization: `Bearer ${env.GATEWAY_API_TOKEN}`, ...(route[2] ? { "Content-Type": "application/json" } : {}) }, body: route[2] ? JSON.stringify(route[2]) : undefined });
  const data = await response.json();
  if (!response.ok) throw failure(response.status, data.error || "gateway_error");
  return data;
}

async function requireMcpToken(request, env) {
  const token = (request.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "");
  if (!token) throw oauthRequired();
  const row = await env.DB.prepare("SELECT scope,expires_at,revoked_at FROM mcp_tokens WHERE token_hash=? AND token_type='access' AND resource=?").bind(await sha256(token), RESOURCE).first();
  if (!row || row.revoked_at || row.expires_at <= new Date().toISOString() || !String(row.scope).split(" ").includes(SCOPE)) throw oauthRequired();
}

async function validateAuthorization(params, env) {
  const auth = Object.fromEntries(["client_id", "redirect_uri", "response_type", "code_challenge", "code_challenge_method", "state", "resource", "scope"].map(k => [k, String(params.get(k) || "")]));
  const client = await env.DB.prepare("SELECT redirect_uris_json FROM mcp_clients WHERE client_id=?").bind(auth.client_id).first();
  if (!client || !JSON.parse(client.redirect_uris_json).includes(auth.redirect_uri) || auth.response_type !== "code" || auth.code_challenge_method !== "S256" || !/^[A-Za-z0-9_-]{43,128}$/.test(auth.code_challenge) || auth.resource !== RESOURCE || auth.scope !== SCOPE || !auth.state) throw failure(400, "invalid_authorization_request");
  return auth;
}

function validRedirect(value) { const u = new URL(String(value)); if (u.protocol !== "https:" || u.hostname !== "chatgpt.com") throw failure(400, "invalid_redirect_uri"); return u.toString(); }
function tool(name, description, properties, readOnly, required = [], idempotent = false) { return { name, title: name.replaceAll("_", " "), description, inputSchema: { type: "object", properties, required, additionalProperties: false }, annotations: { readOnlyHint: readOnly, destructiveHint: !readOnly, idempotentHint: readOnly || idempotent, openWorldHint: true } }; }
function str() { return { type: "string" }; } function bool() { return { type: "boolean" }; } function obj() { return { type: "object", additionalProperties: true }; } function integer(minimum, maximum) { return { type: "integer", minimum, maximum }; } function array(items) { return { type: "array", items }; }
function pick(object, keys) { return Object.fromEntries(keys.filter(k => object[k] !== undefined).map(k => [k, object[k]])); }
function query(object) { return new URLSearchParams(Object.entries(object).map(([k, v]) => [k, String(v)])).toString(); }
function json(body, status = 200, headers = {}) { return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json", "Cache-Control": "no-store", ...headers } }); }
function html(body) { return new Response(`<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><main>${body}</main>`, { headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store", "Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; frame-ancestors 'none'" } }); }
function rpcResult(id, result) { return json({ jsonrpc: "2.0", id, result }); } function rpcError(id, code, message) { return json({ jsonrpc: "2.0", id, error: { code, message } }); }
function failure(status, code) { const e = new Error(code); e.status = status; e.code = code; return e; }
function oauthRequired() { const e = failure(401, "authentication_required"); e.headers = { "WWW-Authenticate": `Bearer resource_metadata="${ISSUER}/.well-known/oauth-protected-resource", scope="${SCOPE}"` }; return e; }
function random(bytes) { return base64url(crypto.getRandomValues(new Uint8Array(bytes))); }
async function sha256(value) { return base64url(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(value))); }
async function equal(a, b) { if (a.length !== b.length) return false; let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i); return d === 0; }
function base64url(input) { const bytes = input instanceof ArrayBuffer ? new Uint8Array(input) : input; let s = ""; for (const b of bytes) s += String.fromCharCode(b); return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, ""); }
function escape(value) { return String(value).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]); }
