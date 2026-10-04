# Visual-to-Motion Handoff

Visual Narrative Production owns the accepted still-state truth. When handing a shot/beat to Generative Video Direction, expose visual authority by role rather than flattening it into one prose prompt.

```yaml
shot_or_beat_id:
accepted_visual_anchors:
start_frame:
optional_end_frame:
reference_roles:
visual_continuity_state:
scene_geometry:
object_state:
performance_state:
composition_camera_state:
lighting_style_state:
locked_visual_invariants:
allowed_visual_change:
known_visual_debt:
source_sequence_role:
ordered_bridge_anchors:
pairwise_reachability_notes:
```

If Generative Video Direction determines that a missing end frame, pose/geometry reference, or corrected start state would materially improve control, it may return a `keyframe_or_reference` request. VNP should create/correct that still while preserving accepted anchors; it does not take over temporal motion/camera direction.


## Video-first bridge production

When accepted stills will drive generated video, optimize transitions for temporal reachability rather than still-image novelty. If an arc-to-arc handoff changes stance/support, prop possession/load, body facing, and camera family, create enough intermediate full-frame anchors that adjacent states remain reachable. GVD decides the temporal density target; VNP owns producing/repairing the requested visual states.
