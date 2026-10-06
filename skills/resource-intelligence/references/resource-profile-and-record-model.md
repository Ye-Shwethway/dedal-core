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