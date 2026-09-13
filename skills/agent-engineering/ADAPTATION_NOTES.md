# Agent Engineering Adaptation Notes

_Date: 2026-09-14_

This skill is a DEDAL-native synthesis of public research, official engineering guidance, and mature agent-system implementations. It is not a verbatim import of one framework.

## Primary conceptual sources

- Anthropic, `Building Effective AI Agents` — augmented LLMs, workflow-vs-agent distinction, evaluator/optimizer and orchestrator/worker patterns, complexity discipline.
- Anthropic, `Effective context engineering for AI agents` (2025) — finite context as an engineering resource, right-altitude instructions, just-in-time retrieval.
- Anthropic, `Writing effective tools for AI agents` (2025) — agent-oriented tool affordances, tool-set minimization, token-efficient results, actionable errors, eval-driven tool improvement.
- Anthropic, `Effective harnesses for long-running agents` (2025) and `Harness design for long-running application development` (2026) — bounded progress, structured handoff artifacts, planner/generator/evaluator patterns.
- Anthropic, `How we built our multi-agent research system` (2025) — breadth-oriented parallelism, explicit delegation contracts, observability and stopping heuristics.
- OpenAI, `A practical guide to building agents` and current Agents SDK docs — model/tools/instructions foundations, run loops, guardrails, handoffs, sessions, tracing, human intervention.
- ReAct (Yao et al., 2022), Self-Refine (Madaan et al., 2023), Reflexion (Shinn et al., 2023) — action-feedback and iterative refinement patterns.
- SWE-agent / Agent-Computer Interface — model-facing command and feedback design as a major performance lever.
- DSPy — task signatures, metrics, examples/instructions as optimizable program parameters.

## Pinned public repositories inspected

- `humanlayer/12-factor-agents` @ `d20c728368bf9c189d6d7aab704744decb6ec0cc` — Apache-2.0.
- `stanfordnlp/dspy` @ `ecba33763316d2a4c6c756046a1118ecbff033e7` — used conceptually; exact library/runtime not imported.
- `SWE-agent/SWE-agent` @ `3ea751c087f32b16e039a2233dd6eefecef325d5` — used conceptually; exact harness/runtime not imported.

## DEDAL adaptations

Retained:
- context as a scarce, actively curated resource;
- simple capable baseline before orchestration complexity;
- deterministic code around model judgment;
- explicit loop exits and bounded retries;
- tool ergonomics as part of model performance;
- observability and eval-driven changes;
- externalized continuity for long-horizon work;
- multi-agent use only when decomposition/parallelism justifies it.

Rejected or constrained:
- framework lock-in;
- one universal agent topology;
- unbounded autonomous loops;
- self-reflection without an external or explicit quality signal;
- treating hidden chain-of-thought as an application interface or required persisted artifact;
- prompt engineering as the default fix for failures owned by tools, state, retrieval, permissions, or orchestration;
- stale harness assumptions becoming permanent Kernel rules.

No third-party agent framework, package, or executable was installed or executed during this adaptation.
