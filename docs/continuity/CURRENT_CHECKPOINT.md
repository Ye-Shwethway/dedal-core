# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.15.0`
- Purpose: durable public operational core for DEDAL

## Active skills

Domain: `$msa`, `$pra`, `$ika`.

Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Interface Design, Agent Engineering, Security Engineering, Project Bootstrap, Release Engineering, Data Operations, Writing / Editorial Engineering, **Visual Direction / Image Production**, Automations, Skill Acquisition.

## Capability expansion roadmap

Roadmap: `docs/evolution/CAPABILITY_EXPANSION_ROADMAP.md`.

Status:
1. Security Engineering — active;
2. Project Bootstrap / Context Adapter — active;
3. Release / Deployment Engineering — active;
4. Data / Spreadsheet / Operational Workflow Engineering — active;
5. Writing / Editorial Engineering — active;
6. **Visual Direction / Image Production — active;**
7. Decision / Planning Intelligence v2 — planned next;
8. Knowledge / Memory Architecture — planned.

## Visual Direction v1

Audit: `skills/skill-acquisition/references/visual-direction-capability-audit-2026-09-14.md`.
Eval: `evals/visual-direction/contract-v1.md`.

Core lifecycle:
`purpose -> reference hierarchy -> canonical locks -> shot/set plan -> generate/edit -> visual inspection -> drift classification -> narrow revision -> accept/reject -> persist durable visual truth`

Key boundaries:
- reference authority is assigned by dimension rather than treating all reference images as equal;
- identity, body/shape, grooming, wardrobe/props, composition, style, and environment are distinct controls;
- canonical invariants are separated from allowed variation;
- local defects prefer targeted edits when supported;
- actual rendered output must be inspected before visual acceptance claims;
- drift is classified rather than answered only with longer prompts;
- rejected/experimental outputs do not silently redefine canonical identity/style;
- automated image scores are advisory and do not override human/Creator acceptance.

Primary corpus:
- current OpenAI Academy image-generation guidance;
- current Google AI image-generation/reference guidance;
- DreamBooth, CVPR 2023 / arXiv:2208.12242;
- `tencent-ailab/IP-Adapter` @ `62e4af9d0c1ac7d5f8dd386a0ccf2211346af1a2`, Apache-2.0.

No third-party image model, adapter, package, or script was installed or run for this adaptation.

## Harness benchmark

Harness v1 remains contract-validated with accumulating outcome evidence.

Current compact evidence:
- GH-01: prior clean rerun PASS, but **new regression observed during v0.15 authoring**: two direct contents writes were mistakenly invoked during an intended atomic work unit. The temporary files are removed by the final reconciliation tree without force/history rewrite. Treat this as renewed evidence that documentation-only tool allowlists do not enforce runtime selection.
- GH-02: PASS;
- RS-01: PARTIAL;
- RS-02: PASS;
- LH-01 / LH-02: await representative continuity/recovery work.

Do not hide the GH-01 regression or call the full harness outcome-validated.

## Next executable phase

1. Exercise Visual Direction naturally on real image-generation/editing work and capture identity/continuity regressions when meaningful.
2. Harden Agent Engineering/GitHub mutation tooling when a true runtime-enforceable tool allowlist becomes available; do not pretend prose rules provide enforcement.
3. Continue capability roadmap with **Decision / Planning Intelligence v2**.
4. Then evaluate Knowledge / Memory Architecture, merging rather than multiplying skills where independence is weak.
5. Re-exercise RS-01 and LH cases only on representative real work.