#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
skill=(ROOT/'skills/facebook-page-management/SKILL.md').read_text()
for phrase in [
    'personal Facebook profile',
    'explicit intent',
    'Prefer low-impact validation',
    'Verify remote truth',
    'fail closed',
    'tool exposure',
    'public/private',
]:
    if phrase.lower() not in skill.lower(): errors.append(f'missing skill guard: {phrase}')
contract=json.loads((ROOT/'evals/facebook-page-management/contract-v1.json').read_text())
if len(contract.get('cases',[])) < 10: errors.append('expected >=10 eval cases')
routing=json.loads((ROOT/'state/routing-boundaries.json').read_text())
if not any(x.get('id')=='facebook-page-boundary' for x in routing.get('clusters',[])):
    errors.append('facebook-page-boundary missing')
registry=(ROOT/'index/SKILL_REGISTRY.yaml').read_text()
if 'facebook-page-management:' not in registry: errors.append('skill registry entry missing')
master=(ROOT/'index/MASTER_INDEX.md').read_text()
if 'facebook-page-management' not in master: errors.append('master index entry missing')
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('PASS facebook-page-management contract')
