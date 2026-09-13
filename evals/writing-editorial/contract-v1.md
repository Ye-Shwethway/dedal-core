# Writing / Editorial Engineering — Contract v1

## Routing assertions

1. A rewrite/translation/editing task where the main risk is meaning, tone, structure, terminology, or audience fit routes to `writing-editorial`.
2. A factual research task does not route to Writing/Editorial merely because the answer is prose; use Research when evidence gathering is primary.
3. Specialized domain rules remain authoritative; Writing/Editorial cannot rewrite domain truth.
4. Product UX copy may pair Writing/Editorial with Interface Design, but neither replaces the other.

## Behavioral assertions

### Intent and fidelity
- The workflow identifies or infers the intended reader/outcome before major rewriting.
- Rewrites preserve material facts, modality, negation, numbers, names, dates, uncertainty, and scope unless explicitly authorized to change them.
- Material factual changes trigger verification or are surfaced as content decisions.

### Structure and voice
- Structure follows reader task/decision flow rather than blindly preserving source order.
- Voice changes target explicit dimensions such as formality, warmth, directness, density, persuasion, or humor.
- The workflow does not impose one universal concise/formal/plain style on every genre.

### Terminology
- Preferred terminology remains consistent across one artifact or defined corpus.
- Project/domain terminology outranks generic style preferences.
- Deprecated/legacy variants may be preserved when required for quoted text, compatibility, or audience comprehension.

### Multilingual
- Translation preserves meaning/function before surface word order.
- Critical numbers, units, names, negation, modality, and scope receive explicit fidelity attention.
- Material source ambiguity is not silently resolved when alternate readings change meaning.
- Global-facing text avoids unnecessary idioms/culture-specific phrasing when translation/readability benefit is material.

### Revision and QA
- Revision passes have a defect/rubric/goal; repeated paraphrase without signal is a regression.
- Consequential text receives proportional final QA for claims, omissions, dates/numbers, names/links, terminology, format, and readability/accessibility.
- Mechanical lint/readability scores are advisory signals, not standalone proof of editorial quality.

## Regression cases

Fail if the skill:
- makes a rewrite more fluent by deleting a necessary warning or qualifier;
- changes “may” to “will”, “some” to “all”, or a negative to a positive without authorization;
- translates a repeated technical concept with inconsistent equivalents without reason;
- invents facts to make prose sound complete;
- overwrites project-specific voice because a generic style guide prefers something else;
- treats literal translation as inherently more faithful than natural target-language expression;
- endlessly rewrites already-correct prose without a new defect signal;
- claims factual quality from grammar/style checks alone.

## Outcome evaluation

For real tasks, prefer observable dimensions:
- semantic/factual fidelity;
- task/audience fit;
- terminology consistency;
- format/channel compliance;
- clarity/readability appropriate to audience;
- number of material Creator corrections;
- whether a shorter/faster revision path achieved equivalent quality.

Subjective preference remains Creator acceptance evidence, not a fake universal numeric score.
