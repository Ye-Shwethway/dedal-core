---
name: visual-narrative-production
description: Plan, generate, inspect, and deliver coherent successive scene shots or visual-novel stills. Use for recurring-character image sequences, scene coverage, action/contact realism, reference consistency, camera and environment continuity, visual QA, variation sets, and accepted visual anchors.
---

# Visual Narrative Production

Use this skill when still-image work must do more than make a plausible picture: it must express a story beat, preserve recurring characters and places, choose a purposeful shot, maintain continuity across successive images, and survive visual QA before becoming accepted project state.

`visual-direction` is a backward-compatible routing alias for this skill, not a separate faculty.

## Ownership boundary

This skill owns **narrative-to-visual production**: beat visualization, shot selection/design, character/reference control, performance direction, pose/anatomy/contact reasoning, environment and spatial continuity, cinematography, lighting, prompt compilation, rendered-output QA, and accepted visual-anchor promotion.

It does **not** own prose-story canon or dialogue architecture (`story-weaver`), temporal video assembly/motion editing (`video-production`), factual research (`research`/domain owner), general copy editing (`writing-editorial`), or the execution surface of a specific image model.

## Core lifecycle

`receive story/scene truth -> identify visual beat -> load authoritative anchors -> build scene state -> design shot -> compile provider-appropriate prompt/edit contract -> generate/edit -> inspect rendered output -> classify defects -> revise narrowly -> Creator/project acceptance -> persist durable visual state`

## Default production path

Use one compact scene card for ordinary sequences; expand only the risky dimensions. Before the first render, record: (a) scene state and accepted references, (b) one line per planned shot with its new story information, action phase/performance, camera/crop, and state delta, and (c) delivery format/location. The next shot must start from the prior shot's plausible end state. Do not write a long prompt as a substitute for this map.

For each shot, follow four gates:
1. **Preflight:** bind the minimal authoritative pixel references; identify which image controls identity, geometry, place, and style. Check camera/scene geography and any physical interaction that could become impossible in a crop. Inspect the execution tool's actual reference/edit/structural-control capabilities; image references alone do not guarantee pose or layout control.
2. **Render:** compile only the current shot and its material constraints. Generate one full image per call. If exploring alternatives, vary a named phase, camera, or composition dimension while preserving accepted state.
3. **Review:** inspect the returned pixels and compare them with the shot card and adjacent accepted shots. Reject a material identity, continuity, anatomy/contact, or role failure before presenting a candidate. A failed structural relation calls for a changed phase/crop/guide strategy, not repeated adjective accumulation.
4. **Deliver:** provide the requested individual review assets with verified links/count. Record accepted alternatives and known debt; promote an image only for the roles the Creator accepts.

Read `references/tool-capability-and-failure-routing.md` when generation repeatedly misses geometry, identity, or edit locality. Read `references/self-review-and-sequence-audit.md` for multi-shot or variation-set review. Use the Core evaluation at `../../evals/visual-narrative-production/outcome-evaluation-v1.md` when changing this skill or claiming a performance gain.

## Required workflow

1. **Start from story truth, not prompt improvisation.** Identify the scene, beat, character state, and visual purpose before choosing a camera or writing generation language.
2. **Establish reference authority by dimension.** Identity, physique/proportions, grooming, wardrobe, expression/performance, pose/geometry, environment, composition, and style may have different anchors.
3. **Bind recurring-character anchors as actual image inputs.** When authoritative visual references exist and identity/physique/grooming consistency matters, the execution call must receive pixel-bearing reference images for those roles. Merely searching, reading, viewing, or summarizing a Library image does not bind it to the image model. Bridge/materialize Library references into the execution surface when necessary. Text description may supplement a visual anchor but must not silently replace it. If the execution surface cannot accept the required visual references, state that limitation and do not claim an identity lock.
4. **Lock only durable invariants.** Separate `must preserve` from `may vary`; do not freeze incidental pixels or over-constrain exploration. An environment anchor owns place identity and stable geography, not a universal background framing.
5. **Preflight scene geometry before camera design.** For movement/action shots, establish subject start position, destination/action target, movement vector, screen direction, gaze target, and what should be visible, partial, or offscreen from the chosen viewpoint. Same location does not imply the same background composition.
6. **Maintain a Visual Continuity Ledger for sequences.** Track character, wardrobe, prop, environment, lighting/time, damage/dirt/wetness, spatial position, camera axis/screen direction, emotion, and accepted anchors. Same-scene shots normally apply state deltas rather than reinventing the scene.
7. **Choose the shot for narrative function.** Establishing, interaction, reaction, reveal, action, emotional pivot, insert/detail, aftermath, or transition are different jobs. Do not default every beat to a centered portrait.
8. **Treat camera and lighting as consequences of intent.** Shot size, angle, lens feel, camera height/distance, eye line, negative space, depth of field, motivated light, contrast, atmosphere, and palette must serve readability and story state.
9. **Direct performance, not only facial labels.** Expression, gaze, head angle, posture, breath/tension, hand behavior, interpersonal distance, and body weight should agree with the emotional beat and current action target. Do not inherit a look-away pose from an identity reference when the action logically requires looking at/along the task target.
10. **Model pose, contact, load, and anatomy explicitly when they matter.** Check limb count, joints, weight bearing, balance, grip, prop contact, occlusion, fabric response, and plausible force paths. Dynamic/action shots require stronger anatomy/contact QA than neutral portraits.
    For a body interacting with equipment, set the action phase and a visible contact chain before composing the crop. Keep enough landmarks in frame to judge the load path; if a tight crop hides essential evidence, widen or reframe it. A prompt alone is not a geometry guarantee.
11. **Compile prompts; do not merely accumulate adjectives.** Convert the structured shot spec into concise provider-appropriate language: purpose, subject/state, action/blocking, environment, camera, lighting/style, reference roles, preserve/change constraints, and exclusions only when material.
12. **Neutralize ambiguity without changing legitimate scene meaning.** Use precise production/anatomical language for benign scenes and avoid needless sensational wording. This is semantic clarification, not policy evasion; never disguise prohibited content.
13. **Prefer edit-first correction when the accepted image is mostly right.** For a local defect, preserve accepted identity/geometry/composition/lighting unless the requested fix requires broader regeneration.
14. **Rendered inspection is mandatory.** Prompt/source review is not evidence that identity, anatomy, contact, text, scene continuity, or visual intent succeeded.
15. **Self-review before offloading QA to the Creator.** After each render, classify the shot as pass, usable-with-debt, or fail; detect shot-role mismatch, repetition, invented state, missing/incorrect reference binding, implausible gaze/action relation, and obvious continuity defects before asking for feedback. For sequences, run a cross-shot audit every 2–3 accepted shots and immediately after a repeated-pattern correction.
    Apply the same inspection to every comparison candidate; exclude a material failure from a choice set instead of calling it a variation. Present inspectable individual files/links in the requested destination, and verify access and count before asking for a choice.
16. **Propagate Creator feedback across the sequence.** When the Creator identifies a defect class, scan recent shots for the same failure, update future shot constraints, and avoid requiring the same correction again.
17. **Classify drift before revising.** Separate identity, physique/proportion, age/grooming, performance, anatomy/joints, pose/action, object contact/physics, wardrobe/prop, composition/camera, spatial continuity, environment, lighting/time, style/grade, text/detail, and edit-spillover failures.
18. **Promote anchors deliberately.** Only accepted outputs may become identity, physique, expression, wardrobe, environment, pose, composition, or scene-continuity anchors. Rejected experiments never redefine canon.
19. **Persist durable truth, not prompt debris.** Save approved anchors, trait/state contracts, continuity ledgers, and generalizable lessons; do not store every failed generation as project truth.

## Visual-novel / sequential still mode

For a scene with multiple images:
- break narrative prose into visual beats before generating;
- select shots for coverage and emotional/spatial clarity rather than illustrating every sentence;
- establish scene geography before close coverage when spatial understanding matters;
- preserve camera axis, screen direction, eye lines, relative positions, wardrobe/prop state, and motivated lighting unless a deliberate transition changes them;
- carry character state across location changes while opening a new environment state;
- allow composition diversity without sacrificing subject identity or scene truth;
- use the previous accepted shot as a continuity anchor when it contains useful state that must survive.

## Production modes

- **Reference / anchor production** — canonical face, physique, wardrobe, expression, pose, object, or environment references.
- **Narrative single shot** — one image selected to express a specific story beat.
- **Sequential scene** — successive stills in one location/time block with continuity ledger and delta updates.
- **Scene transition** — new location/time or material state change; carry only the state that should persist.
- **Action / biomechanics** — body mechanics, force, contact, balance, anatomy, and readable silhouette dominate QA.
- **Edit-first** — accepted base image is authoritative and only bounded elements should change.
- **Exploration** — deliberately vary one or more dimensions, but keep experiments non-canonical until accepted.

## Progressive references

Load only what the task needs:
- `references/reference-hierarchy-and-canonical-locks.md`
- `references/narrative-to-shot-planning.md`
- `references/visual-continuity-ledger.md`
- `references/performance-expression-and-emotion.md`
- `references/pose-anatomy-contact-and-load.md`
- `references/tool-capability-and-failure-routing.md`
- `references/cinematography-and-screen-direction.md`
- `references/lighting-atmosphere-and-environment.md`
- `references/prompt-compilation-and-neutralization.md`
- `references/drift-detection-and-visual-qa.md`
- `references/self-review-and-sequence-audit.md`
- `references/generation-edit-and-anchor-promotion.md`
- `schemas/shot-spec.schema.json`
- `schemas/visual-continuity-ledger.schema.json`

## Pairing

Pair with `story-weaver` when prose/canon/scene beats must be authored or interpreted, `video-production` when shots become temporal media, `research` when factual visual truth matters, `files`/`knowledge-memory` when approved anchors or state must persist, and `quality-engineering` when independent readiness verification is required.

Do not infer a real person's physical traits from memory when an authoritative current reference is required. Do not claim consistency, anatomical correctness, or continuity without inspecting the rendered output.
