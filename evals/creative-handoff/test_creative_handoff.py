import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'))
from validate_creative_handoff import check

class CreativeContracts(unittest.TestCase):
    def scene(self):
        return dict(kind='scene_shots',scene_id='s1',beat_id='b1',canon_subject_ids=['d'],distinct_action_phases=True,shots=[dict(id='1',subject_ids=['d'],action_phase='reach',camera_axis='left',contact_edges=[]),dict(id='2',subject_ids=['d'],action_phase='grip',camera_axis='left',contact_edges=[])])
    def test_valid_scene(self):self.assertEqual(check(self.scene()),[])
    def test_unknown_character(self):
        x=self.scene();x['shots'][0]['subject_ids']=['new'];self.assertTrue(check(x))
    def test_repeated_phase(self):
        x=self.scene();x['shots'][1]['action_phase']='reach';self.assertTrue(check(x))
    def test_unmotivated_axis_cross(self):
        x=self.scene();x['shots'][1]['camera_axis']='right';self.assertTrue(check(x))
    def test_obscured_contact_cannot_pass(self):
        x=self.scene();x['shots'][0]['contact_edges']=[{'observability':'occluded','verdict':'PASS'}];self.assertTrue(check(x))
    def test_creator_acceptance_required(self):
        x=self.scene();x['acceptance']='accepted';self.assertTrue(check(x))
    def test_edl_valid(self):
        x=dict(kind='edit_decisions',assets={'x':{'duration_s':10}},clips=[{'asset_id':'x','in_s':2,'out_s':7,'timeline_start_s':0}]);self.assertEqual(check(x),[])
    def test_edl_out_of_bounds(self):
        x=dict(kind='edit_decisions',assets={'x':{'duration_s':10}},clips=[{'asset_id':'x','in_s':8,'out_s':12,'timeline_start_s':0}]);self.assertTrue(check(x))
    def test_render_verification_requires_evidence(self):
        x=dict(kind='edit_decisions',assets={'x':{'duration_s':10}},clips=[{'asset_id':'x','in_s':0,'out_s':2,'timeline_start_s':0}],render_status='verified');self.assertTrue(check(x))
    def test_evidence_pass_requires_reference(self):
        x=dict(kind='evidence',assertions=[{'id':'a','status':'PASS'}]);self.assertTrue(check(x))
    def test_evidence_unknown_allowed(self):
        x=dict(kind='evidence',assertions=[{'id':'a','status':'UNKNOWN'}]);self.assertEqual(check(x),[])
if __name__=='__main__': unittest.main()

class DefensiveContractTests(unittest.TestCase):
    def test_malformed_shots(self):
        self.assertTrue(check({'kind':'scene_shots','scene_id':'s','beat_id':'b','shots':[None]}))
    def test_malformed_subjects(self):
        self.assertTrue(check({'kind':'scene_shots','scene_id':'s','beat_id':'b','shots':[{'id':'x','subject_ids':'d','camera_axis':'left'}]}))
    def test_malformed_assets(self):
        self.assertTrue(check({'kind':'edit_decisions','assets':[],'clips':[{'asset_id':'x'}]}))
    def test_nan_time(self):
        self.assertTrue(check({'kind':'edit_decisions','assets':{'a':{'duration_s':10}},'clips':[{'asset_id':'a','in_s':float('nan'),'out_s':1,'timeline_start_s':0}]}))
    def test_boolean_time(self):
        self.assertTrue(check({'kind':'edit_decisions','assets':{'a':{'duration_s':10}},'clips':[{'asset_id':'a','in_s':True,'out_s':1,'timeline_start_s':0}]}))
    def test_empty_acceptance_marker(self):
        self.assertTrue(check({'kind':'scene_shots','scene_id':'s','beat_id':'b','shots':[{'id':'x','camera_axis':'left'}],'acceptance':'accepted','creator_acceptance_evidence':''}))
    def test_nonobject_evidence(self):
        self.assertTrue(check({'kind':'evidence','assertions':[None]}))

class FurtherNegativeTests(unittest.TestCase):
    def test_duplicate_canon(self):
        self.assertTrue(check(dict(kind='scene_shots',scene_id='a',beat_id='b',canon_subject_ids=['a','a'],shots=[dict(id='1',camera_axis='left',action_phase='a')])) )
    def test_duplicate_subject(self):
        self.assertTrue(check(dict(kind='scene_shots',scene_id='a',beat_id='b',canon_subject_ids=['a'],shots=[dict(id='1',subject_ids=['a','a'],camera_axis='left',action_phase='a')])) )
    def test_boolean_acceptance_evidence_rejected(self):
        self.assertTrue(check(dict(kind='scene_shots',scene_id='a',beat_id='b',shots=[dict(id='1',camera_axis='left')],acceptance='accepted',creator_acceptance_evidence=True)))
    def test_boolean_playback_evidence_rejected(self):
        self.assertTrue(check(dict(kind='edit_decisions',assets={'x':{'duration_s':5}},clips=[dict(asset_id='x',in_s=0,out_s=1,timeline_start_s=0)],render_status='verified',playback_evidence=True)))
    def test_boolean_assertion_evidence_rejected(self):
        self.assertTrue(check(dict(kind='evidence',assertions=[dict(status='PASS',evidence_ref=True)])))
    def test_whitespace_axis_justification_rejected(self):
        self.assertTrue(check(dict(kind='scene_shots',scene_id='a',beat_id='b',shots=[dict(id='1',camera_axis='left'),dict(id='2',camera_axis='right',axis_crossing_justification='  ')])))
