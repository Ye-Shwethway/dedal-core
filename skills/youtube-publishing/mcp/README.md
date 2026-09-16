# DEDAL YouTube MCP

Thin, authenticated orchestration layer for the bounded DEDAL YouTube Gateway.

Production topology:

`ChatGPT / DEDAL -> mcp.youtube.drthorne.uk/mcp -> youtube.drthorne.uk -> YouTube APIs`

Large media follows the separate Gateway-job to VPS-runner path.

## Boundary

- MCP stores no Google OAuth credential.
- Gateway bearer material remains a Worker secret.
- MCP access/refresh tokens are opaque; D1 stores hashes rather than plaintext tokens.
- OAuth authorization code + PKCE (`S256`) protects the client connection.
- Exact channel ownership is reasserted by the Gateway before mutation.
- Dedicated typed tools are preferred. A generic YouTube API bridge, when present, is limited to missing read surfaces or bounded diagnostics and does not expand mutation authority.
- Consequential writes require explicit action intent. Deletes/unsets require explicit destructive intent; visibility/publication have their own intent flags.
- Readback is required when the provider exposes readable state; unreadable unmanaged state fails closed.

## Live-gated dedicated families

Current production evidence covers:
- captions: list, insert, update, download, delete;
- playlist images: list, set/managed replace, delete;
- channel banner: set with apply/readback;
- video thumbnail: set.

Watermark set/unset tools are exposed, but the watermark lifecycle is intentionally **not** classified as fully live-gated because YouTube does not expose a reliable current-watermark read/list baseline.

## Version evidence

The checked-in MCP source snapshot identifies itself as `0.1.0`. This reconciliation does not invent a newer deployed version number. Exact deployed/source parity is part of `YOUTUBE-SOURCE-SYNC-01`.

## Developer-mode registration

Use the production MCP endpoint configured for the environment. OAuth discovery and dynamic client registration remain the connection mechanism; Creator approval remains explicit.
