# Harness Shadow Record — Visual Direction Build / GH-01 Regression

_Date: 2026-09-14_

Case: GH-01 Atomic multi-file mutation.

## Result
**FAIL -> safe recovery pending/finalized by v0.15 reconciliation commit.**

## Observed regression
During an intended atomic multi-file work unit, two direct contents writes were mistakenly invoked, creating temporary files `_should_not_use.tmp` and `_never.tmp` in two separate commits. This violates the atomic-mode tool allowlist and demonstrates that documentation-level rules do not enforce runtime tool selection.

## Recovery contract
- no force push or history rewrite;
- refresh live HEAD;
- use only `create_blob -> create_tree -> create_commit -> update_ref` for the reconciliation mutation;
- delete both temporary paths in the final tree;
- include the intended Visual Direction capability changes in the same reconciliation milestone;
- verify final diff/state and CI before completion claim.

## Lesson
The GitHub skill's allowlist remains useful guidance but is not a deterministic runtime guard. Future harness improvement should prefer an execution surface that can actually hide/disable forbidden mutation actions once a work-unit mode is locked.