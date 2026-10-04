# Adaptive Keyframe Density and Transition Bridges

## Purpose

Treat accepted stills as temporal control points for generated motion, not merely as attractive storyboard images. The density of control points must increase as adjacent states become harder to interpolate.

A transition is **temporally sparse** when the next anchor changes too many independent dimensions at once (for example body position, body facing, prop possession, support/contact, camera yaw, framing scale, and environment relation). Sparse transitions often force the video model to invent missing motion, causing visible jumps, morphs, teleports, abrupt reframes, or "stitched stills" rather than continuous cinematic flow.

## Adaptive density rule

Do not use a fixed number of source images for every arc.

- Simple, monotonic exercise/action phases may be adequately described by a small mini-arc.
- Complex arc-to-arc transitions require more intermediate control states.
- The correct number is the smallest set that keeps every adjacent pair physically and cinematically reachable.

Before generation, compare every adjacent anchor pair and ask whether one short generated segment can plausibly connect them without inventing a major unseen event.

## Transition complexity dimensions

Increase keyframe density when one or more of these change materially:

- subject world position or travel distance;
- body facing/orientation or major posture class;
- support/contact mode (seated -> standing, supported -> free standing, etc.);
- prop possession, grip, count, load, or placement;
- equipment identity or weight/load selection;
- camera yaw/pitch/height/distance or shot scale;
- screen direction or action vector;
- environment region / occlusion relation;
- performance/fatigue state that should visibly evolve;
- lighting or time state when continuity matters.

If several dimensions change together, split them across intermediate states instead of asking one interpolation to solve all of them.

## One-major-change heuristic

For continuity-critical transitions, prefer one **major** state change per adjacent pair and only small secondary changes. Example:

`arms lower -> weights settle at sides -> first light dumbbell set down -> second light dumbbell set down -> reach heavier pair -> lift first heavier dumbbell -> lift second heavier dumbbell -> stand/reset -> small body turn -> exercise-ready stance`

The intermediate frames may look visually boring. That is acceptable; their job is temporal control.

## Pairwise reachability gate

Each adjacent anchor pair must pass:

1. **Physical reachability** — can body, contact, and props move from A to B naturally in the intended duration?
2. **Camera reachability** — can camera position/scale move from A to B without an unintended cut or warp?
3. **Identity/geometry stability** — does the model only need to animate motion, rather than reconstruct the character/equipment from a substantially different view at the same time?
4. **Object-state causality** — are pickup, put-down, handoff, load swap, or support changes actually represented?
5. **Temporal readability** — would a viewer understand the movement path without inventing a missing beat?

If any answer is no, add an intermediate anchor or split into another generated segment.

## Provider-aware compilation

More source keyframes do **not** imply sending every keyframe to one provider request.

- When a provider supports ordered multi-keyframe/reference workflows, use the verified feature and map the ordered states explicitly.
- When a provider supports only first+last control, compile a dense source sequence into overlapping adjacent segments: `A->B`, `B->C`, `C->D`, preserving the shared boundary anchor.
- When a provider supports only a start image, use the accepted tail frame of one take as a candidate continuation anchor only after rendered QA; rebuild from a clean canonical still when recursive continuation begins to drift.
- If a provider exposes video-extension or video-to-video motion preservation, prefer that mode when preserving an already-good motion path is more important than regenerating it from stills.

Provider limits and behavior are volatile and must be freshly verified.

## Temporal continuity budget

Use relative rather than hard universal thresholds. Adjacent anchors should stay within a conservative continuity budget for:

- subject translation;
- body rotation;
- limb phase change;
- camera angle change;
- subject scale / crop change;
- prop displacement;
- support/contact changes.

If a transition feels like a new shot rather than the next instant of the same shot, either mark it as an intentional editorial cut or add bridge states.

## Camera rule

Do not rotate the performer, equipment, and camera substantially in the same transition. When a camera-family change is needed, stage it gradually across bridge states or make it an intentional cut. Preserve framing and lens feel enough for interpolation to read as one continuous shot.

## Motion-vector rule

Track subject and camera vectors at the end of each state. The next state should continue, decelerate, settle, or deliberately reverse that vector. Avoid unexplained vector discontinuities.

## Video-readiness audit

Before handing stills to a video provider, inspect the source sequence itself for:

- pairwise reachability;
- keyframe density proportional to transition complexity;
- no simultaneous unexplained body/object/camera jump;
- stable aspect ratio and framing family where continuity is intended;
- explicit prop/load transitions;
- clean first/last states for each compiled segment;
- no duplicate semantic phase unless a deliberate hold is intended;
- a clean canonical recovery point to prevent recursive drift.

A beautiful source sequence can still fail this audit.

## Research basis (reviewed 2026-10-04)

Current first-party provider guidance reinforces provider-specific temporal controls rather than one universal workflow:

- Google Veo 3.1 supports first+last-frame interpolation and up to three content reference images.
- ByteDance/BytePlus Seedance 2.5 supports strict first/last-frame generation plus ordered independent keyframes in reference workflows; its guidance explicitly distinguishes multi-panel storyboards from independent keyframes and supports timestamped shot/timeline descriptions.
- Luma Dream Machine supports start/end keyframes and extension toward image keyframes; current Ray3 Modify also combines keyframes with character reference in video-to-video workflows.
- Runway image-to-video guidance emphasizes that the input image defines the initial visual state and prompts should focus on motion; current product documentation separates image references, image-to-video, and keyframe/edit workflows.

Community practice also reports that overloading one short generation with several simultaneous camera/subject changes or recursively reusing degraded end frames can produce visible seams or drift. Treat such reports as operational evidence, not provider guarantees.
