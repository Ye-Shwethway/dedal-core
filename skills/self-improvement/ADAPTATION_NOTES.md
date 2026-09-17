# Adaptation Notes — Self-Improvement

## Why a dedicated skill now exists

A 2026-09-14 audit concluded that a separate self-improvement skill was not yet justified because Agent Engineering already owned controlled self-change and there was no representative DEDAL outcome failure proving a routing gap.

That decision is superseded by later real workflow evidence: a previously successful production behavior was repaired live but not fully synchronized into canonical source and regression coverage, so a later refactor reintroduced retired behavior. The failure crossed Agent Engineering, Reliability, Quality, source control, continuity, and private learning boundaries. A dedicated closure orchestrator became independently routable and useful.

## External research pass — 2026-09-18

The first v0.32.0 implementation was subsequently re-audited through the full Skill Acquisition workflow rather than treated as complete from internal design alone. Patterns were compared across first-party guidance and public repositories, then adapted rather than copied.

### Sources reviewed

- OpenClaw current `self-learning` and `creating-skills` documentation — immediate targeted repair, staged/propose/auto learning modes, and skills as durable procedures.
- OpenAI, “Building self-improving tax agents with Codex” (2026-05-27) — practitioner/production feedback -> structured finding -> targeted plus regression evals -> scoped engineering task -> validation/promotion.
- OpenAI, “Inside OpenAI’s in-house data agent” (2026-01-29) — continuous evals as regression canaries for an evolving agent.
- Anthropic, “Demystifying evals for AI agents” (2026-01-09) — evaluate complete agent behavior and use evals to expose regressions before production.
- `pskoett/self-improving-agent` at `b889ef0724c27b7181111b8dd1ac3a108d0b5160` — explicit correction/error/feature-request capture, recurrence keys, opt-in hooks, redacted learning logs. GitHub did not expose a repository license at review time, so methodology only; no code copied.
- `ECNU-ICALK/AutoSkill` at `94c47ca488d4ba4117d20272e66d49b9877e68cf` — `discard / improve / merge / create` lifecycle triage, proactive reusable-experience detection, replay pools, frozen promotion tests, mutation budgets. GitHub did not expose a repository license at review time, so methodology only; no code copied.
- `phnx-labs/.agents` at `c4649ee30426e4d891a4471579ea7699312f9a62` — session learning routed to the nearest canonical owner, prefer correction over new rules, and require generalization/recurrence/root-cause/durability filters. GitHub did not expose a repository license at review time, so methodology only; no code copied.
- `RangeKing/self-evolving-agent` at `c9781daa5d2be7c6c3abad4e99b3f01f6dead9b1` (MIT) — separate memory capture from mastery, explicit learning maturity states, transfer proof before promotion, and smallest-mode retrieval.

### Adapted into DEDAL

- candidate triage before durable mutation: `discard | improve | merge | create`;
- learning maturity: `recorded -> understood -> practiced -> passed -> generalized -> promoted`;
- transfer/recurrence evidence before broad promotion;
- automatic capture may be lightweight, but durable promotion remains evidence-gated;
- skill creation explicitly routes through Skill Acquisition's external research/provenance/eval workflow.

### Already covered before this pass

DEDAL already had live/canonical source reconciliation, source-sync debt, executable regression guards, public/private lesson routing, protected evaluation, Creator/tool authority boundaries, rollback/revert semantics, and explicit unresolved debt.

### Rejected or not adopted

- unbounded autonomous self-rewrite loops;
- automatic promotion from one interaction;
- installing third-party hooks/runtimes merely to gain learning capture;
- copying external storage layouts such as `.learnings/` or `.evolution/` into DEDAL;
- treating repository popularity as quality proof;
- weakening independent evals so a candidate can pass its own acceptance test.

## DEDAL-specific position

Self-Improvement remains a bounded orchestration faculty. Agent Engineering owns harness design, Skill Acquisition owns external skill research/adaptation, domain skills own implementation, Quality Engineering owns independent acceptance, and the private overlay holds Creator-specific operational lessons.
