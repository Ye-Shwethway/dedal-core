# DEDAL Memory Architecture

_Date: 2026-09-14_

This document defines the durable public architecture for how DEDAL reasons about state across turns, sessions, projects, and external systems. It defines contracts, not private memory payloads.

## State layers

### 1. Working context
The bounded task context currently supplied to the model. It should contain only what materially influences the next action.

### 2. Episodic trace
Session/workflow history: actions attempted, outcomes, failures, temporary plans, tool evidence, and checkpoint material. Most trace is not permanent knowledge.

### 3. Durable project knowledge
Accepted project facts, decisions, constraints, current state, canonical references, and evidence-linked records. Project-owned artifacts/archives are preferred owners.

### 4. Global/user working memory
Stable cross-project preferences and conventions that genuinely generalize and are appropriate to retain. Keep narrow to reduce scope leakage and stale assumptions.

### 5. External authoritative state
Repositories, files, databases, services, primary sources, deployments, devices, and other systems that remain the canonical owner of live truth.

## Authority principle

Persistence does not grant authority. A remembered statement yields to the current canonical owner when that owner is available and material to the task.

Default pattern:
`live authoritative state > accepted project state > evidence-linked archive/checkpoint > derived summary > model memory/inference`

Creator instructions and higher-priority runtime/system policy remain subject to their normal authority boundaries.

## Memory transition model

`observe -> classify -> verify if needed -> assign scope/owner -> optionally promote -> retrieve when relevant -> refresh/reconcile -> compact/retire/delete in owner`

Every upward transition should become harder as consequence, sensitivity, blast radius, or generality increases.

## Scope isolation

Do not allow project-local facts to become user-global merely through repetition. Do not load unrelated global/project memory when the task does not need it. Shared knowledge requires an explicit reason to broaden scope.

## Freshness

Freshness is part of the claim, not just the store. Current versions, deployments, prices, schedules, availability, and service state should normally be re-read. Stable preferences and historical decisions may persist until contradicted or changed.

## Conflict model

Contradictions may represent:
- different entities;
- different scopes;
- different time periods;
- a newer state superseding an older one;
- genuinely disputed evidence.

Resolve these dimensions before choosing a claim. Preserve meaningful history rather than silently overwriting it.

## Retrieval and compaction

Retrieval aims for the smallest sufficient package. Start with exact identity/scope/current checkpoint and expand only as needed.

Compaction preserves:
- accepted state;
- evidence of completed work;
- unresolved risk;
- important failures/regressions;
- source/version identities required for re-verification;
- next executable step.

## Governance and privacy

Public Core stores contracts, schemas, sanitized examples, and non-sensitive regression fixtures. Raw private memory belongs in the appropriate private owner.

State operations must respect:
- access/scope;
- sensitivity;
- provenance;
- retention;
- correction/supersession;
- deletion/forgetting controls;
- audit/history where appropriate.

## Relationship to other DEDAL layers

- `$ika`: concrete evidence-linked project archive operations.
- Project Bootstrap: reconstruct the smallest executable project context.
- Agent Engineering: harness/session state and long-horizon continuity.
- Security Engineering: poisoning, access, trust, and privilege threats.
- Files/connectors/repos/databases: actual state owners and retrieval surfaces.

This architecture should remain runtime-neutral. Future memory products or stores may implement parts of it without redefining the public contract.
