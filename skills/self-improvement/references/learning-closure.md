# Learning Closure Contract

Use this after a correction, regression, incident, or verified better workflow that may matter again.

## Durability triage

Classify the event as `transient` or `durable`. Transient events may close with a short no-promotion reason. Durable events require closure evidence.

## Durable closure matrix

A durable correction is not fully closed until all applicable rows are resolved:

| Layer | Required question | Acceptable evidence |
|---|---|---|
| User/runtime path | Is the affected behavior restored? | representative call/task/read-back |
| Canonical source | Can a future deploy/restart reproduce the fix? | repository/skill/config read-back at accepted revision |
| Regression guard | Would the previous failure now be caught? | focused test, eval, invariant, or explicit `not_testable` rationale |
| Durable learning | Will future sessions know the corrected rule without chat replay? | public Core rule or private lesson with correct scope/provenance |
| Continuity | Does future work depend on this state? | checkpoint/handoff update or explicit `not_required` |
| Verification independence | Did the candidate avoid grading itself? | independent CI/read-back/verifier or protected evaluator |
| Rollback/recovery | Can the change be safely reversed or compensated? | rollback path, prior revision, or explicit irreversibility note |

## Source-sync debt rule

When production/live behavior is changed outside canonical source, immediately create source-sync debt. The incident may be mitigated, but it is not durably closed until canonical source is reconciled and verified.

Never use `works in production now` as evidence that repository drift is harmless.

## Reopen rule

Reopen a supposedly closed learning when the same failure recurs, canonical source contradicts accepted live behavior, a later change removes the regression guard, outcome validation contradicts the original hypothesis, or the durable lesson is stale/overgeneralized.

The second occurrence is evidence that the previous learning loop may have been incomplete.
