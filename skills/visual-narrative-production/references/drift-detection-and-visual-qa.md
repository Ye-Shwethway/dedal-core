# Drift Detection and Visual QA

## Drift taxonomy
Classify visible failures rather than saying only "looks wrong":
- identity/facial drift;
- physique/proportion/height drift;
- age/grooming drift;
- expression/performance drift;
- anatomy/joint/limb-count defect;
- pose/action mismatch;
- object-contact/load/physics defect;
- wardrobe/prop drift;
- composition/camera/axis drift;
- environment/spatial continuity drift;
- lighting/time/weather drift;
- style/medium/grade drift;
- text/logo/detail corruption;
- narrative mismatch;
- edit spillover / unrelated accepted content changed;
- missing visual-reference binding / text-only identity fallback;
- scene-geometry contradiction (movement/facing/gaze vs destination);
- environment-to-composition leakage (place anchor incorrectly freezing camera/background).

## Visual QA pass
1. inspect the rendered image itself;
2. verify required pixel references were actually bound to the generation call, then compare each material dimension with its authoritative reference/ledger state;
3. check identity and physique before aesthetic polish;
4. check shot purpose, composition, action, and performance;
5. check anatomy, joints, hands/feet, contact, load, and object relationships;
6. check environment, screen direction, lighting/time, wardrobe/props, and sequence continuity;
7. check text/details and obvious artifacts;
8. decide: accept, accept-with-note, targeted revise, or reject/regenerate.

## Bounded revision
Use the narrowest correction that solves the observed defect while preserving accepted dimensions. Repeated cross-regressions are a sign to improve reference/control strategy or simplify the shot spec, not to append endless prompt clauses.

## Metrics
Similarity/reward/perceptual metrics may triage batches but do not overrule obvious visual mismatch, story intent, anatomy defects, or Creator acceptance.

## Acceptance record
Store accepted output ID/path, role(s), new durable visual truth, tolerated deviation, and supersession relationship when relevant.


## Cross-shot sequence QA
Rendered correctness is not enough when adjacent frames are redundant. Every 2–3 accepted shots, compare the sequence for repeated stance/silhouette, camera sameness, attacker/blocking repetition, unexplained prop or weapon appearance, pacing compression, injury/damage continuity, and whether each shot adds distinct narrative information.

If the Creator reports a repeated visual pattern, treat it as a sequence-level defect and inspect prior accepted shots for the same class before generating the next shot.

Do not make the Creator repeatedly discover defects DEDAL can inspect directly. Route durable recurring lessons through Self-Improvement.
