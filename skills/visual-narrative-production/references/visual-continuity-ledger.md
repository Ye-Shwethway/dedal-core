# Visual Continuity Ledger

## Purpose
A sequence of still images should behave like shots from one production, not independent illustrations that happen to share names.

## Scene-level state
Track when material:
- scene/location ID and environment geometry;
- time/date/daypart/weather;
- motivated light sources and lighting state;
- character IDs and canonical anchor IDs;
- wardrobe/grooming state;
- injuries, dirt, sweat, wetness, damage, carried items;
- prop/object identities and positions;
- character positions, facing, eye lines, and relative distance;
- camera axis and screen direction;
- current emotion/performance state;
- accepted previous shot(s);
- continuity notes and unresolved defects.

## Delta rule
Within the same scene, a new shot should normally declare the **delta** from the current ledger rather than restating/reinventing every element. Preserve everything not intentionally changed.

Examples of valid deltas:
- character crosses from doorway to bed;
- hand releases a prop;
- lamp remains camera-right while camera moves closer;
- jacket becomes torn after the fight;
- expression changes from guarded to relieved.

## Scene transition
When location/time materially changes:
- open a new environment/lighting/camera state;
- carry forward only character/prop/injury/wardrobe/emotional state that should persist;
- explicitly resolve anything that is reset by travel, time passage, costume change, cleanup, or story logic.

## Camera continuity
When spatial continuity matters, track:
- axis line;
- which subject is screen-left/screen-right;
- gaze direction;
- movement direction;
- camera side of axis;
- deliberate axis crossings.

Do not accidentally mirror screen direction between adjacent shots.
