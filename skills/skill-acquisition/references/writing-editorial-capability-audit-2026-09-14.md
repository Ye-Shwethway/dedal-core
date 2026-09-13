# Writing / Editorial Engineering — Capability Audit 2026-09-14

## Gap

DEDAL could already draft, rewrite, translate, and explain, but lacked one reusable editorial contract that explicitly separated factual content from expression, protected semantic invariants during transformations, governed terminology/voice, and handled multilingual fidelity and publication QA across domains.

## Sources reviewed

### Google Developer Documentation Style Guide
Current web guidance reviewed 2026-09-14.
High-value patterns:
- project/product-specific style has priority over generic style guidance;
- stable terminology and capitalization reduce ambiguity and translation friction;
- global-audience writing benefits from concise, unambiguous structures and reduced idiom/culture-specific phrasing;
- reader needs and task context should drive wording.

Classification: **Adapt / Merge**.

### NIST technical-series and inclusive-language guidance
Current guidance reviewed 2026-09-14.
High-value patterns:
- plain language should serve anticipated readers without sacrificing necessary technical precision;
- proofreading, organization, accessibility, and terminology review belong to publication quality;
- inclusive wording is a clarity/comprehension concern, not merely a banned-word table.

Classification: **Adapt / Merge**.

### Anthropic prompting guidance
Current prompting guidance reviewed 2026-09-14.
High-value pattern:
- explicit examples/format/style instructions improve model steerability for generated prose.

Classification: **Conceptual merge only**. Provider/model-specific prompting details are not editorial law.

### Vale
Repository: `vale-cli/vale`
Pinned commit: `cf649e6e7089804dd1bad745fdcd12aeee7f7aae`
License: MIT verified.
High-value patterns:
- style/terminology rules can be made executable and reusable;
- linting is strongest for repeatable, mechanically detectable defects.

Classification: **Adapt pattern, do not vendor/runtime-depend**.

## DEDAL-native decisions

### Adopt / Adapt
- intent/audience contract before prose;
- project/user style hierarchy;
- fact/expression separation;
- semantic invariants for rewrite/translation;
- targeted revision passes instead of undirected repeated rewriting;
- terminology maps for repeated work;
- global-audience and multilingual discipline;
- proportional publication QA;
- optional executable lint for recurring detectable rules.

### Reject as universal
- one fixed “good writing” voice;
- blanket short-sentence targets regardless of genre/audience;
- US-English or technical-doc conventions for all tasks;
- literal translation as the default fidelity metric;
- automated readability/lint scores as proof of quality;
- mandatory multiple revision passes for trivial messages;
- provider-specific prompt syntax as durable Core behavior.

## Boundary with other skills

- Research owns external factual verification; Writing/Editorial controls how verified facts are expressed.
- Domain skills own specialized truth/terminology/policy; Writing/Editorial may transform language but cannot override them.
- Interface Design owns product-surface UX behavior/visual hierarchy; Writing/Editorial may support UX copy.
- Files/Docs own document mechanics and file formats.

## Promotion decision

**Promote as independent generic skill.** The work is frequent, independently routable, cross-project, and has failure modes not adequately covered by Research, Files, or generic model writing behavior.
