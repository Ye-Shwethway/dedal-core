# Adaptation Notes — Visual Narrative Production

_Date: 2026-09-30_

This is a DEDAL-native synthesis and migration of the former `visual-direction` skill. `visual-direction` remains an alias only; there is one canonical skill implementation.

## Evidence corpus

### Current product guidance
- OpenAI image prompting guidance (reviewed 2026-09-30): describe subject/composition/style/constraints, specify people/actions and object interaction, assign roles to references, separate requested changes from preservation constraints, and iterate deliberately with rendered inspection.
- Blender Storyboarding App Template (reviewed 2026-09-30): each shot can be represented as an independent scene while a master sequencer organizes the larger sequence.
- Unreal Engine Sequencer documentation (reviewed 2026-09-30): cinematic state is organized through sequences, shots/takes, cameras, characters, lights, objects, tracks, and camera cuts rather than one monolithic instruction.

### Research patterns
- DreamBooth (CVPR 2023 / arXiv:2208.12242): recurring-subject preservation is a distinct problem from generic prompting.
- IP-Adapter (`tencent-ailab/IP-Adapter`, previously pinned at `62e4af9d0c1ac7d5f8dd386a0ccf2211346af1a2`, Apache-2.0): image conditioning can be separated from text conditioning; useful as a conceptual boundary between subject/style/reference roles.
- InstantID (`InstantX/InstantID`): single-reference identity preservation motivates explicit identity anchors rather than relying on prose recollection.
- PuLID (`ToTheBeginning/PuLID`, Apache-2.0): identity customization research reinforces identity as an independent conditioning concern.
- ControlNet (`lllyasviel/ControlNet`): pose/depth/edge/segmentation conditioning motivates a provider-agnostic pose/geometry specification independent from identity/style.
- StoryMaker (`RedAIGC/StoryMaker`): storytelling consistency extends beyond faces to body, hairstyle, clothing, and multi-character presentation.
- StoryDiffusion (`HVISION-NKU/StoryDiffusion`): long-range visual story generation motivates sequence-level continuity rather than independent-shot prompting.
- ConsiStory (`NVlabs/consistory`): cached/anchor-based subject consistency motivates accepted-anchor reuse while allowing layout variation.

## Adapted
- `visual-direction` -> canonical `visual-narrative-production` migration with alias compatibility;
- story beat -> visual beat -> shot-spec planning;
- dimension-specific reference authority and canonical locks;
- scene/sequence Visual Continuity Ledger with delta updates;
- camera axis, screen direction, eye-line, spatial relation, and environment-state continuity;
- performance direction beyond simple emotion labels;
- pose/anatomy/contact/load checks for action and object interaction;
- provider-agnostic structured shot specification plus provider-specific prompt compilation;
- semantic prompt neutralization for legitimate scenes without scene dilution or policy evasion;
- edit-first local correction and accepted-anchor promotion;
- expanded drift taxonomy including biomechanics, contact/physics, and narrative mismatch.

## Generalized real-work lessons promoted

Representative image-production work exposed recurring failures that must be caught by workflow rather than by prompt length alone:
- stable face but drifting physique/proportions;
- identity drift after solving anatomy;
- extra/duplicated limbs in dynamic poses;
- implausible wrist/joint articulation;
- hands intersecting solid objects;
- unrealistic grip/load mechanics;
- prompt/pose instruction drift into a different standard pose;
- a visually attractive image that is unusable as reference because geometry is wrong;
- recurring-character drift when canonical images are retrieved/inspected but not actually bound as pixel references to the generation call;
- environment continuity incorrectly freezing camera/background composition, creating spatially implausible movement or landmark visibility;
- facial-identity preservation attempts that force implausible head/gaze direction during an action instead of solving identity visibility through camera placement;
- benign body/anatomy scenes receiving avoidable false-positive ambiguity from unnecessarily suggestive wording.

These are generalized failure classes only. No private character identity, images, project canon, or private prompts are included in public Core.

## Rejected / bounded
- no model/provider-specific syntax as permanent Core truth;
- no requirement to install or run InstantID/PuLID/ControlNet/ComfyUI or any specific research stack;
- no claim that reference count alone improves consistency;
- no biometric score or automated aesthetic metric as canonical acceptance authority;
- no prompt obfuscation, euphemistic bypassing, or safety-evasion behavior;
- no persistence of rejected experimental outputs as canonical state;
- no collapse of narrative writing, temporal video editing, and still-image production into one giant creative skill.

No external model, adapter, or package is bundled by this adaptation.
