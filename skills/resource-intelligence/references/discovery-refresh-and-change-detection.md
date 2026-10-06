# Discovery, refresh, and change detection

## Two-lane discovery

Every persistent discovery system should balance:

1. **tracked focus** — due/stale known resources, unresolved leads, known high-fit entities, adjacent relationships;
2. **unseen exploration** — new sources, novel entities, adjacent categories, fresh releases/publications/versions, and long-tail opportunities.

Do not freeze a universal percentage. Adjust exploration upward when the catalogue becomes repetitive, source diversity is low, or qualified yield from tracked focus drops. Adjust focus upward when known targets are volatile or have imminent events.

## Refresh plan

Before searching, partition records into:

- due/volatile;
- unresolved/conflicted;
- stable/not due;
- retired/ignored unless reactivation evidence appears.

Generate targeted queries only for the first two plus a bounded exploration set. Prefer conditional/date/version-aware checks where source capabilities allow.

## Delta classes

Classify each material refresh result:

- `NEW`: previously unknown resource, opportunity, or material claim;
- `CHANGED`: previous current value materially differs;
- `CONFIRMED`: independent/current evidence confirms existing state;
- `STALE`: existing fact exceeded its freshness policy without current verification;
- `NO_CHANGE`: targeted check found no material difference;
- `REMOVED_OR_UNAVAILABLE`: previously resolvable resource/source no longer available;
- `CONFLICT`: credible evidence disagrees and cannot yet be reconciled.

`NO_CHANGE` is valid only after a meaningful targeted check; absence of a search hit is not proof of no change.

## Query expansion and stopping

Use aliases, relationships, source families, changed fields, and consumer needs to create bounded queries. Stop when evidence is sufficient for the requested decision, the marginal qualified yield is low, or the time/context budget is reached. Persistent intelligence should reduce search, not institutionalize endless browsing.

## Freshness

Facts have different half-lives. Package versions, prices, availability, schedules, releases, and current roles may decay quickly. Stable identity, historical publication data, and immutable identifiers decay slowly. Refresh fields based on volatility rather than refreshing every record equally.