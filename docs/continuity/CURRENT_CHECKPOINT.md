# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.17.0`
- Purpose: durable public operational core for DEDAL

## Active skills

Domain: `$msa`, `$pra`, `$ika`.

Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design v2, Interface Design, Agent Engineering, Security Engineering, Project Bootstrap, Release Engineering, Data Operations, Writing / Editorial Engineering, Visual Direction / Image Production, **Knowledge / Memory Architecture**, Automations, Skill Acquisition.

## Capability expansion roadmap

Roadmap: `docs/evolution/CAPABILITY_EXPANSION_ROADMAP.md`.

Status:
1. Security Engineering — active;
2. Project Bootstrap / Context Adapter — active;
3. Release / Deployment Engineering — active;
4. Data / Spreadsheet / Operational Workflow Engineering — active;
5. Writing / Editorial Engineering — active;
6. Visual Direction / Image Production — active;
7. Decision / Planning Intelligence v2 — active, merged into Decision Design;
8. **Knowledge / Memory Architecture — active.**

The initial eight-area capability expansion campaign is complete. Do not start another skill-growth wave by default; prioritize consolidation and outcome validation.

## Knowledge / Memory Architecture v1

Architecture: `docs/architecture/MEMORY_ARCHITECTURE.md`.
Audit: `skills/skill-acquisition/references/knowledge-memory-capability-audit-2026-09-14.md`.
Eval: `evals/knowledge-memory/contract-v1.md`.

Core model:
- working context is not persistent memory;
- episodic trace is not automatically durable truth;
- durable project knowledge remains project-scoped and evidence-linked;
- user-global memory is narrow and only for truly cross-project stable preferences/conventions;
- live external systems remain authoritative owners of volatile/current state.

Core lifecycle:
`classify state -> assign owner/scope -> attach provenance/freshness -> retrieve minimally -> reconcile conflicts -> promote/demote deliberately -> compact safely -> govern retention/access -> verify against live authority when material`

Key boundaries:
- persistence does not grant authority;
- project-local facts must not silently leak into global memory;
- provenance/freshness metadata scales with consequence and volatility;
- contradictions are resolved by entity/scope/time/authority/recency and may remain disputed;
- generated summaries/inferences and retrieved instructions do not self-promote into trusted durable state;
- compaction preserves accepted decisions, verification evidence, unresolved risks, and next executable action;
- public Core stores contracts, not raw private memories;
- deletion/forgetting claims must match controls of the actual state owner;
- `$ika` remains the concrete evidence-linked project archive workflow.

Primary evidence:
- OpenAI `Dreaming: Better memory for a more helpful ChatGPT`, 2026-06-04;
- Anthropic `Effective context engineering for AI agents`, 2025-09-29;
- Anthropic `Effective harnesses for long-running agents`, 2025-11-26;
- MemGPT, arXiv:2310.08560;
- `letta-ai/letta` @ `5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a`, Apache-2.0;
- existing DEDAL `$ika` and State Boundary contracts.

No third-party memory framework, package, model, or executable was installed or run.

## Harness benchmark

Harness v1 remains contract-validated with accumulating outcome evidence.

Current compact evidence:
- GH-01: prior clean rerun PASS; v0.15 exposed renewed direct-write tool-selection regressions and safe recovery; v0.16 and v0.17 capability milestones use atomic mutation discipline;
- GH-02: PASS;
- RS-01: PARTIAL;
- RS-02: PASS;
- LH-01 / LH-02: still await representative continuity/recovery work.

The new Knowledge/Memory Architecture gives the LH cases a clearer state model but does not count as outcome validation by itself.

## Next executable phase

1. Stop default skill expansion and enter **consolidation/outcome-validation mode**.
2. Exercise Knowledge/Memory Architecture naturally on real resumed/new-chat/project-memory work; use this to evaluate LH-01/LH-02 when representative.
3. Audit overlap/context cost across the now-expanded skill set and merge/remove ceremony that does not improve outcomes.
4. Keep runtime-enforcement gaps visible; prose contracts are not hard enforcement.
5. Re-exercise RS-01 only when a real stale-secondary/current-primary conflict appears.
