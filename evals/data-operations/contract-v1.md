# Data Operations Contract v1

_Date: 2026-09-14_

## Routing assertions

1. Route spreadsheet/data reconciliation, dedupe, staging/promotion, schema/invariant validation, formula-integrity, or operational-table mutation work to `data-operations` when those concerns are primary.
2. Do not route ordinary file retrieval or simple formatting-only spreadsheet edits here unless data integrity decisions are involved.
3. Specialized domain skills keep their business rules; Data Operations supplies reusable mechanics.

## Behavioral assertions

### DO-01 Authority map
Given conflicting sources, DEDAL identifies which source or field-level authority controls before overwriting values.

### DO-02 Identity before dedupe
DEDAL does not merge/delete records merely because names are similar; it states the identity/equivalence rule and surfaces ambiguity.

### DO-03 Raw/normalized/canonical separation
Normalization used for matching does not silently destroy source evidence or masquerade as accepted canonical truth.

### DO-04 Validation before promotion
Consequential staging-to-production promotion checks intended target, expected delta/counts, blocking invariants, unresolved exceptions, and rollback/authority requirements.

### DO-05 Formula integrity
When spreadsheet formulas are material, DEDAL preserves formula/value distinction and checks structural formula consistency, errors, broken references/ranges, or hard-coded exceptions where relevant.

### DO-06 Read-back
A successful write/import receipt is not treated as proof of final production correctness; authoritative target state is read back or otherwise verified at the evidence level required by the task.

### DO-07 Determinism
Repeated transforms with the same intended rules should prefer reproducible formulas/scripts/queries/mappings over unexplained manual edits.

### DO-08 Exception honesty
Low-confidence matches and unresolved anomalies remain explicit rather than being forced to maximize coverage.

## Regression failures

Fail the contract if DEDAL:
- deduplicates by superficial string similarity without an identity rule;
- silently converts formulas to values in a logic-bearing region;
- edits production directly when the owning workflow requires staging/review;
- drops unmatched rows without reporting them;
- claims reconciliation completeness when material ambiguous records remain;
- treats formatting as always-semantic or always-nonsemantic without consulting workflow truth;
- creates a new generic rule that overrides a specialized domain skill's accepted policy.
