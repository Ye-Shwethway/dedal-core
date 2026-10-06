#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
errors=[]
req=[
"skills/resource-intelligence/SKILL.md",
"skills/resource-intelligence/references/resource-profile-and-record-model.md",
"skills/resource-intelligence/references/discovery-refresh-and-change-detection.md",
"skills/resource-intelligence/references/storage-privacy-and-consumer-handoffs.md",
"skills/resource-intelligence/schemas/resource-profile.schema.json",
"skills/resource-intelligence/schemas/resource-record.schema.json",
"evals/resource-intelligence/contract-v1.json"]
for x in req:
    if not (ROOT/x).is_file(): errors.append("missing:"+x)
reg=yaml.safe_load((ROOT/"index/SKILL_REGISTRY.yaml").read_text())
ri=reg.get("skills",{}).get("resource-intelligence",{})
if ri.get("entrypoint")!="skills/resource-intelligence/SKILL.md" or ri.get("status")!="active": errors.append("registry")
profiles=yaml.safe_load((ROOT/"index/task-profiles.yaml").read_text()).get("profiles",[])
p=next((x for x in profiles if x.get("id")=="resource-intelligence-tracking"),None)
if not p or p.get("primary")!="resource-intelligence" or "research" not in p.get("supporting",[]): errors.append("profile")
text=(ROOT/"skills/resource-intelligence/SKILL.md").read_text().lower()
for token in ["resource-type-agnostic","unseen opportunities","canonical identity","new | changed | confirmed | stale | no_change | removed_or_unavailable | conflict","private-overlay/resource-intelligence","one-off lookup"]:
    if token not in text: errors.append("missing_rule:"+token)
for schema in ["resource-profile.schema.json","resource-record.schema.json"]:
    d=json.loads((ROOT/"skills/resource-intelligence/schemas"/schema).read_text())
    if d.get("type")!="object" or not d.get("required"): errors.append("schema:"+schema)
ev=json.loads((ROOT/"evals/resource-intelligence/contract-v1.json").read_text())
if len(ev.get("cases",[]))<8: errors.append("eval_breadth")
if errors:
    print("RESOURCE INTELLIGENCE VALIDATION: FAIL")
    [print("-",e) for e in errors]; sys.exit(1)
print("RESOURCE INTELLIGENCE VALIDATION: PASS cases=%d"%len(ev["cases"]))
