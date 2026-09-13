# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.13.0`
- Purpose: durable public operational core for DEDAL

## Active skills

Domain: `$msa`, `$pra`, `$ika`.

Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Interface Design, Agent Engineering, Security Engineering, Project Bootstrap, Release Engineering, **Data Operations**, Automations, Skill Acquisition.

## Capability expansion roadmap

Roadmap: `docs/evolution/CAPABILITY_EXPANSION_ROADMAP.md`.

Status:
1. Security Engineering — active;
2. Project Bootstrap / Context Adapter — active;
3. Release / Deployment Engineering — active;
4. **Data / Spreadsheet / Operational Workflow Engineering — active;**
5. Writing / Editorial Engineering — planned next;
6. Visual Direction / Image Production — planned;
7. Decision / Planning Intelligence v2 — planned;
8. Knowledge / Memory Architecture — planned.

## Data Operations v1

Audit: `skills/skill-acquisition/references/data-operations-capability-audit-2026-09-14.md`.
Eval: `evals/data-operations/contract-v1.md`.

Core lifecycle:
`authority -> record contract -> normalize -> reconcile -> validate -> stage -> review -> promote -> verify -> audit`

Key boundaries:
- source/field authority is established before overwrite;
- record identity/equivalence is defined before deduplication;
- raw, normalized comparison, and canonical accepted values remain distinct;
- ambiguous reconciliation remains explicit rather than forced;
- formulas are treated as logic/code when spreadsheet correctness depends on them;
- risky changes use staging/review/promotion when rollback or human review matters;
- successful writes/imports are not sufficient evidence of production correctness;
- specialized domain skills retain their business rules.

Primary corpus:
- `fivetran/great_expectations` @ `3798c021bbfb0b13ff384b2238f643d04bdea5f2`, Apache-2.0;
- `OpenRefine/OpenRefine` @ `6d5d0579ee84c787eb31d04fa1676582f6e7b65e`, BSD 3-Clause-style license;
- current Microsoft Excel formula/error-auditing guidance.

No third-party package or executable was installed or run for this adaptation.

## Harness benchmark

Harness v1 remains active. Current compact benchmark evidence:
- GH-01: latest clean rerun PASS after mutation-mode/tool-allowlist hardening;
- GH-02: PASS;
- RS-01 / RS-02: await suitable real research work;
- LH-01 / LH-02: await suitable real multi-session/new-chat work.

Do not manufacture large artificial tasks merely to complete the scorecard.

## Next executable phase

1. Exercise Data Operations naturally on future spreadsheet/data work and capture regressions when meaningful.
2. Continue capability roadmap with **Writing / Editorial Engineering**.
3. Then evaluate Visual Direction, Decision Intelligence v2, and Knowledge/Memory Architecture, merging rather than multiplying skills where independence is weak.
4. Keep external tool/framework syntax out of Core unless current authoritative verification makes it necessary.
