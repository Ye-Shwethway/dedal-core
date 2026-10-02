#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
skill = (root / 'skills/visual-narrative-production/SKILL.md').read_text()
notes = (root / 'skills/visual-narrative-production/ADAPTATION_NOTES.md').read_text()
contract = (root / 'evals/visual-narrative-production/contract-v2.md').read_text()
shot_schema = json.loads((root / 'skills/visual-narrative-production/schemas/shot-spec.schema.json').read_text())
ledger_schema = json.loads((root / 'skills/visual-narrative-production/schemas/visual-continuity-ledger.schema.json').read_text())
registry = (root / 'index/SKILL_REGISTRY.yaml').read_text()
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
assert {'count', 'morphology', 'spatial_relation', 'contact_state', 'authorized_transition'} <= set(ledger_schema['properties']['props']['items']['properties'])
physical = (root / 'skills/visual-narrative-production/references/object-state-and-proficiency-continuity.md').read_text()
assert 'Morphology integrity' in physical and 'Proficiency-aware movement realism' in physical

assert 'Equipment interaction preflight' in (root / 'skills/visual-narrative-production/references/pose-anatomy-contact-and-load.md').read_text()
assert 'Before presenting a comparison set' in (root / 'skills/visual-narrative-production/references/self-review-and-sequence-audit.md').read_text()
assert '## Default production path' in skill
assert 'Tool Capability and Failure Routing' in (root / 'skills/visual-narrative-production/references/tool-capability-and-failure-routing.md').read_text()
outcome_eval = (root / 'evals/visual-narrative-production/outcome-evaluation-v1.md').read_text()
assert 'First-pass usable rate' in outcome_eval and 'Escaped material defects' in outcome_eval
assert 'previous skill version' in outcome_eval
assert 'Repetition detector' in (root / 'skills/visual-narrative-production/references/self-review-and-sequence-audit.md').read_text()
assert 'visual-narrative-production' in registry
assert 'aliases: ["visual-narrative-production", "visual-direction"]' in registry
assert 'skills/visual-direction' not in registry
assert any('visual-narrative-production' in json.dumps(c) for c in routing['clusters'])
assert 'private character identity' in notes.lower()

print(f'visual narrative production: valid ({len(refs)} references)')
