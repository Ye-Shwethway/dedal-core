# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.7.0`
- Purpose: durable public operational core for DEDAL

## Active Skills

Domain: `$msa`, `$pra`, `$ika`.
Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Automations, Skill Acquisition.

## Skill Ecosystem Campaign

DEDAL now uses a repeatable external-skill acquisition pipeline rather than isolated from-scratch authoring:

`capability gap -> discover -> pin -> audit -> extract patterns -> DEDAL adaptation -> baseline evaluation -> promote/reject -> regression capture`

Key policy: **reuse ideas; do not inherit trust blindly.**

### Completed corpora

1. `mattpocock/skills` @ `3cca18b368ae95cdbdebbff572ccafa662551015`
   - produced Decision Design plus focused Software Development references.
2. `anthropics/skills` @ `34040c9c568585f6929bedeaad110ad08f079624`
3. `vercel-labs/agent-skills` @ `063bee94c3f4df8453406c830b0a7df0f2860278`
4. `microsoft/skills` @ `903dc62b1e4c833235b54db918a9a51cb6d3cc8f`

The second corpus campaign improved Skill Acquisition itself rather than adding more top-level skills.

## Skill Authoring Standard

For new or materially revised skills:
- define trigger/non-trigger contexts, expected outcome, authority/tool dependencies, and success criteria before writing prose;
- match instruction precision to risk: high freedom for heuristics, low freedom for exact/dangerous workflows;
- keep dominant/co-equal hero workflows in the entrypoint and push uncommon detail to references;
- treat always-loaded context as a cost that must justify itself;
- evaluate routing, task quality, efficiency, and robustness separately;
- compare new skills against current/no-skill behavior and revisions against the previous proven version when feasible;
- use objective assertions only for independently verifiable outcomes and qualitative Creator review for subjective work.

See `skills/skill-acquisition/references/authoring-and-evals.md`.

## Knowledge Packaging and Freshness

For large rule/domain/API skills:
- rank rules/categories by impact or risk when that helps prioritization;
- keep granular rules in references with stable names/IDs when useful;
- prefer reproducible source -> generation -> validation pipelines for generated knowledge;
- record source/version/reviewed-or-generated dates when correctness can drift;
- verify current runtime/API/package state before irreversible actions even when the skill is recent.

See `skills/skill-acquisition/references/knowledge-packaging-and-freshness.md`.

## License / Provenance Boundary

- Matt Pocock audit: MIT verified.
- Microsoft skills: root MIT verified.
- Anthropic and Vercel pinned snapshots did not expose one verified repository-wide root license during this audit; DEDAL used conceptual synthesis only and did not copy/install their packages.
- Every future verbatim import still requires source-specific license verification.

## Verification

`repo-integrity.yml` validates foundational/kernel files, registries, active skill entrypoints, imported/adapted provenance, Matt audit, official corpus audit, Skill Acquisition reference set, and semantic version format.

Fresh-chat bootstrap E2E test remains **PASS** (`evals/boot/minimal-bootstrap-v1.md`). Re-run it after boot/kernel/router/layout changes.

## Next Phase

1. Continue high-signal scans with strong public evidence, prioritizing respected authors/organizations and skills.sh/ClawHub candidates that cover genuine DEDAL gaps.
2. Use the new baseline-eval discipline before materially replacing already-proven DEDAL behavior.
3. Prefer improving existing skills over multiplying top-level skills.
4. Consider new top-level skills only when independently routable and repeatedly useful across projects.
5. Keep private/personal/project operational state outside the public core.

Do not expand the Stable Kernel merely to capture ecosystem fashions or project-specific rules.