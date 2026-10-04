# Bridge Contracts

## Story Weaver -> Generative Video Direction

Use when temporal planning is needed directly from accepted story truth, especially before keyframes exist.

```yaml
scene_id:
beat_id:
narrative_function:
characters_and_current_state:
observable_action:
relationship_emotional_state:
critical_props_and_environment:
required_start_state:
required_end_state:
what_must_not_change:
what_may_remain_ambiguous:
```

This is story truth, not camera/model syntax.

## Visual Narrative Production -> Generative Video Direction

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
allowed_visual_change:
locked_visual_invariants:
known_visual_debt:
source_sequence_role:
ordered_bridge_anchors:
pairwise_reachability_notes:
```

GVD owns temporal motion/camera decisions from this point forward.

## GVD -> Visual Narrative Production return request

Use when motion feasibility/control requires a missing or corrected visual state.

```yaml
request_type: keyframe_or_reference
shot_id:
needed_role:
required_state:
geometry_or_pose_requirement:
locked_invariants:
allowed_change:
reason:
requested_bridge_density:
adjacent_state_constraints:
```

## GVD -> Video Post-Production

```yaml
shot_id:
accepted_take_ids:
preferred_take:
source_files_or_refs:
intended_in_point_state:
intended_out_point_state:
cut_boundary_notes:
camera_motion_tail:
audio_tail_or_dialogue_boundary:
continuity_notes:
known_debt:
optional_alternates:
```

Post-Production owns the final editorial choice and timeline integration.
