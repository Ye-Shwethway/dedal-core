---
name: cv-resume-engineering
description: Build accurate, visually compelling and accessible CVs/resumes, with render-verified editable outputs and ATS-safe variants; use when creating, revising or diagnosing professional CVs, résumés and fellowship profiles.
---

# CV / Resume Engineering

## Ownership and routing
Own the CV-specific content architecture, job chronology reconciliation, professional relevance, layout geometry, visual and ATS variants, and submission QA. Pair with Writing Editorial (wording), Presentation Engineering (slide/document mechanics), Quality Engineering (measurable gates), Research (current application standards) as appropriate; smallest sufficient set. Never infer that rich graphics are ATS-compatible.

## Hard gates
1. **Evidence ledger** — inventory every candidate job title/date, degree, license, training, language level and claim from provided sources. Conflicts require resolution or an explicit provisional mark; never silently promote guesses to fact. Do not add certifications, outcomes, metrics, project successes, medical scope, or technologies not verified by the user's sources.
2. **Audience-specific architecture** — distinguish editable human-facing premium CV, PDF print/view version, and simple ATS-safe DOCX. Do not conflate a branded portfolio with a machine-parseable submission. Follow employer-specific instructions first.
3. **Creator authority** — explicit requested changes only. No authoring/agent/template/footer labels; no 'premium CV', 'updated on', unrequested dates, decorative factual claims, fake skill bars, irrelevant iconography or stock-profile images. No invented achievement scores.
4. **Content hierarchy** — identification/title and contact, concise differentiated professional profile, relevant appointments in reverse chronology, education/credentials and role-specific competencies; highlight evidence of responsibility rather than generic praise. Preserve correct degree/date/name spelling.
5. **Grid before text** — declare page dimensions, margins, safe area, column widths, card text rectangles, minimum font sizes and readable line spacing. Text belongs to a single defined container. Allocate space for wrapping at final renderer widths. Never crowd long hospitals or date pills into fixed one-line spans; simplify dates only when source truth is retained.
6. **Visual system** — reserve dramatic styling for meaningful hierarchy: contrast-safe navy/teal, intentional photography, restrained cards, repeatable spacing and consistent typography. Avoid empty bottom third, gratuitous repeated photo/sidebar or unrelated ornaments; page-two layout must remain balanced.
7. **Output integrity** — editable PPTX/DOCX where requested, plus PDF; never promise editability for flattened images. Preserve a single source of truth across deliverables.
8. **Render QA is mandatory** — export each format to PDF, rasterize every page at 150–200 dpi, inspect every page visually, run geometric intersection/overflow tests where measurable, inspect text extraction/order, and verify user-visible source fields. Repeat QA after every edit. No final label until zero clipping, zero unintentional overlap, no unreadable typography and approved page count.

## Stop conditions
Hold as draft when PDF text crosses intended bounding boxes, section titles wrap onto content, dates/truncated employers collide, body type is illegible at normal A4 viewing, exported PDF diverges from editable source, facts are unverified, or unapproved notes appear. Report specific failures instead of hiding them with tiny type.

## Domain-sensitive tailoring
Medical CV: distinguish clinical practice, administrative leadership, public-health responsibilities and digital-health strengths; professional license/qualifications need verification; do not interpret skill claims as board certification or practice authorization. One-page highlight may group early appointments only when full CV preserves individual career history.

## Evidence & evaluation
Use `references/qa-contract.md` and the local `scripts/validate_cv_layout.py` checker for structural/text checks. A machine pass cannot substitute for human visual inspection. Keep sensitive user profiles, personal photos and CV outputs outside public Core.
