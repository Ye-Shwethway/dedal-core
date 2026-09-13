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

## 3. No-op guard

Before a direct update, compare intended content/state with the authoritative current target. If there is no semantic change, do not write.

For an atomic transaction, ensure the prepared tree differs from the observed base tree in the intended paths before creating the milestone commit.

## 4. HEAD drift

The observed parent HEAD belongs to the transaction. If HEAD changes before `update_ref`:

1. do not force;
2. inspect the new HEAD;
3. determine whether the movement is external or from this work unit;
4. rebuild/reconcile from the new authoritative state if the transaction still applies.

## 5. Completion

A mutation is not complete until the final branch/ref state is read back or otherwise verified. CI/build/runtime evidence is separate and should be checked only to the level required by the task.
