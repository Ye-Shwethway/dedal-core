# Changelog

All meaningful DEDAL Core architectural and behavioral changes should be recorded here.

## 0.30.0 — 2026-09-16

### Added
- `skills/youtube-seo/` as a first-party-data-first discovery-intelligence faculty for query/entity research, Search/Browse/Suggested surface strategy, packaging hypotheses, analytics diagnosis, experiment design/readout, and channel learning.
- Transparent YouTube SEO evidence classes and opportunity-factor model that refuse unsupported absolute search volume, universal difficulty, guaranteed rank, or magic-score certainty.
- YouTube SEO routing/eval contract with explicit ownership separation from YouTube Publishing and private-overlay learning.
- Structured YouTube SEO analysis and prospective experiment records for preserving target surface, entity/query evidence, baseline package, hypothesis, missing data, confounders, normalized observation windows, and outcome status.

### Changed
- YouTube Publishing now owns authenticated YouTube operations and bounded API/MCP transport while YouTube SEO owns discovery intelligence; approved SEO changes still pass through Publishing intent/read-back gates.
- YouTube Publishing source now includes dedicated owned-video traffic-source, search-term, and retention read helpers for the YouTube SEO feedback loop; deployed references advanced to Gateway `0.7.43` / MCP `0.8.2`.
- Reporting bridge failures now persist bounded upstream diagnostics to private audit state, allowing service/configuration errors to be distinguished from MCP or aggregation transport failures without exposing credentials.
- Capability routing/registry/consolidation state now recognizes YouTube discovery intelligence as independently routable without turning Data/Analytics/Reporting APIs or third-party SEO tools into faculties.
- YouTube SEO packaging now includes an explicit viewer-facing metadata quality gate: concise natural descriptions, useful context first, verified entities, no internal archival/workflow notes, no keyword dumping, and title/description/thumbnail promise consistency.

## 0.29.0 — 2026-09-16

### Added
- Optional Library-only private operational overlay contract for Creator/project-specific non-secret context, loaded manifest-first and only when task-relevant.
- Fail-closed public privacy guard rejecting private-overlay paths or overlay manifests if they enter the repository tree.

### Changed
- Boot authority now distinguishes public Core contracts, private operational context, live connected-service state, and GitHub repository identity.
- Private overlay data is explicitly excluded from GitHub mutation candidates, public patches, release archives, and public fixtures; actual credentials remain outside both Core and the overlay.

## 0.28.0 — 2026-09-16

### Added
- Cloudflare Worker deployment/connector-recovery reference covering live-source identity, transport fidelity, raw/multipart upload recovery, outcome-unknown mutations, aggregation-layer verification, and automation-first mobile workflows.
- Executable `cloudflare-platform-operations` contract with eight representative failure/recovery cases.

### Changed
- Cloudflare Platform now distinguishes repository/build/deployed/sanitized source identities and forbids replacing newer live Worker code with stale repository source without proven equivalence.
- Connector read/discovery capability no longer implies source-upload fidelity; request serialization failures trigger execution-surface switching rather than application-code distortion.
- Post-mutation transport/read-back errors require state verification before retry when the upstream mutation may already have committed.
- Manual production source editing is a last resort when authorized automation remains practical, with explicit attention to mobile-constrained Creator workflows.
- Cloudflare and integration-aggregation connected capability are marked `verify_per_session` in the public capability registry.
- YouTube hardening validation no longer hardcodes the global Core next-checkpoint ID, preventing unrelated domain checkpoints from causing false CI failures.

### Fixed
- YouTube playlist visibility updates now preserve mandatory snippet metadata and include the required `snippet` part, fixing `400 unexpectedPart` failures on privacy-only changes.
- Video privacy and scheduling mutations now use bounded eventual-consistency read-back; privacy changes also verify scheduled `publishAt` state is cleared, while accepted schedules can report `accepted_pending_readback` instead of a false failure.
- Live outcome validation covered private/unlisted/public round-trips and schedule creation/cancellation, with controlled round-trip state restored during the test before any later Creator-directed publication decisions.
- The existing DEDAL YouTube MCP was also outcome-validated through an aggregation layer for dedicated playlist/video public-visibility mutations, authoritative Data API read-back, and Creator-side YouTube Studio confirmation; the aggregator remains a runtime execution surface rather than the semantic source of truth.

## 0.11.0 — 2026-09-14

### Added
- `skills/agent-engineering/references/dedal-self-application.md` for applying Agent Engineering to DEDAL's own context loading, tool use, Git transactions, polling, completion evidence, progress communication, and long-horizon continuity.
- `evals/agent-engineering/dedal-self-audit-v1.md` as the first explicit baseline audit of DEDAL's own harness.

### Changed
- GitHub operations now require preflight against authoritative repository state before mutation when live access exists.
