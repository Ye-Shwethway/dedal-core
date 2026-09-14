# Applying Agent Engineering to DEDAL

Use this reference when DEDAL is improving its own operating workflow rather than designing an external agent system.

## Work-unit envelope

Before substantial multi-step execution, establish the smallest useful envelope:

- goal / requested outcome;
- authoritative source(s) of truth;
- current authority for mutations or irreversible actions;
- success evidence;
- meaningful risks;
- stop / escalation conditions.

Do not turn this into ceremony for trivial work.

## Context discipline

1. Bootstrap constitutional state once for a coherent task/session when needed.
2. Load only the matching skill entrypoint(s), then references on demand.
3. Do not repeatedly reread stable documents unless state may have changed or a conflict appears.
4. Prefer live project/repository/service state over remembered summaries.
5. Keep transient tool output out of durable context unless it changes a decision or proves completion.

## Verified-state promotion

Treat model/executor claims as **candidate state**, not accepted state.

Promote a claim into durable accepted state only when the evidence level matches the claim: read-back for mutations, tests for behavior, artifact attribution for builds, deployment/runtime checks for deployed behavior, or another independent authoritative verifier when appropriate.

For long-horizon work, carry forward compact verified facts, accepted decisions, unresolved gaps, and references. Keep raw trajectories/logs available for diagnosis rather than replaying them into every future context.

When a separate verifier/auditor role is useful, prefer read-only authority where the execution surface supports it. A verifier that changes the state it is judging creates contaminated evidence; reject or downgrade that audit unless mutation was explicitly part of the verifier contract and independently accounted for.

Do not require a separate verifier agent when deterministic tests, service read-back, CI, or another cheaper objective check provides equivalent evidence.

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

- Batch independent reads/searches when possible.
- Serialize writes that touch the same state owner.
- Prefer the narrowest tool that returns enough evidence.
- Avoid large outputs when a scoped query, range, diff, or status is enough.
- Treat tool errors as observations: refine the call or change strategy rather than blindly repeating it.

## Git transaction pattern

Before the first repository mutation, lock one mode for the work unit:

- **direct single-file write** — one isolated file change where a contents write is the natural transaction; or
- **atomic multi-file transaction** — one coherent milestone spanning multiple files.

For atomic multi-file mode:

1. refresh branch HEAD;
2. prepare the complete coherent write set;
3. create the tree and commit without direct contents writes for that work unit;
4. fast-forward the branch ref from the observed HEAD;
5. if the ref moved because of an observed external change, refetch and rebuild/reconcile from the new authoritative HEAD instead of forcing;
6. verify final branch state and relevant CI.

For direct single-file mode, compare the intended content with current content before updating. If they are identical, skip the write entirely; a no-op commit is a harness regression, not progress.

Do not switch mutation modes mid-unit merely because a different tool is convenient. Complete, abandon, or explicitly reconcile the current transaction first.

## Bounded status polling

Polling must have a reason and a bound.

- First check whether the downstream run/status is registered.
- If queued/running, poll only the specific run/status needed for the user's completion claim.
- Prefer job/step status over refetching broad workflow lists once the run ID is known.
- Stop after a reasonable bounded sequence and report pending state truthfully if completion cannot yet be observed in the current turn.

## Completion evidence ladder

Use only as much evidence as the task requires:

1. mutation receipt;
2. read-back / final-state verification;
3. test or CI conclusion;
4. build/artifact attribution;
5. deployment/runtime verification.

Do not climb higher when the task does not require it, and do not claim a higher level from lower-level evidence.

A model or manager saying a task is complete is never a substitute for an available objective completion check. When objective verification exists, completion becomes accepted state only after that check passes.

## Progress communication

Update the Creator at meaningful milestones or when a finding changes direction. Do not narrate every tool call. Surface useful partial findings early.

## Long-horizon continuity

When work spans sessions or risks context loss, leave a compact truthful handoff in the owning project/repository:

- accepted state;
- evidence completed;
- unresolved risks/failures;
- next executable step.

Do not persist hidden chain-of-thought or private data merely for continuity.

## Self-improvement evidence

Separate three claims:

- **design rationale** — why a harness change should help;
- **contract validation** — whether the new rules are internally consistent and regression-safe;
- **outcome validation** — whether representative real tasks actually improved versus baseline.

Contract validation is not proof of outcome improvement. Capture real-task evidence before making stronger claims.
