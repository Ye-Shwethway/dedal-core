# File-Mediated Creative Agent Bridge

## Purpose

DEDAL may collaborate with an external specialist agent through a shared file workspace when direct agent-to-agent messaging is unavailable or undesirable. The bridge is a durable production protocol, not a chat transcript substitute.

The canonical pattern is:

`DEDAL source-state production -> validated manifest + assets -> shared handoff inbox -> specialist generation/review -> pair-specific feedback -> narrow DEDAL repair`

Use this pattern for workflows such as still-image source production feeding generative-video execution, but keep the protocol workflow-agnostic enough to support future specialist agents.

## Authority model

1. The production `manifest.json` is the source of truth for ordered frames and continuity state.
2. Binary assets are evidence referenced by the manifest; filenames alone are not authority.
3. Handoff JSON files are immutable messages tied to a manifest version.
4. The external execution agent must reject stale-manifest handoffs rather than guessing.
5. Connected-service state such as a shared Drive folder remains externally authoritative; public Core stores only the portable protocol, never private workspace URLs or character/project identifiers.

## Source-sequence responsibilities

DEDAL owns source-image readiness before emitting `images_ready`:
- adaptive temporal density rather than a fixed frame count;
- pairwise reachability across every adjacent continuity-critical frame;
- identity, physical, prop/load, camera, support/contact, and video-readiness validation;
- zero-padded ordered assets plus a manifest carrying frame IDs, phase/arc, camera state, character state, prop state, delta-to-next, and intended motion;
- additional bridge frames whenever several major dimensions would otherwise change at once.

A pair may be classified only as `reachable`, `needs_bridge`, or `intentional_cut`.

## Specialist-agent responsibilities

The downstream agent consumes only the manifest version named in the handoff. It owns execution-specific compilation, generation, take QA, and structured return messages. If motion seams remain, feedback names the exact frame pair and failure class so DEDAL can repair only the missing temporal state instead of broadly regenerating the sequence.

A completed video is not silently accepted. The downstream agent returns `approved` or `needs_bridges`, plus pair-specific review evidence when repair is required.

## Handoff envelope

Each message carries at minimum:
- protocol version;
- message ID and thread/production ID;
- sender and recipient;
- created-at timestamp;
- message type;
- manifest version;
- reply-to pointer when applicable;
- acknowledgement requirement;
- lifecycle status;
- typed body payload.

Lifecycle is `new -> acknowledged -> processing -> completed`. Live inboxes hold only unprocessed messages; completed messages move to an archive/processed area.


## Progressive production-start and set handoff

For long or continuity-sensitive productions, handoff is progressive rather than end-loaded. DEDAL emits `production_started` immediately after the production manifest skeleton and planned set list exist. This lets the downstream specialist enter active review mode before source generation is complete and catch planning errors early.

The default intermediate handoff unit is a **set**. After a set passes DEDAL validation, emit `images_ready` with `scope: set`, the set ID, validated frame list, and check results. The downstream agent may validate format/identity/camera continuity, prepare motion-shot specs, return early frame-pair feedback, or run an explicitly bounded pilot take for a risky beat. Set-level readiness never means the whole production is complete.

After all planned sets pass validation and any early feedback is resolved, DEDAL emits `images_ready` with `scope: production`. Full production generation begins only at production scope unless the specialist explicitly runs a pilot take. The production manifest remains authoritative across every set handoff, and every handoff pins the current manifest version.

A `production_started` body should carry the production label and `planned_sets[]`, each with a stable set ID, arc, and target phases. This planning preview is advisory but actionable: if the specialist sees an impossible or risky plan, it should return early structured feedback before DEDAL compounds downstream work.

## Failure containment

- Never process a stale manifest version.
- Never treat file existence as `images_ready`; validation must already have passed.
- Never hide camera-angle changes between adjacent anchors.
- Prefer narrow bridge insertion over broad sequence regeneration.
- Cap automated correction loops and escalate after repeated failure instead of creating an infinite feedback cycle.

## Privacy boundary

Public Core may encode this protocol and generic validation behavior. Private workspace URLs, private agent deployment identifiers, character names, production IDs, access details, and live folder IDs belong only in the private overlay or the connected service itself.
