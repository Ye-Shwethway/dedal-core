# YouTube Publishing checkpoint — 2026-09-16

## Phase status

The dedicated DEDAL YouTube MCP/Gateway path is active and has progressed from the original upload/playlist promotion gate into production hardening of media, caption, and branding mutations.

Normal control remains:

`ChatGPT / DEDAL -> dedicated YouTube MCP -> bounded Gateway -> YouTube APIs`

Large video bytes continue through the isolated uploader runner rather than MCP/Gateway.

## Newly live-gated

- **Captions:** list -> insert -> readback -> VTT download -> update -> delete -> final empty-state verification completed on an owned test video. The lifecycle intentionally restored the original state.
- **Thumbnail:** a same-asset thumbnail set completed end-to-end on an owned video and returned provider thumbnail variants.
- **Playlist images:** first insert/readback succeeded, followed by a real 512x512 hero-image insert. Production replacement is now managed delete -> insert -> readback with rollback to the previous managed source on insert failure.
- **Channel banner:** a valid 2560x1440 JPEG upload/apply/readback succeeded. Original artwork was restored through a full-resolution Google-hosted rendition source.

## Production lessons

### Playlist image replacement

Direct/native `playlistImages.update` is not a production dependency. Isolated attempts returned HTTP 400 `unexpectedPart`, including diagnostics pointing at the `part` parameter during resumable processing. Google API documentation/discovery behavior was not sufficiently consistent to justify relying on update semantics.

The safe path is:
1. detect existing image;
2. require DEDAL-managed baseline;
3. delete current image;
4. insert replacement;
5. read back and verify;
6. store the new managed source;
7. rollback to the previous managed source if insertion fails.

A second hero insertion also produced `IMAGE_TYPE_ALREADY_EXISTS`, reinforcing explicit replacement semantics.

### Banner recovery

`brandingSettings.image.bannerExternalUrl` is not guaranteed to be a reusable upload source. Preserve a recoverable/full-resolution banner source. A display URL alone is not rollback state.

### Watermark boundary

`youtube_watermark_set` and `youtube_watermark_unset` are exposed, but watermark lifecycle is **not fully live-gated**. The Data API has no reliable get/list baseline for the current watermark. An unmanaged watermark therefore fails closed: DEDAL must not unset/replace it without managed-state evidence or explicit Creator authorization for the unmanaged destructive action.

## Diagnostics

The production debugging loop is:

`dedicated MCP call -> bounded Gateway route -> stage-aware D1 mutation audit -> exact vendor error -> minimal patch -> one bounded retry -> read-back verification -> checkpoint`

Useful audit metadata includes action/outcome, bounded resource IDs, stage, error code, vendor status/reason/message/location/location-type, and resumable sub-stage diagnostics. Secrets/tokens are excluded.

## Runtime-version evidence

The latest external live verification supplied for this hardening sequence reported Gateway `0.7.35` (with managed playlist replacement already present by `0.7.34`). The repository source snapshot still identifies itself as `0.3.0`; this reconciliation therefore records the behavioral/live evidence without pretending the public source is an independently verified byte-for-byte mirror of the deployed Worker. Exact deployed/source equivalence remains an explicit source-sync task.

The MCP remains the dedicated bounded tool layer. Its public repo snapshot identifies itself as `0.1.0`; an exact newer deployed MCP version was not independently established in this repo reconciliation.

## Safety boundary retained

Exact ownership verification, dedicated typed tools, explicit action/destructive/publication intent, bounded retries, post-mutation readback, rollback capture, and fail-closed handling of unreadable prior state remain mandatory.

## Next checkpoint

`YOUTUBE-SOURCE-SYNC-01`: recover/compare the currently deployed Gateway/MCP source against the public repo, import only the verified missing implementation delta, and add managed baseline/rollback for banner and watermark before claiming watermark lifecycle live-gated.
