# Generated Take QA and Targeted Repair

A completed generation job is not evidence of a usable take. Inspect the moving output across time.

## Take QA axes

- start-frame/reference match;
- identity/physique/grooming stability;
- subject action and phase order;
- anatomy/joint/contact/load plausibility;
- prop/object count, morphology, possession and trajectory;
- environment continuity and unintended warping;
- camera path, axis, framing and focus behavior;
- pacing/speed and temporal smoothness;
- end-state match;
- dialogue/lip-sync/audio timing when applicable;
- flicker, morphing, extra objects/limbs, cuts, freezes or texture artifacts;
- compatibility with adjacent accepted shots and intended edit boundary.

Classify each take:

- `pass` — fulfills the shot cleanly;
- `usable_with_debt` — usable with a disclosed non-blocking issue or post-production repair;
- `fail` — material identity, continuity, motion, physics, camera, end-state or artifact failure.

## Failure routing

- **wrong motion / action order** -> simplify motion wording, change phase plan, or split shot;
- **identity drift** -> strengthen/replace identity reference role or choose a better provider mode;
- **contact/physics failure** -> change start/end geometry, crop, phase, or request a pose/keyframe reference;
- **camera failure** -> reduce compound motion or use a verified camera/motion-reference mode;
- **end-state miss** -> use first+last/end-frame control when available, or generate a stronger end anchor;
- **prop morph/teleport** -> strengthen persistent object state and split the transition if needed;
- **environment warp** -> strengthen environment/start frame or reduce camera/path burden;
- **audio/dialogue mismatch** -> separate audio generation/finishing or use a provider with verified relevant support;
- **repeated structural failure** -> stop adjective retries; change control surface/provider/shot decomposition.

Preserve dimensions that already work. A targeted retry should not casually rewrite identity, lighting, location, or camera family when the defect is local.
