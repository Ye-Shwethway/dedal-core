# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.6.0`
- Purpose: durable public operational core for DEDAL

## Active Skills

Domain: `$msa`, `$pra`, `$ika`.
Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Automations, Skill Acquisition.

## Matt Pocock Deep Audit

DEDAL performed a structured audit of `mattpocock/skills` at pinned source commit/tree `3cca18b368ae95cdbdebbff572ccafa662551015` under the MIT license. Evidence and classifications live at `skills/skill-acquisition/references/matt-pocock-deep-audit-2026-09-14.md`.

Key conclusion: the strongest transferable value is methodology and composition, not verbatim prompt text.

Promoted adaptations:
- `decision-design` from the dependency-aware grilling/frontier idea;
- Software Development references for debugging, testing/seams, two-axis review, architecture/domain design, and multi-session delivery.

Deliberately not inherited:
- provider-specific Skill/Claude plugin syntax;
- mandatory native subagents/parallelism;
- issue-tracker assumptions;
- ceremony for trivial changes;
- popularity as trust.

## Software Development Routing

Load specialized references only when needed:
- hard bug/regression/perf -> `debugging-loop.md`;
- tests/TDD/seam choice -> `testing-and-seams.md`;
- code review -> `review-two-axis.md`;
- architecture/domain/interface work -> `architecture-and-domain.md`;
- work spanning contexts -> `multi-session-delivery.md`.

## Decision Design

Use `skills/decision-design/` for deliberate stress-testing of high-impact plans/architectures/product decisions. Resolve retrievable facts with tools; reserve owner-level choices for the Creator. Work outward through only the currently-unblocked decision frontier. Do not use it as routine questioning ceremony.

## Skill Acquisition Policy

`capability gap -> discover -> shortlist -> security/license/provenance audit -> extract patterns -> DEDAL adaptation -> evaluation -> promote/reject -> regression capture`

Key policy: **reuse ideas; do not inherit trust blindly.**

## Verification

`repo-integrity.yml` validates foundational/kernel files, registries, all active skill entrypoints, imported/adapted provenance, the Matt audit, Software Development reference set, and semantic version format.

Fresh-chat bootstrap E2E test remains **PASS** (`evals/boot/minimal-bootstrap-v1.md`). Re-run it after boot/kernel/router/layout changes.

## Next Phase

1. Continue high-signal corpus scans rather than broad catalog scraping: first-party/vendor collections and respected public skill authors.
2. For each corpus, keep a pinned audit with Adopt / Adapt / Merge / Reject decisions.
3. Prefer improving existing DEDAL skills over multiplying top-level skills.
4. Create a new top-level skill only when the workflow is genuinely cross-domain or independently routable.
5. Add evaluation fixtures when a future adaptation materially changes proven behavior.
6. Keep private/personal/project operational state outside the public core.

Do not expand the Stable Kernel merely to capture ecosystem fashions or project-specific rules.
