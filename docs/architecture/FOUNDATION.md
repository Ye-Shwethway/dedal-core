# Foundational Architecture

## Objective

DEDAL Core separates the system into durable layers so that a model upgrade, chat boundary, tool change, or runtime limitation does not erase the collaboration's operating structure.

## Layer Model

```text
┌─────────────────────────────────────┐
│ Model / reasoning engine            │
├─────────────────────────────────────┤
│ Identity + operating contract       │
├─────────────────────────────────────┤
│ Personal context + continuity       │
├─────────────────────────────────────┤
│ Capability + tool registry          │
├─────────────────────────────────────┤
│ Skills / workflows / evaluations    │
├─────────────────────────────────────┤
│ Execution environments              │
├─────────────────────────────────────┤
│ External persistent state           │
└─────────────────────────────────────┘
```

### 1. Model / Reasoning Engine

Provides reasoning, language, multimodal interpretation, planning, and code generation. It is replaceable and should not be the sole holder of durable state.

### 2. Identity + Operating Contract

Stable public principles live in `AGENTS.md` and `docs/IDENTITY.md`.

These define how DEDAL should behave independent of a particular model version.

### 3. Personal Context + Continuity

Personalized context may come from authorized memory, chats, files, and connected sources.

Exact project state must remain in authoritative project systems or canonical checkpoint documents rather than relying on memory alone.

### 4. Capability + Tool Registry

DEDAL should maintain awareness of what it can actually access now, not what an earlier model or environment could access.

Capabilities are dynamic and must be revalidated when important.

### 5. Skills / Workflows / Evaluations

Repeated work should become reusable procedures. Failures should generate tests, rules, or workflow improvements where useful.

### 6. Execution Environments

Possible execution surfaces include:

- ChatGPT sandbox/runtime;
- connected services and plugins;
- GitHub Actions;
- external MCP/API services;
- local or cloud build runners;
- Work/cloud-computer environments when available and economical.

No single execution surface is assumed permanent.

### 7. External Persistent State

Durable state should live in appropriate systems such as:

- GitHub repositories;
- ChatGPT Library;
- Google Drive;
- databases;
- secured custom backends;
- project-specific services.

## Public vs Private Separation

```text
Public DEDAL Core
  ├─ principles
  ├─ schemas
  ├─ workflows
  ├─ evaluations
  └─ sanitized capability metadata

Private / Authorized State
  ├─ personal memory
  ├─ credentials
  ├─ confidential files
  ├─ account data
  └─ sensitive project state
```

The public core may define *how* private state is accessed, but must not contain the private state itself.

## Work-Mode Constraint

Work/cloud-computer execution is treated as a high-value burst capability, not an always-on foundational dependency, because practical paid-plan quotas can be restrictive. Core workflows should remain usable without consuming Work quota unless its browser/computer autonomy materially improves the task.

## Initial Non-Goals

The first foundation does not attempt to:

- create autonomous self-modifying model weights;
- build a large agent swarm;
- duplicate every project repository;
- centralize confidential data;
- add infrastructure without a concrete use case.

Start small. Add capability only when it produces measurable value.
