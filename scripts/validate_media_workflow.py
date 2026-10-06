#!/usr/bin/env python3
"""Negative and transfer cases for review delivery and independent cover authority."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
import yaml
from media_workflow import validate

ROOT = Path(__file__).resolve().parents[1]


def run_cases():
    count = 0
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        video = root/'master.bin'; video.write_bytes(b'accepted exact media fixture')
        cover = root/'cover.bin'; cover.write_bytes(b'accepted exact cover fixture')
        sha = hashlib.sha256(video.read_bytes()).hexdigest()
        image_sha = hashlib.sha256(cover.read_bytes()).hexdigest()
        evidence = 'fixture:external-reference-not-real-approval'
        state = {'schema_version':1,'task_id':'fixture',
                 'asset':{'path':str(video),'sha256':sha,'size_bytes':video.stat().st_size,'duration':12.5,'width':1080,'height':1920,'qc_ref':evidence},
                 'review':{'asset_sha256':sha,'size_bytes':video.stat().st_size,'file_id':'review-fixture','parent_id':'folder-fixture','view_url':'https://example.invalid/review','verified_ref':evidence,'delivered_ref':evidence},
                 'media_approval':{'asset_sha256':sha,'creator_ref':evidence},
                 'package':{'asset_sha256':sha,'locked_ref':evidence},
                 'target':{'channel_id':'channel-fixture','verified_ref':evidence},
                 'publishing_authority_ref':evidence,'single_flight_ref':evidence,
                 'cover_options':[{'id':'a','path':str(cover),'sha256':image_sha,'asset_sha256':sha,'presented_ref':evidence}],
                 'cover_approval':{'mode':'chosen','option_id':'a','creator_ref':evidence,'asset_sha256':sha},
                 'upload':{'video_id':'video-fixture','asset_sha256':sha,'upload_status':'processed','processing_status':'succeeded','verified_ref':evidence},
                 'thumbnail':{'video_id':'video-fixture','cover_sha256':image_sha,'verified_ref':evidence},
                 'publication':{'video_id':'video-fixture','visibility':'public','verified_ref':evidence},
                 'archive_verified_ref':evidence,'checkpoint_ref':evidence}
        measured=lambda _: {'duration':12.5,'width':1080,'height':1920}
        def check(s, action, passes, task='fixture'):
            nonlocal count
            try:
                validate(s,action,task,probe_media=measured)
                accepted=True
            except (ValueError, KeyError, TypeError, OSError):
                accepted=False
            assert accepted is passes,(action,s,passes)
            count+=1
        for action in ('render_review','deliver_review','private_upload','thumbnail','publish','close'):
            check(state,action,True)
        pending=deepcopy(state);pending.pop('cover_approval')
        check(pending,'private_upload',True)
        for action in ('thumbnail','publish','close'):check(pending,action,False)
        # A different presented option with explicit delegation is a held-out positive path.
        delegated=deepcopy(state);delegated['cover_options'][0]['id']='new-option';delegated['cover_approval'].update(mode='delegated',option_id='new-option')
        check(delegated,'thumbnail',True);check(delegated,'close',True)
        supplied=deepcopy(pending);supplied.pop('review');supplied.update(review_required=False,review_not_required_ref=evidence)
        check(supplied,'private_upload',True)
        supplied['review_not_required_ref']='';check(supplied,'private_upload',False)
        drive=deepcopy(state);drive['review']['view_url']='https://drive.google.com/file/d/other-id/view';check(drive,'deliver_review',False)
        drive['review']['view_url']='https://drive.google.com/file/d/review-fixture/view';check(drive,'deliver_review',True)
        check(state,'close',False,task='different-task')
        for section,key,bad,action in [
            ('review','delivered_ref','', 'deliver_review'),
            ('review','view_url','', 'deliver_review'),
            ('review','verified_ref','', 'deliver_review'),
            ('review','asset_sha256','wrong', 'deliver_review'),
            ('asset','duration',9.7,'close'),
            ('asset','duration',float('nan'),'close'),
            ('asset','size_bytes',1,'close'),
            ('asset','sha256','wrong','close'),
            ('asset','qc_ref','', 'render_review'),
            ('media_approval','creator_ref','', 'private_upload'),
            ('media_approval','asset_sha256','wrong','private_upload'),
            ('package','locked_ref','', 'private_upload'),
            ('cover_approval','mode','pending','thumbnail'),
            ('cover_approval','creator_ref','', 'thumbnail'),
            ('cover_approval','asset_sha256','wrong','thumbnail'),
            ('cover_approval','option_id','unknown','thumbnail'),
            ('upload','processing_status','processing','publish'),
            ('thumbnail','cover_sha256','wrong','close'),
            ('publication','video_id','other','close'),
            ('publication','visibility','private','close'),
        ]:
            bad_state=deepcopy(state);bad_state[section][key]=bad;check(bad_state,action,False)
        for field in ('publishing_authority_ref','single_flight_ref','archive_verified_ref','checkpoint_ref'):
            bad_state=deepcopy(state);bad_state[field]='';check(bad_state,'close',False)
        for field in ('presented_ref','asset_sha256','sha256'):
            bad_state=deepcopy(state);bad_state['cover_options'][0][field]='';check(bad_state,'thumbnail',False)
        cover.write_bytes(b'changed image');check(state,'thumbnail',False)
        cover.write_bytes(b'accepted exact cover fixture')
        video.write_bytes(b'changed master');check(state,'private_upload',False)
    return count


if __name__=='__main__':
    count=run_cases()
    profiles={p['id']:p for p in yaml.safe_load((ROOT/'index/task-profiles.yaml').read_text())['profiles']}
    publication=profiles['video-publication']
    assert publication['supporting']==['youtube-seo']
    assert 'skills/youtube-seo/SKILL.md' in publication['required_core']
    assert publication['media_workflow']['execute']=={'prepare':'private_upload','thumbnail':'thumbnail','publish':'publish'}
    assert publication['media_workflow']['close']=={'publish':'close'}
    assert 'youtube upload' not in profiles['publishing-write']['match']['any']
    assert profiles['video-review-delivery']['media_workflow']['close']['deliver']=='deliver_review'
    skill=(ROOT/'skills/candidate-video-finder/SKILL.md').read_text()
    assert '## Runtime-bound workflow integrity' not in skill and 'External DEDAL Runtime/Python Canary MCPs are retired' in skill
    print(f'MEDIA WORKFLOW: PASS {count} positive/negative/transfer cases; local properties only, external authority not authenticated')
