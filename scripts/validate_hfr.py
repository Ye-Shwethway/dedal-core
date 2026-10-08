#!/usr/bin/env python3
import subprocess,sys
from pathlib import Path
import yaml
root=Path(__file__).resolve().parents[1]
registry=yaml.safe_load((root/'index/SKILL_REGISTRY.yaml').read_text())
assert '$hfr' in registry['skills']['hospital-financial-report']['aliases']
profiles=yaml.safe_load((root/'index/task-profiles.yaml').read_text())['profiles']
assert next(p for p in profiles if p['id']=='hospital-financial-report')['primary']=='hospital-financial-report'
result=subprocess.run([sys.executable,str(root/'skills/hospital-financial-report/scripts/test_hfr.py')],capture_output=True,text=True)
assert result.returncode==0,result.stdout+result.stderr
print('HFR contracts: 10 synthetic tests passed; no live approval/authentication claimed')
