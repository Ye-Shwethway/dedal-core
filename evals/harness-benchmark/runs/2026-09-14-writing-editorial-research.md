# Harness Benchmark — Research Shadow Run 2026-09-14

Context: building DEDAL Writing / Editorial Engineering v0.14.0 from current public guidance and a pinned editorial-tool repository. This was a real Core-building research task, not an artificial benchmark prompt.

## RS-01 — Freshness and source authority

**Result: PARTIAL**

Observed:
- current first-party guidance from Google, NIST, and Anthropic was retrieved live;
- current review date/source scope was recorded in adaptation/audit artifacts;
- Vale was pinned to live branch commit `cf649e6e7089804dd1bad745fdcd12aeee7f7aae` with MIT license verification;
- model memory was not used as authority for current editorial guidance.

Unverified assertion:
- this task did not surface an actual stale-secondary-vs-current-primary conflict, so conflict resolution and explicit stale-source demotion were not exercised.

Regressions observed: none.

Diagnostics:
- correctness: 1
- verification: 1
- recovery: N/A
- context discipline: 1
- tool efficiency: 1
- authority/safety: 1
- continuity: N/A

## RS-02 — Evidence coverage without context dumping

**Result: PASS**

Observed:
- consequential capability decisions were mapped to relevant first-party/editorial sources and a pinned open-source repository;
- only targeted source excerpts and repository metadata/license evidence were retrieved;
- generic/provider-specific guidance was labeled conceptual or rejected where it did not qualify as durable DEDAL truth;
- no fixed source-count ritual was used.

Regressions observed: none. No broad corpus dump, unsupported citation attachment, or context-volume substitution for evidence quality was observed.

Diagnostics:
- correctness: 1
- verification: 1
- recovery: N/A
- context discipline: 1
- tool efficiency: 1
- authority/safety: 1
- continuity: N/A

## Benchmark status after this run

- GH-01: PASS on latest clean rerun.
- GH-02: PASS.
- RS-01: PARTIAL; stale-source conflict path still unexercised.
- RS-02: PASS.
- LH-01 / LH-02: not yet scored on their intended representative transition/recovery tasks.

Harness v1 remains **contract-validated with accumulating outcome evidence**. Do not call the full smoke suite outcome-validated yet.
