# Prompt Compilation and Neutralization

## Structured source, concise output
The prompt is compiled from a shot spec. It should not be the source of truth.

Recommended order when relevant:
1. deliverable / shot purpose;
2. subject identity and current state;
3. action/blocking/performance;
4. environment and spatial relations;
5. camera/framing;
6. lighting/atmosphere/style;
7. reference roles;
8. preserve/change constraints;
9. exclusions or failure-specific constraints.

## Reference-binding preflight
Before compiling a recurring-character prompt, verify the execution payload, not only the prose:
1. list each required visual role (identity, physique, grooming, environment, etc.);
2. confirm the authoritative source image for each role;
3. confirm the image is actually attached/passed to the generation tool as a pixel-bearing reference;
4. only then compile text traits as supplemental constraints.

A statement such as "use the canonical reference" is insufficient if the image itself is not present in the execution payload. Library retrieval and model-side visual inspection are preparation steps, not conditioning proof.

For locations, phrase continuity as "same location/architecture/spatial state" rather than "same background" unless identical framing is explicitly required.

## Prompt economy
Use detail to resolve ambiguity or recurring failure. Repeated synonyms and adjective piles often reduce debuggability. For edits, state what changes and what must remain unchanged.

## Reference-role language
Name each reference by role where the tool supports multiple inputs:
- identity;
- physique/proportion;
- expression/performance;
- pose/geometry;
- wardrobe/prop;
- environment;
- composition;
- style/lighting.

## Semantic neutralization
For legitimate scenes that could be misread by automated systems, prefer precise production language:
- adult character / wardrobe state;
- neutral/non-erotic presentation when relevant;
- sports/anatomy/action choreography terminology;
- objective camera and blocking descriptions;
- clinical/anatomical terms when actually needed;
- explicit narrative purpose where useful.

Do not weaken the intended scene merely to make it generic. Do not use obfuscation, coded language, or euphemisms to bypass policy. If the requested content is disallowed, neutralization does not make it allowed.

## Failure-specific constraints
After a rendered defect, add only constraints that target the observed problem, such as:
- preserve exact identity/physique;
- exactly two arms/two legs;
- hands contact the solid surface without intersection;
- retain camera and lighting; change only wrist orientation.
