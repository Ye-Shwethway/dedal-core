# Adaptation Notes — Data Operations

_Date: 2026-09-14_

This skill is a DEDAL-native synthesis. No external runtime or package is required by the skill.

## Primary influences

### Great Expectations / GX
- Repository snapshot: `fivetran/great_expectations` @ `3798c021bbfb0b13ff384b2238f643d04bdea5f2`.
- License verified: Apache-2.0.
- Retained concepts: declarative expectations/invariants; reusable validation checkpoints; validation results as durable evidence; actions only after validation result exists.
- Not adopted: framework-specific Python classes/configuration as a Core dependency; assuming one data-validation product fits spreadsheets and all operational workflows.

### OpenRefine
- Repository snapshot: `OpenRefine/OpenRefine` @ `6d5d0579ee84c787eb31d04fa1676582f6e7b65e`.
- License verified: BSD 3-Clause-style license in `LICENSE.txt`.
- Retained concepts: iterative reconciliation; entity/record matching as distinct from mere string cleanup; semi-automated candidate matching with human review; preserving unresolved ambiguity.
- Not adopted: OpenRefine UI/project format or reconciliation-service API as a required implementation.

### Microsoft Excel guidance
- Current Microsoft documentation reviewed for formula error detection, inconsistent-formula auditing, reference/range failure modes, formula protection, and calculation behavior.
- Retained concepts: formulas require structural auditing; neighboring patterns and precedent/reference checks are useful evidence; a workbook can be syntactically valid yet semantically wrong.

## DEDAL-specific synthesis

The resulting lifecycle is broader than any one source:
`authority -> record contract -> normalize -> reconcile -> validate -> stage -> review -> promote -> verify -> audit`.

Key additions are explicit source/field authority, promotion gates, rollback-aware staging, domain-skill independence, and evidence preservation across spreadsheet/database boundaries.
