# YouTube SEO Evidence and Opportunity Model

## Principle

Retain the evidence vector. Compress to one heuristic score only when a decision surface truly benefits from it, and never hide the factors or imply first-party certainty.

## Recommended factors

| Factor | Meaning | Typical evidence |
|---|---|---|
| semantic_relevance | Query accurately describes the actual content | entity/content analysis |
| entity_specificity | Query targets concrete show/film/episode/character/action entities | entity graph |
| observed_channel_evidence | Similar terms already drove owned-channel search traffic | Analytics `YT_SEARCH` detail |
| trend_evidence | Relative/current interest evidence exists | Studio Trends / Google Trends / current public evidence |
| result_saturation_proxy | Result set is crowded with strong exact matches | live search observation |
| exact_match_gap | Results poorly satisfy the precise intent | live search observation |
| authoritative_competition | Official studio/network/major authoritative results dominate | live search observation |
| freshness | Current result set is old or newly active | published dates/current research |
| channel_fit | Query/content fits the channel niche/history | private profile + channel history |
| packaging_fit | A truthful compelling title/thumbnail can express the intent | package preflight |
| post_publish_evidence | Actual CTR/watch/search/retention response | owned analytics/reporting |

## Competition proxies

Allowed as transparent observations/proxies:
- exact-match coverage in a bounded top result set;
- result age/freshness distribution;
- median/representative public view counts when current video stats are fetched;
- channel-size proxies when current public channel data is fetched;
- official studio/network presence;
- dominant result content type;
- long-form/Shorts mix;
- semantic distance between the query and returned titles/descriptions.

Do not call these "true keyword difficulty".

## Evidence-strength guidance

A — owned first-party data can establish what happened on the Creator's channel, but privacy thresholds and aggregation limits still apply.

B — official documentation establishes platform semantics/contract, not how one specific video will perform.

C — live search observations establish a result landscape at a time/query/region, not universal rank.

D — external methods can suggest useful transforms/scoring ideas but do not inherit authority.

E — community observations are useful hypothesis generators, not causal proof.

## Missing-data behavior

When a field is unavailable:
1. mark it unavailable or unknown;
2. use an explicitly named proxy only when decision-useful;
3. lower confidence/evidence strength;
4. never backfill with invented precision.
