# Adaptation Notes — Visual Direction / Image Production

_Date: 2026-09-14_

This is a DEDAL-native synthesis, not a copied vendor prompt pack.

## Evidence corpus

### Current product guidance
- OpenAI Academy image-generation guidance (reviewed 2026-09-14): concise purpose/subject/action/setting/style prompts, explicit reference roles, iterative targeted edits, and smaller clearer reference sets.
- Google AI image-generation guidance (reviewed 2026-09-14): current image models support multiple object/character references for high-fidelity and character-consistency use cases.

### Research patterns
- DreamBooth (CVPR 2023 / arXiv 2208.12242): subject-driven generation demonstrates that preserving a specific subject across new contexts is a distinct problem from ordinary text prompting.
- IP-Adapter paper/repository: image prompting can condition subject/style/content separately from text; repository pinned at `62e4af9d0c1ac7d5f8dd386a0ccf2211346af1a2`, Apache-2.0.

## Adapted
- explicit reference-role hierarchy;
- canonical invariants vs intentionally variable traits;
- identity/composition/style/environment as separate control dimensions;
- targeted edit over full regeneration for local defects;
- series/set planning and continuity review;
- rendered-output inspection before acceptance;
- drift taxonomy and canonical-anchor promotion.

## Rejected / bounded
- no provider-specific prompt syntax in Core;
- no assumption that more reference images always improve consistency;
- no face-recognition/biometric score as acceptance authority;
- no automated aesthetic/reward metric as substitute for Creator judgement;
- no model-specific adapter/finetuning requirement;
- no persistence of failed generations as canonical state.

No external image package, model, adapter, or script was installed or executed for this adaptation.