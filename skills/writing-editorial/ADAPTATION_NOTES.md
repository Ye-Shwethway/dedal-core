# Adaptation Notes — Writing / Editorial Engineering

_Date: 2026-09-14_

This skill is a DEDAL-native synthesis. No third-party writing package, linter, model prompt bundle, or executable was installed or run for the adaptation.

## Primary public sources

### Google Developer Documentation Style Guide
Reviewed 2026-09-14.
Retained patterns:
- project-specific style outranks generic style guidance;
- clarity/consistency for a defined audience;
- stable terminology and capitalization;
- global-audience/translation-aware wording;
- direct reader/task orientation.

Rejected as universal rules:
- Google-specific product conventions;
- US-English defaults where the Creator or target context requires another language or locale;
- technical-documentation-only assumptions.

### NIST technical/publication guidance
Reviewed 2026-09-14.
Retained patterns:
- plain, precise language for anticipated readers;
- proofreading and publication QA;
- terminology choices should preserve technical comprehension;
- accessibility/inclusive wording is contextual and reader-centered rather than a fixed replacement list.

Rejected as universal rules:
- NIST-specific publication templates and administrative requirements;
- government-report structure as the default for ordinary writing.

### Anthropic prompting guidance
Reviewed 2026-09-14; conceptual use only.
Retained pattern:
- explicit output/format/style constraints and examples can materially improve model steerability.

Rejected:
- provider/model-specific prompt syntax as durable editorial truth.

### Vale
Repository: `vale-cli/vale`
Pinned branch snapshot: `cf649e6e7089804dd1bad745fdcd12aeee7f7aae`
License: MIT.
Retained pattern:
- repeatable editorial/style requirements can be externalized into executable lint rules;
- automated style checks are useful as detectors but do not replace contextual editorial judgment.

Not adopted:
- Vale runtime/config syntax;
- any bundled style package as DEDAL’s universal style;
- mandatory linting for every writing task.

## DEDAL-specific synthesis

DEDAL separates editorial work into intent/audience, factual/content layer, structure, terminology, voice, multilingual fidelity, and surface polish. This avoids a common failure mode where a “rewrite” silently changes facts while improving fluency.

The skill is independently routable because writing/translation/editing recur across technical, operational, medical, product, and creative-adjacent workflows, while domain truth remains owned by the relevant domain skill/source.
