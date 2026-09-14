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

## Newly verified OAuth evidence

- Real Creator-owned Google OAuth completed at 2026-09-14T20:02:42Z.
- Callback resolved display name `CHILIVIDS` and exact channel ID
  `UCO3uj0h4UcRh3X5BXXrc_iw`.
- Profile `chilivids` is enabled with credential reference `yt:chilivids`.
- The credential vault contains AES-GCM ciphertext + IV only; no plaintext token was
  read or exposed during verification.
- OAuth mutation audit records `channel_profile.bind` with outcome `success`.

## Not yet verified

Deliberate channel-ID mismatch rejection,
private resumable upload, interruption resume, and remote YouTube read-back. The
skill remains candidate.

## Next step

Exercise deliberate mismatch rejection and one private resumable upload through the VPS runner. Promotion still
requires a relevant thumbnail/playlist secondary operation.
