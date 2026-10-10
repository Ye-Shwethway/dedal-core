#!/usr/bin/env python3
import json
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
skill = (root / 'skills/visual-narrative-production/SKILL.md').read_text()
notes = (root / 'skills/visual-narrative-production/ADAPTATION_NOTES.md').read_text()
contract = (root / 'evals/visual-narrative-production/contract-v2.md').read_text()
shot_schema = json.loads((root / 'skills/visual-narrative-production/schemas/shot-spec.schema.json').read_text())
ledger_schema = json.loads((root / 'skills/visual-narrative-production/schemas/visual-continuity-ledger.schema.json').read_text())
registry = yaml.safe_load((root / 'index/SKILL_REGISTRY.yaml').read_text())['skills']
routing = json.loads((root / 'state/routing-boundaries.json').read_text())
refs = list((root / 'skills/visual-narrative-production/references').glob('*.md'))

assert 'name: visual-narrative-production' in skill
assert 'visual-direction` is a backward-compatible routing alias' in skill
assert 'Visual Continuity Ledger' in skill
assert 'Neutralize ambiguity without changing legitimate scene meaning' in skill
assert 'Do not use obfuscation' in (root / 'skills/visual-narrative-production/references/prompt-compilation-and-neutralization.md').read_text()
assert 'limb count' in (root / 'skills/visual-narrative-production/references/pose-anatomy-contact-and-load.md').read_text()
assert len(refs) >= 10
assert shot_schema['title'] == 'DEDAL Visual Narrative Shot Spec'
assert ledger_schema['title'] == 'DEDAL Visual Continuity Ledger'
assert 'VNP-12 Story boundary' in contract
assert 'VNP-13 Automatic self-review' in contract
assert 'Self-review before offloading QA to the Creator' in skill
assert 'Bind recurring-character anchors as actual image inputs' in skill
assert 'Preflight scene geometry before camera design' in skill
assert 'Pixel-binding rule for recurring subjects' in (root / 'skills/visual-narrative-production/references/reference-hierarchy-and-canonical-locks.md').read_text()
assert 'Gaze follows action logic' in (root / 'skills/visual-narrative-production/references/performance-expression-and-emotion.md').read_text()
assert 'VNP-16 Pixel-reference binding' in contract
assert 'VNP-17 Environment/composition separation' in contract
assert 'VNP-18 Scene geometry and gaze realism' in contract
assert 'reference_bindings' in shot_schema['properties']
assert 'scene_geometry' in shot_schema['properties']
assert 'interaction_geometry' in shot_schema['properties']
interaction = shot_schema['properties']['interaction_geometry']['properties']
assert {'action_phase', 'fixed_support', 'contact_points', 'visible_joint_chain', 'head_support_relation', 'load_path', 'crop_evidence'} <= set(interaction)
assert 'VNP-19 Visible interaction geometry' in contract
assert 'VNP-20 Comparison-set integrity' in contract
assert 'VNP-21 Reviewable delivery' in contract
assert 'VNP-22 Successive mini-arc continuity' in contract
assert 'VNP-23 Natural action and equipment realism' in contract
assert 'VNP-24 Narrow retry preservation' in contract
assert 'VNP-25 Phase-signature admission' in contract
assert 'VNP-26 Physical-state and proficiency continuity' in contract
assert 'VNP-27 Support-axis and camera-body-equipment coherence' in contract
assert 'VNP-28 Weighted-load and label realism' in contract
assert 'VNP-29 Canonical proportion framing' in contract
assert 'VNP-30 Video-bridge anchor production' in contract
assert 'VNP-31 Collaborative source-sequence handoff' in contract
assert 'VNP-32 Progressive set-scoped source handoff' in contract
mini_arc = (root / 'skills/visual-narrative-production/references/mini-arc-continuity-and-instructor-control.md').read_text()
assert 'Local continuity envelope' in mini_arc
assert 'separate full-frame' in mini_arc
assert 'Natural technique priors' in (root / 'skills/visual-narrative-production/references/pose-anatomy-contact-and-load.md').read_text()
audit = (root / 'skills/visual-narrative-production/references/self-review-and-sequence-audit.md').read_text()
assert 'Successive mini-arc audit' in audit
assert 'Phase-signature admission gate' in audit
assert 'observed rendered action phase' in audit
assert 'Physical-state continuity gate' in audit
assert 'object teleportation' in audit
assert 'proficiency' in audit.lower()
assert 'proficiency_form' in shot_schema['properties']
assert 'support_alignment' in shot_schema['properties']
assert {'body_action_axis', 'support_axis', 'required_axis_relation', 'contact_map', 'camera_projection'} <= set(shot_schema['properties']['support_alignment']['properties'])
assert {'count', 'morphology', 'spatial_relation', 'contact_state', 'authorized_transition'} <= set(ledger_schema['properties']['props']['items']['properties'])
physical = (root / 'skills/visual-narrative-production/references/object-state-and-proficiency-continuity.md').read_text()
assert 'Morphology integrity' in physical and 'Proficiency-aware movement realism' in physical
align = (root / 'skills/visual-narrative-production/references/camera-body-equipment-alignment.md').read_text()
assert 'Support-axis preflight' in align and 'Camera solves visibility' in align
weighted = (root / 'skills/visual-narrative-production/references/weighted-load-and-proportion-realism.md').read_text()
assert 'Strength realism' in weighted and 'Label continuity' in weighted
assert 'weighted_load_plan' in shot_schema['properties']
assert 'proportion_framing' in shot_schema['properties']
assert {'load_label','load_class','label_visibility'} <= set(ledger_schema['properties']['props']['items']['properties'])

assert 'Equipment interaction preflight' in (root / 'skills/visual-narrative-production/references/pose-anatomy-contact-and-load.md').read_text()
assert 'Before presenting a comparison set' in (root / 'skills/visual-narrative-production/references/self-review-and-sequence-audit.md').read_text()
assert '## Default production path' in skill
assert 'Tool Capability and Failure Routing' in (root / 'skills/visual-narrative-production/references/tool-capability-and-failure-routing.md').read_text()
outcome_eval = (root / 'evals/visual-narrative-production/outcome-evaluation-v1.md').read_text()
assert 'First-pass usable rate' in outcome_eval and 'Escaped material defects' in outcome_eval
assert 'previous skill version' in outcome_eval
assert 'Repetition detector' in (root / 'skills/visual-narrative-production/references/self-review-and-sequence-audit.md').read_text()
def valid_visual_registration(skills):
    entry = skills.get('visual-narrative-production', {})
    return (entry.get('status') == 'active'
            and entry.get('entrypoint') == 'skills/visual-narrative-production/SKILL.md'
            and {'visual-narrative-production', 'visual-direction'} <= set(entry.get('aliases', []))
            and all(not str(value.get('entrypoint', '')).startswith('skills/visual-direction/')
                    for value in skills.values()))

assert valid_visual_registration(registry), 'visual registration identity, aliases or active status drift'
# Accept equivalent YAML representations; reject real semantic loss and stale ownership.
for aliases in ['["visual-narrative-production", "visual-direction"]',
                '[visual-direction, visual-narrative-production]',
                '\n  - visual-narrative-production\n  - visual-direction']:
    entry = dict(registry['visual-narrative-production'])
    entry['aliases'] = yaml.safe_load('aliases: ' + aliases)['aliases']
    assert valid_visual_registration({'visual-narrative-production': entry})
for field, value in [('aliases', ['visual-narrative-production']), ('status', 'retired'),
                     ('entrypoint', 'skills/visual-direction/SKILL.md')]:
    entry = dict(registry['visual-narrative-production'])
    entry[field] = value
    assert not valid_visual_registration({'visual-narrative-production': entry})
assert not valid_visual_registration({**registry, 'stale': {'entrypoint': 'skills/visual-direction/SKILL.md'}})
assert any('visual-narrative-production' in json.dumps(c) for c in routing['clusters'])
assert 'private character identity' in notes.lower()

print(f'visual narrative production: valid ({len(refs)} references)')

collab = (root / 'skills/visual-narrative-production/references/collaborative-source-sequence-handoff.md').read_text()
assert 'images_ready' in collab and 'needs_bridge' in collab and 'pairwise reachability' in collab

assert 'production_started' in collab and 'scope=set' in collab and 'scope=production' in collab
