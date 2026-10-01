# Generation, Edit, and Anchor Promotion

## Fresh generation vs edit
Use fresh generation when the scene/pose/composition changes materially or the base image is structurally unsuitable. Use edit-first when most accepted content should remain fixed.

## Iteration loop
0. verify all required recurring-character visual anchors are bound as actual image inputs and that scene geometry/camera visibility are coherent;
1. generate/edit one candidate or a small intentional comparison set;
2. inspect the rendered output;
3. compare relevant dimensions against their authoritative anchors;
4. classify defects;
5. preserve accepted dimensions explicitly;
6. make one coherent correction pass;
7. re-check the actual render.

For a structural action defect that survives one targeted correction, reconsider the shot phase, crop, and contact geometry before another prompt retry. If editing preserves the impossible base geometry, generate a new frame with the accepted identity/place references and a new geometry plan instead. Count only inspected, usable alternatives in a requested variation set.

## Anchor types
An accepted image may be promoted for one or more roles:
- identity;
- physique/proportion;
- grooming;
- expression/performance;
- wardrobe/prop;
- pose/geometry;
- environment/location;
- composition/camera;
- lighting/style;
- scene-continuity state.

Promotion is role-specific. A strong pose reference with mild identity drift can be retained as pose inspiration but must not become an identity anchor.

## Acceptance record
For durable projects, record:
- image ID/path;
- accepted role(s);
- scene/character/version context;
- invariants it establishes;
- tolerated deviations;
- whether it supplements or supersedes another anchor.
