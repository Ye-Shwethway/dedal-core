# Interface Design Adaptation Notes

_Date: 2026-09-14_

This DEDAL-native skill is synthesized from multiple public sources rather than copied wholesale.

## Primary influences

- `Leonxlnx/taste-skill` @ `ccbc15639c97057cbfcf32ecebc38ef716e4bb37` — MIT.
  - retained: brief inference, audience/constraint-first direction, anti-default discipline, honest use of real design systems, redesign awareness.
  - not retained: hardcoded font/library preferences, one-stack defaults, aesthetic opinions as universal rules.
- `pbakaus/impeccable` @ `cb56ed6c19a07329a9fa0cd4e657bee040156593` — Apache-2.0.
  - retained: brief-wins rule, surface-mode framing, refinement-vs-redesign distinction, incumbent visual truth, bounded verification, durable design documentation.
  - not retained: bundled launcher/binary, provider-specific agents/hooks, universal maximalism, command namespace.
- `nextlevelbuilder/ui-ux-pro-max-skill` @ `7f69fed6a2717900085f1bc3b263721f8ba025e2` — MIT.
  - retained: searchable/scoped design-intelligence architecture, domain-vs-stack separation, explicit no-match/fallback semantics, relevance calibration, design-system aggregation, master + surface override persistence, and version/freshness awareness.
  - not retained: vendored CSV catalog contents, Claude/plugin paths, CLI installation/update mechanics, hardcoded current stack versions as durable truth, external logo-generation services, fixed numeric dials as universal design rules, or silent/forced overwrite behavior.

## DEDAL changes

- Provider/runtime-specific mechanics were removed.
- The skill remains framework-agnostic and defers implementation mechanics to Software Development and the live project stack.
- Curated catalog output is treated as recommendation evidence, never as authority over Creator intent, project-local truth, accessibility standards, or current official platform documentation.
- Retrieval uses the smallest relevant design domain and separates semantic UX guidance from implementation-stack guidance.
- A failed retrieval remains an explicit miss; fallback guidance is labeled rather than fabricated as a match.
- Durable design state uses master + surface override precedence and must not be silently overwritten.
- Visual verification is evidence-based and bounded rather than an open-ended self-polish loop.

No third-party package, CLI, script, or executable was installed or run during adaptation.
