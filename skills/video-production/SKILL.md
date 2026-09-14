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
6. **Polish selectively.** Reframe, stabilize, grade/tone-map, retime, mix, caption, and add transitions/effects only when they improve the piece.
7. **Verify the render.** Check duration, dimensions, streams, sync, caption readability, clipping/loudness, visual continuity, effect boundaries, and final playback.
8. **Deliver intentionally.** Preserve masters/intermediates when useful and produce platform-appropriate exports without confusing encode success with editorial quality.

## Durable rules

- A prompt is not a shot; a generated clip is a take; a take is not an approved edit.
- For image-to-video, the image often already supplies appearance/composition; use text primarily to control motion and temporal behavior unless a change is intended.
- Describe physical subject, scene, and camera motion clearly; avoid contradictory choreography and overstuffed short clips.
- Continuity is multi-layered: subject identity, wardrobe/props, location, screen direction, lighting, time, lens/framing language, and motion state.
- Probe before edit. Prefer stream copy only when cut precision/codec constraints permit; otherwise re-encode deliberately.
- For extraction tasks, distinguish **scene boundary**, **requested action boundary**, and **contextual edit boundary**. If the Creator asks for one specific action, do not silently widen it to the whole surrounding scene.
- Sparse contact sheets are for localization, not exact editorial boundaries. Refine candidate cuts with dense frame inspection plus audio/subtitle cues when precision matters.
- External recaps, transcripts, subtitle timing, clip descriptions, or web timestamps may help locate an event, but they are locator evidence only until reconciled with the actual local media timeline.
- When editing a rough cut/excerpt, maintain an explicit original-to-local timeline mapping and verify anchors if keyframe seeking, timestamp preservation, concat, or multiple source ranges may have shifted the nominal offset.
- Build the readable edit before decorating it. A straight cut is the default; transitions, speed ramps, flashes, shake, zooms, blur, LUTs, animated captions, and other effects need an editorial job rather than mere availability.
- Trim first, transition second. Use J/L cuts and audio continuity when they improve anticipation, dialogue flow, ambience, or scene entry/exit.
- For stylized action edits, keep emphasis effects sparse and event-driven. Strong effects repeated on every impact quickly reduce readability and feel synthetic.
- Reframe/geometry operations should usually precede final caption and graphic placement so text stays inside target safe areas.
- Subtitles are editorial objects: timing, safe areas, line length, reading speed, language, glyph coverage, shaping, contrast, and delivery mode (soft versus burned) matter.
- Audio completion requires listening-oriented evidence where available; waveform/codec success alone is not mix quality. Measure loudness/true peak when delivery targets matter, preserve channel layout deliberately, and do not normalize noise as if it were content.
- Distinguish technical color transforms from creative grading. Probe source color/HDR metadata and prefer restrained changes to already graded footage unless a new look is explicitly intended.
- Slow-motion/interpolation, denoise/sharpen, stabilization, compositing, and heavy effects create artifacts as well as benefits; inspect representative output after application.
- Render success is not playback, sync, subtitle readability, effect timing, or narrative-quality proof.
- Tool/model limits, current prompt syntax, supported resolutions/durations/codecs, installed filter libraries, and pricing are live facts; verify when material.

## Progressive references

- `references/generative-video-direction.md`
- `references/post-production-and-delivery.md`
- `references/scene-and-action-boundary-extraction.md`
- `references/professional-post-production-effects.md`
