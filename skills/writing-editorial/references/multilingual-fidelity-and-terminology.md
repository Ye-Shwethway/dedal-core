# Multilingual Fidelity and Terminology

## Translation is a controlled transformation

Protect four layers separately:
1. **Meaning** — facts, scope, negation, modality, uncertainty, sequence.
2. **Function** — instruction, warning, explanation, persuasion, reassurance, legal/clinical notice, etc.
3. **Terminology** — preferred equivalents for domain terms, UI labels, proper names, units, abbreviations.
4. **Naturalness** — grammar, register, collocation, politeness, and readability in the target language.

Literal word order is not a fidelity requirement unless the Creator explicitly asks for literal translation.

## Terminology map

For repeated or consequential multilingual work, maintain a compact map:
`concept -> source term -> preferred target term -> forbidden/legacy variants -> notes`

Use one stable equivalent for one concept when possible. If multiple translations are context-dependent, record the distinction instead of alternating casually.

## Ambiguity handling

When source text is materially ambiguous:
- do not silently choose the most convenient interpretation;
- use surrounding/domain context if authoritative;
- preserve ambiguity when safe;
- otherwise surface the ambiguity and the consequence of each reading.

Minor stylistic ambiguity that does not affect meaning can be resolved naturally without ceremony.

## Global-audience writing

When content may be translated or read by non-native speakers:
- prefer short, unambiguous clauses;
- keep terminology and capitalization stable;
- avoid unnecessary idioms, wordplay, region-specific metaphors, and culture-bound examples;
- define uncommon abbreviations and specialist terms where the audience may not know them;
- keep subject/action relationships explicit.

## Numbers, units, dates, and names

Verify these independently from fluent prose. Localization may change formatting, but must not change the underlying value or identity. When date format could be ambiguous, prefer an unambiguous representation appropriate to the target audience.

## Back-check for high-risk translations

For medical, legal, safety, financial, operational, or public notices, perform a semantic back-check against the source after drafting. This is not necessarily a literal back-translation; verify that each decision-critical invariant survived.