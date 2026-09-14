# Cognitive Runtime and Capability Composition Architecture

## Purpose

DEDAL should behave as one persistent coherent intelligence whose specialist faculties are composed dynamically, not as a launcher that swaps between isolated skill personalities.

This architecture separates what must remain continuously active from what should enter working context only when the current task needs it.

## Four layers

### 0. Constitutional Kernel

Always loaded. Owns identity, authority hierarchy, source-of-truth precedence, public/private state boundaries, honesty, and stable invariants.

### 1. Cognitive Runtime

Always loaded, deliberately compact. Owns the universal operating loop and cross-domain invariants that should survive specialist switching: task framing, capability composition, context discipline, task-scoped authority, evidence promotion, recovery semantics, delegation bounds, and durable continuity.

The Cognitive Runtime is **not** the full Agent Engineering skill. It is a distilled substrate built from rules that proved broadly reusable across domains.

### 2. Capability Composer

Run/subgoal scoped. Chooses the smallest useful capability set and assigns roles:

- `RUNTIME` — always-on substrate;
- `PRIMARY` — current intent owner;
- `SUPPORTING` — distinct necessary supporting skill;
- `EXECUTION` — current tool/plugin/MCP/native action surface;
- `DORMANT` — known but not loaded.

The composer may change roles between subgoals. Skill activation is therefore dynamic state, not a permanent conversation mode.

### 3. Specialists and execution surfaces

Specialist `SKILL.md` bodies load only when selected as PRIMARY/SUPPORTING. Their references/scripts/resources load later, on demand. Tools are discovered and authorized separately from skill choice.

## Why not load every skill?

Full skill bodies consume working context, create overlapping instructions, make routing noisier, and can cause irrelevant domain rules to leak into unrelated tasks. Possessing a capability should not mean keeping its complete instructions in active working memory.

The intended model is:

`always-on brain + on-demand faculties`

not:

`all faculties always in prompt`

and not:

`one skill loaded = all other intelligence disabled`.

## Explicit skill requests

A request such as "load visual-direction" or an alias such as `$msa` is a strong routing instruction for the relevant subgoal. It selects the named domain as PRIMARY when appropriate, but it does not:

- disable the Cognitive Runtime;
- remove Kernel authority/truth rules;
- prohibit another genuinely necessary supporting skill;
- automatically authorize any execution tool.

## Example: image workflow

A character-expression generation task can compose as:

- RUNTIME: Cognitive Runtime
- PRIMARY: Visual Direction
- SUPPORTING: Files when canonical references must be retrieved; Knowledge/Memory only if durable anchor/state governance becomes part of the task
- EXECUTION: current image-generation surface
- DORMANT: Agent Engineering, Software Development, unrelated domain skills

The model can still use runtime verification, context discipline, recovery, and authority rules without loading the full Agent Engineering skill.

## Example: software release workflow

One long task may change PRIMARY owners by phase:

1. implementation/debugging -> Software Development PRIMARY;
2. source/branch mechanics -> GitHub SUPPORTING or PRIMARY for a repo-only subgoal;
3. artifact promotion/deployment -> Release Engineering PRIMARY;
4. unexpected authorization risk -> Security Engineering becomes PRIMARY for that subgoal.

This is recomposition, not spawning a new DEDAL personality.

## External architectural support

The design adapts several independently convergent patterns without adopting their runtimes:

- Agent Skills standard: metadata discovery, full skill activation on match, then resource loading on demand.
- LangChain/DeepAgents: middleware/harness behavior surrounds every model call while skills, memory, subagents, permissions, and tool surfaces are composed dynamically.
- OpenAI Agents SDK: shared run context, dynamically enabled tools/handoffs, deferred tool discovery, and manager/specialist composition.
- 2026 Agent Operating System research: separation of stable control/governance responsibilities from runtime capability selection/coordination.

These sources support the architectural direction but do not prove DEDAL outcome improvement. DEDAL keeps its own Kernel, authority model, skill ownership, and host-boundary honesty.

## Non-goals

- Do not vendor DeepAgents, LangGraph, Agents SDK, or another orchestration runtime into Core merely to mimic the pattern.
- Do not create a new top-level "cognitive runtime skill"; this is infrastructure, not a routed domain skill.
- Do not turn every trivial query into an explicit multi-step composition ceremony.
- Do not claim mechanical host enforcement where ChatGPT/native-provider surfaces expose no programmable interception point.

## Evaluation target

Representative tasks should show that:

1. specialist activation does not erase universal DEDAL behavior;
2. unrelated skills remain out of working context;
3. supporting skills appear only for distinct necessary layers;
4. the active composition can change as the task changes;
5. context/tool overhead does not grow merely because DEDAL knows more capabilities.
