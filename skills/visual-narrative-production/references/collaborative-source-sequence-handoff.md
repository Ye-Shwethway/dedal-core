# Collaborative Source-Sequence Handoff

## Goal
A source-image sequence is ready for a downstream motion agent only when it is temporally usable, not merely visually attractive.

## Production manifest
For every downstream-video production, persist an ordered manifest containing at least:
- `frame_id` and file path;
- phase and arc;
- camera angle/height/distance;
- character/body state;
- prop/load state;
- delta to the next frame;
- intended motion;
- format lock and continuity locks.

## Adjacent-pair gate
For each consecutive pair, compare major dimensions:
- body position;
- body orientation;
- support/contact mode;
- prop/load state;
- camera angle;
- framing scale.

If several major dimensions change at once, classify the pair `needs_bridge` and insert intermediate states before handoff. A silent camera-angle jump is a contract failure.

## `images_ready` admission
`images_ready` means all required frames are present and these checks passed:
- identity continuity;
- physical/biomechanical continuity;
- prop/load continuity;
- pairwise reachability;
- video-readiness.

A frame count is never the acceptance criterion. Temporal density remains adaptive.


## Progressive handoff cadence
When the production is continuity-sensitive, do not wait for the entire source sequence to finish before involving the downstream specialist.

1. Create the production manifest skeleton and stable set plan.
2. Emit `production_started` with the planned sets/arcs/phases.
3. Generate and validate one set at a time.
4. Emit `images_ready(scope=set)` after that set passes identity, physical, prop/load, pairwise-reachability, and video-readiness checks.
5. Incorporate early frame-pair feedback before compounding later sets when that feedback affects downstream planning.
6. After every planned set is validated, emit `images_ready(scope=production)`.

A set-level handoff is an intermediate review boundary, not production completion. The production manifest remains authoritative and its version must be bumped whenever the ordered source state changes. Optional pilot takes are allowed only as bounded risk probes; they do not bypass source validation or final production-scope admission.

## Repair loop
When the downstream agent reports a failing frame pair, preserve accepted frames and regenerate only the missing bridge states. Increment the manifest version and revalidate the modified neighborhood before re-handoff.

## Durable/private boundary
Public Core stores this generic contract. Live shared-folder paths, private production IDs, private characters, agent deployment details, and access-specific pointers live in the private overlay or connected workspace.
