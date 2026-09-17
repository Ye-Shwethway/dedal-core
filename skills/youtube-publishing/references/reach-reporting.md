# YouTube Reach Reporting Contract

Use this reference for scheduled YouTube Reporting API reach payloads consumed by DEDAL SEO/Publishing measurement workflows.

## Canonical transport

1. List generated reports for the existing reach job.
2. Select the report whose `[startTime, endTime)` window is relevant.
3. Download through the bounded `youtube_reporting_api` operation `reports.download`; do not expose or hand off the vendor download URL as the normal workflow.
4. Reject an analysis that depends on content beyond the bounded payload when `truncated: true`; use another bounded extraction path before drawing conclusions.

The live `channel_reach_basic_a1` payload was validated with this header:

`date,channel_id,video_id,video_thumbnail_impressions,video_thumbnail_impressions_ctr`

Treat the two reach metrics as:
- `video_thumbnail_impressions`: registered thumbnail impressions for that row/window;
- `video_thumbnail_impressions_ctr`: click-through rate for those registered impressions.

Do not reinterpret CTR `0` as zero video views. Reach impressions/CTR and general traffic/view metrics are different evidence surfaces.

## Human-readable reporting

Raw Reporting API rows identify videos by `video_id`. User-facing DEDAL reports MUST resolve each relevant `video_id` to its current YouTube title before presentation whenever the title is readable. Present the video title as the primary label and retain the video ID alongside it for traceability. If a title cannot be resolved, explicitly label it `title unavailable` rather than guessing.

Preferred enrichment path:

`reach CSV video_id -> bounded YouTube video lookup -> video title + video_id -> impressions + CTR`

Do not silently reuse stale remembered titles when a live lookup is available. For rows from deleted/unavailable videos, preserve the ID and the measurement row.

## Window and availability semantics

Scheduled Reporting API files can arrive several days after their measured window. A later-generated historical file does not retroactively mean the data was available at an earlier checkpoint. At T0/24h/3d/7d/28d measurement time, use the measurement contract's availability states (`observed_zero`, `observed_nonzero`, `unavailable`, `not_processed_yet`, `suppressed_or_incomplete`, `error`). Backfill a later report into the matching measured window while preserving when the report actually became available.

For a prospective experiment, only use a report row when its measured date/window actually includes that video's post-publish period. Historical pre-publication reports are pipeline validation, not experiment evidence for that video.
