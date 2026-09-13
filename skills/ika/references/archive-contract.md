# Archive Contract

## Purpose

A DEDAL knowledge archive is a durable, evidence-linked representation of project state. It is not a substitute for the live project and it is not a dump of chat history.

## Recommended layout

```text
archives/<project-id>/
├── manifest.json
├── current-context.md
├── knowledge/
│   ├── project-overview.md
│   ├── facts.jsonl
│   ├── decisions.jsonl
│   └── open-questions.md
├── sources/
│   └── source-index.jsonl
└── history/
    └── change-log.jsonl
```

Optional relationship files may be added when a project needs explicit linked knowledge.

## Manifest role

`manifest.json` is the archive control record. It should identify at minimum:

- archive/schema version;
- stable project ID and title;
- project status and sensitivity;
- created/updated timestamps;
- canonical provider/location/revision;
- optional mirror locations and synchronization state.

Never infer a canonical location from old IANEO conventions. Read the current manifest/project contract.

## Atomic records

Facts should preserve stable IDs, statement/state/confidence/sensitivity/evidence/update time.

Decisions should preserve stable IDs, summary/status/rationale/evidence/update time.

Sources should preserve stable source IDs, type/location/authority/capture time/fingerprint or revision identity.

Change history should append operations such as create, refresh, correct, deprecate, sync, and audit. Do not erase provenance to make the archive look cleaner.

## Human-readable surfaces

`current-context.md` is a concise generated retrieval surface, not an independent authority. It should summarize current constraints, decisions, risks/unknowns, next actions, freshness, and canonical revision.

`project-overview.md` contains durable background. `open-questions.md` tracks unresolved questions and next verification steps.

## Authority and conflict

Primary/live evidence outranks archive summaries. When sources disagree, retain the disagreement and record what would resolve it. Prefer correction/supersession/deprecation over destructive rewriting.

## Sensitivity

Use explicit sensitivity labels appropriate to the project. Never move confidential/restricted content into a public repository merely because the archive schema permits Git storage.

## Canonicality

Avoid multi-master state. Mutate the declared canonical archive first, verify the resulting revision, then update optional mirrors. Mirror failure does not invalidate a verified canonical write, but must be reported accurately.
