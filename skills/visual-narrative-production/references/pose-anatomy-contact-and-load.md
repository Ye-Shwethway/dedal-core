# Pose, Anatomy, Contact, and Load

## Action-shot contract
When body mechanics matter, specify:
- stance/base of support;
- center of mass / weight distribution;
- joint positions and intended range of motion;
- limb count and visibility;
- force direction;
- contact surfaces;
- grip type and hand orientation;
- object mass/load implication;
- fabric/prop response;
- intended silhouette/readability.

## Equipment interaction preflight
For a person gripping, hanging from, pushing, or pulling equipment, draw a minimal relationship map before generation: fixed support -> contact point(s) -> wrist/forearm -> elbow -> shoulder -> torso/load. Record the action phase (start, middle, finish), joint bend in qualitative terms, and where the head/torso lies relative to the support. Treat visible geometry as a *relationship*, not an isolated list of body parts. Do not assume that a realistic face/texture proves a feasible pose.

Choose a camera/crop that reveals enough of the chain to inspect the difficult relation. If hands are offscreen, the remaining shoulder/elbow/support spacing must still explain how the action is possible; otherwise reveal part of the grip or widen the frame. Keep the contact point on the usable part of the equipment and inside the intended crop when the grip itself is under review. Mark a bar crossing the head/face or an implausible nearly straight-arm near-finish pose as a material failure, even if the rest of the image is attractive.

When text-only attempts repeatedly miss the same relationship and the tool supports an appropriate structural input, add a simple pose/layout guide as a *geometry-only* reference while retaining canonical identity pixels separately. If no geometry control is available, use clearer framing, render small alternatives with distinct action phases/crops, and inspect them; do not claim deterministic control or exact biomechanical fidelity.

## QA checklist
Inspect the render for:
- exactly plausible limb count;
- correct joint topology and range;
- no fused/duplicated hands, feet, fingers, or legs;
- plausible wrist/forearm orientation;
- feet or support surfaces that actually bear the depicted load;
- hands contacting rather than passing through solid objects;
- grip location appropriate to the task;
- rope/tool/weapon direction consistent with force;
- muscle tension consistent with action, not arbitrary bodybuilding flex;
- occlusion that makes spatial sense;
- no impossible object intersections.

## Reference use
Use pose/anatomy reference images for geometry and mechanics only unless they are also authoritative for identity/physique. A pose reference must not overwrite the canonical character.

## Correction strategy
If the image is otherwise accepted, correct the smallest defective region/relationship. If repeated local edits destabilize identity or geometry, return to a clearer pose/geometry spec rather than stacking more adjectives.
