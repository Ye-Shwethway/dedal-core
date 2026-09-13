# Architecture and Domain Design

Use when shaping module boundaries, interfaces, domain language, or architecture changes.

## Deep-module heuristic

Prefer a small interface that hides meaningful complexity. A good module gives callers **leverage** and maintainers **locality**: callers learn less, and related change/bugs/knowledge stay concentrated.

Useful questions:
- Can the public surface be smaller or simpler?
- Does this abstraction hide real complexity or merely pass calls through?
- If the module disappeared, would its complexity reappear across many callers?
- Is a proposed seam real because behavior actually varies there, or merely hypothetical?
- Can tests and callers use the same stable interface?

## Seam discipline

A seam is a place where behavior can vary behind an interface. Prefer dependencies supplied from outside over hidden construction when variation/testing genuinely matters. Avoid adding abstraction solely for hypothetical future implementations.

## Domain language

Read project-local context/glossaries and relevant ADRs before inventing terminology. Use established domain nouns consistently in code, tests, issues, and docs.

When a new concept or architectural decision genuinely crystallizes, update the appropriate context/ADR/architecture record. Do this lazily from real decisions rather than creating documentation ceremony upfront.

If a proposed design conflicts with an existing ADR or accepted decision, surface the conflict explicitly; do not silently override it.

## Design alternatives

For high-impact interfaces, consider at least two meaningfully different designs before locking one. Compare them on interface complexity, locality, testability, migration cost, reversibility, and fit with existing architecture.

Project-local terminology and conventions outrank this reference's vocabulary.
