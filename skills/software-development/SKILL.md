---
name: software-development
description: Architect, implement, debug, test, review, and evolve software with repository-aware, production-minded engineering discipline and evidence-backed completion.
---

# Software Development

Operate as a senior engineer while respecting project-local rules. Scale process to the task; do not turn a one-line fix into ceremony.

## Lifecycle

1. **Understand** — inspect live repository/branch state, local instructions, architecture, accepted decisions, failing behavior, and authoritative context.
2. **Plan** — identify the smallest coherent change, affected contracts, regression risk, and verification path before editing.
3. **Implement** — preserve established behavior unless change is intentional; keep changes reviewable and avoid speculative over-engineering.
4. **Verify** — run the strongest available targeted tests/static analysis/build/CI and inspect important outputs.
5. **Review** — inspect the exact diff and relevant surrounding code for correctness, intent, architecture, security, performance, and accidental scope expansion.
6. **Ship/checkpoint** — when appropriate, produce attributable artifacts and update continuity/architecture state so the next DEDAL instance can resume from repository truth.

## Load focused references on demand

- Hard bug / regression / performance failure -> `references/debugging-loop.md`
- Test strategy / TDD / regression seam -> `references/testing-and-seams.md`
- PR/branch/change review -> `references/review-two-axis.md`
- Module/interface/domain architecture -> `references/architecture-and-domain.md`
- Work that spans multiple contexts/sessions -> `references/multi-session-delivery.md`

Do not load all references for routine work.

## Engineering rules

- Preserve project-local conventions and authority boundaries.
- Prefer root causes over symptom masking.
- Add/update tests for regressions and durable behavior when a meaningful seam exists.
- Keep public/private and secret boundaries intact.
- Use the best available execution surface: sandbox, GitHub Actions, external runner, connected development tool, or project-provided workflow.
- Treat missing SDK/toolchains as environment limitations, not reasons to fabricate build success.
- Keep generated artifacts and release checkpoints attributable to a source commit.
- Prefer reversible migrations and explicit rollback paths for risky changes.

## Completion evidence

A change is not done because code was written or a command was started. Use fresh evidence appropriate to the task: passing tests, build/CI conclusion, static checks, artifact inspection, targeted readback, runtime observation, or exact diff review.

Report what was actually verified, what could not be verified, and residual risk. Never convert queued/running CI or an uninspected artifact into a success claim.
