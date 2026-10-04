# Visual Narrative Production Contract v2

## Required behaviors

### VNP-01 Reference authority
Different references may independently control identity, physique, grooming, performance, pose/geometry, wardrobe/props, environment, composition/camera, and style/lighting. Conflicts are resolved by dimension, never silently averaged.

### VNP-02 Narrative-to-shot intent
A narrative scene is decomposed into visual beats and shot roles before generation. The workflow does not illustrate every sentence or default every beat to a portrait.

### VNP-03 Continuity ledger
Sequential same-scene images preserve character/environment/prop/light/spatial/camera-axis state and apply explicit deltas. Location/time transitions carry forward only state that should persist.

### VNP-04 Camera continuity
When spatial continuity matters, screen direction, eye lines, relative positions, and camera axis are tracked or deliberately re-established.

### VNP-05 Performance direction
Emotion is expressed through observable performance (gaze, posture, facial tension, gesture, interpersonal distance) rather than a single generic emotion adjective.

### VNP-06 Action anatomy/contact
Dynamic scenes are checked for limb count, joints/range, balance, weight bearing, grip, contact/intersection, force direction, object physics, and readable silhouette.

### VNP-07 Prompt compilation
Generation language is compiled from structured shot/continuity state. Edits distinguish what changes from what must remain preserved.

### VNP-08 Neutralization boundary
Benign scenes may be rewritten in precise technical/production language to reduce ambiguity, but the workflow never uses obfuscation or euphemism to bypass policy or change a prohibited request into an allowed-looking prompt.

### VNP-09 Rendered verification
Identity, anatomy, contact, text, composition, continuity, and story-fit claims require inspection of the actual rendered output.

### VNP-10 Role-specific promotion
Accepted outputs can become anchors only for explicitly approved roles. A useful pose reference with identity drift does not become an identity anchor.

### VNP-11 Edit locality
Local defects in an otherwise accepted image should be corrected narrowly when supported, preserving accepted identity/geometry/composition/lighting unless broader change is required.

### VNP-12 Story boundary
Narrative canon/prose ownership remains with Story Weaver; generative temporal direction remains with Generative Video Direction; temporal media assembly/editing remains with Video Post-Production.

### VNP-13 Automatic self-review
After each rendered shot, the workflow must inspect shot-role fit, objective visual defects, continuity, invented state, and adjacent-shot repetition before relying on Creator feedback. Shots may be classified as pass, usable-with-debt, or fail.

### VNP-14 Sequence-level anti-repetition
Every 2–3 accepted shots, or immediately after a Creator reports repetition, the workflow compares pose/silhouette, camera relation, blocking, action line, performance, state progression, and narrative information across the sequence. Repetition must be corrected at shot-spec/beat/blocking level rather than by adjective accumulation.

### VNP-15 Feedback propagation
A Creator correction to a reusable defect class must be applied to subsequent shots and recent-sequence review so the same correction is not repeatedly offloaded to the Creator. Durable recurring lessons route through Self-Improvement.

### VNP-16 Pixel-reference binding
When recurring-character consistency matters and authoritative visual anchors exist, the actual identity/physique/grooming images must be bound to the generation execution as pixel-bearing/provider-supported image references. Reading, viewing, or describing those images is not sufficient. Text-only fallback is explicit and may not be presented as a locked identity workflow.

### VNP-17 Environment/composition separation
An environment anchor preserves place identity, stable geography, materials, recurring objects, and time/light state; it does not force identical background framing or full landmark visibility across different camera positions unless composition continuity is separately required.

### VNP-18 Scene geometry and gaze realism
Movement/action shots must define a coherent subject start, destination/action target, movement/facing direction, camera side/axis, visibility plan, and action-appropriate gaze. Camera placement should reveal identity without forcing implausible head turns or contradictory movement.

### VNP-19 Visible interaction geometry
Equipment action shots preflight phase, support, contact points, visible joint chain, head/support relation, load path, and crop evidence. A tight frame that hides the only means of judging a disputed contact must be widened or reframed. A visible impossible relationship fails QA regardless of overall image quality.

### VNP-20 Comparison-set integrity
Every candidate in a requested set passes the same rendered inspection. A critical action/contact failure is replaced and is not counted toward the promised set. Differences between valid candidates serve distinct phase/framing choices while preserving accepted identity and environment state.

### VNP-21 Reviewable delivery
When the Creator requests individual review files or a connected destination, the workflow verifies the requested number of accessible individual assets and returns direct links. It does not equate a generation preview or a ZIP with confirmed reviewable delivery.


### VNP-22 Successive mini-arc continuity
A tightly coupled 3–4 shot action mini-arc may be generated as one coherent multi-output request when supported, but every requested shot is a separate full-frame asset. The group shares a local continuity envelope and advances by one micro-delta per frame. A collage, contact sheet, split-screen, or storyboard is a format failure unless explicitly requested.

### VNP-23 Natural action and equipment realism
For exercise or skilled movement, ordinary biomechanics and task-appropriate gaze/head-neck alignment outrank cosmetic face-angle avoidance. Facing toward the camera is allowed when natural. Load-bearing equipment must have believable scale, proportions, supports, and contact geometry relative to the subject and adjacent shots.

### VNP-24 Narrow retry preservation
When a local frame fails inside an otherwise successful sequence, the retry preserves accepted identity, scene, lighting, body/wardrobe state, equipment state, and camera family, changing only the failing relation or phase. Broad prompt rewrites that unnecessarily drift accepted dimensions are a regression.

### VNP-25 Phase-signature admission
Before a 3–4 shot mini-arc is delivered, the workflow maps every rendered slot to its observed action phase and compares that sequence with the planned phase progression. Adjacent outputs that differ only by framing/crop but resolve to the same action state are redundant and must be rejected or narrowly regenerated. Skipped or out-of-order phases also fail admission.

### VNP-26 Physical-state and proficiency continuity
Across successive stills, persistent props/equipment preserve count, morphology/topology, spatial relation, and contact state unless a visible or intentionally justified transition changes them. Unexplained teleportation, fusion/splitting, duplication, disappearance, or functional topology drift fails admission. When a subject has established training/skill, movement form must remain compatible with that proficiency and current scene state; unexplained novice-like stance, balance, joint organization, or foot placement is a realism failure.

### VNP-27 Support-axis and camera-body-equipment coherence
When a support apparatus constrains the action, the workflow must preserve a physically coherent relationship among body/action axis, support-equipment axis, contact map, and camera projection. Camera placement should reveal natural performance rather than forcing head/torso turns or rotating/skewing the apparatus. A frame with locally correct anatomy but implausible performer-to-support alignment fails admission.

### VNP-28 Weighted-load and label realism
Weighted actions plan load logic across dumbbells, barbells, kettlebells, machines, carries, weighted calisthenics, and on-body loads. Visible labels/plate counts/stack settings persist as continuity facts; unexplained strength-inconsistent or randomly changing loads fail realism/continuity review.

### VNP-29 Canonical proportion framing
When canonical height/proportion matters, camera distance and crop must preserve the intended body read. Tight framing or perspective that makes a tall character read short-legged is a correctable composition failure.

### VNP-30 Video-bridge anchor production
When GVD requests temporal bridge anchors, VNP may exceed the ordinary 3–4 shot mini-arc and generate a denser sequence of separate full-frame states. Density is determined by pairwise reachability, not a fixed count.

### VNP-31 Collaborative source-sequence handoff
When accepted stills are prepared for an external motion-generation agent, Visual Narrative Production persists an ordered production manifest, classifies every adjacent pair for reachability, inserts bridges before handoff when needed, and emits `images_ready` only after identity, physical, prop/load, pairwise reachability, and video-readiness checks pass.


### VNP-32 Progressive set-scoped source handoff
For an external motion agent, Visual Narrative Production creates a stable production/set plan and emits `production_started` before full source completion. Each set is independently validated and may be handed off as `images_ready(scope=set)` for early downstream review. A set handoff never implies production completion; `images_ready(scope=production)` is emitted only after the complete ordered source sequence passes validation.

## Regression failures
- recurring character becomes narrower/taller/older/etc. because an action/style reference overrides physique/identity;
- extra limb or fused hand is accepted because the overall image looks attractive;
- hand penetrates a solid prop or grip/load direction is physically implausible;
- same room silently changes windows, key light, prop placement, or screen direction between shots;
- a false-trigger mitigation removes essential benign scene meaning instead of clarifying it;
- a disallowed request is disguised through coded prompt wording;
- previous accepted image is regenerated wholesale for a tiny local correction without need;
- newer output silently replaces canonical anchors;
- prose prompt is treated as the sole continuity record for a multi-shot scene;
- adjacent action shots reuse the same stance/camera/blocking while claiming different narrative roles;
- a weapon or other prop appears without an authorized state transition and is not caught before promotion;
- the Creator must repeatedly point out the same detectable visual defect because prior feedback was not propagated;
- a canonical character image is inspected in Library but not actually passed to the image generator, causing text-only identity drift;
- an environment anchor is treated as a fixed background plate, forcing a destination object into full view and contradicting the chosen side/rear camera logic;
- an action subject turns their head away from the task target merely to expose facial identity, producing implausible performance.
- a pull-like action depicts almost straight arms with the head near the support, or a support passing through the face, and is offered as a valid close-up;
- a repair set promises four options but includes a rejected contact failure or near-duplicate merely to meet the count;
- output is called delivered although the requested individual review location was never read back.
- a four-shot action request is returned as one collage or contact sheet without the user asking for that format;
- a subject bows or turns the head unnaturally only to avoid facing the camera during an exercise;
- a workout bench or other load-bearing object changes to implausible scale/proportions across adjacent shots;
- one failed slot triggers a broad regeneration that drifts an otherwise accepted character/scene/lighting envelope.
- persistent props teleport between established locations, merge/split, duplicate, vanish, or change load-bearing topology without an authorized transition.
- an established trained performer adopts unexplained novice-like stance, foot placement, balance, or joint organization during a routine skilled action.
- the performer has correct local biomechanics but the support bench/platform/rail is skewed or rotated into a physically incompatible relation with the body/contact map.
- a visible weight label/plate count changes between adjacent shots without a load-change action or justification.
- a tall canonical character is framed so tightly that the lower body reads non-canonically short when a wider crop would preserve proportion.
- a video-bound transition jumps across distant states because the still workflow incorrectly enforces a fixed four-frame cap.

## Evaluation posture
Contract validation proves the workflow is encoded. Real outcome validation requires representative multi-shot generation/edit sessions and Creator/project acceptance. Character-specific private regression fixtures stay outside public Core.

## Transfer cases for the next outcome evaluation
- **Overhead bar action:** given a near-finish close crop with nearly straight arms and offscreen grips, reject or reframe; a visible bar crossing the subject's face is an immediate failure.
- **Equipment variation set:** given four requested alternatives and one failed grip/contact render, supply four inspected usable alternatives, with purposeful phase/crop distinctions and individual verified links.
- **Non-equipment transfer:** for a heavy door pull or rope climb, trace support/contact/joint/load geometry and choose a crop that exposes the disputed interaction without copying the overhead-bar wording.

- an external-agent handoff is emitted because files exist even though pairwise reachability or video-readiness has not been validated.
