# YouTube Thumbnail Workflow Contract

## Purpose

Treat the thumbnail as a first-class packaging artifact, not a decorative afterthought. This workflow composes YouTube SEO, Visual Direction, and YouTube Publishing so that strategy, scene/subject truth, image production, mutation, read-back, and measurement stay separate and auditable.

## Ownership map

- **YouTube SEO** owns discovery-surface hypothesis, viewer promise, entity/intent alignment, thumbnail strategy/brief, title-thumbnail consistency, experiment hypothesis, and outcome interpretation.
- **Visual Direction** owns reference authority, visual-truth locking, concept composition, generation/editing, drift detection, mobile readability, and Creator acceptance of the image itself.
- **YouTube Publishing** owns final media validation, DEDAL-controlled staging, authenticated thumbnail mutation, remote read-back, mutation diagnostics, and publication-event evidence.
- **Creator** remains the approval authority for consequential visual/package changes when approval is required by the active workflow.

No layer may silently absorb another layer's authority. In particular, image generation must not begin before strategy and visual truth are sufficiently defined for a scene/character-specific thumbnail.

## Layered workflow

### Layer 0 — Object and objective lock

Resolve the exact video/candidate, target channel/profile, publish state, target discovery surface, and whether the task is a missing-thumbnail completion, launch package, replacement experiment, or factual defect repair.

Output: `thumbnail_object` + `objective`.

### Layer 1 — Content-truth lock

Write the smallest factual scene/subject contract that the thumbnail must represent:

- who/what is actually central;
- action/event/moment shown;
- setting/environment;
- wardrobe/body/prop state when material;
- emotional/tone truth;
- explicit exclusions that would make the thumbnail misleading.

For clip thumbnails, a character/entity name must not be promoted from search competitors or memory alone when clip-level truth is uncertain.

Output: `content_truth_lock`.

### Layer 2 — Discovery and packaging strategy

State the primary discovery hypothesis (Search, Browse, Suggested, mixed, Shorts feed) and the job the thumbnail must do on that surface. Define:

- viewer promise;
- focal entity/action;
- title-thumbnail complementarity;
- whether text is necessary;
- clickability constraints without false clickbait;
- expected experiment/change boundary.

Search-first thumbnails should maximize scene/entity clarity. Browse/Suggested packaging may lean harder on immediate visual appeal and emotion, but must remain truthful.

Output: `thumbnail_strategy_brief`.

### Layer 3 — Visual reference research

Before generation, establish reference authority for identity, body/scale, wardrobe, environment, lighting, and scene language. Prefer the smallest sufficient set.

Reference roles must be explicit. A face reference must not silently redefine body proportions; an environment still must not silently redefine identity; a style image must not override scene truth.

When the source is a known film/series/game scene, research or Creator-provided frames may ground the visual language. Do not fabricate a generic scene when a specific source moment is known.

Output: `reference_map` + `visual_truth_lock`.

### Layer 4 — Concept directions

Create a small number of materially different concepts before rendering when useful. Typical axes:

- impact close-up;
- two-subject faceoff;
- wider action/environment;
- character/emotion-led;
- object/event-led.

Each concept must state framing, focal subject, action, environment, text treatment, and what remains invariant.

Do not batch-generate random variants before concept intent is clear.

Output: `concept_set`.

### Layer 5 — Generation or edit execution

Choose the least-destructive visual operation:

- **generate** when no accepted base exists;
- **edit-first** when a Creator-approved image already has the right composition/identity;
- **text-only edit** when the only requested change is typography;
- **local correction** when one region/trait is wrong.

If the Creator says to preserve body size, composition, face, or other accepted traits, do not re-synthesize them unnecessarily. A text-only request must not resize subjects, alter anatomy, or drift identity.

Output: candidate image(s).

### Layer 6 — Visual QA and Creator acceptance

Inspect the actual render at full view and thumbnail/mobile scale. Check:

- scene/subject truth;
- identity/character resemblance where relevant;
- anatomy and proportional integrity;
- subject hierarchy and crop safety;
- title-thumbnail promise consistency;
- text spelling, contrast, and safe-area placement;
- readability at small size;
- misleading/clickbait risk;
- accidental logos/watermarks/unwanted artifacts;
- continuity against accepted references.

Rejected candidates do not become canonical references. Accepted candidates may become the approved packaging asset.

Output: `approved_thumbnail_asset`.

### Layer 7 — Asset finalization

Prepare an execution-safe asset while preserving the accepted visual:

- use a YouTube-suitable 16:9 image by default;
- validate current platform format/size requirements at execution time;
- avoid needless recompression or crop changes;
- preserve the approved visual and text safe area;
- record a stable asset identity/hash when practical.

Do not infer that a visually correct local image is remotely fetchable.

Output: finalized local/managed asset.

### Layer 8 — DEDAL-controlled media staging

Publishing requires an HTTPS-fetchable source when the dedicated thumbnail setter uses `source_url`. The preferred path is **DEDAL-controlled, ephemeral staging**, not a credit-metered third-party upload host.

Requirements:

1. stage the approved asset on Creator-controlled infrastructure (for example an authenticated upload path backed by Cloudflare R2/Worker or equivalent managed storage);
2. issue a short-lived HTTPS URL or bounded download endpoint;
3. verify the Gateway/Worker can fetch it, not merely that a phone/browser can open it;
4. validate status, redirects, content type, non-empty bytes, and current YouTube media constraints;
5. expire/delete staged media after the mutation/read-back window unless durable managed state is explicitly required.

Third-party upload-to-URL services are fallback-only and require explicit workflow choice; they are not a Core dependency.

Output: `staged_media_url` + preflight evidence.

### Layer 9 — Publish mutation

Hand the approved staged URL to YouTube Publishing. Use the dedicated thumbnail tool, exact owned profile/video, and required explicit action intent. Mutate once boundedly.

If the call returns transport ambiguity or failure, inspect stage-aware evidence before retrying. Do not assume the upstream mutation failed merely because the outer connector returned an error.

Output: mutation result + audit evidence.

### Layer 10 — Authoritative read-back

Success requires remote evidence. Prefer:

- thumbnail-set response variants;
- subsequent YouTube video thumbnail URLs/read-back;
- bounded visual comparison when practical;
- Creator/Studio confirmation when API semantics are insufficient.

An accepted HTTP request alone is not enough.

Output: `thumbnail_applied=true|false|outcome_unknown` with evidence.

### Layer 11 — Experiment registration and measurement

When the thumbnail is introduced after T0 or after another packaging change, record it as a package event/confounder. Capture:

- apply time;
- asset/concept identity;
- changed package fields;
- target surface/hypothesis;
- whether metadata changed simultaneously;
- planned 24h/3d/7d/28d windows where appropriate.

Interpret Reach impressions/CTR, traffic-source mix, retention, and search detail together. A sequential thumbnail change can support association, not isolated causation, unless a stronger concurrent experiment design exists.

## Hard stop rules

Stop and repair the prior layer when:

- the generated subject/scene conflicts with source truth;
- a named character's role is unverified;
- reference roles are ambiguous enough to cause identity/body drift;
- the Creator-approved base would be unnecessarily regenerated;
- text is unreadable or outside safe composition space;
- staging is browser-accessible but Gateway-unfetchable;
- mutation outcome is unknown and has not been read back;
- early metrics tempt package churn before the declared observation window.

## Minimal artifact record

A durable thumbnail workflow record should be able to answer:

`object -> content truth -> target surface -> viewer promise -> reference authority -> concept -> approved asset -> staging evidence -> mutation -> read-back -> package event -> measurement outcome`

Creator/channel-specific records stay private. Public Core retains only generic workflow contracts and sanitized lessons.
