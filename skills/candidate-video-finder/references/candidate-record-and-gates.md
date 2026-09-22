# Candidate Record and Hard Gates

## Canonical record

Fields may be omitted when genuinely unavailable; unknowns must not be invented.

```yaml
candidate_id: cvf:<private-stable-id>
identity:
  source_type: movie|series|episode|other
  source_title:
  season:
  episode:
  episode_title:
  release_year:
  scene_label:
  scene_description:
  primary_entities:
    actors: []
    characters: []
    actions_topics: []
discovery:
  discovered_at:
  discovery_source:
  discovery_reason:
  seed_query:
  related_candidates: []
source_truth:
  source_identity_status: verified|probable|unverified
  scene_exists_status: verified|probable|unverified
  locator_evidence: []
  approximate_timestamps: []
  local_media_available: true|false|unknown
  verification_notes:
decision_aids:
  scene_page_url:
  preview_url:
  direct_media_url:
  aid_kind: direct_scene_preview|scene_page|official_clip|locator_only|unavailable
  verified_at:
  accessibility_notes:
editorial:
  candidate_unit: action_only|contextual_action|mini_scene|performance|dialogue|other
  self_containedness:
  estimated_clip_duration:
  hook_strength:
  resolution_quality:
  editorial_notes:
channel_fit:
  niche_fit:
  known_channel_adjacency:
  existing_similar_uploads: []
  duplication_status: none|partial|duplicate|unknown
  creator_interest: selected|positive|neutral|negative|unknown
opportunity:
  observed_demand:
  owned_channel_evidence:
  result_saturation:
  exact_scene_gap:
  authoritative_competition:
  freshness:
  novelty:
  suggested_adjacency:
  packaging_potential:
risk:
  reuse_risk:
  raw_scene_similarity:
  music_dependency:
  official_source_dominance:
  prior_channel_risk_signal:
  source_restriction_signal:
  unknowns: []
evidence:
  - evidence_id:
    class: A|B|C|D|E
    source:
    observed_at:
    supports:
    observation:
    confidence:
assessment:
  hard_gate_status: pass|fail|hold
  opportunity_band: strong|promising|uncertain|weak
  evidence_confidence: high|medium|low
  risk_band: low_observed|moderate|elevated|unknown
  key_reasons: []
  blockers: []
workflow:
  status:
  creator_decision: SELECT|MAYBE|PASS|HOLD|NEVER|unset
  selected_at:
  production_handoff_ref:
  seo_handoff_ref:
```

## Decision-aid presentation

When a candidate is shortlisted, populate `decision_aids` from evidence already discovered during source/scene verification. A directly viewable scene/preview/media URL should be surfaced to the Creator when available and safe to share; otherwise provide the exact scene page or official clip page. Do not omit an available visual aid. If none is available, set `aid_kind: unavailable`. These links are decision support only and never imply reuse rights or legal clearance.

## Lifecycle

`DISCOVERED -> IDENTIFIED -> SOURCE_VERIFIED -> SCENE_VERIFIED -> GATE_PASSED -> EVALUATED -> SHORTLISTED -> CREATOR_SELECTED -> HANDED_TO_PRODUCTION`

Terminal/paused states: `REJECTED | DUPLICATE | INSUFFICIENT_EVIDENCE | SOURCE_UNAVAILABLE | RISK_HOLD | SUPERSEDED`.

## Gate behavior

### G1 Source identity
Pass only when the work/installment identity is sufficiently grounded for the intended decision. Conflicting episode/source identities remain unresolved rather than guessed.

### G2 Scene existence
A fan title, memory, or model recollection is locator evidence at most. Require supporting source evidence. Local audiovisual inspection becomes authoritative once source media is available.

### G3 Bounded editorial unit
The moment must be isolatable as action-only, contextual action, mini-scene, performance, dialogue, or another intentional unit. Fragmented moments may remain `HOLD` until a coherent unit is found.

### G4 Channel relevance
Use the private channel profile/history. Popularity cannot by itself override a niche mismatch.

### G5 Duplicate/cannibalization
Exact prior publication normally fails. Partial overlap can proceed only when the editorial unit or viewer promise is materially distinct and that distinction is recorded.

### G6 Truthful packaging viability
At least one honest viewer-facing promise must exist. If the only compelling package misrepresents the scene, fail.

### G7 Minimum evidence
One community mention, one opaque third-party score, or model memory is insufficient by itself. Evidence quantity is not fixed; adequacy depends on claim importance and source authority.

### G8 Risk viability
Risk is a triage signal, not legal judgment. An unresolved elevated condition may route to `RISK_HOLD` for Creator review or further research.

## Opportunity bands

- **STRONG** — multiple independent positive signals, adequate source truth/channel fit, and no unresolved blocker.
- **PROMISING** — clear reasons to consider, with meaningful but manageable uncertainty.
- **UNCERTAIN** — interesting but evidence is weak/conflicting/incomplete.
- **WEAK** — valid candidate with little current reason to prioritize.

Bands are decision aids, not universal quality scores.
