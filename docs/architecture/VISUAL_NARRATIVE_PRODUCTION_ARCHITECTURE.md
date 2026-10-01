# Visual Narrative Production Architecture

_Date: 2026-09-30_

## Purpose

Visual Narrative Production is DEDAL's still-image / visual-novel production owner. It converts accepted narrative truth into coherent individual shots and image sequences while preserving character, environment, spatial, performance, and visual state across generations and edits.

## Boundary model

- **Story Weaver** owns fiction canon, scene function, beat causality, dialogue, character knowledge/motivation, and emotional story state.
- **Visual Narrative Production** owns beat selection for visualization, shot design, reference authority, scene continuity, cinematography, performance direction, pose/anatomy/contact, image prompt compilation, generation/edit QA, and accepted visual anchors.
- **Video Production** owns temporal motion, take selection, editing, audio, subtitles, effects, and delivery.
- **Writing / Editorial** owns expression/translation/polish when the main deliverable is prose rather than story canon.
- **Research/domain owners** own factual truth.

The execution model (OpenAI image generation, future ComfyUI/control stacks, or other providers) is an execution surface, not the faculty.

## State model

### Canonical reference authority
Authority is assigned by dimension: identity, physique, grooming, expression, pose/geometry, wardrobe/prop, environment, composition/camera, style/lighting.

### Shot Spec
A provider-agnostic structured description of purpose, subjects, state, action/blocking, performance, environment, camera, lighting, reference roles, preserve/change constraints, continuity delta, and acceptance checks.

### Visual Continuity Ledger
Scene/sequence state for recurring characters, props, environment, time/weather, lighting, spatial positions, camera axis/screen direction, emotion/performance, damage/dirt/wetness, and accepted anchors.

Within one scene, successive shots normally apply state deltas. A location/time transition opens a new environment state and carries forward only the character/prop state that should persist.

## Production pipeline

`canon/scene truth -> visual beat selection -> reference resolution -> continuity state -> shot spec -> prompt/edit compilation -> render -> rendered QA -> targeted correction -> acceptance -> role-specific anchor promotion`

For ordinary sequences, run this as a compact scene card and four checkpoints: preflight of references/geography/interaction, one-image render, pixel-based review against the shot and neighboring frames, then individual verified delivery. Expand the shot spec only on material risks. An image input can condition appearance without enforcing exact pose or composition; inspect the current tool's actual control surface before promising geometry fidelity. After a repeated structural failure, change phase, crop, reference role, or supported control rather than repeating equivalent prose.

## Prompt compiler

Prompts are execution artifacts, not continuity storage. Compile only the detail needed by the active provider and current defect:
- purpose/deliverable;
- subject/current state;
- action/blocking/performance;
- environment/spatial relation;
- camera/framing;
- lighting/style;
- reference roles;
- preserve/change constraints;
- failure-specific exclusions.

Semantic neutralization uses precise benign production/anatomical language where ambiguity could cause false positives. It never obfuscates disallowed content or attempts to bypass safety policy.

## QA gates

Before acceptance, inspect the render itself for:
- identity/physique/grooming/performance consistency;
- narrative purpose/readability;
- limb count, joints, hands/feet, balance and pose;
- object contact/intersection, grip/load and force direction;
- wardrobe/prop correctness;
- composition/camera/axis/screen direction;
- environment/light/time/weather continuity;
- style/text/detail artifacts;
- unintended edit spillover.

Private character/project fixtures remain outside public Core. Only generalized defects and workflow rules may be promoted.

Static contract validation proves instruction presence. `evals/visual-narrative-production/outcome-evaluation-v1.md` defines independent old/new skill comparisons on diverse scene types, with rendered outputs, first-pass usable rate, escaped defects, rework, sequence coverage, and delivery integrity. No lower-model or cross-scene performance claim follows from one accepted sequence or a passing contract validator.
