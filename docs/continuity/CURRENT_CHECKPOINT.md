# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.9.0`
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
9. `nextlevelbuilder/ui-ux-pro-max-skill` @ `7f69fed6a2717900085f1bc3b263721f8ba025e2`

Audit records live under `skills/skill-acquisition/references/`.

## Interface Design v0.9 Refinement

Interface Design now combines two layers:

1. **reasoning/workflow layer** — brief inference, surface mode, incumbent truth, refinement-vs-redesign, quality floor, bounded visual verification;
2. **design-intelligence layer** — scoped knowledge retrieval, semantic-domain vs stack separation, explicit match/fallback semantics, freshness checks, and durable design-system persistence.

The UI/UX Pro Max deep audit contributed the second layer. DEDAL did **not** vendor the upstream catalog, install its CLI, inherit provider-specific paths, or treat upstream rankings/current stack versions as permanent truth.

Design-intelligence authority order:
- Creator + accepted project decisions;
- incumbent project design truth;
- authoritative current platform/design-system/accessibility sources;
- curated catalogs with provenance/freshness;
- generic heuristics.

Durable project design state may use a `MASTER + surface overrides` pattern. Existing master state must be read before regeneration and must not be silently overwritten.

## Decision / Research Refinements

Decision Design sizes substantial work as spike, bounded, or architectural. Hidden complexity can upgrade the path, but routine reversible work does not inherit a universal approval ceremony.

Research separates exploratory evidence from trusted/established evidence. For experiment/comparison campaigns, preserve comparison anchors and do not turn exploratory gains into novelty/SOTA/trusted-reproduction claims without the required evidence.

## Verification

`repo-integrity.yml` validates foundational/kernel files, registries, all active skill entrypoints, imported/adapted provenance, Software Development references, Skill Acquisition audits, Interface Design provenance/reference structure including the UI/UX Pro Max audit, and semantic version format.

Fresh-chat bootstrap E2E remains **PASS** (`evals/boot/minimal-bootstrap-v1.md`). Re-run after boot/kernel/router/layout changes.

## Next Phase

1. Use Interface Design on real project UI work and compare whether scoped retrieval/persistence improves outcomes without adding ceremony.
2. Continue gap-driven scans; likely candidate areas remain durable writing/editorial workflow, visual/image-generation direction, project bootstrap/context adapters, and specialized security/release engineering.
3. Prefer refinement of proven skills over multiplying top-level skills when new sources mostly improve an existing domain.
4. For large knowledge catalogs, prefer adapters/retrieval contracts plus freshness metadata over copying fast-drifting datasets into Core.
5. Keep private/personal/project operational state outside the public core.

Do not expand the Stable Kernel merely to capture ecosystem fashions or project-specific rules.
