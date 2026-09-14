---
name: video-production
description: Plan, direct, assemble, edit, subtitle, mix, verify, and deliver video or motion work, including generative-video workflows and FFmpeg/Remotion-style post-production.
---

# Video Production

Own the temporal media-production layer: how stills, generated clips, footage, audio, captions, motion graphics, and edits become a coherent moving-image artifact.

## Use when

- planning a short film, story sequence, promo, explainer, reel, montage, or cinematic scene;
- directing text-to-video or image-to-video generations across tools such as Veo, Flow, Runway, Seedance, or successor products;
- selecting takes, maintaining shot/scene continuity, or translating a story beat into shot coverage;
- trimming, joining, reframing, transcoding, stabilizing, retiming, captioning, mixing, normalizing, or exporting video/audio;
- composing generated stills/clips into an edited sequence;
- using FFmpeg, Remotion, or another runtime as the execution surface.

## Ownership boundary

Video Production owns temporal storytelling, shot coverage, camera/motion language, generated-take evaluation, editing rhythm, captions/subtitles, soundtrack/dialogue balance, motion-graphics composition, and delivery-specific media decisions.

It does **not** replace:
- Visual Direction for canonical still-image identity/reference hierarchy;
- Writing/Editorial for prose/script language quality;
- Research for external factual claims;
- Quality Engineering for independent acceptance/readiness when that is a distinct subgoal;
- Files for artifact identity/retrieval;
- the actual generation/editing tool, app, CLI, or codec runtime.

## Workflow

1. **Frame the deliverable.** Audience, purpose, duration, aspect ratio, platform, language, source assets, and quality bar.
2. **Build temporal intent.** Define beats, scene order, shot roles, continuity constraints, and audio/caption needs before generating or cutting.
3. **Choose the execution lane.** Generative-video app, footage edit, image-to-video, Remotion/motion graphics, FFmpeg post-production, or a hybrid.
4. **Generate or inspect source media.** Treat generated clips as takes, not canonical truth. Probe real media before editing.
5. **Assemble for meaning.** Prefer motivated cuts, readable pacing, continuity, and audio-led timing over effect density.
6. **Polish selectively.** Reframe, stabilize, grade/tone-map, retime, mix, caption, and add transitions only when they improve the piece.
7. **Verify the render.** Check duration, dimensions, streams, sync, caption readability, clipping/loudness, visual continuity, and final playback.
8. **Deliver intentionally.** Preserve masters/intermediates when useful and produce platform-appropriate exports without confusing encode success with editorial quality.

## Durable rules

- A prompt is not a shot; a generated clip is a take; a take is not an approved edit.
- For image-to-video, the image often already supplies appearance/composition; use text primarily to control motion and temporal behavior unless a change is intended.
- Describe physical subject, scene, and camera motion clearly; avoid contradictory choreography and overstuffed short clips.
- Continuity is multi-layered: subject identity, wardrobe/props, location, screen direction, lighting, time, lens/framing language, and motion state.
- Probe before edit. Prefer stream copy only when cut precision/codec constraints permit; otherwise re-encode deliberately.
- Subtitles are editorial objects: timing, safe areas, line length, reading speed, language, and contrast matter.
- Audio completion requires listening-oriented evidence where available; waveform/codec success alone is not mix quality.
- Render success is not playback, sync, or narrative-quality proof.
- Tool/model limits, current prompt syntax, supported resolutions/durations/codecs, and pricing are live facts; verify when material.

## Progressive references

- `references/generative-video-direction.md`
- `references/post-production-and-delivery.md`
