# Scene and Action Boundary Extraction

Use this reference when the task is to isolate a specific scene, action, performance, fight, dialogue exchange, reaction, or other bounded moment from longer footage.

## Core distinction

Do not treat these as the same target:

- **scene boundary** — the larger narrative location/time/sequence boundary;
- **action boundary** — the exact requested event inside that scene;
- **contextual edit boundary** — intentionally includes a small lead-in/lead-out for comprehension or pacing.

If the Creator asks for a specific action (for example, one character's fight), default to the action boundary. Do not silently widen it to the whole surrounding scene merely because the wider scene is narratively related.

## Inspection protocol

1. **Define the target event explicitly.** Write a compact semantic rule such as `Ravi begins his actual fight with Balli -> Ravi's fight is clearly over`.
2. **Probe the media first.** Capture duration, start time, frame rate, stream layout, subtitle tracks, chapter metadata, and whether timestamps were reset by a prior trim.
3. **Locate coarsely.** Use sparse timeline frames/contact sheets or known episode metadata to find the candidate region.
4. **Refine densely.** Around candidate start/end points, inspect frames at progressively tighter intervals (for example 2 s -> 0.5 s -> 0.1-0.25 s as needed). For motion-sensitive boundaries, inspect consecutive frames rather than isolated thumbnails only.
5. **Use audio/subtitles as temporal evidence.** Dialogue starts/ends, crowd or music cues, punches/impacts, subtitle entries, and waveform changes can disambiguate visual boundaries.
6. **Verify both sides of each cut.** Confirm the last excluded moment is outside the requested event and the first included moment belongs to it; do the inverse at the end.
7. **Apply context only deliberately.** Add pre/post-roll only when the Creator asks for it or when a tiny amount is necessary for a natural cut. Keep it measured and explainable.
8. **Render and re-check.** Sample the first seconds, several interior moments, and the final seconds of the actual output. Render success alone is insufficient evidence of correct editorial boundaries.

## External scene intelligence

Public web sources can help locate the event before local verification:

- official episode runtimes and chapter/episode metadata;
- recaps/reviews that establish event order;
- subtitle or transcript timing when legitimately available;
- interviews, scene descriptions, fan discussions, clip titles, or other secondary references.

Treat external timestamps as **locator evidence, not canonical cut authority**. Releases can differ by intros, recaps, credits, region, frame rate, ads, edits, or platform packaging.

## Mapping original runtime to a rough cut

When the working file is a rough cut or excerpt, maintain an explicit mapping between original and local time.

For a simple contiguous excerpt beginning at original time `O0`:

`original_time = local_time + O0`

`local_time = original_time - O0`

If the rough cut was made with stream copy, keyframe seeking, timestamp preservation, concat, or multiple source ranges, do not assume the nominal filename offset is exact. Verify an anchor event in both timelines and record the measured offset.

For multi-segment excerpts, maintain a segment table instead of one global offset:

| local range | original range | mapping note |
|---|---|---|
| 00:00-02:10 | 36:00-38:10 | direct contiguous |
| 02:10-03:00 | 41:20-42:10 | jump cut |

When an external source gives an original-episode timestamp, map it into local time, then verify the mapped neighborhood against actual frames/audio/subtitles before editing.

## Evidence hierarchy for exact cuts

Prefer, in order:

1. direct local audiovisual evidence near the requested action boundary;
2. local subtitle/audio timing tied to the same media;
3. verified original-to-local timeline anchors;
4. reliable external timestamped sources;
5. untimestamped recaps or descriptions used only to narrow search;
6. inference from sparse frames.

Sparse contact sheets are useful for localization, but they are not sufficient by themselves for frame-accurate action extraction.
