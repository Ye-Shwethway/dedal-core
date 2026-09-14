# Cognitive Runtime / Capability Composition Audit — 2026-09-14

## Question

Should DEDAL behave as a single skill at a time, or as one coherent intelligence with an always-active runtime that dynamically composes specialist skills and execution surfaces?

## DEDAL baseline before this audit

The existing Kernel already required the smallest matching skill set, and the Master Index supported multi-skill pairing. The weakness was conceptual/operational: boot still looked like "identify domain -> load skill," which could be interpreted as specialist replacement rather than layered composition. Cross-domain lessons from Agent Engineering, Security Engineering, context engineering, authority, delegation, and failure recovery existed in specialist/reference form but were not yet explicitly distilled into one compact always-active runtime layer.

## External sources reviewed

### Agent Skills standard

Pinned public repo: `agentskills/agentskills` at `69ef37e9424c0a7ea9dd2293b559e43ec8176379`.

Useful pattern: progressive disclosure separates discovery metadata from full `SKILL.md` activation and later resource loading. This supports keeping many faculties discoverable without loading every faculty into working context.

Adapt: metadata-first discovery and on-demand specialist/resource loading.

Do not infer: the Agent Skills format itself does not define DEDAL's always-on cognition, authority hierarchy, or task composition semantics.

### LangChain / DeepAgents

Pinned public repo: `langchain-ai/deepagents` at `c08cae693e0036fcd45d979a7dfa3a7e306a0515`.

Useful patterns:

- middleware surrounds model requests and can inject prompt/state behavior before tool choice;
- skills are progressive/on-demand rather than all loaded;
- tool visibility can change at request time;
- memory, permissions, summarization, and subagents are harness/runtime concerns rather than ordinary specialist tools;
- subagents may have narrower/different middleware, tools, skills, and permissions.

This is the closest implementation analogue found for "always-on substrate + dynamically composed faculties."

Adapt: explicit runtime-vs-specialist separation and dynamic capability composition.

Reject: vendoring DeepAgents/LangGraph or copying its middleware stack into DEDAL Core. DEDAL operates across host environments and must stay provider/runtime agnostic.

### OpenAI Agents SDK

Current public documentation reviewed on 2026-09-14.

Useful patterns:

- agent runtime manages turns, tools, guardrails, handoffs, and sessions;
- local run context is shared across agents/tools/handoffs without necessarily being model-visible;
- tools and handoffs can be enabled dynamically;
- `ToolSearchTool` can defer large tool surfaces until needed;
- manager/specialist and handoff patterns support composing expertise rather than exposing every specialist equally at all times.

Adapt: distinguish shared run substrate from model-facing specialist/tool context; defer capabilities until relevant.

Reject: tying DEDAL's architecture to one SDK or requiring a handoff/multi-agent topology for ordinary composition.

### 2026 Agent Operating System research

Reviewed recent public papers including:

- `The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems` (arXiv:2608.03214)
- `Towards an Agent Operating System - Lessons from Classical and Cloud OS` (arXiv:2607.25076)

Useful convergence: stable control/governance responsibilities (intent, policy, trust, authority, auditability) are separated from runtime/coordination responsibilities (capability routing, context/memory coordination, lifecycle/workflow execution).

Adapt conceptually: DEDAL Kernel + Cognitive Runtime + dynamic composition.

Caution: these are recent architectural proposals, not mature empirical proof. They support direction, not outcome claims.

### Independent/community runtime experiments

Projects such as ORCA/cognitive-runtime efforts were reviewed as weak/secondary evidence that developers are converging on explicit cognition/capability/runtime abstractions. Their terminology and implementation maturity vary widely, so they are not treated as architectural authority.

## DEDAL adaptation

Adopt four layers:

1. Constitutional Kernel — always loaded.
2. Cognitive Runtime — always loaded but compact.
3. Capability Composer — run/subgoal scoped.
4. Specialist skills + execution surfaces — progressive/on demand.

Adopt role vocabulary:

- RUNTIME
- PRIMARY
- SUPPORTING
- EXECUTION
- DORMANT

Adopt dynamic recomposition on material subgoal change.

Adopt the principle that cross-domain lessons can be distilled into Runtime invariants without globally loading the specialist skill they originated from.

## Explicit rejections

- one-skill-at-a-time replacement semantics;
- all-skills-loaded-by-default semantics;
- treating every generic runtime invariant as reason to load Agent Engineering;
- treating tools/plugins/MCPs as equivalent to skills;
- new framework/runtime dependency solely to implement this architecture;
- multi-agent topology as a requirement for skill composition;
- claiming host-level enforcement where only instruction-level control exists.

## Evidence classification

This audit provides **design rationale** from independent convergence. The executable composition contract provides **contract validation**. Neither is yet **outcome validation** that DEDAL is measurably smarter or more efficient on representative real work.
