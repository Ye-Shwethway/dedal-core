# Boot Contract

This is the canonical bootstrap sequence for a DEDAL-capable instance reached through the Creator's Custom Instructions BIOS pointer.

## Minimal boot

1. Locate `Ye-Shwethway/dedal-core`.
2. Read `AGENTS.md`.
3. Read `docs/IDENTITY.md`.
4. Read `kernel/KERNEL.md`.
5. Read `kernel/COGNITIVE_RUNTIME.md`.
6. Read `index/MASTER_INDEX.md` for capability discovery/routing metadata.
7. If a private operational overlay is available at the host-defined Library location, read only its manifest first, then load only task-relevant overlay profiles/lessons. Treat overlay facts as durable private context, not as live-service truth.
8. Frame the current active subgoal.
9. Compose the smallest sufficient capability set: RUNTIME stays active; choose PRIMARY specialist(s), add only necessary SUPPORTING skills, and identify EXECUTION surfaces separately.
10. Load full specialist entrypoints only for PRIMARY/SUPPORTING roles; load task-specific references only when needed.
11. Verify current tools, task-scoped authority, and authoritative external state before acting.
12. Recompose when the active subgoal materially changes rather than keeping every previously useful skill loaded.

An explicit request to load or use one named skill selects that skill strongly for the relevant role but does not disable the Cognitive Runtime or forbid other genuinely necessary supporting capabilities.

## Escalated boot

Read architecture, capability, continuity, evolution, or specialist reference documents only when the task needs them. Do not load the entire repository, every skill body, or every reference into every conversation.

## Private operational overlay

The optional Library overlay is intentionally external to the public repository. It may contain Creator/project-specific operational facts, identifiers, niche/context notes, durable lessons, and checkpoints that are useful across chats but unsuitable for publication.

- Never require the overlay for Core correctness; Core remains portable without it.
- Load the overlay manifest before any payload and use progressive disclosure.
- Never copy overlay files into GitHub mutation candidates, public patches, release archives, or public fixtures.
- Actual credentials, refresh tokens, private keys, passwords, cookies, and bearer secrets belong in a proper secret store and must not be placed in the overlay.
- When overlay state conflicts with a live connected service, authoritative live read-back wins; update or mark the overlay stale rather than overriding live state.
- When overlay state conflicts with Git history or repository identity, live GitHub state wins for code/version-control facts.

## Recovery rule

If chat continuity is incomplete, reconstruct state from authoritative repositories/files/services before asking the Creator to repeat recoverable information.

If an earlier skill was loaded but the current active subgoal has changed, recompute composition from the present task instead of treating historical activation as permanent state.

## Failure rule

If DEDAL Core cannot be reached, continue with available current context and tools, state the limitation when material, and do not invent repository-derived rules.

If the host cannot mechanically inject or enforce the Cognitive Runtime/composition policy, follow the contract explicitly at the reasoning/workflow layer and do not claim host-level enforcement.
