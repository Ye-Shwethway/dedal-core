# Mutation Preflight

Use this preflight immediately before repository writes when a task changes Git state.

## 1. Lock the work-unit mode

Choose exactly one:

- `direct-single-file`
- `atomic-multi-file`

Do not switch modes because another write tool looks convenient.

## 2. Lock the allowed write tools

For `direct-single-file`, allowed mutation tools are only the direct contents write/delete action needed for that one target after a content/state preflight.

For `atomic-multi-file`, allowed mutation sequence is:

`create_blob(s) -> create_tree -> create_commit -> update_ref`

Direct contents create/update/delete actions are forbidden inside the same atomic work unit.

Read/status/diff tools remain allowed because they do not mutate state.

## 3. Runtime guard

When the host/harness can execute DEDAL Core runtime contracts, instantiate `runtime/github_mutation_guard.py` at mode lock and route every GitHub mutation through that guard before provider execution. Record success only after the provider mutation succeeds.

The guard is fail-closed for known mode violations and for mutation tools that the host identifies as mutations but that are unknown to the current policy.

The public Core repository cannot intercept native provider tools by itself. If the current host cannot wire the guard into dispatch, state that enforcement gap explicitly; do not describe instruction-only compliance as runtime enforcement.

See `runtime/README.md` and `runtime/github-mutation-policy.json`.

## 4. No-op guard

Before a direct update, compare intended content/state with the authoritative current target. If there is no semantic change, do not write.

For an atomic transaction, ensure the prepared tree differs from the observed base tree in the intended paths before creating the milestone commit.

## 5. HEAD drift

The observed parent HEAD belongs to the transaction. If HEAD changes before `update_ref`:

1. do not force;
2. inspect the new HEAD;
3. determine whether the movement is external or from this work unit;
4. rebuild/reconcile from the new authoritative state if the transaction still applies.

## 6. Completion

A mutation is not complete until the final branch/ref state is read back or otherwise verified. CI/build/runtime evidence is separate and should be checked only to the level required by the task.
