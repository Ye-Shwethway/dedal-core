# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.10.0`
- Purpose: durable public operational core for DEDAL

## Active Skills

Domain: `$msa`, `$pra`, `$ika`.
Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Interface Design, **Agent Engineering**, Automations, Skill Acquisition.

## Skill Ecosystem Campaign

Pipeline:

`capability gap -> discover -> pin -> audit -> extract patterns -> DEDAL adaptation -> baseline evaluation -> promote/reject -> regression capture`

Policy: **reuse ideas; do not inherit trust blindly.** Popularity is discovery evidence, not authority.

Completed corpora now include Matt Pocock, Anthropic, Vercel Labs, Microsoft, Superpowers, taste-skill, RigorPilot, Impeccable, UI/UX Pro Max, plus the Agent Engineering corpus covering official agent-engineering guidance, research papers, `humanlayer/12-factor-agents`, `stanfordnlp/dspy`, and `SWE-agent/SWE-agent`.

## Agent Engineering v0.10

`skills/agent-engineering/` is active and independently routable for designing or improving AI-agent systems themselves.

Core model:

`agent outcome = model capability × instruction quality × context quality × tool/interface quality × loop/control quality × state/continuity × evaluation/feedback`

### Durable rules

- Establish a capable-model baseline before adding orchestration complexity.
- Keep deterministic constraints/execution in software where practical; use the model for semantic judgment and adaptive choice.
- Treat context as a finite resource; prefer high-signal progressive/JIT retrieval over context dumping.
- Treat tool descriptions, schemas, result shapes, errors, and output size as part of the model-facing interface.
- Give every loop explicit success, failure, retry, non-progress, budget, authority, and escalation semantics appropriate to the task.
- Use reflection/refinement only when a verifier, rubric, environment/tool feedback, source contradiction, or Creator feedback can materially change the next attempt.
- Prefer a single capable agent until independent parallelism, specialization, or context separation justifies multi-agent coordination.
- Trace and evaluate the complete harness, not only prompt text or the final answer.
- For long-horizon work, externalize goal, decisions, evidence, failures, remaining work, and next step into inspectable artifacts.
- Revisit harness assumptions as models improve; temporary workarounds must not silently become permanent Kernel rules.

Focused references cover prompt/context engineering, harness/tool design, agentic loops, orchestration, and evals/observability. `evals/agent-engineering/contract-v1.md` records initial routing and regression assertions.

## Agent Engineering provenance

Pinned public repository snapshots:
- `humanlayer/12-factor-agents` @ `d20c728368bf9c189d6d7aab704744decb6ec0cc` — Apache-2.0.
- `stanfordnlp/dspy` @ `ecba33763316d2a4c6c756046a1118ecbff033e7` — conceptual use only.
- `SWE-agent/SWE-agent` @ `3ea751c087f32b16e039a2233dd6eefecef325d5` — conceptual use only.

Primary conceptual influences also include Anthropic/OpenAI official agent engineering guidance and ReAct, Self-Refine, Reflexion, and AgentBench research. No third-party agent framework/package was installed or executed.

## Interface Design

Interface Design remains active with both a reasoning/workflow layer and a scoped design-intelligence layer. Curated design catalogs remain below Creator/project truth and current authoritative platform/accessibility guidance. Durable design state may use master + surface overrides and must not silently overwrite accepted direction.

## Verification

`repo-integrity.yml` validates foundational/kernel files, registries, all active skill entrypoints, imported/adapted provenance, Interface Design, Agent Engineering references/provenance/eval contract, Skill Acquisition audits, and semantic version format.

Fresh-chat bootstrap E2E remains **PASS** (`evals/boot/minimal-bootstrap-v1.md`). Re-run after boot/kernel/router/layout changes.

## Next Phase

1. Exercise Agent Engineering on a real DEDAL/project agent workflow and compare against the pre-skill baseline or current harness behavior.
2. Capture observed routing/tool/context/loop failures as concrete eval regressions before adding more agent theory.
3. Review DEDAL's own tool/harness ergonomics using the new skill: tool overlap, response size, JIT context, retry/exit semantics, and durable handoff artifacts.
4. Continue gap-driven ecosystem scans only where they can improve a real DEDAL capability.
5. Keep private/personal/project operational state outside the public core.

Do not expand the Stable Kernel merely to encode temporary model limitations, framework fashion, or project-specific agent topology.
