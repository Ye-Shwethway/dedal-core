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

The broad proactive capability-expansion wave closed at v0.24.0. An explicit Creator request plus demonstrated manual workflows reopened a **bounded creative-production wave** at v0.25.0 for Video Production and Presentation Engineering. This does not reopen default marketplace scanning; future expansion remains evidence-gated.

## Principle

**Reuse ideas; inherit trust only after verification.**

External skills are untrusted inputs until reviewed. Prefer adaptation over verbatim import unless exact portability, license, provenance, and security have all been established.

## Pipeline

1. **Define the capability gap.** Start from a concrete DEDAL workflow or known weakness, not generic browsing.
2. **Check existing ownership first.** Consult current routing/consolidation state. If an active skill already owns the intent, prefer TUNE/MERGE analysis over creating another top-level entrypoint.
3. **Discover broadly.** Search open standards, first-party/vendor collections, mature public repositories, and registries when relevant.
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

For instruction-heavy skills, default to synthesis: keep the useful idea, rewrite the operational contract around DEDAL, and record influences in adaptation notes or benchmark evidence. Proprietary skill material may be used only as high-level comparative evidence when its license forbids copying or derivative reuse.

## References

Core acquisition references include source evaluation, security audit, adaptation/evals, authoring, freshness, and the historical capability audits in this directory.

Latest creative-production audits:
- `references/video-production-deep-audit-2026-09-14.md` — generative-video direction, Remotion/FFmpeg, temporal ownership, tool boundary, and promotion decision.
- `references/video-post-production-hardening-audit-2026-09-14.md` — professional editing/effects, transitions, audio, captions, color, automation patterns, and TUNE/MERGE decision.
- `references/presentation-engineering-deep-audit-2026-09-14.md` — source-first PPTX, narrative/evidence architecture, editability/render QA, licensing boundary, and promotion decision.

Previous wave close:
- `references/infrastructure-engineering-deep-audit-2026-09-14.md` — infrastructure lifecycle promotion and v0.24.0 broad-wave close.
