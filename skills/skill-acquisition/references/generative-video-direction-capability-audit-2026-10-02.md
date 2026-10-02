# Generative Video Direction Capability Audit — 2026-10-02

## Concrete gap

DEDAL's former `video-production` owner combined pre-generation motion direction with post-generation editing/finishing. Real sequential-image story work now needs an independently routable layer that can translate accepted story + still state into model-feasible motion while adapting across providers.

## Current provider evidence

First-party sources reviewed on 2026-10-02 showed a convergent move from text-only prompting toward richer creative controls:

- Google Veo 3.1: image-to-video, consistent-element references, first/last-frame transitions, synchronous audio in supported modes, and staged workflows.
- Runway Gen-4.5: I2V image supplies composition/appearance/style while text primarily directs motion/camera/temporal progression; iterative simplicity is recommended.
- ByteDance Seedance 2.5: long/multi-shot generation, multimodal reference sets, motion/creative references, and editing controls in supported surfaces.
- Adobe Firefly Video: first/last frames and camera-motion reference video.

Conclusion: provider capability selection and reference-role orchestration are now first-class production decisions. Exact limits remain volatile and are not frozen into Core.

## Public repo comparison

Compared public skill patterns included `smixs/visual-skills`, `0xhughs/director-skills`, `nigo-studio/ai-film-skills`, and `runwayml/skills`.

Generalizable patterns adopted in DEDAL-native form:

- do not make one giant prompt the production architecture;
- separate story/visual state, motion direction, model adaptation, diagnostics, and assembly;
- keep provider-specific knowledge behind adapters/references;
- mark unsupported/unverified model capabilities unknown rather than guessing;
- treat execution skills/API wrappers as transport, not creative authority;
- use explicit QA/iteration rather than assuming prompt correctness.

No third-party text/code is copied into DEDAL. External repos are methodology/comparison evidence only.

## Architecture decision

Promote `generative-video-direction` as a new creative-production owner. Rename/refocus the previous combined owner to `video-post-production`; preserve `video-production` and `video-editing` as aliases for backward compatibility.

New boundary:

`Story Weaver -> Visual Narrative Production -> Generative Video Direction -> Video Post-Production`

with a return bridge from GVD to VNP when missing/corrected keyframes or geometry references are needed.

## Promotion criteria

- independent routing and no duplicate ownership;
- provider-neutral Motion Shot Spec and Temporal Continuity Ledger;
- explicit reference-role mapping;
- fresh provider capability resolution with `unknown` support;
- generated-take inspection and targeted repair;
- clean post-production handoff;
- regression validators and privacy scan pass;
- broader outcome claims deferred until representative real provider runs.
