---
name: candidate-video-finder
description: Discover, verify, evaluate, and shortlist scene-level video candidates for a Creator-owned YouTube channel before production, using source truth, channel evidence, bounded public demand/competition observations, risk signals, and explicit Creator selection.
---

# Candidate Video Finder

Own the upstream decision layer that turns broad source/topic possibilities into a small evidence-backed shortlist of **specific scene-level candidates**. Stop before media cutting, SEO packaging, thumbnail creation, or YouTube mutation.

## Trigger when

Use this skill when the Creator wants to:

- find promising scenes/videos to make next for a known channel or niche;
- inspect a film/series/episode/franchise for clip-worthy moments;
- compare candidate scenes using demand, competition, freshness, channel fit, or risk evidence;
- build or revisit a candidate shortlist before Video Production starts;
- learn which candidate-selection hypotheses were supported by later channel outcomes.

Do **not** route here merely because an already-prepared video needs SEO, a thumbnail, editing, or publishing.

## Ownership boundary

Candidate Video Finder owns:

`discover -> identify source/scene -> verify -> hard-gate -> evaluate -> shortlist -> Creator selection`

It composes with:

- **Research** for current external facts, release/episode verification, trends, and non-YouTube source evidence;
- **YouTube SEO** for YouTube discovery-surface reasoning, owned analytics interpretation, and later packaging/measurement;
- **Video Production** only after selection, for local audiovisual verification and exact editorial boundaries;
- **Visual Direction** only downstream of a verified content/thumbnail strategy brief;
- **YouTube Publishing** only after production/packaging approval, for authenticated YouTube operations.

Candidate Finder has no publication or channel-mutation authority.

## Candidate definition

A candidate is not an entire movie, series, season, or episode. It is a **specific bounded scene, action, performance, interaction, or event** from an identifiable source that can plausibly become an intentional clip.

Prefer the smallest self-contained editorial unit that preserves the requested moment and enough setup/resolution to feel deliberate. External timestamps are locator evidence, not final cut authority.

## Core workflow

1. **Frame the search.** Resolve target channel/profile context, niche, source universe, time/freshness window, language/region when material, and whether the run is exploratory, production-oriented, evergreen, or news/reactive.
2. **Generate candidates broadly but boundedly.** Use owned channel history, public YouTube observations, official/source metadata, current web/trend evidence, and community salience only for the claims each source can support.
3. **Resolve source identity.** Identify work, installment/episode when applicable, named entities, and the exact claimed scene/event. Never promote a remembered or fan-labeled scene to fact without evidence.
4. **Verify scene existence.** Prefer official/source metadata when available; once local media exists, local audiovisual evidence outranks external locators for exact scene truth.
5. **Apply hard gates.** Require source identity, scene existence, bounded editorial viability, channel relevance, duplicate/cannibalization check, truthful packaging viability, minimum evidence, and no unresolved blocker that warrants `RISK_HOLD`.
6. **Build an evidence vector.** Preserve scene salience, channel fit, owned-channel evidence, observed demand, saturation, exact-scene gap, authoritative competition, freshness, novelty, Suggested adjacency, packaging potential, editorial self-containment, source accessibility, reuse-risk signals, and evidence confidence.
7. **Do not hide uncertainty in a magic score.** Use qualitative opportunity bands by default. A convenience heuristic is allowed only for large candidate sets and must expose components/provenance; it cannot override a failed hard gate.
8. **Shortlist for the Creator.** Present a small interpretable set with why it may work, main weakness, evidence confidence, source status, observed risk, and a **decision visual aid** when one is available. If the discovery/source page exposes a directly viewable scene page, preview, or media link that can be safely shared, resolve and verify the current URL and surface it with the candidate. Do not hide an available scene/preview link behind prose. If no usable visual aid is available, say so explicitly. The Creator decides `SELECT | MAYBE | PASS | HOLD | NEVER`.
9. **Handoff cleanly.** Selected candidates go to Video Production with source/scene/locator truth. Verified content then flows to YouTube SEO, Visual Direction, and Publishing through their existing contracts.
10. **Learn prospectively.** Preserve the pre-publication candidate hypothesis. After 24h/3d/7d/28d or other planned windows, compare outcomes without rewriting history and keep channel/Creator-specific learning private.

## Hard gates

A candidate does not enter the normal shortlist unless these are satisfied or explicitly marked as a hold:

- **G1 Source identity** — the underlying source is identifiable with adequate confidence.
- **G2 Scene existence** — the claimed moment is verified/probable from actual evidence, not model memory alone.
- **G3 Bounded editorial unit** — the moment can become an intentional clip rather than requiring the whole source.
- **G4 Channel relevance** — it plausibly fits the channel's established/Creator-approved domain; raw popularity is insufficient.
- **G5 Duplicate/cannibalization** — exact prior uploads or materially equivalent scenes are resolved.
- **G6 Truthful packaging viability** — at least one honest viewer-facing title/thumbnail promise exists.
- **G7 Minimum evidence** — enough provenance exists to evaluate rather than guess.
- **G8 Risk viability** — unresolved elevated signals may route to `RISK_HOLD`; the skill never claims legal clearance.

Detailed record semantics live in `references/candidate-record-and-gates.md`.

## Evidence discipline

Reuse the YouTube SEO evidence classes where applicable:

- **A — OWNED_FIRST_PARTY**: Creator-owned Analytics/Reporting/Studio/read-back evidence.
- **B — OFFICIAL_PUBLIC**: official source/platform documentation or source metadata.
- **C — LIVE_SEARCH_OBSERVATION**: bounded current public YouTube/search-result observation.
- **D — EXTERNAL_METHOD**: third-party/open-source methodology used comparatively.
- **E — COMMUNITY**: discussion/anecdote useful mainly for discovery/salience.

Authority is claim-specific. Owned analytics can establish what happened on the channel but not prove a scene exists. Official episode metadata can establish source facts but not YouTube demand. Search results are observations, not universal volume/rank claims.

Never infer `zero demand` from missing/suppressed analytics detail. Never invent absolute YouTube search volume, universal keyword difficulty, scene timestamps, episode identity, view counts, or copyright certainty.

## Default shortlist surface

For each shortlisted item show, in human-readable form:

`Candidate | Source | Scene | Opportunity band | Evidence confidence | Why it may work | Main weakness | Risk signal | Source status | Visual aid`

Use `STRONG | PROMISING | UNCERTAIN | WEAK` as triage bands, not objective universal ratings. Preserve the underlying factor vector.

### Decision visual-aid rule

For every shortlisted candidate, attempt to surface the strongest currently usable decision aid that already exists in the evidence chain:

1. prefer the exact scene/preview/media URL exposed by the discovery/source page;
2. otherwise surface the exact scene page or official preview/clip page;
3. verify that the URL still resolves before presenting it when practical;
4. label what the link is (`direct scene/preview`, `scene page`, `official clip`, or `locator only`);
5. if the page exposes a direct media URL, include it in addition to the page URL when it is safe and technically available;
6. if no usable visual aid exists, state `Visual aid: unavailable` rather than omitting the field.

A visual-aid link is evidence for Creator review only. It is not proof of reuse rights, copyright clearance, source ownership, or final cut suitability. Candidate Finder must not download or republish third-party media merely because a preview URL is available.

## Risk boundary

Return observed risk as `low_observed | moderate | elevated | unknown`. Consider raw-scene similarity, official-source dominance, music dependence, clip-length dependence, source/platform restrictions, previous channel enforcement patterns, and transformative/editorial context when evidence exists.

Do not output `copyright safe`, `fair use guaranteed`, or other legal certainty.

## Private/public boundary

Public Core may contain generic lifecycle, schema, gates, evidence methodology, handoff contracts, sanitized examples, and evals.

The private operational overlay owns real channel/video IDs, private Analytics rows, actual candidate ledgers, Creator selections/rejections, niche weights, learned actor/franchise/scene preferences, candidate-to-outcome history, and any private risk/enforcement history.

## References

- `references/candidate-record-and-gates.md`
- `references/discovery-evidence-and-risk.md`
- `references/handoffs-and-learning.md`
