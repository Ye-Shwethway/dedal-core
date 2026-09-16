# YouTube SEO Measurement and Closeout Contract

## Purpose

Turn one-off SEO diagnosis into a repeatable prospective experiment loop without forcing metadata churn or pretending sparse data is conclusive. This contract is public-safe: real channel/video identifiers and actual outcomes belong in the private operational overlay.

## Experiment lifecycle

1. **T0 freeze** — after an approved package is applied and authoritatively read back, record the exact package, publication time, target surface, baseline SERP observations, public stats, and data availability.
2. **24h** — collect the first comparable launch window. Treat absent Analytics/Reporting rows as `unavailable/not_processed` unless the source explicitly establishes zero.
3. **3d** — compare against T0/24h without changing metadata merely because the sample is early.
4. **7d** — make the first directional readout: `supports`, `mixed`, `does_not_support`, or `inconclusive`. Preserve confounders and avoid causal language for sequential changes.
5. **28d** — produce the main learning readout using normalized-age context and traffic-source mix.
6. **Mature** — optional later/lifetime readout when enough volume or a specific decision warrants it.

Sparse channels may require longer windows. Window labels describe intended comparison points, not statistical significance.

## Minimum measurement bundle

When available, collect:
- authoritative current metadata/read-back and publication age;
- public statistics;
- per-video traffic-source mix;
- visible YouTube Search terms, explicitly marked non-exhaustive when privacy/detail suppression can apply;
- audience retention / relative retention;
- thumbnail impressions and CTR from a validated Reach source;
- bounded live SERP observations for the hypothesis queries, with query/time/region/language context;
- concurrent changes/confounders.

Do not make one unavailable source block the entire experiment. Record source availability independently.

## Availability semantics

Use distinct states:
- `observed_zero` — the authoritative source returned a supported zero value;
- `observed_nonzero` — the source returned measured data;
- `unavailable` — source/tool/report not available;
- `not_processed_yet` — expected source exists but the requested window has not populated;
- `suppressed_or_incomplete` — privacy/aggregation/detail limits make visible rows non-exhaustive;
- `error` — retrieval failed and should not be reinterpreted as zero.

Never collapse these into a single empty value.

## Stability / anti-churn rule

Once a prospective package is applied and verified, keep title/description/tags stable through the planned observation window unless one of these applies:
- factual error or unsupported entity claim;
- broken link/critical viewer-facing defect;
- explicit Creator-directed change;
- safety/policy/legal correction;
- experiment plan explicitly calls for a scheduled sequential change.

Weak early performance alone is not a defect and is not sufficient reason to rewrite.

## SERP measurement rule

SERP observations are bounded evidence, not universal rank. Record:
- exact query;
- region and relevance language when controlled;
- observation timestamp;
- result-set depth/page;
- owned result position within that returned set when present;
- obvious semantic drift.

Stop or down-weight deeper pagination when results drift materially away from the intended query universe. More pages are not automatically stronger evidence.

## Window record

```yaml
window: T0|24h|3d|7d|28d|mature
observed_at: <timestamp>
publication_age: <duration>
metadata_state: <authoritative summary>
public_stats:
  availability: observed_zero|observed_nonzero|unavailable|not_processed_yet|error
  values: {}
traffic_sources:
  availability: <state>
  rows: []
search_terms:
  availability: <state>
  exhaustive: false|unknown
  rows: []
retention:
  availability: <state>
  summary: <bounded observation>
reach:
  availability: <state>
  impressions: <value|null>
  ctr: <value|null>
serp_snapshot:
  availability: <state>
  observations: []
confounders: []
notes: []
```

## Readout semantics

- `supports` — observed evidence moves in the hypothesized direction with no stronger contradictory evidence; does not imply causation for sequential experiments.
- `mixed` — meaningful evidence points in different directions.
- `does_not_support` — the measured outcome runs materially against the stated hypothesis for the observed context.
- `inconclusive` — volume, source availability, suppression, or confounding prevents a useful directional read.

## Skill closeout gate

The YouTube SEO implementation can be considered **feature-complete for the current scope** when all are true:
1. surface-specific research and bounded SERP controls are implemented and live-validated;
2. viewer-facing metadata quality rules are encoded;
3. approved mutations remain owned by YouTube Publishing with authoritative read-back;
4. typed per-video traffic-source, search-term, and retention feedback paths are live-validated;
5. Reach/CTR has a validated job/report path or is explicitly optional until the first report materializes;
6. structured prospective experiment + measurement records exist;
7. normalized 24h/3d/7d/28d measurement semantics and missing-data states are encoded;
8. private channel learning and public sanitized promotion boundaries are enforced;
9. eval contracts cover no-fake-volume, bounded-rank claims, user-facing copy, anti-churn, missing-data semantics, and measurement readouts.

A pending real-world 24h/3d/7d/28d outcome does **not** block code/skill closeout; it is longitudinal validation of the already-implemented contract. New evidence may reopen the skill for refinement.
