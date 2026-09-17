# Post-production and Delivery

Use this reference for FFmpeg/ffprobe, Remotion/programmatic motion, subtitles, audio finishing, and export decisions.

## Probe first

Before editing real media, inspect format, duration, frame rate, dimensions, pixel format, audio streams, sample rate/channel layout, subtitle streams, and rotation/color metadata. Do not guess source properties from filename or player appearance.

## Editing principles

- Prefer lossless/stream-copy operations only when keyframe precision and container/codec compatibility make them safe.
- Re-encode deliberately for exact trims, filter graphs, scaling, stabilization, color work, speed changes, compositing, burned captions, or incompatible joins.
- Separate master/intermediate quality from delivery compression.
- Preserve aspect ratio intentionally; crop/reframe with subject/safe-area awareness rather than blind center-crop.
- Use J/L cuts, audio overlap, beat timing, or motivated transitions when they serve pacing; transitions are not a default requirement.
- Normalize/dialogue-process with a target appropriate to the platform; clipping-free encode success is not the same as a balanced mix.
- For subtitles, verify timing, line breaks, readable duration, safe margins, contrast and multilingual font/render behavior.

## Programmatic motion

Remotion-style composition is useful when timing, typography, charts, captions, UI demos, explainers, branded motion, or reproducibility matter. Treat React/motion code as an execution surface beneath Video Production. Preview representative key frames and final motion, not just source code.

## Verification

After render/export:
1. probe output metadata;
2. verify expected duration/dimensions/streams;
3. inspect beginning, transitions/cuts, subtitle-heavy moments and ending;
4. check sync and audio peaks/loudness evidence where available;
5. confirm intended playback/container compatibility;
6. preserve the command/project/source needed to reproduce material edits when valuable.

## Upstream patterns reviewed

`kajisho5/ffmpeg-skill@a6232b95f595aa35fa8cea0d055f0163baa908e9` (MIT) provides a mature probe → edit → check → verify discipline and broad FFmpeg operations including captions, loudness, sync, HDR/SDR, multicam and project rendering.

`remotion-dev/skills@bd566b65d521b40fe92e1f26766e82de9e291693` is an actively maintained first-party Remotion skill corpus covering creation, markup, render, captions, multimedia, maps, interactivity and docs lookup. Adapt methodology only; use current upstream/tool documentation for API details.

## Creator Drive media lifecycle

When the Creator uses Google Drive as the handoff surface for YouTube clips, keep production state explicit:

`rough/source upload -> sandbox/local edit -> Edited Videos -> YouTube publish + authoritative verification -> Uploaded YT Videos`

- `Edited Videos` is the ready-for-publishing staging area for approved masters.
- Do not move a master out of `Edited Videos` merely because an upload was attempted.
- Move it to `Uploaded YT Videos` only after YouTube Publishing verifies the intended remote video/channel/visibility state.
- A failed, partial, duplicate, blocked, or otherwise unverified upload stays in `Edited Videos` until the publishing state is resolved.
- Preserve the same Drive file when practical; prefer a true move/re-parent over copy-plus-delete so identity and revision history stay stable.
- Drive folder names are operational labels, not authority by themselves; verify exact folder/file IDs before consequential moves.

