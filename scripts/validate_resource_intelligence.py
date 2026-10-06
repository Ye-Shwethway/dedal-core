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

from copy import deepcopy
import hashlib
import tempfile
from resource_review import check

def review_regressions(cases):
    failures=[]
    # Synthetic image bytes test sniff/hash discipline only, never visual quality.
    data=b'\x89PNG\r\n\x1a\nsynthetic-validator-fixture'
    policy={'visual_required':True,'creator_acceptance_required':True,
            'visual_dimensions':['appearance','muscularity'],
            'allowed_resource_evidence':['resource_image','opportunity_image'],
            'allowed_opportunity_evidence':['opportunity_image']}
    e={'asset_id':'proof-1','scope':'resource','opportunity_id':None,'kind':'resource_image',
       'origin':'retrieved','source_ref':'fixture:attributed-photo','storage_ref':'fixture:persisted-id',
       'sha256':hashlib.sha256(data).hexdigest(),'media_type':'image/png',
       'inspection':{'profile_id':'test-profile','status':'passed','read_ref':'fixture:pixel-read','observed_at':'2026-01-01T01:00:00Z',
       'dimensions':[{'id':x,'result':'pass','reason':'fixture dimension observation'} for x in policy['visual_dimensions']]},
       'display_ref':'fixture:display','displayed_at':'2026-01-01T02:00:00Z'}
    review={'profile_id':'test-profile','scope':'resource','opportunity_id':None,'status':'accepted','reason':'fixture Creator decision',
            'decision_source':'fixture:explicit-user-message','decided_at':'2026-01-01T03:00:00Z','evidence_refs':['proof-1']}
    with tempfile.TemporaryDirectory() as tmp:
        from pathlib import Path
        path=Path(tmp)/'proof.png'
        for case in cases:
            path.write_bytes(data)
            p={'profile_id':'test-profile','review_policy':deepcopy(policy)}; r={'visual_evidence':[deepcopy(e)],'reviews':[deepcopy(review)]}
            x=r['visual_evidence'][0]; dec=r['reviews'][0]; v=case['variant'];scope=case.get('scope','resource')
            opp='scene-1' if scope=='opportunity' else None
            if scope=='opportunity':
                x['scope']='opportunity';x['opportunity_id']=opp;x['kind']='opportunity_image'
                dec['scope']='opportunity';dec['opportunity_id']=opp
            if v=='missing_policy':p={}
            elif v=='wrong_profile_acceptance':dec['profile_id']='another-profile'
            elif v=='wrong_profile_inspection':x['inspection']['profile_id']='another-profile'
            elif v=='invalid_policy':p['review_policy']['visual_required']=None
            elif v=='tags_only':r['visual_evidence']=[]
            elif v=='no_inspection':x['inspection']={}
            elif v=='dimension_fail':x['inspection']['dimensions'][1]['result']='fail'
            elif v=='dimension_unknown':x['inspection']['dimensions'][1]['result']='unknown'
            elif v=='unsaved_preview':x['storage_ref']=''
            elif v=='no_display':x['display_ref']=''
            elif v=='no_creator':r['reviews']=[]
            elif v=='early_acceptance':dec['decided_at']='2026-01-01T01:30:00Z'
            elif v=='actor_photo_scene':x['kind']='resource_image'
            elif v=='actor_approval_scene':dec['scope']='resource';dec['opportunity_id']=None
            elif v=='rejected':dec['status']='rejected'
            elif v=='automatic_repromotion':
                prior=deepcopy(dec);prior['status']='rejected';r['reviews'].insert(0,prior)
            elif v=='reconsidered':
                prior=deepcopy(dec);prior['status']='rejected';prior['evidence_refs']=['old-proof'];r['reviews'].insert(0,prior)
                dec['reconsideration_reason']='Creator explicitly reviewed materially different new proof'
            elif v=='generated':x['origin']='generated'
            elif v=='html_error':path.write_bytes(b'<html>Site Unavailable</html>');x['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
            elif v=='changed_bytes':path.write_bytes(data+b'changed')
            elif v=='nonvisual_package':p['review_policy']={'visual_required':False,'creator_acceptance_required':False,'visual_dimensions':[],'allowed_resource_evidence':[],'allowed_opportunity_evidence':[]};r={}
            elif v=='present_only':r['reviews']=[]
            elif v=='missing_dimension_reason':x['inspection']['dimensions'][1]['reason']=''
            result=check(p,r,case.get('stage','accept'),scope,opp,{'proof-1':str(path)})
            expected=case.get('expected_error')
            if expected and (result['passed'] or expected not in result['errors']):failures.append(case['id']+':'+repr(result))
            elif not expected and result['passed']!=case.get('expected_pass'):failures.append(case['id']+':'+repr(result))
    return failures

errors.extend(review_regressions(ev.get('review_cases', [])))
if len(ev.get('review_cases', [])) < 22: errors.append('review_regression_breadth')
if errors:
    print("RESOURCE INTELLIGENCE VALIDATION: FAIL")
    [print("-",e) for e in errors]; sys.exit(1)
print("RESOURCE INTELLIGENCE VALIDATION: PASS cases=%d review_cases=%d"%(len(ev["cases"]),len(ev["review_cases"])))
