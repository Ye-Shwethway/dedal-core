---
name: resource-intelligence
description: "Build and operate persistent, resource-type-agnostic discovery and tracking systems: define what qualifies, discover broadly, resolve canonical identities, preserve provenance, refresh tracked resources, detect changes, surface unseen opportunities, and hand high-value records to downstream skills."
---

# Resource Intelligence

Own the reusable layer that turns repeated resource finding into **persistent resource intelligence**. The atomic object may be a person, organization, software library, paper, product, media work, supplier, dataset, service, place, opportunity, or another user-defined resource type.

## Trigger when

Use this skill when the Creator wants a resource class to be discovered **and remembered/tracked across runs**, wants a watchlist/catalogue refreshed, wants changes since the last check, or wants downstream work to start from accumulated qualified resources rather than blind search.

Do not trigger for a one-off lookup with no persistence, refresh, delta, catalogue, or repeated-selection intent; ordinary Research owns that.

## Ownership boundary

Resource Intelligence owns:

`define tracking profile -> discover -> resolve identity -> retrieve proof -> inspect -> qualify provisionally -> present -> Creator review -> persist scoped decision -> refresh -> classify delta -> rank attention -> hand off`

It composes with **Research** for current external facts and source discovery, **Knowledge/Memory** for general memory governance when needed, and domain skills that consume qualified resources. It does not take over the consumer's domain-specific decision gates or mutations.

Examples: Candidate Video Finder may consume actor/work/scene leads; Software Development may consume tracked packages; Research may consume a tracked paper corpus. None of those consumers become dependencies of this skill.

## Core workflow

1. **Resolve tracking intent.** Define resource type, purpose, desired values, hard requirements, exclusions, freshness needs, evidence floor, refresh cadence or trigger, and what downstream decisions the catalogue should support.
2. **Create a profile, not a prompt fragment.** Persist the tracking contract using `schemas/resource-profile.schema.json`. Subjective preferences are profile-relative qualification criteria, not universal facts.
3. **Discover with two lanes.** Search high-probability tracked/adjacent targets and preserve an explicit exploration lane for unseen opportunities. Default strategy is adaptive rather than a fixed 70/30 quota: increase exploration when catalogue diversity or discovery yield falls; increase tracked focus when known entities have volatile/new activity.
4. **Resolve canonical identity before promotion.** Merge aliases and duplicate sightings into one canonical resource when evidence supports equivalence. Do not force-merge ambiguous entities. Preserve alias/source identity evidence.
5. **Retrieve and screen decision evidence before qualification.** Resolve `review_policy` before promoting or presenting records. If visual criteria matter, retrieve real attributable images, save original bytes and persistent identities, then directly inspect the pixels yourself. Evaluate each required dimension against the exact profile: tags, captions, actor fame, model memory and lean/fit proxies do not establish stronger muscularity requirements. Mark obscured dimensions unknown. Fail/unknown stays a lead or hold; do not label it high-potential from metadata or delegate your first screening to the Creator. If scene proof is inaccessible, search for attributable resource photos for resource review; label them explicitly and keep the scene unresolved. Record confidence and rationale, without a magic score.
6. **Present retained proof and record scoped Creator decisions.** Display the saved image alongside identity, source, what it demonstrates and unknowns before requesting acceptance. Keep DEDAL screening, catalogue insertion, resource acceptance and opportunity acceptance separate. Creator-relative acceptance is never implied by confidence, lifecycle, ranking or silence. Bind the explicit decision/reason/time to the exact displayed proof; resource acceptance cannot accept opportunities automatically. Preserve rejections and suppress their rediscovery. See `references/resource-profile-and-record-model.md` for typed evidence/reviews and `scripts/resource_review.py` for declared-evidence checks.
7. **Persist provenance.** Every material claim/state must retain source, observed time, freshness/validity information when available, evidence class, confidence, and supersession/change history.
8. **Refresh by delta, not blind repetition.** On later runs, read the existing tracked set first, identify stale/volatile fields, perform targeted refresh plus bounded exploration, and classify material results as `NEW | CHANGED | CONFIRMED | STALE | NO_CHANGE | REMOVED_OR_UNAVAILABLE | CONFLICT`.
9. **Prioritize attention.** Use interpretable factors such as profile fit, freshness, change magnitude, unresolved value, evidence confidence, opportunity density, and downstream relevance. Human-readable bands are preferred over opaque universal scores.
10. **Handoff without ownership leakage.** Consumers receive canonical resource identity, qualification basis, relevant changes, evidence/provenance, uncertainty, and source pointers. The downstream owner re-applies its own domain gates.
11. **Learn prospectively.** Later downstream outcomes may update private profile weights or heuristics, but never rewrite the evidence that supported an earlier decision.

## Persistent-state rules

Public Core contains only generic schemas, workflow contracts, examples, routing, and evals. Actual tracked resources, Creator preferences, selections/rejections, private outcome history, and private watchlists belong in `/DEDAL/private-overlay/resource-intelligence/` or another registered private workstream path.

Canonical state is not a pile of dated search reports. Maintain stable identities for the current catalogue/profile, preserve immutable discovery/change evidence separately, and regenerate derived indexes from canonical records.

A record may be useful without being fully verified. Keep `candidate`, `tracked`, `watch`, `hold`, `retired`, and analogous lifecycle states distinct from confidence. Unknown is not false; missing search evidence is not zero opportunity.

## Search strategy

Do not blindly re-search the whole universe every run. Before external discovery:

- load the relevant tracking profile and canonical current catalogue;
- identify due/stale tracked resources and unresolved leads;
- derive targeted queries from known aliases, adjacent entities, source families, and changed context;
- reserve bounded exploration for novel entities/sources;
- stop expansion when marginal qualified yield is low or the task's evidence budget is reached.

See `references/discovery-refresh-and-change-detection.md`.

## Evidence and contradiction discipline

Source authority is claim-specific. A vendor page may own current package version but not community adoption; a paper publisher may own bibliographic identity but not practical quality; a niche catalogue may be a discovery signal but not downstream demand. Preserve contradictory claims rather than flattening them prematurely.

Never promote model memory, a prior generated summary, or a derived index above current canonical records and live authoritative sources.

## Visual proof and acceptance gates

Use visual review only when the profile requires it; resolve an explicit nonvisual policy for packages/papers rather than demanding pictures everywhere. For visual resources, preserve evidence scope and authenticity. A portrait may establish identity/face but cannot prove obscured physique; a resource photo cannot prove a particular scene, episode or duration. Never generate a lookalike as discovery proof.

Verify actual bytes/content type, not extension: an HTML error page named `.mp4` or `.jpg` is unavailable evidence. Try a bounded alternate image source when direct scene access fails; do not bypass access restrictions. If only a transient search preview is displayable, label it unsaved and keep acceptance blocked until a retrievable retained proof is available. Explicit rejection can still be recorded without pretending retained proof exists.

Before closing a review/handoff, run `scripts/resource_review.py` for the relevant scope with an `--asset-paths` map when local pixels are available. A pass checks declarations, chronology, references and optional bytes; it does not independently certify visual quality, genuine Creator consent, future retrieval, or host interception. Actual image inspection and Creator/tool evidence remain necessary. Missing legacy policy/evidence means unreviewed, not accepted. Migrate from authoritative scoped decision/proof history without inventing read/display events.

## Success criteria

A successful run should reduce repeated search work while preserving discovery diversity. Contract validation can prove schema/routing/state discipline; only representative real workflows can prove improved time-to-qualified-resource, precision, recall, or downstream outcomes.

## References

- `references/resource-profile-and-record-model.md`
- `references/discovery-refresh-and-change-detection.md`
- `references/storage-privacy-and-consumer-handoffs.md`
- `schemas/resource-profile.schema.json`
- `schemas/resource-record.schema.json`
