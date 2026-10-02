# Mini-Arc Continuity and Instructor Control

## Why this mode exists
As image generators become more capable, sequence quality increasingly depends on orchestration: selecting the right anchors, preserving accepted local state, choosing physically natural phase changes, and avoiding unnecessary prompt or camera drift. A stronger engine does not remove the need for an intelligent instructor; it makes poor instruction more visible because the model can faithfully render the wrong staging.

## Local continuity envelope
A mini-arc is 3–4 separate full-frame stills that depict one tightly coupled action or transition. Define one shared envelope:
- accepted start frame / immediate handoff anchor;
- identity, physique, grooming;
- wardrobe and body state such as sweat, dirt, damage, fatigue;
- place/geography and material landmarks;
- lighting/time/grade;
- equipment/prop state;
- coherent camera family.

The envelope is more authoritative than generic re-description during that mini-arc.

## Micro-delta planning
Each still should change one readable action phase. Examples:
- reach -> grasp/load -> active phase -> release;
- setup -> start position -> peak effort -> controlled return;
- stand -> sit/setup -> rack/load -> press.

Do not compress multiple phases into one frame or create a large unmotivated jump merely for visual novelty.

## Instructor-control priority
Prefer natural action logic over cosmetic identity exposure. Do not force head turns, downward gaze, or awkward posture to avoid a frontal view. Facing the camera is not intrinsically wrong. The question is whether head, gaze, spine, support, and load path fit the depicted action.

Treat equipment proportions as part of the scene model. A bench, seat, pad, rack, or handle that changes scale can make a technically plausible body pose feel false.

## Retry discipline
When one slot fails:
1. keep accepted references and local continuity envelope unchanged;
2. identify the failure class;
3. alter only the failing action relation, crop, equipment geometry, or camera detail;
4. regenerate the failed slot;
5. re-audit adjacency.

Do not broadly rewrite the prompt after a local failure. Broad retries can erase the exact consistency the sequence already proved.

## Output semantics
"Generate four successive shots" means four separate full-frame review assets unless the user explicitly requests a collage/contact sheet/storyboard. Multi-output generation is useful when it preserves a common action envelope; it must not be rendered as one multi-panel image by accident.


## Physical-state handoff
A local mini-arc handoff includes more than character pose. Carry forward persistent-object count, morphology, and spatial placement. If a frame establishes two objects at distinct positions, the next frame inherits those positions unless its planned micro-delta explicitly moves them.

Movement expertise is also part of the local envelope. Preserve the established performer's form quality across phases; do not trade correct stance or joint organization for a more dramatic silhouette.
