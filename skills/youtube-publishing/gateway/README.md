# DEDAL YouTube Gateway

Production-minded Cloudflare control plane with a separate VPS byte-transfer runner. Video bodies go from the runner directly to YouTube and never through the Worker.

## Deployment and source identity

- Worker: `dedal-youtube-gateway`
- Domain: `https://youtube.drthorne.uk`
- D1: `dedal-youtube-gateway-prod` (`DB`)
- API family: `v1`
- Latest external hardening evidence in the 2026-09-16 checkpoint reports deployed Gateway `0.7.44`.
- Public source version: `0.4.4`.
- Authorized deployed-reference version used for source sync: Gateway `0.7.44`.
- Public and deployed version numbers are intentionally independent. `YOUTUBE-SOURCE-SYNC-01` reconciles verified behavior/source deltas; it does **not** claim byte-for-byte identity with the deployed Worker export.

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

## Source-sync status

`YOUTUBE-SOURCE-SYNC-01` imports the verified public-safe implementation delta reconstructed from authorized deployed-source inspection. Raw Worker exports, live operational identifiers, credentials, D1 rows, debug assets, and Creator-specific state are intentionally excluded. The public source is behaviorally reconciled for the covered contracts, not asserted to be byte-for-byte deployment parity.

## Video metadata read-back

Video snippet updates use bounded eventual-consistency verification for every requested mutable field. Tag comparison is order-insensitive because YouTube may normalize tag order. A mutation is not reported successful until requested title, description, category, and tags are independently read back.
