---
name: skill-acquisition
description: Discover, audit, compare, adapt, evaluate, and promote external Agent Skills patterns into DEDAL without blindly trusting or copying third-party packages.
---

# Skill Acquisition

Use the public skill ecosystem as a source of tested ideas, not as an authority boundary.

## Principle

**Reuse ideas; inherit trust only after verification.**

External skills are untrusted inputs until reviewed. Prefer adaptation over verbatim import unless exact portability, license, provenance, and security have all been established.

## Pipeline

1. **Define the capability gap.** Start from a concrete DEDAL workflow or known weakness, not generic browsing.
2. **Discover broadly.** Search official/vendor skill collections, the Agent Skills ecosystem, reputable GitHub repositories, and public registries such as ClawHub/skills.sh when relevant.
3. **Shortlist by evidence.** Evaluate relevance, maintenance, author/repository signals, documentation quality, tests/evals, license, portability, runtime assumptions, and security surface. Popularity is only a weak signal.
4. **Audit before execution.** Read `references/security-audit.md`. Do not install or run third-party scripts merely to inspect a skill.
5. **Extract patterns.** Identify useful workflow gates, trigger design, progressive-disclosure structure, failure handling, verification, schemas, tests, and tooling ideas. Separate generalizable ideas from provider-specific mechanics.
6. **Adapt to DEDAL.** Preserve Stable Kernel rules, Creator authority, smallest-sufficient routing, live-state-over-memory, public/private separation, truthful capability reporting, and provider-agnostic execution where practical.
7. **Evaluate.** Compare current DEDAL behavior against the candidate-derived design on representative tasks or regression fixtures. A prettier SKILL.md is not evidence of improvement.
8. **Promote deliberately.** Activate only when the adapted skill is clearly useful, license/provenance are recorded, security boundaries are acceptable, and evaluation shows no material regression.
9. **Review later.** External sources can drift. Re-check important upstream patterns when the relevant DEDAL skill is being materially revised.

## Source classes

Prefer, in order when quality is otherwise comparable:

- open standards/specifications and first-party vendor examples;
- mature public repositories with tests, history, and clear licensing;
- well-audited registry packages;
- community examples used primarily for ideas.

Never treat stars, install counts, registry badges, malware scans, or model-generated security verdicts as sufficient proof of safety or quality.

## Copying versus adapting

Verbatim import requires a compatible license, preserved attribution/provenance, understood scripts/dependencies, and a strong reason exact code/content is better than a DEDAL-native rewrite.

For instruction-heavy skills, default to synthesis: keep the useful idea, rewrite the operational contract around DEDAL, and record influences in adaptation notes or benchmark evidence.

## References

- `references/source-evaluation.md` — shortlist and scoring criteria.
- `references/security-audit.md` — trust-boundary and supply-chain review.
- `references/adaptation-and-evals.md` — adaptation and promotion gates.
- `references/initial-benchmark-2026-09-14.md` — first ecosystem survey and accepted/rejected patterns.
