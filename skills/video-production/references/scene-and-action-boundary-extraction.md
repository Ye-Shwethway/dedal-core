# Scene and Action Boundary Extraction

Use this reference when the task is to isolate a specific scene, action, performance, fight, dialogue exchange, reaction, or other bounded moment from longer footage.

## Core distinction

Do not treat these as the same target:

- **scene boundary** — the larger narrative location/time/sequence boundary;
- **action boundary** — the exact requested event inside that scene;
- **contextual edit boundary** — intentionally includes a small lead-in/lead-out for comprehension or pacing;
- **editorial boundary** — the cut point that best preserves viewer orientation, dramatic entry, and resolution, even when it extends slightly beyond the literal first/last action frame.

If the Creator asks for a specific action (for example, one character's fight), do not silently widen it to the whole surrounding scene merely because the wider scene is narratively related. But do not default to a mechanically literal first-hit/last-hit cut either when that would make the clip feel abrupt or confusing. The preferred target is usually the smallest self-contained editorial unit that preserves the requested action and just enough setup/resolution to make it feel intentional.

## Editorial unit model

For many action extractions, think in three beats:

1. **entry beat** — the shortest moment that orients the viewer and establishes that the action is about to happen;
2. **action beat** — the requested event itself;
3. **resolution beat** — the shortest aftermath that lets the action land before the next unrelated plot beat begins.

Examples of useful entry beats include entering the ring, approaching the opponent, removing a shirt/jacket before a fight, a referee/organizer cue, or a final pre-action look. Useful resolution beats include a victory reaction, opponent down, crowd response, a character catching their breath, or reclaiming clothing immediately after the action.

Do not keep unrelated setup, investigation, travel, exposition, or the next plot event merely to add context. The goal is **orientation without bloat** and **resolution without drift**.

## Inspection protocol

1. **Define the target event explicitly.** Write a compact semantic rule such as `Ravi enters/prepares for his fight -> the fight completes -> immediate victory beat resolves`.
2. **Define the intended editorial unit.** Decide whether the request needs literal action-only, contextual action, or a standalone mini-scene. When the user says “the fight scene” and wants something pleasant to watch, prefer a compact standalone mini-scene unless they explicitly request frame-tight action-only extraction.
3. **Probe the media first.** Capture duration, start time, frame rate, stream layout, subtitle tracks, chapter metadata, and whether timestamps were reset by a prior trim.
4. **Locate coarsely.** Use sparse timeline frames/contact sheets or known episode metadata to find the candidate region.
5. **Refine densely.** Around candidate start/end points, inspect frames at progressively tighter intervals (for example 2 s -> 0.5 s -> 0.1-0.25 s as needed). For motion-sensitive boundaries, inspect consecutive frames rather than isolated thumbnails only.
6. **Use audio/subtitles as temporal evidence.** Dialogue starts/ends, crowd or music cues, punches/impacts, subtitle entries, and waveform changes can disambiguate visual boundaries and reveal natural editorial beats.
7. **Verify both sides of each cut.** Confirm the last excluded moment is outside the intended editorial unit and the first included moment belongs to it; do the inverse at the end.
8. **Test viewer orientation at the start.** Ask: if the clip starts here with no prior context, does a viewer understand what is happening within a few seconds? If not, move the start earlier to the nearest compact entry beat.
9. **Test emotional completion at the end.** Ask: does the final action have time to land before the cut? If the ending feels snapped off, extend to the nearest compact resolution beat, but stop before the next unrelated plot event.
10. **Render and re-check.** Review the first 5-10 seconds, the action transition, and the final 5-10 seconds of the actual output. Render success alone is insufficient evidence of correct editorial boundaries.

## Avoid the two common failure modes

### Over-wide extraction

Symptoms:
- long unrelated setup before the requested event;
- venue/investigation/exposition included merely because it occurs in the same scene;
- unrelated aftermath or next plot beat retained.

Correction: shrink toward the nearest meaningful entry/action/resolution beats.

### Over-tight extraction

Symptoms:
- clip opens after action has already begun;
- first frame is a punch, impact, or mid-motion pose with no orientation;
- ending cuts immediately after the last hit without a reaction or resolution;
- viewer feels momentarily confused even though the literal action is technically present.

Correction: add only the smallest missing entry or resolution beat. Editorial precision is not the same as minimizing duration.

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

1. direct local audiovisual evidence near the requested action/editorial boundary;
2. local subtitle/audio timing tied to the same media;
3. verified original-to-local timeline anchors;
4. reliable external timestamped sources;
5. untimestamped recaps or descriptions used only to narrow search;
6. inference from sparse frames.

Sparse contact sheets are useful for localization, but they are not sufficient by themselves for frame-accurate or viewer-friendly extraction.

## Acceptance test for a standalone action clip

Before calling the extraction ready, verify all four:

- **Orientation:** the opening gives enough information for a viewer to understand the impending action;
- **Completeness:** the requested action is fully present;
- **Resolution:** the ending has a brief natural landing rather than an abrupt stop;
- **Containment:** no materially unrelated preceding or following plot beat remains.

A technically exact action boundary can still fail this test. Prefer the smallest cut that passes all four.