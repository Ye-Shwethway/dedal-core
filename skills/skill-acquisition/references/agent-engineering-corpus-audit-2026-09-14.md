# Agent Engineering Corpus Audit — 2026-09-14

## Scope

Question: which prompt/context engineering, harness, agentic-loop, orchestration, and evaluation patterns are strong enough to become durable DEDAL guidance?

The audit prioritized primary papers, official engineering guides, and mature public agent repositories. Popularity was not treated as proof.

## Sources reviewed

### Official engineering guidance
- Anthropic: Building Effective AI Agents.
- Anthropic: Effective context engineering for AI agents.
- Anthropic: Writing effective tools for AI agents.
- Anthropic: Effective harnesses for long-running agents.
- Anthropic: Harness design for long-running application development.
- Anthropic: How we built our multi-agent research system.
- OpenAI: A practical guide to building agents.
- OpenAI Agents SDK: agents, guardrails, sessions/handoffs, tracing.

### Research patterns
- ReAct — interleaving environment actions with updated reasoning/state.
- Self-Refine — iterative feedback/refinement without model-weight updates.
- Reflexion — linguistic feedback plus episodic memory between attempts.
- AgentBench — interactive agent evaluation across heterogeneous environments.

### Public repositories
- `humanlayer/12-factor-agents` @ `d20c728368bf9c189d6d7aab704744decb6ec0cc` (Apache-2.0).
- `stanfordnlp/dspy` @ `ecba33763316d2a4c6c756046a1118ecbff033e7`.
- `SWE-agent/SWE-agent` @ `3ea751c087f32b16e039a2233dd6eefecef325d5`.

## High-value findings

### 1. Context engineering subsumes prompt-only thinking — ADOPT
Agent behavior depends on the full inference state: durable instructions, retrieved evidence, tools, history, examples, and task state. Long-running agents need active context curation and just-in-time retrieval.

DEDAL adaptation: smallest high-signal context, progressive disclosure, stable references, live-state refresh, and separation of context classes.

### 2. Harness/interface quality can change the effective capability of the same model — ADOPT
SWE-agent's Agent-Computer Interface and Anthropic's tool-design work both treat model-facing commands, schemas, results, and errors as performance-critical.

DEDAL adaptation: tool affordance rules, result-token budgets, actionable errors, namespace/overlap review, and authority-aware tool surfaces.

### 3. Agent loops require explicit termination and recovery semantics — ADOPT
A while-loop over model/tool calls is powerful but dangerous when completion, retries, non-progress, and escalation are vague.

DEDAL adaptation: explicit exit contract, failure classification before retry, bounded reflection, and checkpoint state.

### 4. Reflection/refinement is conditional, not universally beneficial — ADAPT
ReAct/Self-Refine/Reflexion show useful feedback-driven improvement patterns, but self-generated critique can reinforce errors or waste turns when no new signal exists.

DEDAL adaptation: refine only with an evaluator, test, environment feedback, source contradiction, rubric, or Creator feedback capable of changing the next attempt.

### 5. Multi-agent systems are topology choices, not default upgrades — ADOPT
Official production accounts show strong gains for breadth-first parallel research and specialized work, while also exposing coordination cost and failure multiplication.

DEDAL adaptation: single-agent first; parallel workers for independent breadth; manager/worker for specialized contexts; evaluator/optimizer for gradable outputs.

### 6. Long-horizon reliability comes from externalized state — ADOPT
Anthropic long-running harness work repeatedly relies on task decomposition, bounded progress, and structured artifacts that survive context resets.

DEDAL adaptation: goal/decisions/evidence/remaining work/next step become inspectable project artifacts at worthy boundaries.

### 7. Prompt/tool optimization should be metric-driven — ADAPT
DSPy treats prompts and examples as optimizable program parameters. This is powerful when a metric and representative task set exist.

DEDAL adaptation: no automatic optimizer dependency; retain the general principle of baseline + task set + meaningful metric + regression inspection.

### 8. Deterministic software should own deterministic constraints — ADOPT
12-Factor Agents and production agent guidance both converge on keeping state, permissions, tool execution, schemas, and reliable transitions in software rather than asking the model to remember every invariant.

DEDAL adaptation: model chooses where judgment is useful; deterministic code validates and executes where possible.

## Explicit rejects

- blanket “multi-agent is better” claims;
- unlimited retry/reflection loops;
- huge context dumps as a substitute for retrieval design;
- exposing raw API surface merely because it exists;
- using a prompt as the only protection for irreversible authority boundaries;
- storing private hidden reasoning traces as durable project state;
- framework-specific topology as a Stable Kernel rule;
- optimizing prompts against weak metrics or a tiny overfit benchmark and calling it general improvement.

## Promotion decision

**PROMOTE `agent-engineering` as an independent generic skill.**

Reason: the domain is cross-project, repeatedly useful, independently routable, and not reducible to Software Development or Skill Acquisition. It governs AI-system behavior itself: context, tools, harness control, loops, orchestration, and evals.
