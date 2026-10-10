# CV QA contract v1

A release-quality CV must pass: (a) source claim ledger including exact dates and titles, (b) explicit output mode (human visual vs ATS safe), (c) no unauthorized text, (d) no overflow/overlap, (e) adequate readable body text at A4 actual size, (f) no cropped/clipped portrait or text, (g) file open/save roundtrip, (h) PDF page count and extracted facts, (i) visual review of all pages, and (j) signoff that files actually rendered as shown.

Suggested measurements: PPTX text-box safe width and occupied height using font metrics; PDF line positions against page area; intentional overlap whitelist for backgrounds, decorations, frames only; title/subheading bounding box checks; no body type under 9pt without an explicit exception; no text hidden behind icons. Do not take a heuristic bounding-box pass as proof that the final renderer wraps identically.

Regression fixtures: employer name longer than a column, job date spanning a second line, five or more appointments, long professional summary, two-column clinical competencies, photo/sidebar geometry, footnote/agent-note contamination, PPTX-to-PDF font replacement, and ATS-safe text order.

Failure handling: failed gate -> revise document -> rerender all pages -> rerun checks. Persist only sanitized generic learnings to public Core; keep identity photos and personal CVs private.

External reference influences (guidance synthesized, no quoted templates): university career center ATS/plain-format guidance, employer-specific submission requirements, legibility/accessibility conventions; sourced research must be dated when used.
