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
- Source-truth and demand/opportunity are separate axes.
- Local audiovisual verification is authoritative for final cut boundaries once media is available.
- Copyright/reuse results are risk signals, not legal clearance.
- Creator selection remains the decision gate.
- Channel-specific Analytics, candidate history, preferences, selections and weights remain private operational state.

## Rejected patterns

- opaque "overall opportunity score" as the sole decision mechanism;
- fake/synthetic absolute search volume;
- ranking without source/scene verification;
- autonomous publishing;
- binary copyright-safe claims;
- automatically treating scene-detection boundaries or recap timestamps as canonical cut boundaries;
- copying third-party trend-finder code/data into Core;

## Evaluation

A focused 12-case contract covers routing boundaries, bad-source rejection, channel-fit gating, duplicates, opaque-score refusal, risk uncertainty, Creator authority, private learning and cut-locator boundaries.
