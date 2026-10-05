---
name: generative-video-direction
description: Convert accepted story and visual state into model-feasible generative-video shots, motion/camera/performance choreography, provider-neutral motion specs, provider-specific generation contracts, generated-take QA, and targeted repair plans across video-generation providers.
---

# Generative Video Direction

Own the layer between **accepted narrative/visual state** and **usable generated moving-image takes**. This is generative cinematography and motion direction, not a prompt-pack skill and not post-production editing.

## Use when

- turning a story beat, storyboard, still sequence, start frame, end frame, or reference set into text-to-video/image-to-video/reference-to-video instructions;
- deciding how a shot should move through time: performance, body/object motion, environmental response, camera path, focus, pacing, sound when supported;
- deciding which provider control surface is most appropriate: text-only, start frame, first+last frame, multi-image/reference inputs, motion/camera reference video, audio reference, extension/edit mode, or another verified mechanism;
- compiling provider-specific prompt/control packages for Seedance, Veo, Runway, Firefly, Kling, Luma, or successor systems;
- inspecting generated takes for identity, motion, physics/contact, camera, continuity, timing, end-state, audio, or provider-execution failure and planning a narrow retry.

## Ownership boundary

Generative Video Direction owns:

`accepted story/visual truth -> temporal shot design -> motion feasibility -> reference-role plan -> provider capability match -> generation contract -> generated take -> rendered take QA -> targeted retry/acceptance`

It does **not** own fiction canon (`story-weaver`), canonical still/keyframe production (`visual-narrative-production`), timeline editing/assembly/finishing (`video-post-production`), factual/provider truth without fresh verification (`research`), or the execution surface of a particular generator.

## Core principles

1. **Direction before prompt.** The canonical object is a structured Motion Shot Spec; provider prose/JSON is compiled from it.
2. **State transition over restatement.** For image-to-video, the visual input already carries appearance/composition/style; direct the intended temporal change unless a visual change is deliberate.
4. **Reference roles are explicit.** Identity, environment, start frame, end frame, motion, camera, style, audio, and geometry references are not interchangeable.
5. **Choose the control surface, not just the model.** Prefer the provider mode that exposes the needed constraint instead of forcing one prompt format onto every shot.
6. **One shot should be achievable.** Split overloaded action chains when duration, physics, camera, or model reliability make one generation implausible.
7. **Motion is physical state.** Track direction, velocity/pace, contact, weight transfer, object possession, secondary motion, screen direction, and start/end state.
8. **Camera is choreography.** Define whether the camera is locked, motivated by subject motion, or independently moving; avoid accidental compound moves.
9. **Prompts are execution artifacts.** They are not continuity storage and must not become the only record of the scene.
10. **Generated clips are takes.** Inspect actual frames/time progression; do not infer success from the prompt, job completion, or one attractive frame.
11. **Repair the failure class.** Change the smallest responsible layer: motion wording, action phase, reference role, start/end keyframe, crop, duration, provider mode, or shot decomposition.
12. **Keyframe density is adaptive.** Source-image density increases with transition complexity. A simple monotonic action may use a sparse mini-arc; a transition that changes body orientation, prop state, support mode, and camera cannot be forced into the same fixed count.
14. **Compile source sequences to provider capability.** Dense source keyframes are a planning truth; providers may receive them as ordered keyframes, first/last pairs, overlapping short segments, or extension/video-reference controls depending on freshly verified support.
14. **External-agent handoffs are versioned production contracts.** When a separate specialist agent executes generation, send only validated manifest-pinned assets/messages and require pair-specific feedback for narrow repair.
15. **Progressive handoff beats end-loaded handoff.** For continuity-sensitive productions, announce `production_started`, then hand off validated source sets incrementally with `images_ready(scope=set)`. Let the specialist validate/spec/risk-test early, incorporate pair-specific feedback while the source context is still warm, and emit `images_ready(scope=production)` only after all sets are ready.

## Default workflow

**Scope first:** if DEDAL has no video execution surface or the task ends at source images, load `references/source-only-motion-readiness.md` and use its source-only path instead of steps for generating/accepting takes. Plans without pixels remain planned with QA pending. Source readiness, sent handoff, external acknowledgement, and verified motion are distinct evidence states.

1. **Receive authoritative state.** Load the relevant Story Weaver handoff, accepted Visual Narrative Production anchors/keyframes/continuity state, or user-provided media. For external-agent productions, also load the live manifest and handoff protocol.
2. **Declare production and sets when collaborating externally.** Create/pin the manifest skeleton, define stable set IDs/arcs/phases, and emit `production_started` before source generation proceeds.
4. **Define the temporal objective.** What changes during this shot? What must be true at the start and end? What story/performance information must land?
4. **Preflight feasibility.** Check duration, action count, contact/physics, occlusion, camera burden, identity/reference burden, and whether the desired final state is reachable without teleportation or contradictory motion.
5. **Build a Motion Shot Spec.** Record narrative function, start/end state, subject/object/environment motion, performance, camera, timing, continuity locks, audio intent, and acceptance checks.
6. **Plan references by role and density.** Bind the smallest authoritative set, then run a pairwise reachability check across intended temporal anchors. If adjacent states require too many simultaneous body/object/camera changes, request additional bridge keyframes from Visual Narrative Production instead of asking the video model to invent the missing motion.
7. **Resolve provider capabilities fresh.** Current model/provider facts are volatile. Verify only the capabilities material to this shot and mark unsupported/uncertain controls as `unknown` rather than inventing support.
8. **Choose a generation strategy.** Text-to-video, image-to-video, first+last frame, reference-to-video, camera/motion-reference, multi-shot, extension, or another verified mode.
9. **Compile the provider contract.** Convert the Motion Shot Spec into concise provider-native prompt/control inputs; do not dump the entire project state into the prompt.
10. **Generate bounded takes.** Preserve shot ID, provider/model/version when known, inputs, prompt/controls, duration, and take ID so comparisons are attributable.
11. **Inspect the moving result.** Review start match, identity, motion path, contact/physics, camera behavior, temporal continuity, end state, environment/prop integrity, audio/dialogue when relevant, and artifacts across the whole clip.
12. **Classify and repair.** `pass | usable_with_debt | fail`; use a targeted repair plan and preserve successful dimensions.
14. **Hand off accepted takes.** Send accepted take IDs/files plus continuity/end-state notes to Video Post-Production. Do not conflate take acceptance with final edit approval.

## Shot decomposition gate

Split a requested shot when one generation would require too many independent state changes or weakly coupled actions. Common triggers:

- several sequential locomotion/contact actions plus a complex camera move;
- a prop must appear/disappear/change hands without a visible transition;
- the requested end pose contradicts the start frame or available duration;
- camera motion hides the only evidence needed to judge contact/physics;
- dialogue/performance, action, environment change, and camera choreography compete for the same short window;
- prior takes repeatedly fail the same structural relation.

Prefer a small number of purposeful shots with clean handoffs over one overloaded prompt.

## Output package

For each shot, produce or persist as needed:

- Motion Shot Spec;
- Temporal Continuity delta;
- Reference Role Map;
- provider capability assumptions with evidence/freshness state;
- provider-specific generation contract (prompt + controls + input mapping);
- take log and acceptance result;
- targeted retry plan when needed;
- post-production handoff for accepted takes.

## Progressive references

- `references/source-only-motion-readiness.md`
- `references/motion-shot-design.md`
- `references/temporal-continuity-ledger.md`
- `references/reference-role-and-provider-capability.md`
- `references/prompt-compilation-and-provider-adaptation.md`
- `references/generated-take-qa-and-repair.md`
- `references/bridge-contracts.md`
- `references/adaptive-keyframe-density-and-transition-bridges.md`
- `references/file-mediated-agent-handoff.md`
- `providers/README.md`
- `schemas/motion-shot-spec.schema.json`
- `schemas/temporal-continuity-ledger.schema.json`
- `schemas/generation-contract.schema.json`

## Pairing

Pair with `story-weaver` for narrative truth, `visual-narrative-production` for accepted visual anchors/keyframes and still-state corrections, `video-post-production` after usable takes exist, `research` for current provider/model facts, `files`/`knowledge-memory` for durable project state, and `quality-engineering` when independent readiness verification is required.
