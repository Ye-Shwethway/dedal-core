# Candidate Video Finder Capability Audit — 2026-09-17

## Gap

Existing DEDAL skills covered YouTube discovery/packaging (YouTube SEO), editing (Video Production), images (Visual Direction), publishing (YouTube Publishing), and external fact research. None cleanly owned the upstream workflow of discovering and verifying **specific scene-level candidates** before production while preserving Creator selection and private channel learning.

## Sources reviewed

### YouTube Data API — `search.list`
Official Google documentation reviewed 2026-09-17. Useful for bounded public result observations with query, order, publication windows, region/language and pagination. Search results and ordering are not treated as universal rank or absolute demand. Current documentation also notes possible indexing delays/incomplete result behavior and quota cost.

Decision: **ADOPT semantics, not a new dependency**. Reuse the existing DEDAL YouTube MCP/Data API surface.

### YouTube Analytics / Reporting traffic-source detail
Official Google documentation reviewed 2026-09-17. `traffic_source_detail` can expose search terms for YouTube Search traffic and referring video IDs for Suggested/referral contexts, subject to aggregation/privacy limitations.

Decision: **ADOPT as owned-channel evidence** through existing YouTube SEO/Publishing transport. Missing detail is not zero demand.

### Google Trends
Official Google Trends help reviewed 2026-09-17. Trending/Explore surfaces provide relative, time- and region-scoped interest plus related queries and export/UI evidence; they do not establish absolute YouTube search volume.

Decision: **ADAPT for freshness/current-interest evidence** when available through live research or Creator-assisted UI evidence. No unsupported Core API dependency.

### Breakthrough/PySceneDetect
Public repository/documentation reviewed 2026-09-17. Current public material describes technical scene/cut detection and start/end timecode lists; repository license is BSD-3-Clause.

Decision: **METHOD-ONLY**. Automated scene detection may accelerate local inspection but cannot replace Video Production's audiovisual/editorial boundary verification. No package installed or executed for this audit.

### `artdelpi/youtube-trend-finder`
Public repository reviewed 2026-09-17. Useful comparative pattern: separate volatile trend evidence from stable editorial/channel profile context, preserve raw evidence, track previously covered subjects, and distinguish trend strength from profile fit.

License was not established from the reviewed surface, so no code/text was copied.

Decision: **METHODOLOGY-ONLY**, DEDAL-native rewrite.

## Architecture decision

Promote a new independently routable `candidate-video-finder` because the workflow occurs before Video Production and before YouTube SEO packaging, requires distinct source/scene verification and Creator selection state, and would otherwise blur ownership across existing skills.

Public Core contains only generic methodology/evals. CHILIVIDS-specific candidate history, Analytics, preferences, scores/weights, selections, and risk history remain private overlay data.

## Promotion criteria

- route candidate discovery to the new skill without stealing existing SEO/edit/publish intents;
- require source/scene truth and hard gates;
- preserve evidence provenance and uncertainty;
- no autonomous publishing or legal certainty;
- exact cut authority transfers to Video Production;
- channel-specific learning remains private;
- executable routing validator and regression cases pass.
