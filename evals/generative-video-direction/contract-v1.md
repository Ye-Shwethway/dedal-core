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
