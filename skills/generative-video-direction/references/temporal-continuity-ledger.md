# Temporal Continuity Ledger

The Visual Continuity Ledger describes still-state truth. The Temporal Continuity Ledger extends it with motion state between accepted frames/takes.

Track only material state:

- scene/shot IDs and time relation;
- accepted start/end visual anchors;
- character position, facing, screen direction and movement vector;
- action phase and body/contact state;
- prop count, identity, possession, contact, orientation and movement;
- environment motion state;
- camera position/axis and current trajectory;
- pace/velocity class and whether motion is accelerating/decelerating/settling;
- gaze/performance progression;
- wardrobe/hair/fabric/injury/dirt/wetness state affected by motion;
- audio/dialogue state when continuity depends on it;
- accepted generated take IDs and known debt.

## Delta rule

A new generated shot declares the intended temporal delta. Everything else remains preserved unless a visible or narratively justified transition changes it.

## Cut-boundary state

For post-production handoff, record the final usable motion state:

- subject position/direction;
- object possession/contact;
- camera motion at tail;
- audio tail/dialogue boundary;
- whether the take ends settled or mid-motion;
- any continuity debt that constrains the next cut.

This prevents a visually plausible take from creating an impossible edit into the next shot.
