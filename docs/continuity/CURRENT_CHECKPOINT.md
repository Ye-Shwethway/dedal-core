# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.16.0`
- Purpose: durable public operational core for DEDAL

## Active skills

Domain: `$msa`, `$pra`, `$ika`.

Generic/meta: GitHub, Files & Artifacts, Research, Software Development, **Decision Design v2**, Interface Design, Agent Engineering, Security Engineering, Project Bootstrap, Release Engineering, Data Operations, Writing / Editorial Engineering, Visual Direction / Image Production, Automations, Skill Acquisition.

## Capability expansion roadmap

Roadmap: `docs/evolution/CAPABILITY_EXPANSION_ROADMAP.md`.

Status:
1. Security Engineering — active;
2. Project Bootstrap / Context Adapter — active;
3. Release / Deployment Engineering — active;
4. Data / Spreadsheet / Operational Workflow Engineering — active;
5. Writing / Editorial Engineering — active;
6. Visual Direction / Image Production — active;
7. **Decision / Planning Intelligence v2 — active, merged into Decision Design;**
8. Knowledge / Memory Architecture — planned next.

## Decision Design v2

Audit: `skills/skill-acquisition/references/decision-planning-v2-capability-audit-2026-09-14.md`.
Eval: `evals/decision-design/contract-v2.md`.

Core model:
`decision weight ~= irreversibility × downside × uncertainty × blast radius`

Core lifecycle:
`frame -> classify facts/assumptions/uncertainties/values/constraints -> weight decision -> map dependency frontier -> reduce high-value uncertainty -> compare alternatives -> commit/experiment/defer/stop -> record/review when durable`

Key boundaries:
- reversible, low-downside decisions should not inherit heavyweight irreversible-decision process;
- effectively irreversible/high-blast-radius choices require stronger evidence and explicit authority;
- facts, assumptions, uncertainties, Creator preferences, and hard constraints remain distinct;
- experiments must target decision-relevant uncertainty and have bounded cost, observable evidence, and stop conditions;
- analysis continues only while the next evidence has plausible decision value;
- durable deferrals use reevaluation triggers rather than vague `later` notes;
- premortems are bounded and reserved for consequential/fragile plans;
- post-decision review distinguishes decision quality from outcome luck/hindsight.

Primary evidence:
- Amazon 2015 shareholder letter (one-way/two-way door decisions);
- NASA Decision Analysis and Risk-Informed Decision Making guidance;
- Gary Klein, HBR 2007 project premortem;
- Martin Fowler 2026 Architecture Decision Record guidance;
- original `mattpocock/skills` adaptation source @ `3cca18b368ae95cdbdebbff572ccafa662551015`, MIT.

No third-party decision package or executable was installed or run.

## Harness benchmark

Harness v1 remains contract-validated with accumulating outcome evidence.

Current compact evidence:
- GH-01: prior clean rerun PASS; v0.15 authoring exposed renewed direct-write tool-selection regressions, recovered without force/history rewrite;
- GH-02: PASS;
- RS-01: PARTIAL;
- RS-02: PASS;
- LH-01 / LH-02: await representative continuity/recovery work.

Do not call the full harness outcome-validated yet.

## Next executable phase

1. Exercise Decision Design v2 naturally on real product/architecture/planning choices; capture regressions only when meaningful.
2. Continue capability roadmap with **Knowledge / Memory Architecture**.
3. Keep runtime-enforcement gaps in GitHub mutation mode visible; prose allowlists are guidance, not hard enforcement.
4. Re-exercise RS-01 and LH cases only on representative real work.