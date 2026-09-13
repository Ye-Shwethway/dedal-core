# Interface Design Adaptation Notes

_Date: 2026-09-14_

This DEDAL-native skill was synthesized from multiple public sources rather than copied wholesale.

## Primary influences

- `Leonxlnx/taste-skill` @ `ccbc15639c97057cbfcf32ecebc38ef716e4bb37` — MIT.
  - retained: brief inference, audience/constraint-first direction, anti-default discipline, honest use of real design systems, redesign awareness.
  - not retained: fixed aesthetic dials, hardcoded font/library preferences, universal frontend-stack assumptions.
- `pbakaus/impeccable` @ `cb56ed6c19a07329a9fa0cd4e657bee040156593` — Apache-2.0.
  - retained: brief-wins rule, surface-mode framing, refinement-vs-redesign distinction, incumbent visual truth, bounded verification, durable design documentation.
  - not retained: bundled launcher/binary, provider-specific agents/hooks, universal maximalism, command namespace.

## DEDAL changes

- Provider/runtime-specific mechanics were removed.
- The skill is framework-agnostic and defers implementation mechanics to Software Development and the live project stack.
- Visual verification is evidence-based and bounded rather than an open-ended self-polish loop.
- Creator-provided brand/canon/product direction outranks generic taste heuristics.

No third-party package or executable was installed or run during adaptation.
