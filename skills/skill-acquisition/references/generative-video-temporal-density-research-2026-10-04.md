# Generative Video Temporal Density Research — 2026-10-04

## Question

How should DEDAL design still-image/keyframe sequences for smoother generative-video continuity, especially when arc-to-arc transitions currently jump in body position, prop state, or camera?

## First-party findings

### Google Veo 3.1
Google documents first+last-frame interpolation, image-to-video, up to three content reference images in Veo 3.1, and video extension. This favors canonical dense planning with provider compilation into adjacent endpoint pairs when intermediate states need strict control.

Source: Google AI for Developers, "Generate videos with Veo 3.1 in Gemini API" (reviewed 2026-10-04).

### ByteDance / BytePlus Seedance 2.5
BytePlus documents both strict first/last-frame mode and independent ordered keyframes in reference mode. It explicitly states that multi-panel storyboards are high-level guidance, while multiple independent keyframe images align more closely with output visuals. It also supports timestamped/shot-based visual timelines and large multimodal reference sets in current ModelArk surfaces.

Sources: BytePlus ModelArk Seedance 2.5 Prompt Guide and Create Video Generation Task API (reviewed 2026-10-04).

### Luma Dream Machine
Luma documents start/end keyframes, extension toward image keyframes, and current Ray3 Modify workflows combining video, keyframes, and character references. This supports pairwise keyframe interpolation and motion-preserving video-to-video strategies.

Sources: Luma Learning Hub, "How to use Keyframes", "Ray3 Modify User Guide", and current Video Capabilities guide (reviewed 2026-10-04).

### Runway
Runway's current image-to-video guidance treats the input image as the initial visual state and recommends focusing the prompt on motion/camera progression. Current product docs separate references, I2V, keyframe/edit, and video-to-video surfaces rather than promising one universal ordered-keyframe interface across models.

Sources: Runway Help Center, current Image-to-Video Prompting Guide, Gen-4/Gen-4.5 material, References, and Edit Studio docs (reviewed 2026-10-04).

## Community/production evidence

Recent creator reports consistently describe visible seams when too many subject/camera changes are demanded in one short generation, and quality drift when recursively chaining model-generated tail frames for long sequences. These are anecdotal and provider/version dependent, but they match DEDAL's own reviewed Darian clips.

## DEDAL conclusion

1. **Canonical source sequence density must be adaptive**, not fixed at four images.
2. **Transition arcs often need denser control than action mini-arcs.**
3. **Pairwise reachability** is the admission test: every adjacent anchor must be physically/cinematically reachable or gain another bridge state.
4. **Provider compilation is separate from canonical planning.** Dense source anchors may become ordered keyframes, overlapping first/last pairs, extension requests, or video-reference edits depending on verified capabilities.
5. **One-major-change-per-pair** is a practical heuristic, not a universal numeric law.
6. **Recursive tail-frame chaining needs clean canonical recovery anchors** to prevent drift accumulation.
7. **Camera/body/object changes should not all happen at once** unless an intentional cut is desired.

## Local outcome evidence

Two Creator-provided Darian workout videos reviewed on 2026-10-04 showed that within-exercise phases with nearby states animated more smoothly than arc-to-arc transitions where body orientation, prop/equipment relation, and camera changed together. This local evidence motivated the adaptive-density and bridge-state contracts but remains private project evidence, not public-core fixture data.
