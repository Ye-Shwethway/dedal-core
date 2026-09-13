# Context Map

The context map is a routing artifact, not a repository dump.

## Discovery order

Prefer a narrow evidence path:
1. project/root agent instructions and README/contribution docs;
2. current checkpoint/roadmap/ADR material;
3. package/build manifests and CI workflows;
4. top-level module tree and actual entrypoints;
5. task-specific code/config/data only after the map indicates where to look.

Do not recursively read the repository without a task reason.

## Map dimensions

### Product
- what user/problem does this project serve?
- what is explicitly out of scope?

### Structure
- primary modules/packages/apps;
- dependency direction and ownership seams;
- generated/vendor directories;
- stateful stores and schemas.

### Execution
- install/setup;
- build;
- tests/lint/static checks;
- local run/dev server;
- environment assumptions.

### Change constraints
- architecture decisions;
- stable branches/releases;
- migrations/backward compatibility;
- protected data or production surfaces.

### Continuity
- accepted decisions;
- completed evidence;
- current failures/risks;
- next executable step.

## Compression test

Remove a fact if deleting it would not change at least one of:
- where the agent looks;
- what it is allowed/expected to change;
- how it verifies work;
- what risk it accounts for;
- how work resumes later.

Prefer references such as `docs/architecture/...` over copied prose when the source is stable and cheap to retrieve.
