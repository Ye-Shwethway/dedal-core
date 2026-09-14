# Professional Post-Production and Effects

Use this reference when the task goes beyond trimming into transitions, pacing, speed changes, subtitles, graphics, compositing, color, audio finishing, or stylistic effects.

## Editorial principle

Effects are subordinate to story clarity. Build a readable edit first, then add the smallest treatment that improves orientation, emphasis, rhythm, continuity, or delivery.

A useful default hierarchy is:

`cut/trim -> pacing -> audio continuity -> transitions -> reframing -> captions/graphics -> color -> sound sweetening -> selective effects -> delivery`

Do not use every available effect merely because the execution surface supports it.

## Transition discipline

- A straight cut is the default transition unless another transition has a clear editorial job.
- Trim first, transition second. Transitions require usable handles on both sides and should not conceal a weak cut.
- Prefer short, motivated fades/crossfades for standalone scene entry/exit or tonal changes.
- Use J-cuts and L-cuts when audio should lead or trail picture to preserve continuity, anticipation, or conversational flow.
- Stylized wipes, zooms, flashes, film-burns, blur transitions, and similar effects are accents, not punctuation for every cut.
- Pair visual transitions with appropriate audio continuity/crossfades when abrupt sound changes would expose the edit.

## Pacing and action emphasis

- Distinguish ordinary playback from intentional time remapping.
- For speed ramps, define the narrative purpose first: anticipation, impact emphasis, compression of dead time, or transition into/out of slow motion.
- Smooth the speed change rather than jumping arbitrarily between rates unless a hard temporal snap is the intended style.
- Slow motion from low-frame-rate footage can judder or require motion interpolation; interpolation can create warping/ghosting and must be visually checked.
- Freeze frames, micro-pauses, punch-ins, flashes, camera shake, blur, and impact emphasis should be sparse and event-driven.
- For fight/action edits, reserve strongest effects for a small number of high-value impacts or turns. Repetition rapidly makes the edit feel synthetic.
- Judge stylization against a clean baseline. If the effect cannot be tied to a clear gain in rhythm, orientation, emphasis, comprehension, or delivery, it is decoration rather than improvement.

## Captions and subtitles

- Choose soft subtitles (muxed/toggleable) when editability, accessibility, language switching, or archival flexibility matters.
- Choose hard-coded subtitles when the delivery surface requires guaranteed rendering or when captions are part of the visual design.
- Reframe/crop before final caption placement; otherwise text can move outside safe areas.
- Verify font glyph coverage for the actual language. Complex scripts require a capable shaping/rendering path.
- Keep line length, reading speed, contrast, outline/background, and lower-safe-area placement readable on the target device.
- Animated/word-highlight captions are a style choice; do not default to social-media caption animation for cinematic or dramatic material.
- Separate subtitle **render quality** from subtitle **text truth**. Readable placement, contrast, and typography do not validate wording or timing.
- If subtitle text comes from web transcripts, recaps, inferred dialogue, OCR, or a different release, treat it as provisional until reconciled with local audiovisual evidence or another trustworthy source tied to the actual cut.

## Audio finishing

Treat audio as a first-class editorial layer, not an afterthought.

- Measure before normalizing. Avoid lifting room tone/noise as if it were content.
- Use EBU R128/loudness targets appropriate to the delivery surface, and verify true peak as well as integrated loudness.
- Prefer two-pass/file-aware loudness normalization when the workflow permits and exact delivery targets matter.
- Use compression/limiting/EQ/dialogue enhancement only to solve a real problem or achieve a defined aesthetic.
- Use music ducking/sidechain behavior when dialogue or critical effects need priority.
- Crossfade adjacent audio when a hard cut creates clicks, ambience discontinuity, or an unnatural scene edge.
- Preserve channel layout deliberately. Do not silently collapse 5.1 to stereo unless delivery requires it.
- Compare candidate loudness/true-peak behavior with the baseline. A louder result is not automatically a better result; new clipping or reduced headroom is a regression.

## Color and image finishing

- Probe color metadata before correction. Distinguish creative grading from technical HDR/SDR/color-space conversion.
- Technical transforms come before creative look development.
- Prefer subtle corrections to already graded source footage unless the Creator explicitly wants a new look.
- Validate exposure, contrast, saturation, white balance, shadows/highlights, clipping, and skin/subject integrity after any grade.
- LUTs are transforms/look assets, not magic quality enhancers; confirm source color assumptions and control intensity.
- Denoise before sharpening when both are necessary. Excess sharpening, denoise, grain, vignette, glow, or clarity effects should be treated as visible stylistic choices.

## Reframing and compositing

- Reframing from wide to vertical can discard most horizontal context. Inspect subject motion and safe areas rather than blind center-cropping.
- Use crop/pan/pad/blur-background strategies according to the content; preserve composition when possible.
- Overlay ordering matters: perform geometry-changing operations before final captions/lower-thirds whenever possible.
- Picture-in-picture, logos, watermarks, lower-thirds, chroma key, masks, and split screens should be designed around hierarchy and occlusion, not merely technically composited.

## FFmpeg execution surface

Useful official FFmpeg capabilities include:

- `fade`, `afade`, `xfade`, `acrossfade` for transitions;
- `trim`, `atrim`, `setpts`, `asetpts`, `atempo` for temporal edits;
- `minterpolate` for motion-interpolated frame-rate conversion/slow-motion support, with artifact risk;
- `subtitles`/`ass` (libass) and `drawtext` for burned text;
- `overlay`, `chromakey`, `blend`, masks/crops/scales/pads for compositing;
- `eq`, `curves`, `colorbalance`, `colorlevels`, `exposure`, `zscale`, LUT filters and related tools for image/color work;
- `loudnorm`, `acompressor`, `alimiter`, `agate`, `equalizer`, `dialoguenhance`, `amix`, `sidechaincompress` and related filters for audio finishing;
- `silencedetect`, black/scene detection, waveform/contact-sheet analysis and metadata probes for edit intelligence.

Filter availability depends on the installed FFmpeg build. Probe capabilities before relying on optional libraries such as libass or stabilization components.

## Programmatic motion lane

Use Remotion-style programmatic composition when repeatability, precise typography, animated captions, data/UI graphics, branded templates, or complex scene transitions matter more than raw-footage NLE ergonomics.

Keep programmatic animation deterministic and previewable. Treat transition timing and presentation separately so timing can change without rewriting the visual effect. Preserve a clean distinction between content, timing, style, and render settings.

## Automation patterns worth keeping

From mature automation/editing tools, preserve these patterns:

- **Analysis before mutation:** probe media, detect silence/motion/scenes, inspect contact sheets/waveforms, then decide.
- **Measured margins:** automatic cut systems should retain configurable pre/post margins so edits do not feel clipped.
- **Lossless versus exact-cut truth:** stream-copy is fast and quality-preserving but keyframe-bound; exact boundaries usually require re-encoding or a verified smart-cut strategy.
- **Proxy lane:** use low-cost proxies/contact sheets for analysis while preserving original media for final render.
- **Declarative edit state:** for multi-step/repeatable work, represent clips, transitions, captions, overlays, music, loudness, and export settings explicitly so edits can be reproduced and revised.
- **Typed operations over arbitrary filter strings:** where a reusable automation layer exists, expose bounded parameters with validation rather than unconstrained command injection.
- **Output verification:** probe the written file, inspect representative frames, and verify duration/streams/sync/loudness/delivery instead of equating process exit code with editorial success.
- **Baseline A/B gate:** compare a candidate with the nearest clean/proven version before handoff. Improvements should be named and regressions should be surfaced rather than hidden by overall enthusiasm.

## Tasteful default versus stylized mode

### Tasteful default
Use for cinematic/dramatic footage unless the Creator asks otherwise:
- straight cuts or subtle fades;
- gentle audio crossfades;
- restrained grade/correction;
- modest loudness/dynamics work;
- readable conventional subtitles;
- only a few event-driven emphasis effects.

### Stylized mode
Use only when the requested aesthetic justifies it:
- speed ramps;
- punch-in zooms;
- shake/flash/blur impact accents;
- animated or word-highlight captions;
- bold transition families;
- visible LUT/look development;
- graphic overlays and motion-design elements.

Never let stylized mode obscure action readability, dialogue, subject identity, or narrative continuity.

## Self A/B review before handoff

When a prior clean/proven render exists, treat it as the baseline and compare the new candidate across both editorial and technical axes.

### Editorial axes

- **Orientation:** does the viewer understand where/when the clip begins?
- **Action readability:** are choreography, gestures, dialogue, and critical visual information still easy to follow?
- **Rhythm/emphasis:** did transitions, retiming, effects, or audio work improve pacing or only add novelty?
- **Entry/exit:** do the opening and ending feel intentional and resolved?
- **Subtitle quality:** are captions readable, non-obstructive, correctly timed, and textually trustworthy?
- **Attention economy:** do effects support the subject, or steal attention from it?

### Technical axes

- duration and frame-rate parity unless a deliberate change was requested;
- dimensions/aspect ratio and color metadata;
- audio stream count/channel layout;
- integrated loudness and true peak;
- subtitle presence/mode and safe-area rendering;
- compression/bitrate/file-size changes with visible quality checks;
- A/V sync and representative playback;
- timestamp health: unexpected non-monotonic DTS/PTS warnings, discontinuities, or muxing anomalies are regressions even when playback appears successful.

### Decision labels

Use one of these conclusions internally before handoff:

- **PROMOTE:** candidate is a net improvement with no material regression.
- **PROMOTE WITH CAVEAT:** candidate improves the viewing experience but has a known non-blocking issue that must be disclosed.
- **HOLD BASELINE:** candidate adds style or features but introduces a meaningful editorial/technical regression; keep the clean version canonical.
- **REJECT:** candidate fails intent, readability, integrity, or delivery requirements.

Do not call an effects-heavy version a production master merely because it is more elaborate than the baseline.

## Acceptance checks

Before calling an effects-heavy render finished, verify:

1. The edit remains understandable without the effects.
2. No transition/effect starts or ends on an accidental frame.
3. Speed changes do not create unacceptable interpolation artifacts or audio pitch/timing errors.
4. Captions remain readable and inside safe areas through reframes/transitions, and their wording/timing has an identified confidence level/source.
5. Audio has no clipping, abrupt ambience jumps, or dialogue masking introduced by the edit.
6. Color transforms did not create illegal/clipped or obviously damaged imagery.
7. Composites/graphics do not cover critical content.
8. The first and last beats feel intentional rather than abruptly truncated.
9. Final output metadata, duration, streams and delivery format match intent.
10. Representative playback/frame/audio evidence has been inspected after render.
11. Mux/timestamp diagnostics show no unexplained DTS/PTS regressions.
12. A baseline A/B review has identified both gains and losses before handoff.

## Source influences

This reference synthesizes patterns from current FFmpeg filter documentation; Adobe Premiere guidance on transitions, J/L cuts, audio crossfades/ducking and time remapping; Blackmagic Design DaVinci Resolve certified editing/color/Fairlight training; Avid split-edit guidance; mature open-source tools including LosslessCut, Auto-Editor, MoviePy, OpenCut and Remotion; and the audited `kajisho5/ffmpeg-skill`. It adapts methodology rather than vendoring third-party implementation or provider-specific command surfaces.
