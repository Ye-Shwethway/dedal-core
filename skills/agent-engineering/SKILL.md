---
name: agent-engineering
description: Design, improve, and evaluate AI-agent systems by engineering instructions, context, tools, harnesses, loops, orchestration, observability, and long-horizon state. Use when agent output quality, reliability, efficiency, or autonomy depends on more than the base model.
---

# Agent Engineering

Treat agent quality as a systems problem, not a prompt-only problem.

A useful mental model is:

`agent outcome = model capability × instruction quality × context quality × tool/interface quality × loop/control quality × state/continuity × evaluation/feedback`

## Start with the smallest sufficient system

1. Define the task, success criteria, risk, and evidence of completion.
2. Establish a capable-model baseline before adding elaborate orchestration.
3. Prefer deterministic software for deterministic work; use the model for judgment, ambiguity, synthesis, and adaptive choice.
4. Add tools, retrieval, memory, loops, or multiple agents only when a measured failure mode justifies them.
5. Prefer one well-equipped agent over multi-agent coordination until decomposition or parallelism has clear value.

## Engineer the context, not just the prompt

Give the model the smallest high-signal context that supports the next decision. Separate durable instructions, task state, retrieved evidence, tool results, and historical artifacts. Prefer references and just-in-time retrieval over dumping all potentially relevant material into every turn.

Read `references/prompt-and-context.md` for instruction and context contracts.

## Design tools for agents

Tools are part of the reasoning interface. Give each tool a distinct purpose, unambiguous inputs, useful errors, bounded outputs, and enough metadata for the model to choose it correctly. Avoid overlapping tool sets and brute-force outputs that waste context.

Read `references/harness-and-tools.md`.

## Control the loop

Every agent run needs explicit state and termination semantics. Define:
- what the model may decide;
- what deterministic code executes;
- what evidence enters the next turn;
- retry / reflection conditions;
- maximum turns or budgets where appropriate;
- success, failure, escalation, and human-intervention exits.

Self-critique or reflection is not automatically useful. Iterate when there is a rubric, tool/environment feedback, verifier, test, or other signal capable of changing the answer. Avoid endless self-review without new evidence.

Read `references/agentic-loops.md`.

## Orchestrate deliberately

Use sequential workflows for dependent steps, parallel workers for independent breadth, evaluator-optimizer loops when quality criteria are inspectable, and manager/worker patterns when specialized contexts or tools genuinely help. Multi-agent topology is an optimization, not a status symbol.

Read `references/orchestration.md`.

## Observe and evaluate

Trace enough of the run to explain failures: model calls, tool selection, tool inputs/results, retries, handoffs, guardrails, state transitions, token/cost/latency where available, and final verification. Evaluate the complete harness, not only the final prompt.

Compare changes against a meaningful baseline. Separate task success, tool-use quality, reliability, context/token cost, latency, safety/authority adherence, and recovery behavior.

Distinguish evidence maturity explicitly:
- **design rationale** — why a change should help;
- **contract validation** — whether rules/tests are internally coherent;
- **outcome validation** — whether representative real tasks actually improved versus baseline.

Do not report contract validation as measured outcome improvement.

Read `references/evals-and-observability.md`.

## Long-horizon work

For work spanning context windows or sessions, externalize state into inspectable artifacts: current goal, accepted decisions, remaining work, completed evidence, known failures, and next executable step. Each session should make bounded progress and leave the next session a truthful handoff rather than relying on hidden conversational memory.

## Apply to DEDAL itself

When optimizing DEDAL's own operating workflow, read `references/dedal-self-application.md`. Use a lightweight work-unit envelope, minimal context loading, bounded tool loops, transactional repository writes, evidence-level completion claims, and executable checkpoints. Do not turn self-optimization into constant ceremony.

## Boundary

This skill designs agent systems and harness behavior. It does not override DEDAL Kernel authority, tool permissions, platform safety requirements, or domain-specific skills. Pair with Software Development when implementing the harness, Research when studying external methods, and Skill Acquisition when adapting third-party agent patterns.
