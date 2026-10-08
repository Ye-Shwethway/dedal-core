#!/usr/bin/env python3
"""Offline synthetic cases. Does not edit a hospital workbook or export real data."""
import copy, tempfile, unittest, zipfile
from pathlib import Path
from validate_review import digest, validate
from verify_exports import verify_file, verify_manifest, REPORTS

def package():
    s={'hospital_id':'fixture','month':'2026-09','revision':1,'currency':'CNY','source_coverage_complete':True,'unresolved':[],'formula_errors':[],
       'totals':{'opening':'100','income':'25','expenses':'8','closing':'117'},
       'transactions':[{'id':'i','source_ref':'fixture:income:1','reporting_date':'2026-09-01','original_currency':'CNY','reporting_currency':'CNY','kind':'income','reporting_amount':'25','included':True,'confirmed':True},
                       {'id':'e','source_ref':'fixture:expense:1','reporting_date':'2026-09-02','original_currency':'CNY','reporting_currency':'CNY','kind':'expense','reporting_amount':'8','included':True,'confirmed':True}]}
    p={'snapshot':s,'snapshot_sha256':digest(s)}
    for k in ['approval','export_request']:p[k]={'hospital_id':'fixture','month':'2026-09','snapshot_sha256':p['snapshot_sha256'],'instruction_ref':'fixture:'+k,'observed_at':'2026-10-01T00:00:00Z'}
    return p

def rehash(p):p['snapshot_sha256']=digest(p['snapshot'])

class HFR(unittest.TestCase):
    def test_review_and_scoped_export(self):self.assertFalse(validate(package(),True)['live_authority_authenticated'])
    def test_approval_is_not_export(self):
        p=package();del p['export_request']
        with self.assertRaises(AssertionError):validate(p,True)
    def test_change_invalidates_approval(self):
        p=package();p['snapshot']['revision']=2;rehash(p)
        with self.assertRaises(AssertionError):validate(p,True)
    def test_wrong_month_authority(self):
        p=package();p['approval']['month']='2026-10'
        with self.assertRaises(AssertionError):validate(p,True)
    def test_missing_source_and_unresolved(self):
        for key,val in [('source_coverage_complete',False),('unresolved',['amount unreadable']),('formula_errors',['#REF!'])]:
            p=package();p['snapshot'][key]=val;rehash(p)
            with self.assertRaises(AssertionError):validate(p)
    def test_duplicate(self):
        p=package();p['snapshot']['transactions'][1]['id']='i';rehash(p)
        with self.assertRaises(AssertionError):validate(p)
    def test_period_and_conversion(self):
        for k,v in [('reporting_date','2026-09-31'),('reporting_date','2026-08-01'),('original_currency','MMK'),('confirmed',False)]:
            p=package();p['snapshot']['transactions'][1][k]=v;rehash(p)
            with self.assertRaises((AssertionError,ValueError)):validate(p)
    def test_reconciliation_and_digest(self):
        p=package();p['snapshot']['totals']['closing']='118'
        with self.assertRaises(AssertionError):validate(p)
        rehash(p)
        with self.assertRaises(AssertionError):validate(p)
    def test_excluded_change_exchange(self):
        p=package();p['snapshot']['transactions'].append({'id':'change','source_ref':'fixture:change','reporting_currency':'CNY','included':False,'reporting_amount':'1000'});rehash(p);validate(p)
    def test_xlsx_byte_checks(self):
        with tempfile.TemporaryDirectory() as d:
            files=[]
            for i,sheet in enumerate(sorted(REPORTS)):
                path=Path(d)/f'{i}.xlsx'
                def write(body='<c r="A1"><v>17</v></c>',extra=None):
                    with zipfile.ZipFile(path,'w') as z:
                        z.writestr('xl/workbook.xml',f'<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheets><sheet name="{sheet}" sheetId="1"/></sheets></workbook>')
                        z.writestr('xl/worksheets/sheet1.xml',f'<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>{body}</sheetData></worksheet>')
                        if extra:z.writestr(extra,'<x/>')
                write();verify_file(path,sheet)
                for body,extra in [('<c><f>1+1</f><v>2</v></c>',None),('<c t="e"><v>#REF!</v></c>',None),('<formula>1+1</formula>',None),('', 'xl/externalLinks/externalLink1.xml')]:
                    write(body,extra)
                    with self.assertRaises(AssertionError):verify_file(path,sheet)
                write();files.append({'sheet':sheet,'path':str(path)})
            self.assertEqual(len(verify_manifest({'files':files})),4)
            with self.assertRaises(AssertionError):verify_manifest({'files':files[:3]})

if __name__=='__main__':unittest.main()
