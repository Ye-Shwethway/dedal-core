# DEDAL YouTube Gateway

Production-minded Cloudflare control plane with a separate VPS byte-transfer runner. Video bodies go from the runner directly to YouTube and never through the Worker.

## Deployment and source identity

- Worker: `dedal-youtube-gateway`
- Domain: `https://youtube.drthorne.uk`
- D1: `dedal-youtube-gateway-prod` (`DB`)
- API family: `v1`
- Latest external hardening evidence in the 2026-09-16 checkpoint reports deployed Gateway `0.7.35`.
- The source snapshot currently committed under `gateway/src/` still identifies itself as `0.3.0`. Treat deployed/source equivalence as **unverified** until `YOUTUBE-SOURCE-SYNC-01` compares the deployed Worker source against this repository.

Do not “fix” this identity gap by changing a version constant without recovering the corresponding implementation.

## Security contract

- Pre-register alias + exact `channel_id` before OAuth.
- OAuth state is browser-bound, short-lived, and single-use; credentials remain encrypted at rest.
- Every mutation rechecks authenticated channel ownership.
- Prefer dedicated typed MCP/Gateway routes over generic passthrough mutation.
- Consequential writes require explicit action intent; deletes/unsets require explicit destructive intent; visibility/scheduling retain their specific intent gates.
- Read back mutations whenever YouTube exposes readable state.
- Replace-style media requires recoverable managed state before destructive replacement.
- If prior state cannot be read/recovered, fail closed unless the Creator explicitly authorizes unmanaged destructive handling.
- D1 audit diagnostics must be sufficient for vendor debugging without persisting secrets/tokens.

## Production-hardened mutation families

Live evidence covers:
- private resumable upload and recovery;
- playlist membership;
- thumbnail upload;
- caption list/insert/download/update/delete lifecycle;
- playlist-image insert/readback and managed replacement;
- channel-banner valid upload/apply/readback plus full-resolution restoration.

Playlist-image replacement uses managed state and delete -> insert -> readback rather than relying on `playlistImages.update`. Banner rollback requires a recoverable/full-resolution source; display-oriented `bannerExternalUrl` alone is not sufficient.

Watermark set/unset remains exposed but not fully live-gated because prior watermark state cannot be reliably read. Unmanaged watermark state must fail closed.

## Stage-aware mutation audit

For hard failures use:

`MCP -> bounded Gateway route -> stage-aware D1 audit -> vendor error extraction -> minimal patch -> one bounded retry -> readback`

Capture bounded fields such as action, outcome, resource identifiers, stage, error code, vendor status/reason/message/location/location type, and safe resumable sub-stage diagnostics. Never capture OAuth tokens, bearer secrets, cookies, or raw credentials.

See `../references/mutation-hardening-and-recovery.md` and `../CURRENT_CHECKPOINT.md` for current production lessons.

## Source-sync limitation

This public repository is the durable Core, but the deployed Worker advanced during live hardening faster than the checked-in source snapshot. Until the deployed source is recovered and compared, use this repository for contracts/checkpoints and use the live service only as runtime evidence; do not claim repo source parity.
