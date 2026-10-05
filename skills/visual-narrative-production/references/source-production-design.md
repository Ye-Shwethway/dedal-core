# Source Production Design

Use for sequential narrative images and source images intended for later motion, especially body/object interaction. Own the production plan here; Story Weaver owns narrative facts and Generative Video Direction owns temporal feasibility and provider compilation. Reuse their beat and pair IDs instead of making competing versions of the scene.

## A small production contract

Before rendering settle the purpose, accepted facts, realism/style intent, required output format, source-only or still-story scope, fixed scene geography, object inventory, intended coverage, and material unknowns. Define three observable success criteria specific to this scene. A neutral portrait may need only one shot spec; use deeper planning only when interaction or continuity warrants it.

Do not convert provisional staging into canon. Do not infer an athlete's actual strength, health, or realistic working load from physique. Use the established fictional load/effort intent; research specialized technique when it materially affects the depiction. Stylized or intentionally impossible action needs a coherent declared world rule rather than accidental realism claims.

## Build the action before the camera

1. Establish a stable world frame: floor regions, support surfaces, entry/exit, object locations, facing and travel directions. World-left/right and subject anatomical-left/right differ from image-left/right; label which you mean. A camera cut may reverse screen projection without moving the objects in world space.
2. Give persistent objects stable IDs, count, geometry/function, location, holder/support, and load facts. A matching dumbbell pair consists of two distinct objects. The implement's rigid geometry stays constant when wrist/forearm orientation changes; visible end faces and label visibility may change with projection.
3. Decompose action at contact and support events: approach, reach, grasp, load transfer, move, settle, release. For each event state precondition, acting hand/body part, destination, support during transfer, and resulting possession. Do not demand a picture of every event; every omitted event must still have an explicit path or editorial ellipsis.
4. Choose economical **evidence anchors**, not a fixed frame count. Select states that expose identity, action phase, contact/load transfer, changed possession, and final consequence. Add a bridge where a pair would otherwise depend on an unseen major event. Repeated cycles can reuse an accepted phase family in the motion plan; do not silently claim that still images prove two completed repetitions.
5. Choose camera/framing that makes those relations inspectable. Keep necessary hand/handle, support, elbow/forearm, feet/floor, or object destination landmarks visible where material. Identity visibility must not force an unnatural body turn. Use a separate identity anchor or a deliberate shot instead.

## Three coupled views of each important anchor

Record compactly in the Shot Spec or linked planning table:

`shot-spec.schema.json` offers optional `production_design` for beat linkage, physical events, hand occupancy, evidence landmarks, occlusion and observed QA. Older ordinary shot specs remain valid. Required real-world observation and readiness judgment remain semantic gates; schema validity cannot certify them.

| View | Decision |
| --- | --- |
| Narrative | Beat ID, purpose, performance cue, audience information, reveal lock |
| Physical | Phase, hand occupancy/contact, support, object positions/orientation, plausible action/load path |
| Image | Camera side/projection, crop, occlusion ordering, visible landmarks proving the planned relation |

Use an **occlusion explanation** for critical contact: which surface is in front, where the handle crosses the palm, how fingers/thumb wrap, and which far end/joint may be hidden. Do not require all fingers or both labels to be visible when that contradicts geometry. Apparent overlap is not proof of contact; a hidden contact is not automatically a defect. Mark `not_observable` when the pixel evidence is insufficient, then reframe or use another anchor when the relation is a readiness requirement.

For a curl, elbow flexion and forearm rotation are different changes. Supination rotates the hand and gripped rigid implement consistently; it must not redraw a plate, move the palm to an end cap, detach the handle, or force a wrist kink. This is a visual depiction constraint, not a universal exercise prescription. Motion-specific factual claims require an appropriate current reference.

## Compile a focused prompt

Use accepted pixel references with explicit roles. Order material relations first: exact phase, interacting bodies/objects, contact/support, world placement and visibility, then performance, camera, lighting/style. Preserve accepted relations while changing the intended phase. Remove competing demands such as 'both weight labels front-facing' plus rotated grip, or 'tight face close-up' plus full support-chain evidence. Keep detailed ledgers outside provider prose; a longer prompt cannot certify geometry.

## Inspect evidence, not intention

After every render inspect the actual image and compare planned versus observed phase, hand occupancy, object identity/count, contact, support, projection, reveal locks, and continuity with adjacent accepted anchors. Record asset ID/version (or unavailable), observed landmark/relation, `pass | fail | not_observable`, severity, and narrow repair. Do not fill observation fields from the prompt. Captions, filenames, metadata, and self-written JSON cannot establish pixel realism.

Apply three gates in order:

1. **Functional:** narrative purpose, canon/reveal, identity, anatomy, contact/support, and object integrity.
2. **Sequence:** state deltas, causal possession changes, geography, distinct ordered phases, and pairwise reachability with GVD.
3. **Finish:** composition, light, material appearance, detail, text, and delivery quality.

A beautiful frame cannot average away a critical functional failure. Unknown required contact evidence blocks source readiness. Noncritical debt remains explicitly located by asset/pair, with downstream implication and accepted scope.

## Repair and stop rules

Correct the smallest failed relation and inspect edit spillover. If two targeted retries repeat the same structural defect, change staging, view, reference, or action decomposition before spending another render. Do not rotate labels at the expense of grip, hide failed physics behind a crop, or regenerate the whole accepted set reflexively. Re-audit neighboring frames after an anchor replacement; bind the replacement version in the handoff.

Close with individual accepted files, ordered IDs, observed QA, remaining debt, and pair decisions. A source package can be ready for external motion planning while generated-motion quality remains untested. No video job, video acceptance, or external ACK may be invented.

## Research basis — reviewed 2026-10-05

Google and Runway first-party I2V guides emphasize clean source images and motion-focused text. Adobe's continuity guidance supports deliberate action-axis and spatial planning. Physics-IQ and PhyWorldBench distinguish attractive video appearance from physical consistency. The workflow above is our production inference from those sources; it does not import a research benchmark as a guarantee.

- https://cloud.google.com/vertex-ai/generative-ai/docs/video/best-practice
- https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide
- https://www.adobe.com/uk/creativecloud/video/discover/what-is-the-180-degree-rule.html
- https://physics-iq.github.io/
- https://research.nvidia.com/labs/cosmos-lab/phyworldbench/
- https://www.acefitness.org/resources/everyone/exercise-library/10/hammer-curl/ (neutral-grip example only; not authority for every curl variant)
