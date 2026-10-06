# Resource profile and record model

## Tracking profile

A tracking profile defines **why** a resource class matters and how to qualify it. Keep these concepts separate:

- `resource_type`: canonical class being tracked.
- `purpose`: downstream decision or workflow the catalogue should support.
- `desired_values`: soft preferences; profile-relative, potentially subjective.
- `hard_requirements`: must-pass constraints.
- `exclusions`: explicit disqualifiers.
- `freshness_policy`: which facts decay quickly and when refresh is due.
- `discovery_policy`: tracked-focus versus exploration behavior, allowed sources, region/language/time window.
- `evidence_floor`: minimum provenance/confidence for promotion to tracked state.
- `consumer_contracts`: downstream owners that may consume records without transferring decision authority.

Do not encode a subjective preference as a universal entity fact. Store `profile_fit` assertions with `profile_id`, rationale, evidence refs, confidence, and observation time.

## Canonical resource record

Each resource gets a stable `resource_id` independent of a display name or one source URL. Preserve aliases and source-specific identifiers.

Important dimensions:

- identity: canonical name/type, aliases, external IDs;
- lifecycle: candidate/tracked/watch/hold/retired/unavailable;
- qualification: hard-gate results and profile-relative fit assertions;
- observations: claim/value/source/time/confidence;
- opportunities: downstream-useful leads or unresolved targets;
- refresh: last checked, next/due logic, volatile fields;
- delta history: new/changed/confirmed/stale/conflict events;
- provenance: source class, locator, observed time, validity window if known;
- relationships: work/person/package/project/citation/dependency/etc. when material.

## Entity resolution

Promote two sightings to one canonical resource only when there is positive identity evidence: stable external identifier, authoritative alias, matching source lineage, or sufficiently strong multi-field agreement.

When ambiguity remains, keep separate candidates and add a possible-match relation. Never resolve duplicates from name similarity alone when collision risk is material.

## No magic score

Large catalogues may use convenience ranking, but the stored truth is the factor vector. Keep components visible: fit, freshness, evidence confidence, opportunity value, novelty, change magnitude, accessibility, risk/constraints, and consumer relevance.

## Review policy and evidence model

Every profile must resolve `review_policy`: `visual_required`, `creator_acceptance_required`, dimension IDs and allowed evidence kinds for resource/opportunity scopes. Nonvisual profiles use empty dimension/evidence lists. Visual profiles require nonempty dimensions; the profile's hard requirements define the actual threshold. For a media person, resource images may demonstrate face/physique while an opportunity image must come from that actual scene; preserve exact known locators separately and keep unknowns explicit.

Store `visual_evidence` entries with immutable asset ID, scope/opportunity identity, kind, origin, attributable source, persistent storage reference, SHA-256, verified image MIME, profile-bound direct inspection read reference/time, per-dimension pass/fail/unknown with reasons, and exact display reference/time. Persist actual original bytes; pointers alone are not retention. Bind inspection/display/decision to the same bytes. Do not replace evidence in place without renewed review; use a new asset identity and retain history.

Store append-only profile-bound scoped `reviews` with status, explicit decision source/time/reason and displayed asset IDs. The last review in the exact scope is current. Pending is not acceptance. A resource approval cannot approve an opportunity; earlier approved edits are only evidence for their exact scope. Creator rejection may be recorded from an unsaved preview with an honest missing-proof annotation, and always blocks promotion; acceptance requires saved proof if the policy requires visual review.

`candidate`/`watch` records are discovery memory, not the accepted catalogue. Confidence and `profile_fits.band` are DEDAL assessment, not Creator decisions. A rejected resource stays excluded from active recommendations. Reconsideration needs new materially relevant proof and an explicit new Creator decision, never a later matching keyword alone.

Run `python scripts/resource_review.py --profile PROFILE --record RECORD --stage present|accept --scope resource|opportunity [--opportunity-id ID] [--asset-paths MAP]`. The optional MAP is JSON from asset IDs to authorized local paths. `present` checks saved, screened, displayed proof declarations; `accept` additionally checks explicit scoped decision and chronology. Pixel judgment and authenticity of read/consent claims require real execution evidence outside this validator.
