# YouTube Publishing Gateway checkpoint — 2026-09-14

## Verified

- Before creation, `youtube.drthorne.uk` had no DNS record, Worker domain/route,
  Access app, Pages domain, or Tunnel mapping.
- Worker `dedal-youtube-gateway`, D1 `dedal-youtube-gateway-prod`, migration 1,
  and the enabled custom domain exist.
- All five secret bindings are present; live `GET /health` returned HTTP 200 with
  `configured: true`.
- Unauthenticated privileged access returned fail-closed HTTP 401.
- `chilivids` is pre-registered against exact channel ID
  `UCO3uj0h4UcRh3X5BXXrc_iw`, disabled until OAuth verification.
- Link-preview behavior exposed premature one-time ticket consumption. Production
  now uses 30-minute reusable connect tickets; each OAuth state remains
  browser-bound, ten-minute, and atomically single-use.
- Existing unrelated Workers, DNS, Access, Pages, D1, and Tunnels were preserved.

## Not yet verified

OAuth callback with the real channel, deliberate channel-ID mismatch rejection,
private resumable upload, interruption resume, and remote YouTube read-back. The
skill remains candidate.

## Next step

Complete OAuth for `chilivids`, read back the encrypted credential/profile binding,
then exercise mismatch rejection and one private resumable upload. Promotion still
requires a relevant thumbnail/playlist secondary operation.
