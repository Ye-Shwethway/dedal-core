# YouTube SEO MVP Workflows

## New video / candidate launch research

Input: actual video/candidate truth + target channel/profile.

1. Resolve content entities and likely viewer intents.
2. Generate a bounded query set across exact scene, episode, character/entity, action/emotion, franchise, and variant spellings.
3. Classify primary discovery surface.
4. Inspect live search landscapes for the highest-value variants.
5. Add owned-channel search-term evidence where related history exists.
6. Build factor vectors and note evidence classes.
7. Produce one primary package and up to two materially different alternates.
8. Run the viewer-facing copy check: title reads naturally, description opens with useful scene context, no internal/operator-note language is exposed, named entities are verified, and keywords are integrated naturally rather than dumped.
9. Run the remaining preflight and hand any approved mutation to YouTube Publishing.

## Existing-video diagnosis

1. Capture the current title/description/tags/playlist/thumbnail reference and publication age.
2. Pull comparable-window performance, not lifetime totals alone.
3. Inspect traffic-source mix.
4. For Search, inspect query details and current result landscapes.
5. For Browse/Suggested, prioritize packaging and engagement diagnosis.
6. Inspect retention before blaming title/thumbnail alone.
7. If impressions/CTR are available, interpret them with source/context and audience expansion.
8. Check whether the current metadata is genuinely viewer-facing. Flag internal notes, archival labels, keyword dumps, duplicate title-as-description, or unsupported entity claims even when they are not the primary ranking problem.
9. Produce diagnosis + proposed experiment, not an automatic rewrite.

## Metadata package quality gate

Before proposing or mutating a package:
- Title: human-readable, truthful, compact, and aligned with the target discovery surface.
- Description: usually one short paragraph or 2–5 sentences; first sentence explains the scene/moment; useful entities/context appear naturally.
- Internal-language rejection: remove notes such as `personal archival upload`, `test upload`, storage/workflow labels, or private experiment language unless intentionally audience-facing.
- No keyword blocks: avoid comma-separated SEO phrases and unrelated trending terms.
- Entity verification: every character, actor, scene, episode, quote, or relationship claim must be supported by the clip or reliable source context.
- Tags/hashtags: small supplemental set only; never use them to compensate for weak title/description copy.
- Promise consistency: title, description, thumbnail brief, and actual clip must describe the same viewer promise.

## Thumbnail package workflow

Use this sequence for a missing/custom thumbnail or a deliberate thumbnail experiment:

`content truth -> discovery strategy -> visual reference map -> concept directions -> generate/edit -> visual QA/Creator acceptance -> asset finalization -> DEDAL staging -> dedicated publish -> remote read-back -> experiment event`

Rules:
- Do not jump from video title to image generation when the source scene/character truth is specific.
- If a base image is accepted, preserve it and edit only the requested layer whenever practical.
- Treat thumbnail text as complementary packaging, not a duplicate full title; prioritize mobile readability and safe composition space.
- The staging URL must be fetchable by the Gateway, not only by a browser.
- Record a post-T0 thumbnail introduction as a confounder/package event in later measurement.
- See `thumbnail-workflow.md` for the full ownership and stop-rule contract.

## Post-publish windows

Suggested comparison windows when enough data exists:
- launch: first 24 hours;
- early: first 3 days;
- first week: first 7 days;
- learning: first 28 days;
- mature: later/lifetime, clearly labeled.

Sparse channels may need longer windows; do not force significance where sample size is tiny.

## Learning write-back

A durable channel lesson should contain:
- observation;
- time/window;
- evidence source/class;
- affected surface/query/entity;
- competing explanations/confounders;
- practical implication;
- confidence/status (`candidate`, `supported`, `superseded`).

Creator/channel-specific records belong in the private operational overlay, never in public Core.

## Prospective experiment runner

1. Apply only an approved package through YouTube Publishing and verify authoritative read-back.
2. Freeze a T0 record: exact package, target surface, publication time/age, bounded SERP baseline, public stats, source availability, and confounders.
3. Hold metadata stable unless a factual/policy defect or explicit Creator-directed change requires intervention.
4. Measure at 24h, 3d, 7d, and 28d when useful. Sparse channels may extend windows rather than forcing a conclusion.
5. At every window, distinguish measured zero from unavailable/not-yet-processed/suppressed/error states.
6. Use per-video traffic sources, visible Search detail, retention, Reach impressions/CTR when available, and bounded SERP observations; no single unavailable source blocks the full readout.
7. At 7d, record a directional status (`supports`, `mixed`, `does_not_support`, `inconclusive`) without upgrading a sequential change into causal proof.
8. At 28d, extract only evidence-backed channel lessons and retain confounders.
9. Keep real experiment identifiers/outcomes private; promote only sanitized reusable rules to Core.

See `measurement-and-closeout.md` for the canonical window schema and closeout gate.
