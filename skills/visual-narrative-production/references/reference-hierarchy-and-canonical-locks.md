# Reference Hierarchy and Canonical Locks

Multiple references can disagree. Resolve authority by dimension rather than averaging them.

## Reference roles
- **identity anchor** — face/subject identity and stable age/structure;
- **physique/proportion anchor** — height impression, body type, silhouette, musculature/proportions;
- **grooming anchor** — hair, beard, makeup, scars/tattoos when relevant;
- **expression/performance anchor** — an approved emotional/performance state without redefining identity;
- **pose/geometry anchor** — body mechanics, blocking, perspective/pose relationship;
- **wardrobe/prop anchor** — clothing, equipment, accessories and object identity;
- **environment anchor** — location/set/architecture/background state;
- **composition/camera anchor** — framing, viewpoint, screen relation;
- **style/lighting anchor** — medium, texture, grade, lighting character.

One image may fill several roles only when it actually has authority for each role.

## Pixel-binding rule for recurring subjects
When recurring-subject consistency is material and authoritative visual anchors exist, visual reference binding is a hard precondition for generation:
- pass the authoritative identity/physique/grooming images to the image-generation execution surface as actual pixel-bearing inputs (or an equivalent provider-supported image-conditioning input);
- retrieving, reading, visually inspecting, or describing a Library image is not the same as binding that image to the generator;
- if the source lives in persistent storage, bridge/materialize it into the execution surface before generation when the tool requires a local/file/image input;
- text traits supplement the pixels and resolve ambiguity; they do not substitute for the pixels when a canonical visual anchor is available;
- use the smallest sufficient reference set and assign each image a role so conflicting references do not get averaged accidentally;
- if the execution surface cannot accept the required image references, downgrade the consistency claim and surface the limitation before generation.

For a recurring character, identity, physique/proportion, and grooming may require separate pixel anchors. A single reference may control multiple roles only when explicitly accepted for those roles.

## Environment anchor is not a composition lock
An environment anchor establishes the identity and durable state of a place: architecture, spatial relationships, recurring equipment/props, materials, time/light state, and other continuity-critical geography. It does **not** require every shot to reproduce the same camera position or display every landmark.

Treat these separately:
- **environment continuity** — same place and stable geography;
- **camera/composition continuity** — only preserved when the sequence or an accepted composition anchor requires it;
- **visibility plan** — from the chosen camera, a destination/landmark may be full, partial, occluded, or offscreen if that is what the scene geometry implies.

Never force a destination object into full view merely to prove location continuity when doing so contradicts the chosen side/front/rear viewpoint or movement logic.

## Canonical trait/state sheet
For recurring subjects, keep compact durable state:
- invariant identity traits;
- allowed variation;
- age/era;
- physique/proportion state;
- grooming;
- distinctive features;
- anti-drift notes;
- approved anchor IDs/locations.

Separate **must preserve** from **may vary**. Do not overfit to incidental pixels.

## Conflict handling
When references conflict:
1. identify the conflicting dimension;
2. choose the authority for that dimension;
3. mark inspiration-only references;
4. never silently blend mutually exclusive traits;
5. surface unresolved material ambiguity.

## Promotion rule
An output becomes a canonical anchor only after explicit acceptance or a project-defined acceptance rule. Newer or prettier does not mean more authoritative.
