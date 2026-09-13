---
name: project-bootstrap
description: Rapidly onboard to an unfamiliar or resumed project by building a compact authoritative context map: goals, repository rules, architecture, commands, source-of-truth files, current checkpoint, risky areas, release path, and next executable step. Use when entering a new repo/project, resuming after context loss, or creating agent-facing project instructions.
---

# Project Bootstrap / Context Adapter

Bootstrap is not summarization. It is the construction of a **minimal executable project model** from authoritative evidence.

## Workflow

1. **Identify authority** — repository/project, target branch/version, explicit Creator constraints, and whether live state is available.
2. **Read instruction hierarchy** — root/local `AGENTS.md`, repository instructions, architecture/continuity docs, contribution/build guidance, and path-specific rules when relevant.
3. **Map the project** — purpose, major modules, important data/state owners, build/test/run commands, dependencies, generated vs hand-edited files, release/deploy path, and sensitive/risky zones.
4. **Resolve current state** — accepted decisions, current checkpoint, open work, known failures, protected branches/releases, and latest verification evidence.
5. **Create a compact context adapter** — preserve only facts that change execution. Link/reference source files rather than copying large documents.
6. **Test executability** — confirm that another capable agent could answer: what am I changing, where, under what rules, how do I verify it, and what must I not assume?
7. **Refresh on drift** — reload the smallest affected slice when branch, architecture, dependency, release, or project instruction state changes.

## Context adapter fields

A useful project profile usually contains:
- project goal / product boundary;
- authoritative repository/ref;
- instruction hierarchy and scoped rules;
- module/ownership map;
- setup/build/test/run commands;
- source-of-truth data/config files;
- architecture decisions that constrain changes;
- release/deploy path and artifact expectations;
- sensitive/destructive zones;
- accepted current state;
- unresolved risks;
- next executable step.

Do not require every field when it does not affect the task.

## Durable rules

- Live project state outranks remembered summaries when both exist.
- `AGENTS.md`/local instructions are scoped guidance, not a replacement for reading the code/state they describe.
- Prefer progressive disclosure: root context should route to deeper module-specific context instead of duplicating it.
- Do not ask the Creator to reconstruct information that is retrievable from authorized project state.
- Distinguish **stable project rules** from **current checkpoint state**. Mixing them causes stale instructions.
- Distinguish **facts** from **assumptions/inferences**; unresolved inference must not become durable project truth.
- Generated outputs and vendor/dependency directories are usually not architecture sources unless the project says otherwise.
- Avoid bootstrap bloat: every retained fact should alter routing, implementation, verification, risk, or continuity.

## Pairing

Pair with `github` for live repository state, `software-development` for implementation, `decision-design` for unresolved architecture choices, `release-engineering` for shipping paths, and `security-engineering` when onboarding untrusted repositories or privileged workflows.

Load references on demand:
- `references/context-map.md`
- `references/instruction-hierarchy-and-drift.md`
