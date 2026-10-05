# Adaptation Notes — Generative Video Direction

_Date: 2026-10-02_

This is a **DEDAL-native rewrite** created from a demonstrated workflow gap. No third-party skill text/code is imported.

## Why a separate faculty

The prior `video-production` package mixed two materially different jobs:

- generative shot/motion direction before usable moving-image media exists;
- editing, assembly, audio, captions, finishing, and delivery after media exists.

Current generative-video systems expose increasingly distinct control surfaces (start/end frames, multiple visual references, motion/camera references, audio references, extension/edit modes, multi-shot controls). Treating these as a small prompting reference inside an editing skill obscured routing and made provider adaptation harder to reason about.

## External evidence used as methodology, not copied content

First-party/vendor evidence reviewed 2026-10-02:

- Google Cloud / Veo 3.1 guidance: image-to-video, reference/ingredient inputs, first+last-frame transitions, synchronous audio, and staged multi-step workflows.
- Runway Gen-4.5 guidance: image-to-video prompts should primarily describe motion, camera, timing, direction and speed; start simple and refine iteratively.
- ByteDance Seedance 2.5 first-party material: long-form/multi-shot generation, large multimodal reference sets, motion/creative references, and timestamp-level editing controls.
- Adobe Firefly guidance: first/last frames and reference-video camera-motion matching.
- Luma/Ray family public guidance was reviewed comparatively for keyframe/reference-oriented control patterns when available.

Public skill/repository patterns reviewed comparatively:

- `smixs/visual-skills` — thin routing, craft references, image->keyframe->motion separation, model files, mandatory checks. License/provenance noted; no text imported.
- `0xhughs/director-skills` — separation of story/shot breakdown/video prompting/model adaptation/diagnostics and explicit `unknown` handling for unsupported model capabilities.
- `nigo-studio/ai-film-skills` — video prompt direction separated from character consistency and from later assembly/edit guidance.
- `runwayml/skills` — provider execution skill as an API/runtime adapter, supporting the boundary that execution surfaces are not creative-direction owners.

## DEDAL-native choices

- canonical object = **Motion Shot Spec**, not a prose prompt;
- provider-neutral temporal state and continuity remain durable; provider syntax is compiled late;
- reference inputs receive explicit roles;
- provider capabilities are verified just-in-time and may be `unknown`;
- missing keyframes/reference geometry can trigger a return request to Visual Narrative Production;
- generated clips are inspected as takes before post-production handoff;
- repeated structural failure changes control strategy/shot decomposition rather than accumulating adjectives;
- `video-production` is migrated to canonical `video-post-production`, with legacy aliases retained.

## 2026-10-05 production refinement
Existing ownership retained; `source-only-motion-readiness.md` converts broad principles into scene-specific causal/physical decisions and evidence-aware source handoffs. Offline fresh-context planning trials support diagnosis only; actual image realism and generated motion remain unmeasured. No private production assets or character canon are included.
