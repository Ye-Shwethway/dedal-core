# Applying Agent Engineering to DEDAL

Use this reference when DEDAL is improving its own operating workflow rather than designing an external agent system.

## Work-unit envelope
Before substantial multi-step execution, establish the smallest useful envelope: goal, authoritative sources, mutation authority, success evidence, meaningful risks, and stop/escalation conditions. Do not turn this into ceremony for trivial work.

## Context discipline
Bootstrap constitutional state once when needed; load only matching skill entrypoints and references on demand; prefer live project/repository/service state over remembered summaries; keep transient tool output out of durable context unless it changes a decision or proves completion.

## Verified-state promotion
Treat model/executor claims as candidate state, not accepted state. Promote only when the evidence level matches the claim: read-back for mutations, tests for behavior, artifact attribution for builds, deployment/runtime checks for deployed behavior, or another authoritative verifier. Prefer compact verified facts and references over raw trajectory replay. Separate verifier roles should be read-only where practical; verifier-created mutation contaminates independent evidence unless explicitly authorized and separately accounted for.

## Controlled self-improvement
Treat every material DEDAL self-change as an experiment, not an assumed upgrade.

1. Start from an observed failure, measurable friction, explicit Creator request, or externally evidenced capability gap.
2. State one bounded hypothesis and the smallest plausible owning-layer change.
3. Freeze the comparison baseline and evaluation contract before judging the candidate.
4. Keep evaluator/verification logic independent from the candidate change where practical; a candidate must not rewrite its own acceptance test.
5. Use representative held-in tasks for the known failure and at least one held-out/regression case for collateral behavior when the change is material.
6. Reject task-specific benchmaxxing or patches that merely memorize named eval cases.
7. Promote only when comparable evidence supports the intended gain without material regression; otherwise revert or mark inconclusive.
8. Preserve failed experiments as evidence when they teach a reusable constraint, but do not carry failed candidate state forward as accepted truth.
9. Do not generalize upstream benchmark gains into DEDAL outcome claims.
10. Automation may propose or test bounded changes, but Creator authority, platform safety, and mutation permissions remain unchanged.

The control loop is:
`observe -> classify owner -> hypothesize -> isolate candidate -> run comparable eval -> inspect regressions -> retain/revert -> record evidence`

## Tool-call discipline
Batch independent reads/searches when possible, serialize writes to the same owner, prefer the narrowest sufficient tool, avoid large outputs, and treat tool errors as observations rather than reasons for blind retry.

## Git transaction pattern
Before repository mutation, lock direct-single-file or atomic-multi-file mode. Atomic mode refreshes HEAD, prepares the whole write set, creates one tree/commit without contents writes, fast-forwards only from the observed HEAD, reconciles drift without force, then verifies final state and relevant CI. No-op commits are regressions, not progress.

## Completion evidence ladder
Use only as much evidence as needed: mutation receipt -> read-back -> test/CI -> build attribution -> deployment/runtime verification. A model saying complete never substitutes for an available objective check.

## Long-horizon continuity
Leave accepted state, completed evidence, unresolved risks/failures, and next executable step. Do not persist hidden chain-of-thought or private data for continuity.

## Evidence maturity
Separate design rationale, contract validation, and outcome validation. Contract validation is not proof that representative real-task outcomes improved.
