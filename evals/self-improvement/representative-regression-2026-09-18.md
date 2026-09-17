# Representative Self-Improvement Regression Replay — 2026-09-18

## Purpose

This is a public-safe replay of the real failure pattern that justified a dedicated Self-Improvement closure layer. It records system behavior, not private project identifiers or credentials.

## Observed pattern

1. A deployed integration had a user-visible authentication/workflow defect.
2. A live production hotfix restored the intended user path.
3. The live fix was not fully reconciled into canonical repository source and durable regression coverage.
4. Later engineering work used the stale canonical source as an input.
5. Retired behavior was reintroduced, forcing the same class of debugging and repair again.

The important failure was not that the first repair was technically wrong. The learning loop closed too early.

## Baseline closure behavior

The older operating discipline could plausibly treat this sequence as complete after:

- the live user path worked again;
- a lesson or checkpoint mentioned the fix;
- local/production verification passed.

That was insufficient because canonical source could still reproduce the old behavior.

## New closure contract replay

### State A — live repair only

- runtime repair: fixed and verified
- canonical sync: pending
- regression guard: absent or incomplete
- durable learning: partial
- independent verification: available
- unresolved debt: source-sync

Expected decision: **do not retain as durably closed**.

`closure-contract-v2` represents this state with `SIC-02` and rejects it.

### State B — durable closure

- runtime repair: fixed and verified
- canonical source: reconciled
- regression guard: added or existing
- durable lesson: captured at correct scope
- continuity: updated when future work depends on it
- independent verification: passed
- unresolved debt: empty

Expected decision: **eligible for retain/closure**.

`closure-contract-v2` represents this state with `SIC-01` and accepts it.

## What this proves

This replay provides representative incident evidence that the new contract distinguishes the exact incomplete-closure state that allowed recurrence from a durably reconciled state.

It does **not** yet prove long-run outcome improvement. Stronger outcome evidence requires future real work showing lower recurrence/rework against a comparable baseline.

## Regression expectation

Future material production hotfixes must create explicit source-sync debt when canonical source has not yet been reconciled. A repeated known failure should trigger inspection of the previous learning closure before being treated as an unrelated fresh bug.
