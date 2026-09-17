# Candidate Video Finder — Adaptation Notes

## Capability gap

DEDAL already had YouTube SEO, Video Production, Visual Direction, Publishing, Research, and Decision Design, but no owner for the upstream question: **which specific scene-level candidate should enter production next?** Reusing YouTube SEO alone would blur candidate discovery/verification with post-candidate packaging and measurement.

## Adopted patterns

- From current YouTube Data API semantics: public search results are bounded observations with query/order/date/filter semantics, not universal demand/rank truth.
- From YouTube Analytics/Reporting: owned traffic-source and search-term detail is high-value channel-specific evidence but may be incomplete/suppressed and cannot prove external market size.
- From Google Trends: use current relative trend/freshness evidence when available, with explicit geography/timeframe; do not translate it into absolute YouTube search volume.
- From PySceneDetect methodology: automated cut/transition boundaries can accelerate local inspection, but detected cuts are technical segmentation aids rather than editorial scene truth.
- From `artdelpi/youtube-trend-finder`: separate volatile trend evidence from stable channel/editorial profile context; keep raw evidence and profile-fit reasoning distinct. No source code was copied or executed.

## DEDAL-native adaptations

- Atomic candidate is a specific bounded scene/event, not a topic or whole episode.
- Deterministic hard gates precede opportunity comparison.
- Factor vectors remain visible; convenience scoring is optional and non-authoritative.
- Creator selection is explicit and private.
- Exact cut authority transfers to Video Production once local media is inspected.
- YouTube SEO remains downstream owner of Search/Browse/Suggested strategy and packaging.
- Public Core stores generic methodology only; CHILIVIDS-specific learning stays in the private overlay.

## Rejected patterns

- automatic "best video" selection without Creator review;
- popularity-only ranking;
- opaque weighted score as the primary output;
- model-memory scene claims without source evidence;
- treating community discussion as canonical source truth;
- treating scene-detection output as an editorial cut decision;
- automated legal/copyright clearance claims;
- full-web scraping or third-party downloader dependence as a Core requirement.

## Evaluation target

Promotion requires routing separation from YouTube SEO/Production/Publishing, hard-gate behavior, source-truth discipline, private-learning isolation, and a useful shortlist handoff without fake precision.
