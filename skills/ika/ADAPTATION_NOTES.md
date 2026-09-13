# $ika Adaptation Notes

## Source

This DEDAL-native skill was derived from the private repository `Ye-Shwethway/ianeo-knowledge-vault` at source commit `fbed860928c1a93261306f70a47fa700da56ce29`, especially `skills/ianeo-knowledge-archive/`.

This is an **adaptation**, not an exact copy.

## Preserved concepts

The following legacy ideas remain valuable and are retained:

- live/primary project state outranks summaries and memory;
- Git-backed canonical archives with explicit provenance and history;
- atomic facts/decisions/source records with stable IDs;
- bounded deterministic retrieval instead of loading entire archives blindly;
- preserved disputes, superseded records, and corrections instead of destructive rewriting;
- one-hop linked knowledge and change-impact review;
- read-back verification after publication;
- no false claims about native multi-agent execution;
- no model-weight-training claims.

## Refined for DEDAL

Legacy IANEO-specific assumptions were removed or generalized:

- identity changed from IANEO-specific orchestration to DEDAL Core routing;
- archive destinations are no longer hardcoded to `IANEO Knowledge Archives`;
- canonical storage is determined by each archive/project contract rather than one fixed vault location;
- worker orchestration is optional and runtime-neutral;
- learning promotion follows DEDAL Core's improvement/kernel rules rather than `IANEO Core` wording;
- private implementation state remains outside the public DEDAL Core repository.

## Deliberately not imported into the default $ika skill

The legacy Writing Chamber and Image Visualization Chamber were useful experiments, but they are not ordinary knowledge-archive responsibilities. They remain historical/private implementation material and may later become separate DEDAL skills if a concrete workflow justifies them.

Legacy scripts, fixtures, archives, registry contents, and private project data were not copied into this public repository. The original private repo remains available as historical implementation/reference state.
