# Visual Direction / Image Production Capability Audit — 2026-09-14

## Gap
DEDAL already had Interface Design and image-generation tools, but lacked a durable provider-agnostic workflow for reference authority, subject continuity, shot/set planning, drift diagnosis, and acceptance/persistence of visual anchors.

## Corpus reviewed

### OpenAI Academy image-generation guidance
Current guidance reviewed 2026-09-14. Useful patterns: concise purpose/subject/action/setting/style prompting; explicit roles for multiple uploaded images; targeted iterative edits; smaller clearer reference sets rather than ambiguous piles.

### Google AI image-generation guidance
Current guidance reviewed 2026-09-14. Useful pattern: modern image models explicitly support multiple object/character references for fidelity/character consistency, reinforcing the need to model reference roles as first-class state rather than prose-only prompting.

### DreamBooth
CVPR 2023 / arXiv:2208.12242. Useful pattern: subject-driven generation is a distinct optimization problem; preserving a specific subject while changing context/pose/style requires explicit identity preservation rather than generic text similarity.

### IP-Adapter
`tencent-ailab/IP-Adapter` @ `62e4af9d0c1ac7d5f8dd386a0ccf2211346af1a2`, Apache-2.0. Useful pattern: image-prompt conditioning can be decoupled from text prompting and used for subject/style/content control; this supports DEDAL's separation of identity, composition, and art direction.

## DEDAL synthesis
Adopt:
- per-dimension reference authority;
- explicit canonical trait locks;
- small role-labeled reference sets;
- shot/set contracts and controlled variation budgets;
- edit-first behavior for local defects;
- drift taxonomy and rendered-output inspection;
- explicit accept/reject/canonical-anchor promotion;
- human/Creator visual judgement as acceptance authority.

Reject/bound:
- no vendor-specific prompt syntax or adapter dependency in Core;
- no assumption that latest output supersedes accepted anchors;
- no biometric/face-recognition score as identity authority;
- no automated aesthetic metric as final acceptance;
- no unbounded prompt accretion or endless regeneration loops;
- no persistence of failed experiments as durable subject truth.

## Boundary
Visual Direction owns image-production reasoning and continuity. Interface Design owns user-interface visual systems. Writing/Editorial owns copy. Image tools execute; they do not define canonical state by themselves.

No third-party image package, model, adapter, or script was installed or executed.