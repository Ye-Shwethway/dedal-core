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
