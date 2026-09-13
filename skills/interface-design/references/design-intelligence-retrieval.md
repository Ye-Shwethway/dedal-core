# Design Intelligence Retrieval

Use this reference when interface work benefits from a design knowledge catalog, platform/design-system corpus, project-local design docs, or live authoritative guidance.

## Retrieval hierarchy

Prefer evidence in this order when applicable:
1. explicit Creator direction and accepted project design decisions;
2. incumbent project UI, components, tokens, assets, and surface-specific overrides;
3. authoritative platform/design-system/accessibility documentation;
4. curated design intelligence or rule catalogs with known provenance/freshness;
5. general design heuristics and model judgment.

A lower layer must not silently override a higher one.

## Query the smallest domain

Do not load an entire design corpus for every UI task. Choose the smallest useful concern:
- product/surface pattern;
- visual style family;
- semantic color/palette;
- typography;
- accessibility/UX behavior;
- forms/feedback;
- navigation;
- motion;
- responsive layout;
- charts/data visualization;
- implementation stack/platform.

For a new product/page direction, combine a small set of complementary domains into a coherent design system. For a targeted defect, query the defect's semantic UX outcome first and implementation stack separately if needed.

## Domain and stack are separate evidence

A semantic UX rule answers **what good behavior is**. Stack/platform guidance answers **how to implement it here**. Do not let framework keywords replace the underlying UX question.

Detect stack from the live project when possible. If stack-specific advice materially matters and cannot be determined, ask or state the uncertainty; do not assume a fashionable default.

## Match confidence and fallback

Treat retrieval as evidence, not magic:
1. inspect returned identity/category and fit;
2. reject clearly off-topic or stale matches;
3. if there is no credible match, retry once with a narrower query or explicit domain;
4. if still unmatched, say so and use clearly labeled general guidance.

Never convert a zero-result, weak match, or unrelated result into a claimed catalog recommendation.

## Freshness

Catalog entries that mention framework versions, packages, APIs, accessibility criteria, official design systems, performance behavior, or platform conventions can drift. Record source/version/review date when available and verify current authoritative state before consequential implementation when drift matters.

Stable aesthetic concepts need less refresh than technical/platform claims.

## Synthesis

A design recommendation should explain fit rather than concatenate search results. Resolve conflicts using the brief, user job, accessibility, incumbent truth, and platform constraints. Keep one coherent direction and surface meaningful uncertainty instead of averaging incompatible recommendations.

## Privacy and execution

Do not send confidential project text, patient data, secrets, or private business information to third-party search services merely to improve design retrieval. Prefer local or trusted sources. Do not install or execute an external design skill/CLI solely to inspect its ideas.
