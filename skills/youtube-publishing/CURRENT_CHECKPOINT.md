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

## Promotion-test hardening prepared and deployed

- The gateway source already fails closed when OAuth resolves a YouTube channel ID
  different from the pre-registered profile: HTTP 409, denied audit record, and no
  credential storage. Upload claim and completion also re-assert the authenticated
  channel against the locked job channel. A deliberate live mismatch proof is still
  required.
- Runner `dedal-youtube-uploader/0.3.0` adds an explicit test-only
  `--test-interrupt-after-chunks` option. It stops only after YouTube has accepted a
  resumable chunk and progress has been recorded; rerunning the same job without the
  flag reuses the stored upload session and queries YouTube for the confirmed offset.
- Runner v0.3.0 is deployed on the VPS through the isolated GitHub Actions route.
  Deployment verified the new test flag, standalone Drive retrieval, absence of the
  shared-rclone-client warning, and unchanged `mirror-bot` start/restart state. No
  YouTube upload was performed by the deployment workflow.
- Gateway source version 0.2.0 now implements optional playlist membership as the
  secondary operation. It verifies playlist ownership against the locked channel,
  checks for existing membership before insertion, inserts only when absent, and
  performs read-back verification. Retrying completion is duplicate-safe because an
  existing playlist item is detected before insertion.
- Gateway v0.2.0 source is committed but is not yet claimed as deployed. The current
  tool surface has no existing GitHub Actions route for the Cloudflare Worker deploy;
  deployment requires the authorized Cloudflare execution path.
- Runtime CI now syntax-checks both the Python YouTube runner and the JavaScript
  gateway in addition to the existing contracts. Repo Integrity and Runtime Contracts
  are green for the hardening changes.
- `youtube-publishing` is explicitly classified `NEEDS_EVIDENCE` in the Core skill
  consolidation state until the live promotion gates below pass.

## Not yet verified

1. A deliberate live channel-ID mismatch rejection with no credential stored and no
   upload initiated.
2. A real interrupted resumable upload that resumes the same session/job and produces
   exactly one YouTube video.
3. A real playlist secondary operation with read-back verification.

The skill remains candidate.

## Next executable step

Use the authorized Cloudflare execution path once to deploy gateway v0.2.0 and verify
`GET /health` reports the new version. Then run the deliberate mismatch test without
an upload. Finally, use one fresh private video job with a valid Creator-owned
CHILIVIDS playlist to combine the remaining two gates: stop after the first accepted
chunk, rerun the same job to resume, verify exactly one resulting video, and verify
idempotent playlist membership by read-back. Promote the skill only after all three
live gates pass.