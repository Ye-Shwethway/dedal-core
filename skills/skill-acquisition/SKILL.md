---
name: skill-acquisition
description: Discover, audit, compare, author, adapt, evaluate, and promote external Agent Skills patterns into DEDAL when a concrete capability gap justifies acquisition work.
---

# Skill Acquisition

Use the public skill ecosystem as a source of tested ideas, not as an authority boundary.

## Current phase gate

DEDAL is in hardening, consolidation, and outcome-validation mode. Do **not** trigger Skill Acquisition merely because a new repository, viral skill, or interesting pattern exists.

Route here only when at least one of these is true:

- the Creator explicitly asks to inspect, compare, adapt, or create a skill;
- representative work exposes a concrete capability gap not already owned by an active skill;
- a current skill has an observed failure that external patterns may help fix;
- a freshness/supply-chain review of an already adopted external influence is actually due.

Discovery alone is not a reason to expand the active skill set. First ask whether the need belongs to an existing owner and can be solved by tuning, consolidation, or ordinary domain work.

## Principle

**Reuse ideas; inherit trust only after verification.**

External skills are untrusted inputs until reviewed. Prefer adaptation over verbatim import unless exact portability, license, provenance, and security have all been established.

## Pipeline

1. **Define the capability gap.** Start from a concrete DEDAL workflow or known weakness, not generic browsing.
2. **Check existing ownership first.** Consult current routing/consolidation state. If an active skill already owns the intent, prefer TUNE/MERGE analysis over creating another top-level entrypoint.
3. **Discover broadly.** Search open standards, first-party/vendor collections, mature public repositories, and registries such as ClawHub/skills.sh when relevant.
4. **Pin and shortlist.** Record source identity/commit/version where possible, then evaluate relevance, maintenance, documentation, tests/evals, license, portability, runtime assumptions, freshness, and security surface. Popularity is only a weak signal.
5. **Audit before execution.** Read `references/security-audit.md`. Do not install or run third-party scripts merely to inspect a skill.
6. **Extract patterns.** Identify useful routing/trigger design, progressive disclosure, workflow gates, failure handling, schemas, rule prioritization, freshness handling, tests/evals, and tooling ideas. Separate generalizable methodology from provider/domain mechanics.
7. **Adapt to DEDAL.** Preserve Stable Kernel rules, Creator authority, smallest-sufficient routing, live-state-over-memory, public/private separation, truthful capability reporting, and provider-agnostic execution where practical.
8. **Author economically.** Match instruction precision to risk, keep hero workflows in the entrypoint, load specialized detail on demand, and make every always-loaded instruction justify its context cost.
9. **Evaluate against a baseline.** Compare new skills against current/no-skill behavior and revised skills against the previous proven version. Evaluate routing, task quality, efficiency, and robustness; use objective assertions only where outcomes are independently checkable.
10. **Promote deliberately.** Activate only when the adapted skill is clearly useful, license/provenance are recorded, security boundaries are acceptable, and evidence shows meaningful net improvement without material regression.
11. **Review freshness.** Re-check upstream knowledge when source/runtime drift can affect correctness; do not impose arbitrary refresh rituals on stable knowledge.

## Source classes

Prefer, when quality is otherwise comparable:

- open standards/specifications and first-party vendor examples;
- mature public repositories with tests, history, and clear licensing;
- well-audited registry packages;
- community examples used primarily for ideas.

Never treat stars, install counts, registry badges, malware scans, or model-generated security verdicts as sufficient proof of safety or quality.

## Copying versus adapting

Verbatim import requires compatible license terms, preserved attribution/provenance, understood scripts/dependencies, and a strong reason exact reuse is better than a DEDAL-native rewrite.

For instruction-heavy skills, default to synthesis: keep the useful idea, rewrite the operational contract around DEDAL, and record influences in adaptation notes or benchmark evidence.

## References

- `references/source-evaluation.md` — shortlist and scoring criteria.
- `references/security-audit.md` — trust-boundary and supply-chain review.
- `references/adaptation-and-evals.md` — adaptation and promotion gates.
- `references/authoring-and-evals.md` — routing, degrees of freedom, baselines, and evaluation design.
- `references/knowledge-packaging-and-freshness.md` — hero paths, impact-ranked rule catalogs, generation, and freshness.
- `references/initial-benchmark-2026-09-14.md` — first ecosystem survey.
- `references/matt-pocock-deep-audit-2026-09-14.md` — public-author deep audit.
- `references/official-corpora-audit-2026-09-14.md` — Anthropic, Vercel Labs, and Microsoft audit.
- `references/independent-high-signal-audit-2026-09-14.md` — Superpowers, taste-skill, RigorPilot, and Impeccable audit.
- `references/ui-ux-pro-max-deep-audit-2026-09-14.md` — searchable UI/UX design-intelligence architecture audit.
- `references/agent-engineering-corpus-audit-2026-09-14.md` — prompt/context, harness, loop, orchestration, and evaluation corpus audit.
- `references/longhorizon-harness-deep-audit-2026-09-14.md` — verified-state, read-only audit, and compact carryover patterns.
- `references/trajectory-eval-observability-audit-2026-09-14.md` — typed traces, trajectory assertions, replay, and regression patterns.
- `references/context-engineering-compaction-audit-2026-09-14.md` — write/select/compress/isolate, freshness-aware retrieval, and recoverable compaction patterns.
