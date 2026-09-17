# Discovery, Evidence, and Risk

## Discovery source roles

Use the narrowest source that actually measures the claim.

| Source | Best use | Do not infer |
| --- | --- | --- |
| Owned YouTube Analytics/Reporting | channel-specific search/referral/performance patterns | total market demand |
| Public YouTube search/API | current result landscape, exact-scene coverage, freshness, authoritative competitors | universal rank or absolute search volume |
| Official source metadata | title/episode/entity/source facts | YouTube demand |
| Google Trends/current web | relative freshness/current interest, regional/time context | YouTube-specific absolute volume |
| Community discussion | scene salience/discovery leads | canonical scene truth |
| Local audiovisual source | actual scene existence and exact editorial evidence | public demand |

## Search collection

For public YouTube evidence, record at least the query, observation time, region/language when material, result order/filter, and enough returned items to support the claim. `relevance`, `date`, and `viewCount` answer different questions; treat reduced/incomplete result sets and indexing delays as limitations.

Prefer multiple deliberately different queries over one keyword string repeated. Keep discovery breadth bounded by the decision value and API quota/cost.

## Owned-channel evidence

Useful signals include:

- search terms that already referred viewers;
- videos/channels that referred Suggested traffic;
- traffic-source mix;
- actor/franchise/scene-type adjacency;
- comparable-age outcomes for similar prior uploads.

Privacy thresholds and aggregation can hide low-volume detail. Missing rows mean `unavailable/suppressed/incomplete` when applicable, not zero demand.

## Factor vector

For every decision-worthy candidate, retain observations for:

- scene salience;
- channel fit;
- owned-channel evidence;
- observed demand;
- result saturation;
- exact-scene gap;
- authoritative competition;
- freshness;
- novelty;
- Suggested adjacency;
- packaging potential;
- editorial self-containment;
- source accessibility;
- reuse-risk signals;
- evidence confidence.

Each important factor should preserve `value | evidence/provenance | confidence | notes` rather than only a scalar.

## Optional heuristic

Only when candidate volume makes triage cumbersome, a transparent convenience score may combine positive opportunity factors and subtract competition/risk penalties. Rules:

- hard-gate failures cannot be scored into acceptance;
- expose components and weights;
- do not call it a YouTube score;
- do not learn stable weights from tiny samples;
- preserve the original evidence vector.

## Risk signals

Return `low_observed | moderate | elevated | unknown`. Consider only evidenced signals such as:

- raw-scene similarity/dependence;
- official-source dominance;
- music-heavy dependence;
- clip-length dependence;
- source/platform restrictions;
- prior channel claim/block patterns;
- transformative/editorial context;
- uncertainty about rights/source provenance.

Absence of observed enforcement is not evidence of legal safety. Candidate Finder does not provide legal clearance or fair-use guarantees.
