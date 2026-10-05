# Self-Review and Sequence Audit

## Purpose
Reduce Creator correction burden by making Visual Narrative Production inspect its own outputs and sequence behavior before asking the Creator to act as the primary QA loop.

## Local post-render self-review

For interaction sequences and motion sources, use `source-production-design.md` to compare intended versus observed state. Name the visible landmark/relation supporting each material judgment, and use `not_observable` when required evidence is hidden. Do not infer a successful grip/contact from a caption or overlap alone. Missing required evidence needs reframing or another anchor; it cannot be recorded as a pass. In source-only work, rendered still QA never proves motion QA or external acknowledgement.
Before generation, fail the shot preflight if a required recurring-character pixel reference has not actually been bound to the execution surface. After every generated or edited shot, inspect the rendered image before presenting or promoting it. In addition to ordinary visual QA, ask:
- were all required identity/physique/grooming pixel references actually bound to the generation call, rather than merely read or described?
- did this image actually fulfill the planned shot role and beat, or only produce a generally attractive frame?
- did the camera, body silhouette, gesture, or action pattern repeat the previous accepted shot without narrative reason?
- did the generation invent a prop, weapon, injury, wardrobe change, environmental element, or spatial relationship that the ledger did not authorize?
- does the subject movement/facing direction agree with the scene-geometry preflight and destination?
- is gaze/head orientation plausible for the current action target, rather than being forced to expose identity?
- did an environment anchor accidentally freeze camera/background framing and contradict the intended shot angle?
- did damage/injury/time progression advance too far or too little relative to the planned beat?
- did a stronger aesthetic frame accidentally compress two planned beats into one and weaken later coverage?
- is there an objectively detectable defect that DEDAL should correct itself instead of asking the Creator to notice it?
- for equipment interaction, can the visible contact chain, joint bend, head/support separation, and load path be traced without inventing hidden anatomy?
- for exercise/skilled movement, is head-neck posture natural for the phase, or was it awkwardly bowed/turned only to avoid a camera-facing face?
- is equipment scale and support geometry believable relative to the subject and adjacent accepted frames?
- do the body/action axis, support-equipment axis, contact map, and camera projection describe one coherent 3D setup rather than individually plausible pieces that conflict?

Classify the shot as:
- `pass` — fulfills role and continuity cleanly;
- `usable_with_debt` — usable, but carries a known non-blocking issue that must be prevented or repaired later;
- `fail` — misses the shot role, breaks material continuity, repeats prior coverage without purpose, or contains a material visual defect.

Do not silently promote a `fail` shot. A Creator saying only “proceed” does not erase an objectively detectable material failure; record the defect and either repair it or carry explicit debt when the image is still useful.

Before presenting a comparison set, run this gate on each candidate and compare each candidate with the accepted sequence. Keep meaningful differences in beat phase, camera distance, crop, or body action. Replace failed candidates before delivering the requested set; label known non-blocking debt plainly. If the Creator requests a Drive or other review location, verify the individual files and links there. A generated output existing only in an inaccessible preview is not a reviewable deliverable.


## Successive mini-arc audit
For a tightly coupled 3–4 image mini-arc, audit the group as one local continuity envelope in addition to per-image QA. Verify:
- every output is an individual full-frame image, not a collage/contact sheet/split-screen unless explicitly requested;
- identity, physique, grooming, wardrobe/body state, place, lighting, and equipment state stay within the accepted envelope;
- each image advances exactly one readable micro-delta rather than jumping phases or repeating the same pose;
- the camera stays within a coherent family unless a deliberate cut is part of the mini-arc;
- natural action biomechanics outrank artificial face-angle avoidance;
- the previous accepted image is used as an immediate handoff anchor when it contains useful local state;
- a local retry preserves all accepted envelope dimensions and changes only the failing relation.

If three frames are strong and one frame fails, regenerate the failed slot locally. Do not discard the successful envelope or broadly rewrite the sequence. A broad retry that changes character, place, lighting, styling, or equipment without need is itself a drift failure.

### Phase-signature admission gate
Before delivery, map each planned mini-arc slot to the **observed rendered action phase**, not merely to camera/framing differences. Use a compact signature such as `support/contact state + joint/load state + object position + body orientation + action direction`. Compare adjacent slots against the planned phase sequence.

Reject or narrowly regenerate a slot when:
- two adjacent outputs resolve to the same action phase while the plan called for different phases;
- a frame skips the intended intermediate phase and therefore compresses the arc;
- a camera/crop change creates visual variety but adds no new action or story information; or
- the observed phase cannot be distinguished from its neighbor without relying on framing alone.

A mini-arc passes admission only when every slot contributes a distinct, correctly ordered phase. This is a semantic action check, not an image-similarity score.


### Physical-state continuity gate
For adjacent shots containing persistent equipment or props, compare **count + morphology/topology + spatial relation + contact state**. Reject unexplained object teleportation (for example, items changing sides of a bench without an intervening move), fusion/splitting, duplicated or missing components, or topology changes that alter function. Camera movement alone is not an explanation for a changed object relation.

For skilled movement, compare the rendered stance and joint organization with the character's established proficiency. A trained performer should not acquire novice-like form merely because the pose is visually dramatic. Check base of support, stance width, foot orientation, knee/hip relation, torso control, head/neck alignment, grip, and load path. Allow deviations only when scene state explains them (fatigue, injury, instability, deliberate technique variation, etc.).

## Sequence audit cadence
For sequential stills, perform a sequence-level audit after every 2–3 new accepted shots, and immediately when the Creator reports a repeated pattern.

Compare the current sequence across:
- shot-role diversity and narrative coverage;
- camera distance, angle, height, axis, and subject placement;
- pose, silhouette, gesture, and action-mechanic repetition;
- character identity/physique continuity;
- wardrobe, prop, injury, dirt, blood, and damage progression;
- environment geography and background-state continuity;
- lighting/time/weather progression;
- emotional/performance progression;
- newly invented props, unexplained prop relocation, count/topology changes, or other unexplained state changes;
- whether each shot adds new story information;
- whether movement quality remains consistent with established skill/proficiency and current fatigue/injury state.

## Repetition detector
Repetition is a quality defect when two or more adjacent shots reuse substantially the same:
- stance or limb geometry;
- subject placement and camera relation;
- dominant action line;
- attacker arrangement/blocking;
- camera distance/angle;
- facial/performance beat;
while claiming to serve different narrative jobs.

When detected, do not merely add adjectives. Change the visual logic at the shot-spec level: choose a different beat moment, camera relation, body mechanic, blocking arrangement, or shot role while preserving continuity.

## Feedback propagation
When the Creator identifies a defect class:
1. inspect the current shot for that issue;
2. scan the recent sequence for the same pattern;
3. update the active shot constraints/continuity debt;
4. prevent recurrence in subsequent generation;
5. if durable and reusable, route the lesson through Self-Improvement for promotion into the owning workflow or eval.

The Creator should not need to restate the same correction shot after shot.

## Burden-minimization rule
Ask the Creator for creative judgment when multiple valid directions exist. Do not ask the Creator to perform routine defect detection that DEDAL can inspect itself: anatomy errors, continuity drift, unexplained prop changes, repetitive coverage, obvious shot-role mismatch, or visible identity/physique drift.

## Scene-block closure
At the end of a scene block, produce a compact internal closure record:
- accepted shots and roles;
- known tolerated deviations;
- unresolved continuity/quality debt;
- new anchors promoted;
- recurring failure classes observed;
- workflow changes justified by evidence.

Use Self-Improvement maturity levels for durable lessons rather than immediately globalizing every observation.

## Support-axis admission gate
When a support apparatus constrains the action, compare the rendered body/action axis with the support longitudinal axis and the planned contact map before promotion. A side-profile subject with a visibly skewed bench/platform is not acceptable merely because the anatomy is correct. Camera perspective may change the 2D projection, but the inferred 3D relationship must remain plausible.

If biomechanics are correct but the apparatus orientation is wrong, repair the support/camera relation narrowly while preserving accepted identity, pose phase, lighting, and environment.
