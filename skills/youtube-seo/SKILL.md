---
name: youtube-seo
description: Research, package, diagnose, experiment, and learn from YouTube discovery performance using first-party channel analytics, public search evidence, transparent heuristics, and the existing YouTube Publishing execution surface.
status: active
---

# YouTube SEO

Own the discovery-intelligence layer around YouTube publishing. Optimize for the surface that actually matters—Search, Browse, Suggested, or Shorts feed—using evidence that is available and explicitly labeling evidence that is estimated, observational, or unavailable.

## Use when

- researching queries, topics, entities, competing result sets, seasonality, or content gaps for a YouTube video or channel;
- preparing title, description, tag, playlist, thumbnail-brief, or packaging recommendations before publication;
- diagnosing an existing video's search/discovery performance from traffic sources, search terms, retention, impressions/CTR, or age-normalized history;
- planning or interpreting title/thumbnail experiments;
- deciding whether a candidate is a Search, Browse, Suggested, mixed, or Shorts-feed opportunity;
- extracting channel-specific discovery lessons for the private operational overlay.

## Ownership boundary

YouTube SEO owns discovery research, intent/entity modeling, surface classification, transparent opportunity factors, packaging hypotheses, analytics diagnosis, experiment design/readout, and discovery-learning synthesis.

It does **not** replace:
- YouTube Publishing for authenticated channel targeting, metadata writes, uploads, privacy/scheduling, playlists, thumbnails, captions, analytics transport, or other YouTube mutations;
- Research for external factual claims and current platform-policy verification;
- Visual Direction for creating/editing thumbnail art;
- Writing/Editorial for substantial prose beyond bounded metadata packaging;
- Video Production for the media master, opening hook/edit, audio, captions, or temporal quality;
- Quality Engineering for independent readiness/acceptance when a separate verifier is warranted;
- the YouTube Data/Analytics/Reporting APIs, Studio UI, MCP, Gateway, browser, or other execution surface.

## Core rule

**Do not turn missing data into fake precision.**

Never present an absolute YouTube keyword search volume, universal keyword difficulty, guaranteed rank, universal CTR benchmark, or causal claim unless the underlying evidence actually supports it. A DEDAL combined score, if explicitly useful, must be labeled a heuristic and expose its component factors/provenance.

## Default workflow

1. **Define the object and objective.** Resolve the exact video/candidate, audience, content truth, channel/profile context, and whether the task is launch research, existing-video diagnosis, experiment planning, or channel learning.
2. **Map entities and intent.** Extract the smallest useful graph: franchise/show/film, season/episode, character/actor, scene/action/event, relationship/quote/topic, plus obvious variants or misspellings.
3. **Classify discovery surface.** State the primary hypothesis: Search, Browse, Suggested, mixed, or Shorts feed. Do not apply one SEO template to every surface.
4. **Collect bounded evidence.** Prefer first-party owned-channel analytics, then official APIs/docs, then live public search observations. Use external tool/community methodology only as lower-authority comparative evidence.
5. **Build a factor vector, not a magic score.** Track semantic relevance, entity specificity, observed channel evidence, trend evidence, result saturation, exact-match gap, authoritative competition, freshness, channel fit, packaging fit, and later post-publish response.
6. **Propose packaging.** Produce a primary package plus deliberately different alternates when useful: title, description, minimal tags, playlist placement, and thumbnail promise/brief. Keep the package truthful to the actual video.
7. **Preflight.** Check API limits, factual fit, duplicate/cannibalization risk, target playlist/niche, title-thumbnail promise consistency, and whether the proposed change could damage an already-performing surface.
8. **Separate proposal from mutation.** Hand writes to YouTube Publishing. Consequential changes retain its ownership/intent/read-back gates.
9. **Evaluate on normalized windows.** Prefer comparable-age windows (launch/early/first-week/28-day/mature) and segment by traffic source when possible. Do not compare a new upload's raw lifetime totals with an old video's lifetime totals.
10. **Learn with provenance.** Store Creator/channel-specific evidence in the private operational overlay; promote only sanitized generic lessons to public Core.

## Evidence classes

Use these labels when they materially improve traceability:

- **A — OWNED_FIRST_PARTY:** Creator-owned YouTube Analytics/Reporting/read-back or Creator-confirmed first-party Studio evidence.
- **B — OFFICIAL_PUBLIC:** current YouTube/Google API documentation or official public guidance.
- **C — LIVE_SEARCH_OBSERVATION:** bounded public YouTube search-result observation at a stated time/region/query.
- **D — EXTERNAL_METHOD:** third-party/open-source methodology or aggregated tool model.
- **E — COMMUNITY:** creator/community anecdote or discussion.

Higher classes do not automatically answer every question; use the source that actually measures the claim.

## Surface strategy

### Search
Prioritize exact user intent, entity clarity, truthful query-title alignment, relevant description context, and observed search-term feedback. Search-result position is an observation, not a durable rank claim.

### Browse
Prioritize idea/packaging appeal, title-thumbnail promise, and downstream engagement/satisfaction. Do not force awkward keyword phrasing merely to improve lexical match.

### Suggested
Prioritize adjacency: entities, topic/scene relationships, format compatibility, session-chain logic, and packaging that fits nearby viewing behavior without copying competitors.

### Shorts feed
Treat feed discovery separately from long-form Search/Browse assumptions. Use fresh first-party evidence when materially different Shorts semantics apply.

## Analytics diagnosis

When the surfaces are available, combine rather than isolate:
- `YT_SEARCH` terms and traffic-source detail;
- traffic-source mix;
- views/engaged views, watch time, average view duration/percentage;
- per-video retention and relative retention;
- thumbnail impressions/CTR from YouTube Reporting Reach reports;
- playlist/referral contribution;
- experiment results and age-normalized history.

Privacy thresholds may suppress low-volume search terms/detail rows. Missing detail does not prove zero demand or zero traffic.

## Experiment rules

- Record a hypothesis before changing metadata.
- Prefer YouTube native title/thumbnail Test & Compare when eligible and available.
- Treat sequential before/after metadata changes as weaker quasi-experiments because time, audience expansion, and traffic-source mix can confound them.
- Record changed fields, observation window, traffic-source context, confounders, outcome metrics, and evidence class.
- Do not "rescue" a performing video with bulk optimization merely because a generic score is low.

## Current execution assumptions

- Existing typed YouTube search-term and Analytics summary paths are useful first-class inputs when live-verified.
- Public search research should remain bounded and quota-aware.
- Reach/impressions/CTR should use Reporting API when the live transport is validated; do not assume schema exposure proves runtime success.
- Studio Trends and native A/B surfaces may require Creator/UI-assisted evidence where no supported public API exists.

## Progressive references

- `references/evidence-and-opportunity-model.md`
- `references/mvp-workflows.md`
- `ADAPTATION_NOTES.md`
