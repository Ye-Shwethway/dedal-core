# Orchestration Patterns

Choose topology from task structure, not fashion.

## Single agent first

A single capable agent with clear tools and context is easier to evaluate, debug, secure, and maintain. Start here unless the task has a concrete reason to decompose.

## Sequential workflow

Use when later steps depend on validated outputs from earlier steps. Keep deterministic transformations outside the model when possible.

## Parallel workers

Use when subtasks are materially independent and breadth or latency benefits justify coordination overhead. Give every worker:
- a distinct objective;
- boundaries/non-goals;
- source/tool expectations;
- required output contract;
- enough shared context to avoid duplicated or incompatible work.

Parallelism without partitioning creates duplicated effort and noisy synthesis.

## Manager / worker

Use a lead agent to decompose, delegate, and synthesize when specialized contexts, tools, or independent exploration improve quality. The manager should retain the global goal and authority boundaries while workers receive only the context needed for their slice.

## Evaluator / optimizer

Use when an output can be meaningfully graded and iterative revision has demonstrated value. The evaluator should return actionable defects tied to explicit criteria. Stop after success or bounded non-progress; do not create ceremonial critique loops.

## Routing

Use routing when distinct request classes require materially different prompts, tools, models, or policies. Prefer deterministic routing where classification rules are stable; use a model when the boundary itself needs semantic judgment.

## Multi-agent caution

Multi-agent systems multiply coordination cost, token usage, latency, failure surfaces, and authority complexity. They are especially useful for breadth-first independent search or specialized parallel work, but are not automatically superior for tightly coupled tasks.

## Handoffs

A handoff should carry:
- objective and completion definition;
- relevant evidence/source identifiers;
- accepted decisions and constraints;
- completed work;
- unresolved risks/questions;
- next expected action.

Do not forward an entire noisy transcript when a smaller structured handoff is sufficient.
