# Optional structured creative handoff (advisory)

For complex creative handoffs only, an owner can serialize one of three documents:

- `scene_shots`: nonblank `scene_id`, `beat_id`, optional `canon_subject_ids`, and 1–4 `shots` each with `id`, `subject_ids`, `action_phase`, `camera_axis`, optional `axis_crossing_justification`, and `contact_edges`. A contact may claim `PASS` only when observability is `visible`.
- `edit_decisions`: `assets` keyed by identifier with finite positive `duration_s`, `clips` carrying `asset_id`, `in_s`, `out_s`, `timeline_start_s`. Source interval must be within asset duration.
- `evidence`: `assertions` containing a status `PASS|FAIL|UNKNOWN` and `evidence_ref` when PASS.

The fields are lightweight constraints and should not force ordinary short-form creative conversations into verbose structures. The owning skill still performs preflight, actual image/footage inspection, and Creator review. `PASS` indicates structural consistency only. The optional tool is invoked on demand and is not part of session boot.

Examples: `python scripts/validate_creative_handoff.py scene.json`; never confuse a valid example with production acceptance. Current validation rejects invalid identifiers, duplicated subject IDs, unmotivated left/right axis jumps, unobservable contact PASS, missing Creator acceptance evidence, out-of-bounds edit time, and unevidenced PASS assertions.
