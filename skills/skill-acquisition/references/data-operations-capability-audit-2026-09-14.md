# Data Operations Capability Audit — 2026-09-14

## Goal

Determine whether Data / Spreadsheet / Operational Workflow Engineering deserves an independently routable DEDAL skill and which external patterns should be adapted.

## Sources reviewed

### Great Expectations / GX
- Current docs reviewed for Expectations, reusable Checkpoints, Validation Results, and post-validation Actions.
- Pinned repository snapshot: `fivetran/great_expectations` @ `3798c021bbfb0b13ff384b2238f643d04bdea5f2`.
- License: Apache-2.0 verified.

Useful patterns:
- encode important data assumptions as executable expectations;
- reusable validation checkpoints separate configuration from individual runs;
- persist validation results;
- trigger follow-up actions from observed validation results.

Rejected as universal Core behavior:
- framework-specific Python/config objects;
- requiring GX installation for spreadsheet or small operational workflows;
- treating schema/data quality as only a warehouse/pipeline concern.

### OpenRefine
- Current reconciliation documentation reviewed.
- Pinned repository snapshot: `OpenRefine/OpenRefine` @ `6d5d0579ee84c787eb31d04fa1676582f6e7b65e`.
- BSD 3-Clause-style license verified in `LICENSE.txt`.

Useful patterns:
- reconciliation is record/entity matching, not simple text cleanup;
- clustering/cleanup can precede reconciliation;
- matching should be iterative;
- ambiguous candidates require review rather than forced automation.

Rejected as universal Core behavior:
- OpenRefine project/UI mechanics;
- one reconciliation service protocol;
- assuming every workflow has an external canonical authority service.

### Microsoft Excel guidance
Current Microsoft documentation reviewed for formula/error auditing, inconsistent formulas, broken references/ranges, calculation behavior, and formula-cell protection.

Useful patterns:
- spreadsheets can contain syntactically valid but structurally inconsistent formulas;
- neighboring formula patterns and reference auditing are useful signals;
- formula cells and editable input cells may require different protection/handling;
- displayed values cannot always be trusted without calculation/reference context.

## Existing DEDAL gap

Domain skills such as MSA/PRA contain strong operational data rules, but those rules are intentionally specialized. Files handles artifact mechanics; Software Development handles code; Research handles external evidence. None owns the reusable lifecycle for operational data state transitions across spreadsheets/CSV/tables.

## Decision

**Adopt/Adapt as new top-level `data-operations` skill.**

Independent routing is justified because the domain has its own recurring failure modes:
- ambiguous source authority;
- unsafe deduplication/entity matching;
- formula/value confusion;
- silent row loss;
- production edits without staging/review;
- validation after rather than before promotion;
- irreproducible manual cleanup;
- missing lineage/audit evidence.

## DEDAL-native synthesis

Core lifecycle:
`authority -> record contract -> normalize -> reconcile -> validate -> stage -> review -> promote -> verify -> audit`

Promotion principles:
- ambiguity may remain unresolved;
- 100% match rate is not a quality goal;
- formula integrity is part of data integrity;
- staging is a risk-control mechanism, not ceremony;
- production read-back matters;
- domain-specific business rules remain with the owning specialized skill.

No third-party package or executable was installed or run during this audit.
