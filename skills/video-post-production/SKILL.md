---
name: video-post-production
description: Select, assemble, edit, subtitle, mix, finish, verify, and deliver existing video/audio media or generated takes. Use for footage editing, rough cuts, pacing, reframing, retiming, captions, audio, effects, color, encoding, and final media delivery; not for generative-video shot prompting or model direction.
---

# Video Post-Production

Own the **edit-and-finish layer after usable moving-image media exists**. Turn source footage, generated takes, still-derived clips, audio, captions, graphics, and approved shot selections into a coherent deliverable.

`video-production` and `video-editing` are backward-compatible routing aliases for this skill. They are not separate faculties.

## Use when

- selecting among existing takes or source segments;
- extracting a bounded scene/action/performance from longer footage;
- assembling clips into a narrative, montage, reel, short, promo, or scene;
- trimming, joining, reframing, stabilizing, retiming, transcoding, grading, captioning, mixing, normalizing, adding restrained transitions/effects, or exporting;
- using FFmpeg, Remotion, an NLE, or another editing runtime as the execution surface;
- finishing generated-video takes **after** Generative Video Direction has produced/accepted them.

## Do not use as the primary owner when

- the task is to turn story/visual state into model-feasible generative-video shots, motion prompts, camera choreography, reference-role plans, or provider-specific generation contracts — route to `generative-video-direction`;
- the task is to author still/keyframe identity, environment, pose, or scene anchors — route to `visual-narrative-production`;
- the task is fiction canon, causality, beats, dialogue, or character motivation — route to `story-weaver`.

## Ownership boundary

Video Post-Production owns source/take inspection, editorial boundary truth, take selection for the cut, timeline structure, pacing, continuity at edits, captions/subtitles, audio finishing, motion graphics/effects, color/technical finishing, encoding, delivery, and post-render verification.

It does **not** own generative-video motion direction or provider prompt compilation (`generative-video-direction`), canonical still/reference production (`visual-narrative-production`), story canon (`story-weaver`), factual research, independent QA verdicts, or provider/editor execution surfaces themselves.

## Workflow

1. **Frame the deliverable.** Audience, purpose, duration target/range, aspect ratio, platform, language, source assets, master/proxy status, and quality bar.
2. **Probe source truth.** Inspect actual duration, streams, resolution, frame rate, timestamps, audio/subtitle tracks, and source quality before cutting.
3. **Choose the editing method.** Explicitly select **Simple / Narrative Edit** or **Fan / Visual-Montage Edit** when those modes fit; otherwise state the editorial thesis and constraints.
4. **Map coverage before a serious cut.** For non-trivial edits, identify target-subject coverage, secondary coverage, continuity bridges, strongest moments, crop risk, audio dependency, and likely entry/ending beats.
5. **Build the structural rough.** Validate selection, order, timing, framing/crop, continuity, target coverage, entry/ending, and audio intent before decoration.
6. **Refine boundaries.** Distinguish source scene boundary, requested action boundary, contextual edit boundary, and final editorial boundary using dense local audiovisual evidence rather than sparse thumbnails alone.
7. **Polish selectively.** Reframe, stabilize, retime, grade/tone-map, mix, caption, and add transitions/effects only when they improve the accepted structure.
8. **Render and inspect.** Render success is not playback or editorial proof. Check duration, dimensions, streams, sync, caption readability, clipping/loudness, crop through motion, visual continuity, effect boundaries, timestamp health, and representative playback.
9. **Compare against a baseline.** Identify improvements and regressions relative to the source or prior clean/proven cut.
10. **Deliver intentionally.** Preserve masters/intermediates when useful; label proxies clearly; provide platform-appropriate exports and verified review assets.

## Durable rules

- A generated clip is a **take**, not automatically an approved edit.
- Structural acceptance precedes effects polish.
- Probe before edit; never infer precise cut truth from metadata or external timestamps alone.
- For extraction, distinguish scene, action, contextual, and editorial boundaries.
- External recaps/transcripts/timestamps are locator evidence until reconciled with the actual media.
- Maintain original-to-local timeline mapping after rough cuts, keyframe seeking, concat, or multi-range extraction.
- A straight cut is the default. Every transition/effect needs an editorial job.
- Editing mode is explicit: **Simple / Narrative Edit** preserves source meaning/chronology; **Fan / Visual-Montage Edit** prioritizes a declared subject/motif and rhythm.
- In target-centric edits, inspect the whole bounded source segment before the first rough; do not rely on Creator feedback to discover obvious coverage gaps.
- Duration is an editorial consequence, not an arbitrary habit.
- Low-resolution proxies may support structural review but may not silently become the production master when a better source exists.
- Music-led edits require audible rhythmic anchors; texture/hiss is not a substitute for a beat.
- End intentionally: hold, cut, audio tail, dip, or fade must be chosen and verified.
- Reframe/geometry usually precedes final caption/graphic placement.
- Subtitle timing, wording, shaping, safe areas, language, and confidence/source all matter.
- For subtitle sync, check early/middle/late anchors; one arithmetic offset is not enough when drift exists.
- AI remaster/enhancement requires representative-segment validation and motion/identity/flicker/detail inspection before full acceptance.
- Full-frame white flashes/strobes are not a default transition system.

## Progressive references

- `references/editing-modes.md`
- `references/scene-and-action-boundary-extraction.md`
- `references/post-production-and-delivery.md`
- `references/professional-post-production-effects.md`
- `references/copyright-reuse-risk-aware-editing.md`

## Pairing

Pair with `generative-video-direction` when accepted generated takes need editing/assembly, `visual-narrative-production` when high-quality still/keyframe/thumbnail assets are needed, `story-weaver` for narrative truth, `writing-editorial` for substantial caption/script language, `research` for factual claims, and `quality-engineering` for independent readiness when distinct from self-review.
