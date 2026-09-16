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

## Structured analysis record

For a decision-worthy video/candidate, retain a structured record rather than only prose. Fields may be omitted when genuinely unavailable, but must not be silently invented.

```yaml
object:
  kind: video|candidate
  id_or_private_ref: <private operational reference>
  publication_age/window: <launch|early|first_week|learning|mature|pre_publish>
objective: <launch research|existing diagnosis|experiment>
target_surface:
  primary: Search|Browse|Suggested|Mixed|Shorts
  confidence: low|medium|high
entities:
  franchise: []
  season_episode: []
  characters_actors: []
  scene_actions_topics: []
  variants: []
query_landscape:
  queries: []
  region: <observed region or unknown>
  language: <research language or unknown>
  observed_at: <timestamp>
  notes: []
factors:
  semantic_relevance: <observation>
  entity_specificity: <observation>
  observed_channel_evidence: <observation>
  result_saturation_proxy: <observation>
  exact_match_gap: <observation>
  authoritative_competition: <observation>
  freshness: <observation>
  channel_fit: <observation>
  packaging_fit: <observation>
evidence:
  - class: A|B|C|D|E
    source: <surface>
    claim_supported: <bounded claim>
missing_data: []
packaging:
  current: <summary>
  proposed_primary: <summary>
  alternates: []
hypothesis: <falsifiable expected direction, not guaranteed outcome>
confidence: low|medium|high
```

Public Core examples must use synthetic/private-neutral references. Real Creator video IDs, channel IDs, profile aliases, live analytics rows, and experiment outcomes belong in the private operational overlay.

## Experiment record

Record the hypothesis before a metadata mutation so post-publish analysis does not rewrite history.

```yaml
experiment_id: <private stable id>
object_ref: <private video/candidate ref>
created_at: <timestamp>
target_surface: Search|Browse|Suggested|Mixed|Shorts
hypothesis: <specific directional claim>
evidence_at_start:
  classes: []
  summary: <bounded baseline>
baseline_package:
  title: <current>
  description_summary: <current>
  tags_summary: <current>
  thumbnail_ref: <private ref if needed>
proposed_change:
  fields: []
  package_summary: <new package>
mutation:
  status: proposed|approved|applied|rejected|rolled_back
  applied_at: <timestamp or null>
observation_windows:
  - window: 24h|3d|7d|28d|mature
    traffic_source_mix: <when available>
    search_term_evidence: <when available>
    impressions_ctr: <when available>
    retention: <when available>
    notes: []
confounders: []
outcome_status: pending|supports|mixed|does_not_support|inconclusive
lesson_status: candidate|supported|superseded
```

A sequential metadata change is not a clean causal A/B test. Preserve traffic-source changes, age effects, audience expansion, seasonality, and concurrent content changes as confounders.

## Missing-data behavior

When a field is unavailable:
1. mark it unavailable or unknown;
2. use an explicitly named proxy only when decision-useful;
3. lower confidence/evidence strength;
4. never backfill with invented precision.
