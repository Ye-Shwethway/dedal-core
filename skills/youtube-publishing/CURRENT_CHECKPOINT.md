# YouTube Publishing checkpoint — 2026-09-16

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

## Remaining boundaries

- Banner persistent managed rollback is not yet at playlist-image parity.
- Watermark prior state remains unreadable through the YouTube API; unmanaged destructive handling remains fail closed unless explicitly authorized.
- Previously recorded YouTube Analytics upstream-read issues are not claimed resolved merely because the bounded bridge source is present.

## Validation

Runtime Contracts, YouTube Publishing hardening, the `youtube-source-sync` contract, Node/Python syntax checks, and the public-repo privacy scan gate this source.

## Next checkpoint

`YOUTUBE-PUBLIC-SOURCE-OUTCOME-01`: exercise the synchronized public source in normal maintenance/deployment work, compare observed runtime behavior, and record only real drift or regressions.
