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
Narrative canon/prose ownership remains with Story Weaver; temporal media assembly remains with Video Production.

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

## Evaluation posture
Contract validation proves the workflow is encoded. Real outcome validation requires representative multi-shot generation/edit sessions and Creator/project acceptance. Character-specific private regression fixtures stay outside public Core.

## Transfer cases for the next outcome evaluation
- **Overhead bar action:** given a near-finish close crop with nearly straight arms and offscreen grips, reject or reframe; a visible bar crossing the subject's face is an immediate failure.
- **Equipment variation set:** given four requested alternatives and one failed grip/contact render, supply four inspected usable alternatives, with purposeful phase/crop distinctions and individual verified links.
- **Non-equipment transfer:** for a heavy door pull or rope climb, trace support/contact/joint/load geometry and choose a crop that exposes the disputed interaction without copying the overhead-bar wording.
