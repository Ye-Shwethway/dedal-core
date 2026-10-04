# Generative Video Direction Contract v1

## Routing

### GVD-01 Image sequence to motion
Accepted sequential stills that must become generated motion route primarily to `generative-video-direction`, with `visual-narrative-production` supporting authoritative visual state.

### GVD-02 Editing boundary
Existing generated takes that need cutting, assembly, subtitles, mix, effects, finishing or delivery route to `video-post-production`, not GVD.

### GVD-03 Story boundary
Fiction canon, character motive, dialogue and beat causality remain with `story-weaver`.

## Production contracts

### GVD-04 Motion Shot Spec before prompt
A provider-specific prompt is compiled from a provider-neutral Motion Shot Spec; prose prompt text is not the only continuity record.

### GVD-05 Reference-role mapping
Identity, environment, start/end frame, geometry, motion, camera, style and audio references receive explicit roles; a motion/style reference cannot silently redefine canonical identity/place.

### GVD-06 Capability uncertainty
Material provider features are fresh-verified and may be marked `unknown`; unsupported/uncertain capabilities are not hallucinated.

### GVD-07 Feasibility / decomposition
Overloaded action/camera chains are split when necessary rather than forced into one generation.

### GVD-08 I2V motion focus
When an input image already establishes appearance/composition/lighting/style, the generation contract primarily directs temporal change unless a visual change is intentional.

### GVD-09 Take inspection
Generation completion is not acceptance. Actual moving output is inspected across time for identity, motion, physics/contact, prop/environment integrity, camera, pacing, end state and audio where material.

### GVD-10 Targeted repair
Repeated structural failures change the responsible layer — reference, keyframe geometry, phase, duration, control surface, provider or shot split — rather than accumulating adjectives.

### GVD-11 Visual return bridge
When missing/corrected keyframes materially improve control, GVD issues a structured request back to Visual Narrative Production rather than inventing visual truth.

### GVD-12 Post-production handoff
Accepted takes carry shot/take IDs, boundary/end-state/audio-tail/continuity notes into Video Post-Production; take acceptance is not final edit approval.

### GVD-13 Adaptive keyframe density
Source-image/keyframe density scales with transition complexity. A bridge that changes body position/facing, support mode, prop/load state, and camera cannot be forced into the same fixed frame count as a simple monotonic action.

### GVD-14 Pairwise reachability
Every adjacent continuity-critical anchor pair is classified as reachable, needing a bridge, or an intentional cut. Unseen major body/object/camera jumps trigger additional anchors or shot decomposition.

### GVD-15 Provider-aware keyframe compilation
A dense canonical source sequence is compiled to the provider's freshly verified control surface: ordered keyframes when supported, overlapping first/last pairs when only pairwise interpolation is supported, or extension/video-reference workflows when they preserve motion more reliably.

### GVD-16 Versioned specialist-agent handoff
When generative-video execution is delegated through a shared file workspace, the handoff pins the production manifest version, treats `images_ready` as a validated state rather than file existence, rejects stale manifests, and returns pair-specific bridge requests for narrow repair.


### GVD-17 Progressive production-start and set handoff
For external specialist collaboration, DEDAL announces `production_started` with planned stable sets before source generation completes. Each validated set may be handed off as `images_ready(scope=set)` for early validation, motion-spec preparation, pair-specific feedback, or an explicitly bounded pilot take. Full production generation waits for `images_ready(scope=production)` unless a pilot is intentionally requested.

## Regression failures

- model-specific syntax becomes project continuity truth;
- one reference is implicitly used for contradictory identity/style/motion roles;
- a provider capability is assumed because another model/version supports it;
- a 5–10 second shot is overloaded with unrelated action, transformation and compound camera moves without feasibility review;
- one attractive frame causes a temporally broken take to be accepted;
- prop possession or contact jumps without visible/causal transition;
- repeated physics failure triggers only synonym/adjective retries;
- an end-state-critical shot is repeatedly prompted text-only despite an available verified first/last-frame workflow;
- GVD performs timeline assembly/finishing that belongs to Post-Production;
- Post-Production rewrites motion-generation direction instead of returning a take-level issue to GVD.
- a complex transition is represented by only a few distant still states even though adjacent states visibly jump in body pose, prop state, or camera.
- a provider that only supports start/end control is given a dense storyboard as if it natively enforces all intermediate keyframes.

- a downstream agent processes a stale manifest, or returns only vague feedback when a specific broken frame pair can be named.

- a continuity-sensitive production is held until the end instead of exposing planned sets and validated set-level handoffs early enough for specialist feedback.
