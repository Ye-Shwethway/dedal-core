# Generative Video Direction

Use this reference when the task involves text-to-video, image-to-video, reference-video generation, or generated-shot continuity.

## Model-neutral shot brief

Capture only what materially controls the shot:
- beat/purpose;
- subject and action;
- environment and environmental motion;
- framing/lens feel;
- camera motion;
- lighting/style;
- duration/pace;
- continuity anchors from adjacent shots;
- start/end state when matching an edit matters;
- sound/dialogue only when the generator supports or needs it.

For image-to-video, avoid redundantly redescribing appearance already fixed by the image. Prefer motion language: subject action, environmental response, camera motion, direction, speed, and timing.

## Iteration discipline

Start with the essential motion and camera behavior. Add one material control at a time when the output misses. This makes failure diagnosis possible and reduces contradictory prompts.

Treat each generation as a take. Record why a take is accepted or rejected: identity drift, unwanted cuts, camera mismatch, physics/motion defects, temporal discontinuity, bad hands/faces, prop drift, dialogue mismatch, or simply wrong performance.

## Continuity across generated shots

Maintain a compact continuity ledger for multi-shot work:
- canonical subject/reference image(s);
- wardrobe/props;
- location/weather/time;
- screen direction and position;
- lighting/color world;
- focal-length/framing family;
- motion state at cut boundaries;
- approved shot/take IDs.

Do not force a single tool to solve every shot. Pick the generator by current capability and use post-production to stabilize, trim, reframe, or bridge otherwise usable takes.

## Evidence reviewed 2026-09-14

- Google DeepMind Veo 3 prompt guide: framing/camera motion, style, lighting, character, location/action and sound are explicit prompt dimensions.
- Runway current Gen-4/4.5 guidance: start simple; image-to-video prompts should emphasize motion; use clear positive physical descriptions; camera terminology and reference media are first-class controls.
- ByteDance Seedance first-party material: native multi-shot storytelling, prompt following, subject/style consistency, large motion range and camera control.
- OpenAI Sora product page: Sora product discontinued 2026-04-26; preserve only transferable creative patterns, not product-specific routing assumptions.

Provider/model behavior changes quickly. Verify current first-party docs before relying on duration, input/reference limits, audio support, prompt syntax, product availability, or pricing.
