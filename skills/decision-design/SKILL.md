---
name: decision-design
description: Stress-test a plan, architecture, product decision, or idea by scaling process to the task, mapping dependent decisions, and resolving only the currently-unblocked frontier. Use for deliberate design/grilling sessions, not routine tasks.
---

# Decision Design

Use when the Creator wants a plan or idea challenged before action, or when a high-impact decision has material unresolved branches.

## Size the process first

Use the lightest process that safely fits the work:

- **Spike** — answer a feasibility/unknown cheaply; output is evidence/recommendation, not production code by default.
- **Bounded** — a well-scoped change to an existing flow; inspect context, resolve material uncertainty, then proceed without unnecessary design artifacts.
- **Architectural** — a new subsystem/project or change to shared interfaces/structure; map dependencies, compare approaches, and record durable decisions when useful.

If hidden complexity appears, upgrade the process path. Do not silently keep treating architectural work as a bounded tweak. Do not downgrade merely to avoid necessary reasoning.

This sizing is guidance, not a universal approval ritual. Existing Creator authority rules determine which decisions require explicit approval.

## Model the decision tree

Treat the design as dependencies between decisions. A question belongs to the current **frontier** only when its prerequisites are already settled or can be verified from available evidence.

Do not ask downstream questions whose answers depend on unresolved upstream choices.

## Facts are DEDAL's job; decisions are the Creator's

Before asking the Creator for factual information that can be inspected from repositories, files, tools, or public research, retrieve it. Present meaningful options, tradeoffs, and a recommendation.

Ask the Creator for choices that genuinely express goals, risk tolerance, product behavior, canon, irreversible direction, or other owner authority.

## Work in rounds

For substantial design sessions:
1. Map the unresolved branches.
2. Resolve facts with tools where possible.
3. Present the currently-unblocked decisions together, with concise recommendations.
4. Incorporate the Creator's answers.
5. Recompute the frontier.
6. Finish when no material unresolved branch remains or the Creator chooses to proceed with known uncertainty.

## Anti-ceremony rule

Do not turn ordinary work into an interview. If the task is already sufficiently specified, act. Use this skill deliberately for uncertainty that materially changes the solution.

## Completion

Summarize the settled decisions, rejected alternatives that matter, unresolved risks, and the next executable step. Propose a durable spec/ADR/checkpoint update when the decisions are worthy of persistence.
