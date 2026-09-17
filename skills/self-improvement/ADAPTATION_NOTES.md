# Adaptation Notes — Self-Improvement

## Why a dedicated skill now exists

A 2026-09-14 audit concluded that a separate self-improvement skill was not yet justified because Agent Engineering already owned controlled self-change and there was no representative DEDAL outcome failure proving a routing gap.

That decision is superseded by later real workflow evidence: a previously successful production behavior was repaired live but not fully synchronized into canonical source and regression coverage, so a later refactor reintroduced retired behavior. The failure crossed Agent Engineering, Reliability, Quality, source control, continuity, and private learning boundaries. A dedicated closure orchestrator became independently routable and useful.

## External influences

Patterns were adapted, not copied verbatim:
- OpenClaw current self-learning documentation — immediate repair, propose/auto learning modes, learned skills as durable procedures.
- `pskoett/self-improving-agent` at `b889ef0724c27b7181111b8dd1ac3a108d0b5160` — explicit error/correction triggers and durable learning capture.
- `X-RayLuan/openclaw-self-improvement` at `31602e115385c1cc185eab9f8ec4a8a70b8a99ef` — repeated-failure guardrails, repair loops, and promotion into operating rules.

Reviewed on 2026-09-18. No third-party runtime, hook, or script is required.

## DEDAL-specific additions

DEDAL adds live/canonical source reconciliation, source-sync debt, executable regression guards when testable, public/private lesson routing, protected evaluation, and explicit unresolved debt instead of optimistic closure.
