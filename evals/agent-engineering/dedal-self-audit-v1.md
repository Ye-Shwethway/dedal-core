# DEDAL Self-Audit v1

_Date: 2026-09-14_

## Purpose

Apply the Agent Engineering skill to DEDAL's own operating workflow and establish a truthful baseline for future harness improvements.

This audit distinguishes design rationale, contract validation, and measured outcome improvement. It does **not** claim that the changes below improve all DEDAL tasks until representative real-task evidence exists.

## Scope

Reviewed:
- boot / source-of-truth behavior;
- skill/context loading;
- GitHub mutation workflow;
- CI/status verification;
- tool-call efficiency;
- progress communication;
- long-session continuity;
- skill-promotion evidence.

## Existing strengths

1. Live repository/service state outranks memory.
2. The Master Index routes to the smallest matching skill set.
3. Skills use progressive disclosure instead of loading every reference by default.
4. GitHub Actions queued/running states are not treated as success.
5. Durable project state is externalized through checkpoints rather than relying only on conversational memory.
6. Creator authority and public/private boundaries are explicit.

## Findings

### AE-01 — Repository mutation path can be more transactional

Observed evidence: recent history contains a separate `noop` commit before the v0.9 Interface Design atomic commit. This resulted from mixing a direct contents write with a prepared tree transaction and then reconciling from the new HEAD.

Risk: extra commits, temporary partial states, avoidable reconciliation, and more tool calls.

Improvement: choose one mutation path for a coherent multi-file change. Prefer refresh HEAD -> complete tree -> commit -> fast-forward ref -> verify. If a direct write has already advanced HEAD, treat it as authoritative and rebuild from that HEAD rather than forcing.

### AE-02 — CI polling should become ID-scoped and bounded

Observed pattern: after a push, broad workflow-list/status calls may be repeated until the new run appears, then the specific run/job is checked.

Risk: unnecessary calls/context output and ambiguous stopping behavior when registration is delayed.

Improvement: one bounded registration check, capture the specific run ID, then poll only that run/job. Pending state remains pending if completion cannot be observed.

### AE-03 — Context loading is good but lacks an explicit no-reread rule

Current boot and routing rules already minimize skill loading, but they do not explicitly say that stable constitutional files need not be reread repeatedly inside one coherent task.

Improvement: bootstrap once when appropriate, then reload only on conflict, state change, or task transition.

### AE-04 — Promotion evidence can be stated more precisely

Several newer skills have architecture/contract validation before extensive real-world use. This is useful, but contract correctness is not the same as measured task improvement.

Improvement: label evidence stage explicitly in claims: design rationale, contract validation, or outcome validation. Use representative task comparisons before claiming measured improvement.

### AE-05 — Long-horizon continuity is strong but can be made more executable

Checkpoints preserve accepted state well. Some checkpoints can improve by emphasizing the next executable step and unresolved verification risk, rather than mainly summarizing completed architecture.

Improvement: worthy checkpoints should include accepted state, completed evidence, unresolved risks, and next executable step.

## Harness v1 contract

DEDAL should use this lightweight execution loop for substantial tool-using work:

`frame work unit -> load minimal context -> inspect live state -> execute with bounded tools/loops -> verify at required evidence level -> report -> checkpoint only if durable`

### Work-unit fields

- goal;
- authority;
- live sources of truth;
- success evidence;
- risk/irreversibility;
- loop/stop conditions.

These fields may remain implicit for routine work; do not add user-visible ceremony without benefit.

## Regression assertions

Fail future harness revisions if they encourage:
- rereading the entire Core on every turn;
- broad tool output when scoped evidence is sufficient;
- concurrent writes to the same state owner;
- force-updating refs to avoid normal reconciliation;
- unbounded CI/status polling;
- declaring outcome improvement from contract checks alone;
- checkpoint prose that omits unresolved risk or the next executable step when those matter.

## Outcome-validation plan

Use future real tasks from at least three different domains, such as:
1. a multi-file GitHub/Core update;
2. a current-information research task with several sources;
3. a long-session software/project workflow.

Compare qualitative friction and, where observable, tool-call count, redundant context retrieval, recovery behavior, completion evidence, and Creator corrections. Do not optimize a single metric at the expense of correctness.
