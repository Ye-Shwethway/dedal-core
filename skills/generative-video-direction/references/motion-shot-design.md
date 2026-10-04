# Motion Shot Design

## Temporal objective

A motion shot should define a visible change through time, not merely a beautiful moving frame. Record:

- narrative/visual function;
- start state;
- decisive temporal change;
- end state;
- duration target/range;
- information/emotion/action that must land.

## Motion layers

When material, separate:

- subject locomotion and body mechanics;
- hands/contact/prop interaction;
- gaze/expression/performance progression;
- object motion and possession state;
- environmental motion (wind, water, smoke, crowds, machinery, fabric/hair);
- camera movement and focus behavior;
- audio/dialogue timing.

Avoid contradictory vectors or several unrelated actions competing inside a short shot.

## Phase planning

For complex physical action, define phases such as `setup -> initiation -> load/contact -> completion -> settle`. A generation need not show every phase, but its start and end must imply a plausible path.

If the model repeatedly collapses phases, split the shot or request a stronger start/end keyframe pair.

## Camera choreography

Camera movement has one main motivation unless the intended style clearly requires more:

- locked observation;
- follow/track subject;
- reveal/reframe information;
- emotional push/pull;
- orbit/arc around a stable action center;
- POV/subjective move;
- deliberate handheld energy.

Do not combine pan + orbit + dolly + zoom + rack focus by default. Camera complexity consumes generation reliability and can hide motion defects.

## Feasibility test

Before generation ask:

1. Can the end state physically follow from the start state in the available duration?
2. Are prop/contact transitions visible or at least causally plausible?
3. Does the camera preserve enough evidence to judge the important action?
4. Is the shot asking the model to solve more than one difficult identity/geometry/action problem at once?
5. Would two shots communicate the beat more reliably than one overloaded take?


## Adaptive source-keyframe density

Keyframe count is not a stylistic constant. After phase planning, inspect each adjacent state for subject translation/rotation, support/contact changes, prop possession/load changes, camera change, and shot-scale change. Add bridge states until every adjacent pair is physically and cinematically reachable within the intended segment duration.

A complex arc-to-arc transition often needs more control states than the exercise/action mini-arc it connects. Intermediate states may be mundane; temporal continuity outranks poster-frame novelty.

When several independent dimensions change at once, sequence them across adjacent anchors. Do not ask one short generation to simultaneously swap props, rotate the body, move the camera, and establish a new support mode unless a deliberate cut is intended.

Read `adaptive-keyframe-density-and-transition-bridges.md` for provider-aware compilation.
