# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.11.0`
- Purpose: durable public operational core for DEDAL

## Active Skills

Domain: `$msa`, `$pra`, `$ika`.
Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Interface Design, **Agent Engineering**, Automations, Skill Acquisition.

## Harness v1

Execution contract:

`frame work unit -> load minimal context -> inspect live state -> execute with bounded tools/loops -> verify at required evidence level -> report -> checkpoint only if durable`

Harness v1 remains **contract-validated with accumulating outcome evidence**.

## Harness Benchmark v1

Compact suite: `evals/harness-benchmark/`.

Six cases across three domains:
- GH-01 atomic multi-file mutation;
- GH-02 pending CI semantics;
- RS-01 freshness/source authority;
- RS-02 evidence coverage without context dumping;
- LH-01 executable checkpoint;
- LH-02 interruption/recovery.

Ground truth prioritizes deterministic verification and authoritative sources. Creator feedback is an acceptance/friction/intent signal, not the default technical oracle.

### Smoke run 001

Record: `evals/harness-benchmark/runs/2026-09-14-smoke-001.md`.

- **GH-01: FAIL, safe recovery.** The run mixed mutation paths, created an avoidable checkpoint commit plus a mistaken same-content `VERSION` `noop` commit, then recovered by refreshing live HEAD, rebuilding from authoritative state, and fast-forwarding without force/history rewrite.
- **GH-02: PASS.** Repo Integrity run `34776303822` was captured after one commit-scoped registration lookup; subsequent checks targeted that run only, and success was not claimed until the job reached `completed / success`.

New regression lesson: before a coherent multi-file mutation, lock the mutation mode for the work unit (`tree transaction` or `direct single-file write`). Do not switch modes unless an observed external state change makes reconciliation necessary.

This failure is outcome evidence that the Harness contract still needs execution reinforcement; it is not hidden or reclassified as success.

## Verification / release status

VERSION remains `0.11.0`. The benchmark suite is evaluation infrastructure, not a new capability release. Do not bump the release merely because the suite exists.

Fresh-chat bootstrap E2E remains **PASS** (`evals/boot/minimal-bootstrap-v1.md`).

## Next executable step

1. Encode the GH-01 mutation-mode lock into the GitHub/Agent Engineering workflow before the next substantial multi-file Core mutation.
2. Exercise RS-01/RS-02 on the next suitable real current-information research task; avoid manufacturing a large artificial job.
3. Exercise LH-01/LH-02 on the next real multi-session/new-chat transition.
4. After all six cases have evidence, decide whether Harness v1 is outcome-validated or needs another revision.

Unresolved risk: one of the two immediately exercised GitHub cases failed. Do not claim general efficiency improvement yet.
