# YouTube Publishing Gateway checkpoint — 2026-09-15

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

## Verified OAuth evidence

- Real Creator-owned Google OAuth completed at 2026-09-14T20:02:42Z.
- Callback resolved display name `CHILIVIDS` and exact channel ID
  `UCO3uj0h4UcRh3X5BXXrc_iw`.
- Profile `chilivids` is enabled with credential reference `yt:chilivids`.
- The credential vault contains AES-GCM ciphertext + IV only; no plaintext token was
  read or exposed during verification.
- OAuth mutation audit records `channel_profile.bind` with outcome `success`.

## Verified private-upload evidence

- The isolated VPS runner authenticated with its scoped credential without receiving
  a Google or YouTube refresh token.
- A private Google Drive object was resolved by exact Drive file ID. Filename, byte
  length, MIME type, and SHA-256 were verified on the VPS before job creation.
- D1 migration 2 adds `google_drive` as a bounded source type. The runner attests
  SHA-256 at claim time and the gateway locks it before creating a YouTube session.
- One real private video completed the official resumable upload path directly from
  the VPS to YouTube; the Worker did not proxy the media body.
- Gateway read-back verified the returned video identity, exact target channel,
  requested title, and `private` privacy. Evidence IDs and private video metadata
  remain outside this public repository.

## Verified runtime decoupling evidence

- The first proof upload reused the Link-to-File Bot `mirror-bot` container to execute
  rclone. That was accepted as a proof path but exposed an undesirable runtime
  dependency.
- Root cause of repeated Telegram boot messages was identified separately: the
  Link-to-File Bot generic VPS deploy workflow previously ran on every `main` push
  and rebuilt/restarted `mirror-bot`, including YouTube-workflow-only commits.
- The bot deploy trigger now ignores workflow-only, agent-mailbox, documentation, and
  root Markdown changes so YouTube workflow maintenance does not redeploy the bot.
- The YouTube runner now owns a dedicated rclone v1.75.1 binary and a private mode-600
  copy of the existing rclone configuration under runner-owned paths.
- Google Drive retrieval now runs directly through the runner-owned rclone binary and
  config; normal YouTube publishing no longer calls `docker exec mirror-bot`.
- A real small Drive file-ID retrieval succeeded through the standalone runner-owned
  rclone path.
- `mirror-bot` start time and restart count were checked before and after runner
  installation and the Drive proof; both remained unchanged and restart count stayed
  zero during the isolation test.
- No YouTube upload was performed during the isolation proof.

## Verified Creator-owned Google Drive OAuth migration

- The `gdrive:` remote was migrated away from rclone's retiring shared Google Drive
  client ID to a Creator-owned Desktop OAuth client.
- Existing bot and dedicated-runner rclone configurations were backed up before the
  change, and the failed first attempt rolled back cleanly before retry.
- The Creator-authorized token was installed non-interactively; no VPS browser or
  loopback OAuth flow is required for normal operation.
- Both the original bot-side `gdrive:` configuration and the dedicated YouTube runner
  configuration passed authenticated Drive API checks after migration.
- A standalone Drive file-ID retrieval through the dedicated runner succeeded with
  the Creator-owned OAuth client.
- The previous `shared Google Drive client_id` retirement warning was absent during
  that proof.
- `mirror-bot` remained untouched throughout migration and final verification;
  restart count remained zero.

## Promotion gates passed

- A temporary pre-registered profile intentionally used a channel ID different from
  the authenticated CHILIVIDS identity. The real OAuth callback returned HTTP 409,
  wrote a denied `channel_profile.bind` audit with `channel_id_mismatch`, stored no
  credential, left the profile disabled, and created no job, session, or video. The
  temporary profile/state/ticket rows were removed; the denied audit was retained.
- Runner `dedal-youtube-uploader/0.3.1` includes an explicit test-only
  `--test-interrupt-after-chunks` option. It stops only after YouTube has accepted a
  resumable chunk and progress has been recorded; rerunning the same job without the
  flag reuses the stored upload session and queries YouTube for the confirmed offset.
- The first live promotion attempt exposed a pre-upload Python compatibility defect:
  `hashlib.compare_digest` is unavailable. No YouTube session/video was created. The
  runner was corrected to `hmac.compare_digest`, promoted to v0.3.1, and redeployed
  without changing the `mirror-bot` start time or restart count.
- One fresh private Drive job then created exactly one resumable session. The first
  execution recorded one accepted 8 MiB chunk and stopped intentionally. The second
  execution reused that session, queried the confirmed remote offset, resumed the
  remaining bytes, and produced exactly one YouTube video.
- Gateway read-back verified exact video identity, locked channel ID, requested title,
  and `private` privacy before marking the job verified.
- Gateway version 0.3.0 implements optional playlist membership as the
  secondary operation. It verifies playlist ownership against the locked channel,
  checks for existing membership before insertion, inserts only when absent, and
  performs read-back verification. The live retry returned `already_present` with
  membership count one, proving duplicate-safe playlist behavior.

## MCP-ready control surface

- Gateway v0.3.0 is deployed at `youtube.drthorne.uk`; its D1 and existing secret
  bindings were preserved. It exposes bounded authenticated operations for channel
  profiles, recent videos, one-video read/update, private-first privacy and scheduling,
  playlists, upload jobs, analytics summary, and search terms.
- Public/unlisted changes still require explicit visibility intent. Scheduling still
  requires explicit publication intent. Every remote video/playlist mutation resolves
  a connected profile, refreshes server-side credentials, and reasserts the exact
  YouTube channel before mutation.
- A dedicated scoped `MCP_API_TOKEN` Worker secret lets a thin MCP service call only
  the bounded Gateway surface. It does not expose Google credentials or unrestricted
  Google API passthrough.
- `dedal-youtube-mcp` v0.1.0 is deployed at `mcp.youtube.drthorne.uk/mcp`. It stores no
  Google token, supports Streamable HTTP JSON-RPC, advertises 13 narrow tools, and
  implements OAuth discovery, dynamic client registration, authorization-code + PKCE,
  short-lived access tokens, rotating issuance, and hashed-token D1 storage.
- An end-to-end self-test passed OAuth discovery, registration, approval, PKCE token
  exchange, MCP initialization, tool listing, and a real `youtube_channels` call through
  MCP to Gateway. Test client/code/token/ticket records were removed afterward.
- Live Analytics calls currently fail at the Google upstream boundary. The configured
  OAuth scope is present; the likely remaining project-side prerequisite is enabling
  the YouTube Analytics API. Do not claim analytics retrieval until enabled and read back.

## Remaining integration boundary

1. Enable the YouTube Analytics API in the existing Google Cloud project, then rerun
   the bounded summary and search-term reads.
2. Register `https://mcp.youtube.drthorne.uk/mcp` in ChatGPT developer mode and complete
   the MCP OAuth screen with a fresh single-use Creator approval ticket.

The promotion gate is satisfied. `youtube-publishing` is active and classified KEEP.

## Intended normal control surface

Normal channel management is:

`ChatGPT / DEDAL -> dedal-youtube MCP -> Gateway -> YouTube Data/Analytics APIs`

Large media alone uses:

`Gateway upload job -> dedicated VPS runner -> direct resumable YouTube upload`

GitHub Actions remains a deployment, maintenance, and exceptional remote-execution
bridge. It is not the normal Creator-facing YouTube management interface.
