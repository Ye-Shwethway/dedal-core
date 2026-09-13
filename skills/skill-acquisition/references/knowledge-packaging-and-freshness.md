# Knowledge Packaging and Freshness

Use this reference for skills that contain substantial domain knowledge, generated guidance, rule catalogs, SDK/API instructions, or fast-changing external facts.

## Hero-path discipline

Keep the dominant workflow(s) in `SKILL.md` and move less-common variants into references.

Use an 80/20 heuristic, not a rigid quota:
- if one workflow covers most real tasks, make it the hero path;
- if two or more workflows are genuinely co-equal, keep each visible in the entrypoint;
- do not mislabel a valid common alternative as "advanced" merely to shorten the file.

## Rule catalogs

When a skill contains many checks or recommendations:
- group them by coherent category;
- rank categories/rules by expected impact or risk;
- run critical/high-value checks before low-impact polish;
- give stable rule IDs or names when findings need provenance or regression tracking;
- keep detailed examples/explanations in references when the index can stay compact.

Impact ordering is a prioritization aid, not a substitute for project-local requirements.

## Generated knowledge

Generated skill content requires a source-of-truth path. Prefer a reproducible pipeline:

`authoritative source -> extraction/normalization -> generated skill/reference -> validation/tests`

Do not manually patch generated output without fixing or documenting the generating source/process when regeneration would overwrite the change.

Validate generated packages for at least:
- required sections/schema;
- broken internal links/references;
- duplicate/conflicting rules;
- stale source identifiers or versions;
- secret/private-data leakage;
- representative behavior/eval cases when feasible.

## Freshness metadata

For knowledge likely to drift, record enough metadata to decide when re-verification is needed, such as:
- source repository/documentation identity;
- pinned commit/version where appropriate;
- generated/reviewed date;
- runtime/SDK/API version assumptions;
- refresh policy or stale-after guidance when a meaningful interval exists.

Do not pretend stable knowledge needs arbitrary periodic refresh. Apply freshness gates to information whose correctness genuinely changes over time.

## Runtime verification

Even a recently generated skill may disagree with the installed/runtime version. When implementation depends on current APIs, verify the relevant live documentation, package version, tool capability, or service state before making irreversible changes.

## Context efficiency

Every always-loaded instruction consumes shared context. Keep common routing/workflow information near the entrypoint and move detail that is rarely needed behind explicit references. Measure success by preserved decision quality per unit of context, not by shortest possible file size.