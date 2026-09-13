# Retrieval, compaction, and governance

## Retrieval goal

The goal is not maximum recall. The goal is the smallest context package that preserves task correctness and continuity.

Prefer this order:
1. exact canonical record/file/entity IDs;
2. project/task/scope filters;
3. current checkpoint/index/manifest;
4. high-signal lexical/semantic retrieval when available;
5. bounded broader fallback only when narrow retrieval misses necessary evidence.

Do not load every memory layer by default.

## Context assembly

A good task context pack contains only what materially influences the next action:
- current goal;
- accepted decisions/constraints;
- relevant evidence or source pointers;
- unresolved risks/questions;
- current state/version identity;
- next executable step.

Raw historical chat/tool traces are not automatically useful context.

## Compaction

Compaction converts a larger trace into a smaller continuity artifact. Preserve:
- decisions that constrain future work;
- completed actions with verification evidence;
- failures/regressions that prevent repetition;
- unresolved risks/blockers;
- source identities needed for re-verification;
- next executable step.

Discard first:
- duplicated explanations;
- superseded scratch plans;
- raw tool payloads whose durable result is already recorded;
- conversational filler;
- repeated restatements.

Never compact uncertainty into certainty. If source/evidence was incomplete, the compacted record must retain that limitation.

## Checkpoint quality

A checkpoint is executable when a fresh session can answer:
- what is accepted/current?
- what is already done and verified?
- what failed or remains risky?
- what must not be re-asked or silently changed?
- what exact next step should run?

A narrative history without a next action is not enough.

## Governance

Memory systems need explicit controls for:
- scope/access;
- sensitivity;
- retention/retirement;
- correction/supersession;
- deletion/forgetting in the actual owner;
- auditability;
- migration between stores;
- derived summaries/indexes.

Do not claim a model can delete or revoke state it does not own.

## Evaluation

Evaluate memory architecture on downstream behavior:
- relevant recall without context dumping;
- correct live-state re-verification;
- low contradiction/staleness error rate;
- correct scope isolation;
- continuity after context reset;
- resistance to untrusted-memory poisoning;
- appropriate retention and forgetting;
- bounded token/tool cost.

Large memory size or high retrieval count is not a success metric by itself.
