# YouTube Publishing checkpoint Ã¢ÂÂ 2026-09-16

## Phase status

`YOUTUBE-SOURCE-SYNC-01` is complete for the public repository source surface. The dedicated YouTube MCP/Gateway path remains:

`ChatGPT / DEDAL -> dedicated YouTube MCP -> bounded Gateway -> YouTube APIs`

Large video bytes continue through the isolated uploader runner rather than MCP/Gateway.

## Public source reconciliation

The public Gateway now carries the verified public-safe source delta for external-media guards, captions, thumbnails, playlist images, banner diagnostics, watermark safety boundaries, bounded Data/Reporting/Analytics bridges, and dedicated video deletion. Native media staging now uses a dedicated short-lived Cloudflare Worker/KV service behind authenticated Gateway stage/unstage routes, removing the normal dependency on credit-metered upload-to-URL services. The MCP surface exposes 54 bounded `youtube_*` tools, including native ephemeral media stage/unstage operations. Three dedicated read-only SEO analytics helpers now expose owned-video traffic sources, owned-video search terms, and owned-video retention without requiring callers to assemble generic Analytics queries. `youtube_search` also exposes bounded SEO research controls for region, relevance language, publication bounds, pagination, and safe-search policy without forcing owned-only results.

Playlist-image replacement requires a managed baseline and uses delete -> insert -> read back with rollback to the previous managed source if insertion fails. Native `playlistImages.update` is not a production replacement dependency.

Raw deployed Worker exports, credentials, Creator-specific resource identifiers, live audit rows, internal debug assets, and operational Cloudflare identifiers are not part of the public source snapshot.

Channel-management outcome validation now covers playlist `private -> unlisted -> private`, playlist `private -> public -> private`, video `private -> unlisted -> private`, video `private -> public -> private`, and private-video scheduled publication with independent read-back plus schedule cancellation. Playlist updates preserve required snippet metadata, and video visibility/scheduling read-back tolerates bounded YouTube propagation delay without silently claiming unverified completion.

Aggregation-layer outcome validation also passed with the existing remote MCP preserved as the semantic/tool-schema source. Through the aggregation surface, DEDAL discovered and invoked the dedicated playlist/video visibility tools, independently read back authoritative YouTube status through the bounded Data API bridge, and received Creator-side YouTube Studio confirmation of the resulting public visibility. This validates the tested aggregation path for these operations; availability and fidelity remain `verify_per_session` runtime facts rather than permanent Core assumptions.

## Version identity

- Public Gateway source: `0.4.6`
- Authorized deployed Gateway reference used for reconciliation: `0.7.47`
- Public MCP source: `0.2.3`
- Authorized deployed MCP reference used for reconciliation: `0.8.4`

These version lines are intentionally independent. The checkpoint establishes public-safe behavioral/source reconciliation for the covered contracts; it does not claim byte-for-byte parity with deployed exports.

Reporting API failures now record bounded upstream diagnostics in the private mutation audit. Live outcome testing has now passed Reporting API service enablement, report-type discovery, and scheduled-job creation/read-back. Generated Reach report availability remains asynchronous and should be verified before impressions/CTR are treated as available evidence.

Video metadata writes now use bounded eventual-consistency read-back for all requested snippet fields, including order-insensitive tag verification. This closes a live case where title/description committed but immediate tag state was not verified.

Thumbnail mutation hardening now records bounded `media` versus `upload` failure stages. A live custom-thumbnail case confirmed that browser-accessible third-party CDN media may still be unfetchable from the Gateway, while a Gateway-fetchable staged source succeeds. Public Core therefore treats DEDAL-controlled ephemeral media staging plus Gateway fetch preflight as the preferred future workflow; external credit-metered upload hosts are fallback-only.

## Native media staging live validation

After the custom MCP catalog was resynchronized, the deployed 54-action surface exposed `youtube_media_stage` and `youtube_media_unstage` with the expected typed schemas. A known-good PNG completed the live stage path and returned bounded metadata, a short-lived signed HTTPS source URL, and a stage id; explicit unstage then deleted the object successfully. Temporary validation objects were cleaned up.

The existing approved production thumbnail was intentionally left unchanged during this validation. A malformed/truncated large Base64 test payload failed before any YouTube mutation, so this does not count as a production-thumbnail failure. Future callers should transfer the approved file bytes intact before invoking `youtube_media_stage`; do not silently recompress or substitute a lower-quality asset merely to satisfy transport limits.

## Remaining boundaries

- Banner persistent managed rollback is not yet at playlist-image parity.
- Watermark prior state remains unreadable through the YouTube API; unmanaged destructive handling remains fail closed unless explicitly authorized.
- Previously recorded YouTube Analytics upstream-read issues are not claimed resolved merely because the bounded bridge source is present.

## Validation

Runtime Contracts, YouTube Publishing hardening, the `youtube-source-sync` contract, Node/Python syntax checks, and the public-repo privacy scan gate this source.

## Next checkpoint

`YOUTUBE-PUBLIC-SOURCE-OUTCOME-01`: exercise the synchronized public source in normal maintenance/deployment work, compare observed runtime behavior, and record only real drift or regressions.


- Native staging transport hardening: chunked upload/finalize added for MCP body limits; deployed target Gateway 0.7.48 / MCP 0.8.5 / staging Worker 0.1.1; expected MCP surface 56.

- Chunk transport was revised after live validation: production MCP remains 0.8.4 / 54 actions; Gateway 0.7.49 transparently multiplexes chunk/finalize control envelopes through existing `youtube_media_stage`. This avoids deploying sanitized public MCP auth code over the prod-specific MCP runtime.

- Output-schema compatibility hardening: chunk acknowledgements now retain the existing `youtube_media_stage` required response fields and set `pending: true`; only finalize returns a usable signed URL. Target Gateway 0.7.50.

## Thumbnail Workflow â CLOSED

Status: CLOSED / production-validated.

Closure criteria met:
- layered strategy/content-truth/reference/generation/QA workflow is documented;
- creator-approved asset preservation rules are documented;
- DEDAL-owned native staging replaces credit-metered third-party upload hosts as the default path;
- bounded chunk transport is production-validated for larger thumbnail assets;
- thumbnail mutation, authoritative read-back, cleanup, and experiment/confounder recording are operational;
- live Shadow and Bone validation passed end-to-end;
- future work should reopen this section only for a contract gap, vendor/API change, or materially new thumbnail capability.
## Video Rating Support â bounded bridge

The YouTube Data API allowlist already includes `videos.getRating` and `videos.rate`. A live read-only `getRating` call succeeded for the connected channel identity. A dedicated 56-action MCP alias deployment was tested but caused the existing aggregation OAuth connection to return 401; it was immediately rolled back to the known-good MCP `0.8.4` / 54-action deployment.

Current supported path is therefore the existing allowlisted `youtube_data_api` bridge: `getRating` is read-only; `rate` accepts only `like`, `dislike`, or `none` and remains behind the bridge's explicit-action gate. Dedicated rating aliases are deferred until the production MCP auth source can be reconciled without invalidating existing clients. No live rating write was performed during this extension.

## YouTube Reporting / Measurement Transport — CLOSED

Status: CLOSED / production-validated transport.

The first generated `DEDAL SEO Reach Basic` (`channel_reach_basic_a1`) report was downloaded through the authenticated bounded Reporting bridge. The live CSV schema was verified as `date,channel_id,video_id,video_thumbnail_impressions,video_thumbnail_impressions_ctr`; the payload was complete (`truncated: false`) and demonstrated that scheduled reach files can arrive several days after their measured window.

Gateway `0.7.51` adds bounded `reports.download` support with authenticated vendor fetch, report metadata, a 2,000,000-character response cap, and an explicit truncation flag. User-facing Reach reports must enrich report `video_id` rows with live-resolved video titles whenever readable, retain the ID for traceability, and never treat CTR zero as zero views. Historical pre-publication windows validate the pipeline but are not evidence for a later video experiment.

With metadata/publishing, thumbnail, captions, playlists, comments, ratings, Analytics/Reporting transport, ownership/intent gates, read-back, and source-sync boundaries all covered at the current scope, YouTube Publishing is CLOSED / capability-complete. Reopen only for a contract defect, vendor/API change, production regression, or Creator-requested materially new capability. Longitudinal SEO measurement remains observation work and does not reopen Publishing.

