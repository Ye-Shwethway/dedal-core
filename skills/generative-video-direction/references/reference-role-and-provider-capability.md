# Reference Roles and Provider Capability Resolution

## Reference Role Map

Assign each input an explicit job. Common roles:

- `identity_anchor` — face/body/character identity;
- `environment_anchor` — place/material/geography identity;
- `start_frame` — authoritative first visual state;
- `end_frame` — desired terminal visual state;
- `pose_geometry_reference` — spatial/body relation only;
- `motion_reference` — subject/object movement pattern;
- `camera_motion_reference` — camera path/tempo;
- `style_reference` — visual treatment only;
- `audio_reference` — voice/music/ambience/rhythm when supported.

One asset may serve several roles only when those roles do not conflict. Do not let a motion/style reference silently override canonical identity or place.

## Missing-reference return path

If reliable motion generation depends on a visual state that does not yet exist, issue a structured request to Visual Narrative Production:

```yaml
request_type: keyframe_or_reference
shot_id:
needed_role: start_frame | end_frame | pose_geometry_reference | environment_anchor | other
required_state:
must_preserve:
may_vary:
reason:
```

Do not invent a weak text-only substitute and then claim the shot is locked.

## Provider capability resolution

Provider/model capabilities change quickly. Before compiling a contract, verify only the controls material to the shot, for example:

- text-to-video / image-to-video;
- first+last frame;
- number/types of visual references;
- reference video / motion or camera reference;
- audio/dialogue/reference audio;
- duration/aspect/resolution/FPS;
- multi-shot or extension behavior;
- editing/inpainting/replacement controls;
- negative prompts or other syntax constraints.

Record `supported | unsupported | unknown | not_checked` with source/date/version when material. `unknown` is valid; guessing is not.
