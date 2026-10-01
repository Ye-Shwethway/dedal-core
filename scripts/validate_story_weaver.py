#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
skill = (root / 'skills/story-weaver/SKILL.md').read_text()
contract = (root / 'evals/story-weaver/contract-v1.md').read_text()
registry = (root / 'index/SKILL_REGISTRY.yaml').read_text()
routing = json.loads((root / 'state/routing-boundaries.json').read_text())
refs = list((root / 'skills/story-weaver/references').glob('*.md'))

assert 'name: story-weaver' in skill
assert 'Canon before invention' in skill
assert 'Visualizable handoff is structured' in skill
assert len(refs) >= 3
assert 'visual handoff' in contract.lower()
assert 'story-weaver:' in registry
assert any(c['id']=='creative-production' and 'story-weaver' in c['primary_owner_by_intent'].values() for c in routing['clusters'])

print(f'story weaver: valid ({len(refs)} references)')
