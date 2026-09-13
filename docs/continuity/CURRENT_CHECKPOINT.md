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

## Agent Engineering self-application

DEDAL has applied Agent Engineering to its own operating workflow. Baseline audit: `evals/agent-engineering/dedal-self-audit-v1.md`. Durable guidance: `skills/agent-engineering/references/dedal-self-application.md`.

Harness v1:

`frame work unit -> load minimal context -> inspect live state -> execute with bounded tools/loops -> verify at required evidence level -> report -> checkpoint only if durable`

Current rules include atomic/coherent mutation paths for multi-file GitHub work, bounded run-ID-scoped CI verification, minimal/JIT context loading, evidence-maturity labels, and executable long-horizon checkpoints.

## Harness Benchmark v1

A compact outcome-validation suite now lives at `evals/harness-benchmark/`.

It intentionally uses only six cases across three domains:
- GitHub transaction / CI verification;
- research freshness / evidence coverage;
- long-horizon checkpoint / interruption recovery.

Ground-truth policy:
1. deterministic verifier or exact state readback;
2. authoritative source or fixed rubric;
3. independent evaluator when needed;
4. Creator feedback for acceptance/friction/intent, not as the default low-level technical oracle.

Score results are PASS / PARTIAL / FAIL. Diagnostic counts are recorded only when observable; no synthetic precision or invented percentage gain is allowed.

Promotion gate: Harness v1 remains **contract-validated with accumulating outcome evidence** until all six cases have representative runs, no correctness/authority/completion-evidence regression is observed, and at least one prior harness failure is demonstrably avoided or recovered better.

## Existing self-audit evidence

- Source-of-truth, smallest-skill routing, truthful completion, Creator authority, and public/private boundaries are strong.
- Historical v0.9 work contains a standalone `noop` reconciliation commit from a mixed write path; this is the principal baseline for GH-01 transactional improvement.
- CI queued/running states remain explicitly non-success.
- Stable constitutional/context files should not be repeatedly reread inside one coherent task without state-change/conflict reason.

## Verification status

Repo Integrity continues to validate the Core and active skills. Harness Benchmark v1 is an evaluation layer, not a new capability release; therefore VERSION remains `0.11.0` until outcome evidence warrants a later release decision.

Fresh-chat bootstrap E2E remains **PASS** (`evals/boot/minimal-bootstrap-v1.md`).

## Next executable step

1. Complete the first smoke run by using benchmark-suite creation itself as GH-01 and its CI as GH-02.
2. Exercise RS-01/RS-02 on the next suitable current-information research task rather than manufacturing a large artificial research job.
3. Exercise LH-01/LH-02 on the next real multi-session/new-chat project transition.
4. After all six have evidence, compare regressions/friction and decide whether Harness v1 is outcome-validated or needs revision.

Unresolved risk: only GitHub cases can be outcome-tested immediately without creating artificial work. Research and long-horizon cases should accumulate from real tasks.

Do not expand the Stable Kernel merely to optimize benchmark scores or encode temporary model/tool limitations.
