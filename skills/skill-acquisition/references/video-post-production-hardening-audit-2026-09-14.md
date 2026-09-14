# Video Post-Production Hardening Audit — 2026-09-14

## Trigger

Hands-on extraction/editing of a dramatic fight scene exposed a concrete gap: the initial Video Production skill had good high-level post-production ownership but insufficiently explicit guidance for professional transition discipline, viewer-friendly edit boundaries, effects taste, speed-ramp/interpolation risk, caption placement, color/audio finishing, and reproducible effects-heavy workflows.

The Creator explicitly requested external research and adaptation before further effects testing.

## Sources reviewed

### First-party / professional guidance

- **FFmpeg official filter documentation** — current filtergraph surface including `xfade`, `fade`, `afade`, `acrossfade`, `loudnorm`, `subtitles`/`ass`, `drawtext`, `minterpolate`, compositing, color and audio filters. Used as capability truth, not editorial taste authority.
- **Adobe Premiere current documentation** — transition handling, trim-before-transition/handles, J/L cuts, audio crossfades, automatic ducking, speed/duration and time-remapping concepts.
- **Blackmagic Design DaVinci Resolve certified training** — editing as storytelling; refining rough cuts; audio mixing; transitions/titles; color management; Fairlight sound editing/sweetening; variable-speed effects and delivery.
- **Avid current split-edit guidance** — L-cut/audio-video transition separation and timeline-based continuity concepts.

### Mature open-source/editor ecosystems

- **mifi/lossless-cut** — mature FFmpeg-based lossless workflow, keyframe limitations, waveform/thumbnails, scene/silence detection, segment state and review-after-export discipline. Popularity was treated only as a maturity signal.
- **WyattBlue/auto-editor** — analysis-first automatic editing, audio/motion predicates, and configurable pre/post margins to prevent clipped-feeling automatic cuts.
- **remotion-dev/skills + Remotion docs** — first-party Agent Skills, transition timing/presentation separation, captions, programmatic motion and deterministic render workflows.
- **Zulko/moviepy** — scriptable cuts, concatenation, titles, compositing and preview-oriented programmatic editing.
- **OpenCut-app/OpenCut** — modern open-source NLE direction with plugin-first/headless/automation goals; used as ecosystem evidence rather than copied architecture.
- **kajisho5/ffmpeg-skill** — agent-oriented probe→edit→check→verify discipline; typed operations, proxy/contact-sheet analysis, captions, loudness, color, overlays, declarative project render, delivery checks and structured failure semantics. MIT-licensed upstream was already audited; DEDAL adapts patterns rather than importing its tool layer wholesale.

## Durable findings

1. **Edit before effect.** A readable cut, pacing and audio continuity should exist before decoration.
2. **Straight cut is the default.** Transitions need a job; trim first, transition second.
3. **Audio continuity is editorial.** J/L cuts, crossfades, ducking and ambience continuity can make an edit feel more professional than adding visual effects.
4. **Effects need scarcity.** Fight/action emphasis works better when zoom/shake/flash/blur/speed effects are reserved for a few high-value beats.
5. **Time remapping is not free.** Low-frame-rate slow motion and interpolation can create visible artifacts; output must be inspected.
6. **Captions belong after geometry.** Reframe/crop before final caption placement; verify safe areas, glyph coverage and shaping.
7. **Audio needs measurement and listening.** Loudness normalization should consider integrated loudness and true peak; avoid amplifying noise; preserve channel layout intentionally.
8. **Color needs source awareness.** Separate technical HDR/color transforms from creative grading and avoid gratuitous regrading of already-finished footage.
9. **Lossless versus exact is a real tradeoff.** Keyframe-bound stream copy is not equivalent to frame-accurate editing.
10. **Analysis proxies and declarative edit state improve agent workflows.** Use cheap inspection surfaces while preserving source masters; make multi-step edits reproducible when iteration is expected.
11. **Verification must cover the picture and sound actually delivered.** Exit code/encode completion is insufficient.
12. **Tasteful and stylized modes should be distinct.** Default dramatic/cinematic work to restraint; only enable dense social/action effects when requested or clearly appropriate.

## Rejected / bounded ideas

- Do not create separate top-level skills for FFmpeg, Remotion, captions, audio, color, transitions or effects; Video Production already owns the temporal post-production outcome.
- Do not copy entire external CLI/tool suites into DEDAL Core merely because they are popular.
- Do not use stars or virality as quality/security proof.
- Do not make social-media animated captions, speed ramps, LUTs or flashy transitions default behavior.
- Do not freeze platform loudness/export values in the always-loaded core when they are delivery-specific and can change.

## Changes made

- Added `skills/video-production/references/professional-post-production-effects.md`.
- Hardened `skills/video-production/SKILL.md` with concise durable rules for effect discipline, transition/audio continuity, captions, color/audio finishing and artifact verification.
- Preserved deeper operational detail under progressive disclosure rather than bloating the entrypoint.

## Decision

**TUNE/MERGE — no new top-level skill.**

The observed gap belongs cleanly to the existing Video Production faculty. External professional guidance and mature repositories materially improve its post-production depth, but do not justify another capability owner.
