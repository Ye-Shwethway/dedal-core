#!/usr/bin/env python3
"""Inspect four final OOXML files without recalculating or generating reports."""
import argparse, hashlib, json, re, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
REPORTS={'Cashier Summary Report','Income','Expenses','Monthly Report to Head Office'}
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def verify_file(path, expected_sheet):
    with zipfile.ZipFile(path) as z:
        names=z.namelist()
        assert not any(n.startswith('xl/externalLinks/') for n in names),'external links'
        assert not any(n.endswith('vbaProject.bin') for n in names),'macro content'
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        sheets=wb.findall('m:sheets/m:sheet',NS)
        assert len(sheets)==1 and sheets[0].get('name')==expected_sheet,'wrong sheet scope'
        assert sheets[0].get('state','visible')=='visible','hidden report'
        for n in names:
            if not n.endswith('.xml'): continue
            root=ET.fromstring(z.read(n))
            assert not any(el.tag.rsplit('}',1)[-1] in {'f','formula','formula1','formula2','calculatedColumnFormula','totalsRowFormula'} for el in root.iter()),f'formula in {n}'
            if n.startswith('xl/worksheets/'):
                assert not root.findall('.//m:c[@t="e"]',NS),'error cell'
        for name in wb.findall('m:definedNames/m:definedName',NS):
            assert name.get('name') in {'_xlnm.Print_Area','_xlnm.Print_Titles','_xlnm._FilterDatabase'},'formula-bearing defined name'
            assert '[' not in (name.text or '') and '#REF!' not in (name.text or ''),'invalid defined reference'
            assert re.fullmatch(r"(?:'[^']*(?:''[^']*)*'|[A-Za-z_][A-Za-z0-9_ ]*)!\$[A-Z]+\$\d+:\$[A-Z]+\$\d+(?:,(?:'[^']*'|[A-Za-z_][A-Za-z0-9_ ]*)!\$[A-Z]+\$\d+:\$[A-Z]+\$\d+)*",name.text or '') or (name.get('name')=='_xlnm.Print_Titles' and re.fullmatch(r"(?:'[^']*'|[A-Za-z_][A-Za-z0-9_ ]*)!(?:\$\d+:\$\d+|\$[A-Z]+:\$[A-Z]+)(?:,(?:'[^']*'|[A-Za-z_][A-Za-z0-9_ ]*)!(?:\$\d+:\$\d+|\$[A-Z]+:\$[A-Z]+))*",name.text or '')), 'non-static print reference'
        for n in names:
            if n.endswith('.rels'):
                for rel in ET.fromstring(z.read(n)):
                    assert not rel.get('Type','').endswith('/externalLink'),'external link relationship'
    return {'path':str(Path(path).resolve()),'sheet':expected_sheet,'sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'formula_free':True}

def verify_manifest(manifest):
    files=manifest['files']
    assert len(files)==4 and {f['sheet'] for f in files}==REPORTS,'exactly four reports required'
    assert len({str(Path(f['path']).resolve()) for f in files})==4,'duplicate file path'
    return [verify_file(f['path'],f['sheet']) for f in files]

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('manifest');args=p.parse_args()
    with open(args.manifest) as f: manifest=json.load(f)
    print(json.dumps(verify_manifest(manifest),indent=2))
