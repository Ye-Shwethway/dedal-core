# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.8.0`
- Purpose: durable public operational core for DEDAL

## Active Skills

Domain: `$msa`, `$pra`, `$ika`.
Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Interface Design, Automations, Skill Acquisition.

## Skill Ecosystem Campaign

DEDAL uses a repeatable external-skill acquisition pipeline:

`capability gap -> discover -> pin -> audit -> extract patterns -> DEDAL adaptation -> baseline evaluation -> promote/reject -> regression capture`

Key policy: **reuse ideas; do not inherit trust blindly.** Popularity/install counts are discovery signals only.

### Completed corpora

1. `mattpocock/skills` @ `3cca18b368ae95cdbdebbff572ccafa662551015`
2. `anthropics/skills` @ `34040c9c568585f6929bedeaad110ad08f079624`
3. `vercel-labs/agent-skills` @ `063bee94c3f4df8453406c830b0a7df0f2860278`
4. `microsoft/skills` @ `903dc62b1e4c833235b54db918a9a51cb6d3cc8f`
5. `obra/superpowers` @ `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`
6. `Leonxlnx/taste-skill` @ `ccbc15639c97057cbfcf32ecebc38ef716e4bb37`
7. `lllllllama/RigorPilot-Skills` @ `bd91195ad73199b95e24532b581ff12c07dcce09`
8. `pbakaus/impeccable` @ `cb56ed6c19a07329a9fa0cd4e657bee040156593`

Audit records live under `skills/skill-acquisition/references/`.

## Interface Design

`skills/interface-design/` is now active and independently routable for user-facing software surfaces.

Core rules:
- inspect incumbent visual/product truth before redesigning;
- infer surface mode and design direction from brief, audience, task, references, brand, and constraints;
- let explicit brief/product/platform/accessibility requirements outrank generic taste;
- distinguish refinement from redesign;
- use actual design systems honestly and avoid template autopilot;
- verify rendered results when practical, in bounded passes rather than open-ended self-polish;
- persist durable design direction in the owning project when worthy.

Primary adaptation sources are `Leonxlnx/taste-skill` (MIT) and `pbakaus/impeccable` (Apache-2.0). DEDAL did not import their runtime-specific packages.

## Decision / Research Refinements

Decision Design now sizes substantial work as spike, bounded, or architectural. Hidden complexity can upgrade the path, but routine reversible work does not inherit a universal approval ceremony.

Research now separates exploratory evidence from trusted/established evidence. For experiment/comparison campaigns, preserve comparison anchors and do not turn exploratory gains into novelty/SOTA/trusted-reproduction claims without the required evidence.

## Verification

`repo-integrity.yml` validates foundational/kernel files, registries, all active skill entrypoints, imported/adapted provenance, Software Development references, Skill Acquisition audits, Interface Design provenance/reference structure, and semantic version format.

Fresh-chat bootstrap E2E remains **PASS** (`evals/boot/minimal-bootstrap-v1.md`). Re-run after boot/kernel/router/layout changes.

## Next Phase

1. Evaluate Interface Design on real project/UI tasks against baseline behavior and capture Creator feedback.
2. Continue gap-driven high-signal scans rather than leaderboard harvesting for its own sake.
3. Likely next candidate areas: durable writing/editorial workflow, visual/image-generation direction, project bootstrap/context adapters, and specialized security/release engineering — only if repeated work justifies them.
4. Keep improving existing skills when new sources mostly refine methodology rather than creating independent routing domains.
5. Keep private/personal/project operational state outside the public core.

Do not expand the Stable Kernel merely to capture ecosystem fashions or project-specific rules.
