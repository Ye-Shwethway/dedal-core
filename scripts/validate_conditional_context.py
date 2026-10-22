#!/usr/bin/env python3
"""Conditional source closure, source tamper, and no-profile planning tests."""
from pathlib import Path
from copy import deepcopy
import json
import tempfile
import shutil
import yaml
from context_plan import plan, skill_plan, ROOT
from validate_core_contracts import validate

profile = 'recurring-character-image-sequence'
decisions = {'canonical_subject': True, 'local_edit': False, 'sequence': False,
             'physical_interaction': False, 'weighted_action': False, 'multiple_subjects': True,
             'repeated_failure': False, 'motion_handoff': False, 'collaborative_handoff': False}
simple = plan(profile, conditions=decisions)
assert simple['conditional_resolution'] == 'resolved_declarations'
assert simple['content_bytes'] < 15000
assert not any('production-detail' in p for p in simple['read_full'])
assert any('reference-hierarchy' in p for p in simple['read_full'])
sequence = plan(profile, conditions={**decisions, 'sequence': True})
assert any('production-detail' in p for p in sequence['read_full'])
assert plan(profile)['conditional_resolution'] == 'pending'
for bad in [{}, {**decisions, 'extra': False}, {**decisions, 'sequence': 'false'}]:
    try: plan(profile, conditions=bad)
    except ValueError: continue
    raise AssertionError('unresolved or non-boolean branch accepted')
with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    names = ['VERSION', 'state/active-release.json', 'state/release-manifest.json',
             'index/task-profiles.yaml', 'context/budgets.yaml', 'index/skill-catalog.yaml',
             'scripts/context_plan.py', 'scripts/selected_sources.py', *simple['read_full']]
    for name in names:
        p=root/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/name,p)
    assert plan(profile, root, conditions=decisions)['content_bytes'] == simple['content_bytes']
    source=root/'skills/visual-narrative-production/references/reference-hierarchy-and-canonical-locks.md'
    source.write_text('wrong bytes')
    try: plan(profile, root, conditions=decisions)
    except ValueError: pass
    else: raise AssertionError('conditional digest tamper accepted')
assert skill_plan('research')['execution_readiness'].startswith('unverified')
try: skill_plan('nonexistent')
except ValueError: pass
else: raise AssertionError('unknown owner accepted')
load=lambda p:yaml.safe_load((ROOT/p).read_text())
base=[load('index/task-profiles.yaml'),load('index/routing.yaml'),load('index/SKILL_REGISTRY.yaml'),
      load('index/document-schema.yaml'),set(json.loads((ROOT/'core-files.json').read_text())['files'])]
for mutation in [lambda p:p['conditional_core'][0].update(sources=['missing.md']),
                 lambda p:p['conditional_core'].append(deepcopy(p['conditional_core'][0]))]:
    fixture=deepcopy(base);p=next(p for p in fixture[0]['profiles'] if p['id']==profile);mutation(p)
    assert validate(*fixture)
print('CONDITIONAL CONTEXT: PASS simple/sequence closures, pending resolution, partial tree, tamper and unknown owners')

# A publication change between metadata and dependency verification must abort.
from unittest.mock import patch
from selected_sources import ReleaseSnapshot
from context_plan import measure_disclosure
original_verify = ReleaseSnapshot.verify
calls = []
def moved_release(self, paths):
    result = original_verify(self, paths)
    calls.append(1)
    if len(calls) == 1:
        self.active = {**self.active, 'release_sha256': '0' * 64}
    return result
with patch.object(ReleaseSnapshot, 'verify', moved_release):
    try: plan(profile, conditions=decisions)
    except ValueError as exc: assert 'release changed' in str(exc)
    else: raise AssertionError('mixed release plan accepted')
# Byte accounting includes its own envelope and respects a near-threshold limit.
boundary = measure_disclosure({'content_bytes': 100, 'byte_budget': 150, 'budget_status': 'within', 'label': 'မြန်မာ'})
assert boundary['budget_status'] == 'exception_reason_required'
encoded = json.dumps(boundary, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
assert boundary['plan_bytes'] == len(encoded)
assert boundary['disclosure_bytes'] == 100 + len(encoded)
assert measure_disclosure({**boundary, 'byte_budget': 10000})['budget_status'] == 'within'
try: plan('unknown-profile')
except ValueError: pass
else: raise AssertionError('unknown profile accepted')
print('SNAPSHOT/BUDGET: PASS changed release rejected; UTF-8 envelope and boundary accounting verified')
