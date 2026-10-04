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


## Natural technique priors
For exercise, sport, labor, or other skilled physical actions, do not optimize identity visibility at the expense of ordinary technique. Unless the movement specifically calls for another posture:
- keep the trunk and support base stable for the depicted load;
- keep head and neck neutral or aligned with the movement rather than artificially bowed, twisted, or turned away;
- let gaze follow the task or a natural forward line; facing or nearly facing the camera is acceptable when that is the natural action axis;
- preserve plausible shoulder, elbow, wrist, hip, knee, and foot relations through the phase transition.

A deliberately lowered or averted head used only to avoid a camera-facing face is a performance/biomechanics defect when it makes the action look awkward.

## Equipment geometry and scale
Treat exercise benches, racks, handles, seats, pads, cables, weights, and other load-bearing equipment as geometry, not decoration. Check:
- believable width, length, thickness, and support structure;
- subject-to-equipment scale;
- seat/back-pad proportions and separation where applicable;
- contact surfaces that could physically carry the shown load;
- no unexplained widening, stretching, fused pads, or impossible support members across adjacent shots.

When an equipment shape is slightly imperfect but does not break the action, classify it as non-blocking debt; when it changes support/contact mechanics, treat it as material failure.


## Proficiency-conditioned form
When the subject's experience level is established, use it as a movement-quality constraint. A highly trained performer should normally show efficient, repeatable, balanced mechanics rather than arbitrary stance width or unstable joint organization. For loaded seated/standing exercise, check foot placement, base-of-support symmetry, knee/hip tracking, torso control, and whether the stance is plausibly chosen for the movement. Treat unexplained novice-like form as a realism defect even if the anatomy is otherwise possible.

## Persistent equipment identity
Across adjacent shots, equipment has state: count, topology, placement, and contact. Two separate dumbbells remain two separate dumbbells; they must not fuse into a multi-headed object, duplicate, vanish, or relocate without a visible/justified transition. Preserve left/right/near/far relations when those relations are established and materially visible.

## Body-support-camera alignment
Local joint correctness is insufficient when the support apparatus is geometrically misaligned with the performer. For bench-, platform-, rail-, table-, or machine-supported actions, preflight the body/action axis, support longitudinal axis, required axis relation, contact map, and camera projection together. The camera may create perspective convergence, but it must not imply an impossible yaw/rotation of the support relative to the body.

Use camera placement to obtain a natural side/profile view. Do not rotate the head, torso, support limb, or equipment merely to improve face visibility. For unilateral supported pulling patterns, preserve neutral cervical alignment, task-aligned gaze, stable hand/knee/foot support, and a load path close to the torso while the bench/support remains physically aligned with the body.
