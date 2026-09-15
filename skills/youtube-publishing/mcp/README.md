# DEDAL YouTube MCP

Thin, authenticated MCP orchestration layer for the DEDAL YouTube Gateway.

Production topology:

`ChatGPT / DEDAL -> mcp.youtube.drthorne.uk/mcp -> youtube.drthorne.uk -> YouTube APIs`

Large media follows the separate Gateway-job to VPS-runner path and never crosses this Worker.

## Security boundary

- The MCP Worker stores no Google OAuth credential.
- `GATEWAY_API_TOKEN` is a scoped Cloudflare Worker secret and is never committed.
- MCP access and refresh tokens are random opaque values; D1 stores SHA-256 hashes only.
- OAuth authorization code + PKCE (`S256`) is required.
- Dynamic client registration accepts only HTTPS `chatgpt.com` redirects.
- Creator approval uses a short-lived, single-use ticket inserted through the privileged control plane.
- Public/unlisted privacy and scheduling remain protected by Gateway explicit-intent checks.

## Cloudflare bindings

- D1 binding: `DB` -> `dedal-youtube-gateway-prod`
- Worker secret: `GATEWAY_API_TOKEN`
- Custom domain: `mcp.youtube.drthorne.uk`

## Developer-mode registration

Use `https://mcp.youtube.drthorne.uk/mcp`. The client discovers OAuth metadata from the well-known endpoints and uses dynamic client registration. The Creator enters a fresh one-time approval code on the authorization page.
