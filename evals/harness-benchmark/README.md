# DEDAL Harness Benchmark v1

_Date: 2026-09-14_

## Goal

Provide a small, repeatable verification suite for DEDAL Harness v1 without making the Creator act as a technical ground-truth oracle.

The suite favors mechanical verification, authoritative source checks, and explicit rubrics. Creator feedback is an acceptance/UX signal, not the primary correctness oracle.

## Size

Six compact cases across three domains:

- GitHub / transactional tool use: 2
- Research / evidence handling: 2
- Long-horizon continuity / recovery: 2

This is intentionally a smoke benchmark, not a giant leaderboard.

## Evidence hierarchy

For each case, prefer:
1. deterministic verifier / test / exact state readback;
2. authoritative source or fixed rubric;
3. independent evaluator with explicit criteria;
4. Creator acceptance signal for intent/friction/taste.

Do not claim outcome improvement from contract conformance alone.

## Score dimensions

Each case scores only dimensions that are observable:
- correctness;
- verification quality;
- recovery / non-progress behavior;
- context discipline;
- tool-call efficiency;
- authority/safety adherence;
- continuity/handoff quality.

Use PASS / PARTIAL / FAIL for primary assertions. Record counts only when they are actually observable.

## A/B policy

Use the nearest meaningful baseline:
- historical observed pre-Harness behavior when the same failure mode is documented;
- previous proven harness behavior for future revisions;
- no-special-harness behavior only when it can be run comparably.

Do not invent synthetic numeric gains when exact comparable runs are unavailable.

## Files

- `cases.yaml` — six benchmark cases and assertions.
- `scorecard.md` — scoring and promotion rules.
- `runs/2026-09-14-smoke-001.md` — first live run using benchmark-suite creation itself as the transactional GitHub case.
