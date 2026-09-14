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

## Newly verified private-upload evidence

- The isolated VPS runner authenticated with its scoped credential without receiving
  a Google or YouTube refresh token.
- A private Google Drive object was resolved by exact Drive file ID through the
  existing authenticated media-gateway route. Filename, byte length, MIME type, and
  SHA-256 were verified on the VPS before job creation.
- D1 migration 2 adds `google_drive` as a bounded source type. The runner attests
  SHA-256 at claim time and the gateway locks it before creating a YouTube session.
- One real private video completed the official resumable upload path directly from
  the VPS to YouTube; the Worker did not proxy the media body.
- Gateway read-back verified the returned video identity, exact target channel,
  requested title, and `private` privacy. Evidence IDs and private video metadata
  remain outside this public repository.

## Not yet verified

A deliberate channel-ID mismatch rejection, interruption/resume behavior, and a
relevant thumbnail or playlist secondary operation. The skill remains candidate.

## Next step

Exercise deliberate mismatch rejection and interruption recovery without creating a
duplicate. Then validate one relevant secondary operation before promotion.
