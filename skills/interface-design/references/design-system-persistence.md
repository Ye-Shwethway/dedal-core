# Design System Persistence

Use when a UI task produces durable visual/product decisions worth carrying across sessions and surfaces.

## Master + surface overrides

Recommended project-local pattern:

```text
design-system/<project-or-product>/
├── MASTER.md
└── surfaces/
    ├── dashboard.md
    ├── settings.md
    └── landing.md
```

`MASTER.md` owns cross-product foundations such as brand direction, semantic color, typography, spacing/radius principles, iconography, motion policy, accessibility floor, and global component conventions.

A surface file contains only deliberate exceptions or additions for that surface. When both apply, the surface override wins only for its declared scope.

## Read before write

Before generating or modifying durable design state:
1. check whether a master already exists;
2. read it and relevant surface override;
3. inspect incumbent implementation for divergence;
4. identify whether the task is refinement, extension, migration, or redesign.

Missing documentation does not erase incumbent visual truth.

## Safe updates

- Do not silently replace a master design system because a new recommendation ranks higher.
- Preserve accepted decisions unless the Creator or owning project explicitly changes them.
- New surfaces should normally add overrides without rewriting the master.
- A master rewrite is a design migration/redesign decision and should expose material changes.
- Never use a force/overwrite mechanism merely for convenience.

For routine reversible project writes already authorized by the workflow, update normally with exact diffs and verification. For broad identity changes, destructive replacement, or ambiguous ownership, obtain Creator authority.

## Provenance and freshness

When useful, record:
- originating brief/decision/spec;
- source design system or catalog references;
- framework/platform assumptions;
- last reviewed date for drift-sensitive guidance;
- superseded direction and migration notes.

Do not turn generated recommendations into historical fact. Mark proposed vs accepted design direction clearly when the distinction matters.

## Retrieval order for implementation

When building a surface:
1. read `MASTER.md`;
2. read the matching surface override if present;
3. inspect current implementation and tokens;
4. resolve conflicts explicitly rather than silently choosing the newest file.

The owning project's repository conventions override this suggested path/layout.
