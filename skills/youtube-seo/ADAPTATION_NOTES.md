# YouTube SEO — Adaptation Notes

Reviewed: 2026-09-16
Decision: DEDAL-native synthesis; no third-party code or instructions imported verbatim.

## Capability gap

YouTube Publishing already owns authenticated YouTube operations and bounded analytics transport, but repeated Creator work exposed a distinct need for discovery research, surface-specific packaging, analytics diagnosis, experiments, and channel-specific learning. That intent is independently routable and should not overload publishing/mutation mechanics.

## Primary evidence

First-party YouTube/Google documentation informed the platform-truth boundary: Search relevance/engagement/quality, metadata semantics, Data API search, Analytics traffic/search/retention, Reporting Reach reports, Studio Trends, CTR interpretation, and native title/thumbnail experiments.

## External patterns reviewed

- `deeployCO/youtube-seo-skills`, release `v0.1.0` (`b853be5`), MIT — comparative patterns for surface classification, entity/topic coverage, competition proxies, and refusal to fabricate unavailable first-party metrics.
- `adityaarsharma/youtube-marketing-skills`, reviewed 2026-09-16, MIT — private Analytics + MCP write-back, command decomposition, and analysis-to-action separation.
- `adamgordonbell/youtube-analytics-tool`, reviewed 2026-09-16, MIT — search-term analysis, traffic-source breakdown, historical persistence, and first-week comparisons.
- `m0ntydad0n/pseo-engine-oss`, reviewed 2026-09-16, Apache-2.0 — source-backed pipelines, information-gain/review gates, schema validation, and public/private separation.
- vidIQ and TubeBuddy public methodology/documentation — comparative evidence only for packaging emphasis, estimated keyword models, and metadata experiment design.
- creator-community discussions — hypothesis-generating evidence only, never authority.

## Adopted patterns

- Search/Browse/Suggested/Shorts surface classification.
- Entity/topic graph before query expansion.
- Transparent competition/opportunity factor vector.
- Comparable-age analytics windows and traffic-source-aware diagnosis.
- Proposal/approval/mutation/read-back separation.
- Hypothesis-first experiments with explicit confounders.
- Private channel learning separated from sanitized generic Core lessons.

## Rejected or constrained patterns

- proprietary-looking absolute search volume without a supported source;
- universal keyword-difficulty or SEO scores presented as truth;
- tag-count optimization as a primary strategy;
- fixed title-flip timing independent of traffic-source evidence;
- unofficial autocomplete/scraping endpoints as required infrastructure;
- single-query/region result position treated as durable rank;
- sequential metadata changes described as clean A/B tests;
- bulk auto-optimization without review;
- copying competitor metadata instead of extracting gaps/patterns.
