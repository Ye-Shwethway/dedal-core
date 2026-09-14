# Video Production Deep Audit — 2026-09-14

## Gap

DEDAL had strong still-image Visual Direction but no owner for temporal storytelling, generated-video shot direction, post-production, subtitles/audio, motion graphics, or final media delivery. The Creator already performs these workflows manually with dedicated video-generation apps and editing tools, making this a demonstrated gap rather than speculative expansion.

## Sources reviewed

### First-party generative-video guidance
- Google DeepMind Veo 3 current prompt guide: shot framing/motion, style, lighting, character, location/action and sound as explicit controls.
- Runway current Gen-4/4.5 prompting/reference/camera guidance: simple iterative prompts, positive physical descriptions, image-to-video motion emphasis, camera terminology and reference-media continuity.
- ByteDance Seedance first-party pages: prompt following, native multi-shot storytelling, subject/style consistency, camera/motion control.
- OpenAI Sora product page checked for current state: Sora product unavailable as of 2026-04-26; therefore Sora-specific product assumptions must not be frozen into DEDAL.

### Mature skill/tool corpora
- `remotion-dev/skills@bd566b65d521b40fe92e1f26766e82de9e291693`: official Remotion Agent Skills, actively maintained (main updated 2026-09-12), with create/markup/render/captions/multimedia/maps/docs/interactivity coverage. Public repo did not expose a root license in the audited snapshot, so DEDAL adapts methodology only and does not vendor its material.
- `kajisho5/ffmpeg-skill@a6232b95f595aa35fa8cea0d055f0163baa908e9`, MIT, current release 1.16.1 on 2026-09-14: mature probe→edit→check→verify workflow and broad FFmpeg/ffprobe coverage including captions, loudness, sync, HDR/SDR, multicam and project rendering.
- Additional community video-agent skills were reviewed as corroboration, but not treated as primary authority when they were young or lightly adopted.

## Durable findings

1. Generative-video direction is filmmaking/temporal direction, not merely longer image prompting.
2. Image-to-video should usually prompt motion/temporal behavior rather than redescribe the supplied frame.
3. Multi-shot quality requires a continuity ledger and take-selection discipline.
4. Generated clips should be treated as takes; approval and editorial assembly are separate stages.
5. FFmpeg post-production should probe source media before mutation and verify rendered output after mutation.
6. Programmatic video (for example Remotion) is a useful execution lane for captions, typography, UI demos, charts, explainers and repeatable motion graphics, but it is not the faculty identity.
7. Render/encode success does not prove sync, subtitle readability, continuity, mix quality or storytelling quality.
8. Model/tool capabilities drift quickly, so duration/reference/audio/resolution/syntax/pricing facts require current first-party verification when material.

## Ownership test

Existing owners do not cover the gap cleanly:
- Visual Direction: still-frame/reference/canonical visual continuity.
- Writing/Editorial: script wording.
- Software Development: code implementation for a motion system, not editorial ownership.
- Quality Engineering: independent acceptance, not creative assembly.

Video Production therefore has an independently routable recurring ownership layer.

## Decision

**PROMOTE — Video Production as a top-level faculty.**

FFmpeg, Remotion, Veo/Flow, Runway, Seedance and future generators/editors remain progressive references or execution surfaces beneath it.
