---
name: github
description: Inspect and operate GitHub repositories safely: repository state, files, branches, commits, pull requests, issues, Actions, logs, and artifacts. Use for DEDAL work that depends on live GitHub state.
---

# GitHub Operations

Use GitHub as authoritative state for repository facts.

## Workflow

1. **Read** — identify the exact repository and branch/ref, inspect live state, and read repository-local `AGENTS.md`, continuity docs, architecture rules, and relevant file history when present.
2. **Plan** — distinguish inspection from mutation authority, choose the smallest coherent write set, and identify concurrency/rollback risks.
3. **Write** — make focused changes. Refetch first when the target may have changed; never overwrite a conflict blindly.
4. **Verify** — inspect the exact diff/changed files, final branch/commit state, and any requested CI/Actions result.
5. **Report** — state the final observed repository state and unresolved review/CI risk.

## Mutation discipline

- Prefer small coherent commits and attributable changes.
- For coherent multi-file changes, choose one mutation path before writing. Prefer refresh HEAD -> complete tree -> commit -> fast-forward ref when supported.
- Do not mix unrelated direct contents writes into a prepared atomic tree transaction. If HEAD advances, refetch and reconcile from the new authoritative HEAD rather than forcing.
- Serialize writes that touch the same file/ref/state owner.
- Do not merge, force-push, delete branches/files, rewrite history, or make production-impacting changes without the authority required by the project.
- Preserve rollback paths for architectural or migration changes.
- Keep secrets and private data out of public repository content and logs.
- Treat an API write receipt as evidence that the write was accepted, not that downstream build/deploy behavior succeeded.

## Pull requests and review

For PR/review work, inspect the actual changed files/patch rather than only the PR description. Separate correctness, unintended behavior changes, security/privacy, tests, architecture, and operational risk. Avoid inventing findings not supported by the diff or repository context.

## Actions

GitHub Actions is an execution surface, not a source of truth by itself. Pin inputs when reproducibility matters, keep secrets out of workflow files/logs, inspect the relevant run/job/step conclusion, and remove one-shot write-capable workflows when their purpose is complete.

Queued or running is never equivalent to success. When artifacts matter, verify the artifact exists and is attributable to the intended commit before presenting it as the result.

Status polling must be bounded and scoped. After a push, check registration, capture the specific run ID when available, then poll that run/job rather than repeatedly fetching broad workflow lists. If completion cannot be observed within a reasonable bounded sequence, report the state as pending instead of pretending success.
