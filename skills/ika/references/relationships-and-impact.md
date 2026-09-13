# Relationships and Change Impact

## Purpose

Use explicit links when project knowledge needs navigable dependencies without turning the archive into an opaque graph system.

## Direct relationships

Within one project, useful relation types include:

- `supports`
- `derived-from`
- `supersedes`
- `conflicts-with`
- `depends-on`
- `affects`

Across projects, keep the relation set smaller and explicit, for example `depends-on`, `affects`, `shares-with`, and `conflicts-with`.

## Traversal rule

Default traversal is **one hop only**. Do not recursively expand relationships unless a future skill explicitly introduces a bounded, tested multi-hop contract.

Never invent links from semantic similarity alone. Unknown projects or record IDs fail closed.

## Change-impact review

When a known record changes, return the direct records/projects that should be reviewed and explain the relation/reason. Severity may be derived from relation type, but it remains advisory.

Impact analysis must not automatically:

- rewrite linked records;
- refresh other archives;
- deprecate or supersede related facts;
- resolve conflicts;
- promote learning into DEDAL Core.

The result is a review queue, not a mutation command.

## Ownership

Each record remains owned by its original archive. Cross-project links do not transfer authority or canonical ownership.
