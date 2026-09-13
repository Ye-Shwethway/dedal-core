---
name: github
description: Inspect and operate GitHub repositories safely: repository state, files, branches, commits, pull requests, issues, Actions, logs, and artifacts. Use for DEDAL work that depends on live GitHub state.
---

# GitHub Operations

Use GitHub as authoritative state for repository facts.

## Start

1. Identify the exact repository and branch/ref.
2. Inspect live state before relying on memory.
3. Read repository-local `AGENTS.md`, continuity docs, and architecture rules when present.
4. Distinguish inspection from mutation authority.

## Mutation discipline

- Prefer small coherent commits.
- Do not overwrite concurrent changes blindly; refetch and reconcile on conflicts.
- Do not merge, force-push, delete branches/files, or make production-impacting changes without the authority required by the project.
- Never claim CI/build/deploy success without checking the actual run/status/logs.
- Preserve rollback paths for architectural changes.

## Actions

GitHub Actions is an execution surface, not a source of truth by itself. Pin inputs when reproducibility matters, keep secrets out of public workflow files, inspect run conclusions, and remove one-shot write-capable workflows when their purpose is complete.

## Completion

Report the observed final branch/commit state and any unresolved CI or review issue.
