---
name: self-improvement
description: Detect, repair, learn from, and close durable DEDAL failures or corrections by reconciling runtime truth, canonical source, regression guards, durable learning, and continuity state. Use for repeated mistakes, user corrections, regressions of previously fixed behavior, live/source drift, successful workarounds that should become canonical, or explicit DEDAL self-improvement work.
---

# Self-Improvement

Turn observed mistakes and successful recoveries into verified system improvement. This skill is a bounded learning-and-closure orchestrator, not an autonomous self-rewrite loop.

## Trigger when

Use this skill when the Creator corrects DEDAL, a failure may recur, a previously fixed behavior regresses, live/deployed behavior contradicts canonical source, a workaround proves a better recurring procedure, an existing skill is discovered to be wrong/incomplete, or the Creator explicitly asks DEDAL to learn or self-correct.

Do not trigger for every harmless transient error. One-off failures with no reusable correction may close as transient with a short reason.

## Core invariant

**A material fix is not closed until the relevant runtime truth, canonical source, regression guard, durable lesson, and continuity state are reconciled.**

A working hotfix is candidate state. A remembered lesson is candidate state. A green test alone is candidate state. Closure requires the right evidence at each owning layer.

## Operating loop

1. Observe and classify the symptom, evidence, and durability.
2. Restore the user path first when safe and authorized.
3. Identify the narrowest owning layer for implementation.
4. Find the source-of-truth chain that must agree.
5. Reconcile canonical source; production-only fixes create source-sync debt until cleared.
6. Add a regression guard when the failure is testable.
7. Route durable learning to the correct private/public layer.
8. Verify independently with read-back, CI, representative tasks, or another objective oracle.
9. Promote, revert, or mark inconclusive based on evidence.
10. If any required sink is missing, keep explicit learning/source-sync debt instead of claiming full closure.

Read `references/learning-closure.md` and `references/promotion-and-guardrails.md`.

## Learning modes

- **Automatic capture:** recognize corrections, recurring failures, regressions, and verified better procedures as learning candidates.
- **Same-turn repair:** repair the active workflow when existing authority and risk permit.
- **Bounded durable update:** update skills/tests/docs/checkpoints only through normal authority and mutation rules.
- **Propose-only escalation:** architecture-wide, permission-expanding, security-sensitive, or ambiguous changes remain proposals until required authority/evidence exists.

Self-improvement never expands Creator authority, tool permissions, platform permissions, or safety boundaries.

## Evidence discipline

Separate incident evidence, repair evidence, closure evidence, and outcome evidence. Lesson capture alone is not self-improvement. A deployed hotfix is not durable improvement if canonical source can overwrite it later.

## Boundaries

Self-Improvement owns learning-loop orchestration and closure, not every implementation. Pair with Reliability Engineering for incidents, Agent Engineering for harness changes, Quality Engineering for independent regression evidence, Skill Acquisition for external patterns, Knowledge/Memory for durable scope/provenance, and domain owners for behavior correction.

Reject unbounded autonomous self-modification, evaluator weakening, benchmark memorization, silent permission expansion, and broad rewrites without observed failure or evidence-backed capability gap.
