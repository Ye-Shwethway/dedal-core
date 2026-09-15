const VERSION = "0.1.0";
const ISSUER = "https://mcp.youtube.drthorne.uk";
const RESOURCE = `${ISSUER}/mcp`;
const GATEWAY = "https://youtube.drthorne.uk";
const SCOPE = "youtube:manage";

const TOOLS = [
  tool("youtube_channels", "List verified YouTube channel profiles.", {}, true),
  tool("youtube_videos_list", "List recent videos for a verified profile.", { profile_alias: str(), max_results: integer(1, 50) }, true, ["profile_alias"]),
  tool("youtube_video_get", "Get one video after exact channel ownership verification.", { profile_alias: str(), video_id: str() }, true, ["profile_alias", "video_id"]),
  tool("youtube_video_update", "Update bounded video metadata on the verified channel.", { profile_alias: str(), video_id: str(), title: str(), description: str(), tags: array(str()), category_id: str() }, false, ["profile_alias", "video_id"]),
  tool("youtube_video_set_privacy", "Set video privacy. Public or unlisted requires explicit visibility intent.", { profile_alias: str(), video_id: str(), privacy: { type: "string", enum: ["private", "unlisted", "public"] }, explicit_visibility_intent: bool() }, false, ["profile_alias", "video_id", "privacy"]),
  tool("youtube_video_schedule", "Schedule a private video for publication with explicit publication intent.", { profile_alias: str(), video_id: str(), publish_at: str(), explicit_publication_intent: bool() }, false, ["profile_alias", "video_id", "publish_at", "explicit_publication_intent"]),
  tool("youtube_playlists_list", "List playlists owned by the verified channel.", { profile_alias: str(), max_results: integer(1, 50) }, true, ["profile_alias"]),
  tool("youtube_playlist_add", "Idempotently add an owned video to an owned playlist.", { profile_alias: str(), playlist_id: str(), video_id: str() }, false, ["profile_alias", "playlist_id", "video_id"], true),
  tool("youtube_playlist_remove", "Idempotently remove a video from an owned playlist.", { profile_alias: str(), playlist_id: str(), video_id: str() }, false, ["profile_alias", "playlist_id", "video_id"], true),
  tool("youtube_upload_create", "Create a private-first upload job. Media bytes never pass through MCP or Gateway.", { profile_alias: str(), source_type: { type: "string", enum: ["direct_url", "local_file", "google_drive"] }, source_locator: str(), source_fingerprint: str(), title: str(), description: str(), tags: array(str()), category_id: str(), made_for_kids: bool(), playlist_id: str(), requested_privacy: { type: "string", enum: ["private", "unlisted", "public"] }, publish_at: str(), explicit_visibility_intent: bool(), explicit_publication_intent: bool(), idempotency_key: str() }, false, ["profile_alias", "source_type", "source_locator", "title", "idempotency_key"], true),
  tool("youtube_upload_status", "Get an upload job status and verified result.", { job_id: str() }, true, ["job_id"]),
  tool("youtube_analytics_summary", "Get a bounded YouTube Analytics summary.", { profile_alias: str(), start_date: str(), end_date: str() }, true, ["profile_alias"]),
  tool("youtube_search_terms", "Get bounded YouTube search-term analytics where available.", { profile_alias: str(), start_date: str(), end_date: str(), max_results: integer(1, 50) }, true, ["profile_alias"]),
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
  const routes = {
    youtube_channels: ["GET", "/v1/channels"],
    youtube_videos_list: ["GET", `/v1/channels/${enc(a.profile_alias)}/videos?max_results=${a.max_results || 10}`],
    youtube_video_get: ["GET", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}`],
    youtube_video_update: ["PATCH", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}`, pick(a, ["title", "description", "tags", "category_id"])],
    youtube_video_set_privacy: ["POST", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/privacy`, pick(a, ["privacy", "explicit_visibility_intent"])],
    youtube_video_schedule: ["POST", `/v1/channels/${enc(a.profile_alias)}/videos/${enc(a.video_id)}/schedule`, pick(a, ["publish_at", "explicit_publication_intent"])],
    youtube_playlists_list: ["GET", `/v1/channels/${enc(a.profile_alias)}/playlists?max_results=${a.max_results || 25}`],
    youtube_playlist_add: ["POST", `/v1/channels/${enc(a.profile_alias)}/playlists/${enc(a.playlist_id)}/videos/${enc(a.video_id)}`],
    youtube_playlist_remove: ["DELETE", `/v1/channels/${enc(a.profile_alias)}/playlists/${enc(a.playlist_id)}/videos/${enc(a.video_id)}`],
    youtube_upload_create: ["POST", "/v1/upload-jobs", a],
    youtube_upload_status: ["GET", `/v1/upload-jobs/${enc(a.job_id)}`],
    youtube_analytics_summary: ["GET", `/v1/channels/${enc(a.profile_alias)}/analytics/summary?${query(pick(a, ["start_date", "end_date"]))}`],
    youtube_search_terms: ["GET", `/v1/channels/${enc(a.profile_alias)}/analytics/search-terms?${query(pick(a, ["start_date", "end_date", "max_results"]))}`],
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
function str() { return { type: "string" }; } function bool() { return { type: "boolean" }; } function integer(minimum, maximum) { return { type: "integer", minimum, maximum }; } function array(items) { return { type: "array", items }; }
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
