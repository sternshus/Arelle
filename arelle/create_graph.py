'''
Created on Dec 21, 2015

@author: redward
'''
import sys
from arelle import CntlrCmdLine
from collections import defaultdict
import json

def get_gson(furi='/home/redward/sternshus/gcs/data/1000623/000100062316000141/0001000623-16-000141-xbrl.zip'):
    errors = []
    try:
        success, uri, model, graph = CntlrCmdLine.xbrlTurtleGraphModel(furi)
        sids, metas = get_xbrl_metaids(model)
        gson = (format_body(metas, uri, s, p, o) for s, p, o in graph)
    except Exception as e:
        return(False, furi, str(e))
    return (True, sids, gson)

def get_xbrl_metaids(model):
    elements = ['EntityRegistrantName', 'DocumentType', 'EntityCentralIndexKey', 'DocumentPeriodEndDate']
    sids = defaultdict(list)
    for i, f in enumerate(model.facts):
        sids[f.localName].append((i, f.sourceline, f.objectIndex))
    metas = {e: sids[e] for e in elements}
    return (sids, metas)

def format_body(metas, uri, s, p, o):
    ddate = metas["DocumentPeriodEndDate"].replace('-', '')
    dtype = metas["DocumentType"].replace('-', '')
    cik = metas["EntityCentralIndexKey"].replace('-', '')
    entity = metas["EntityRegistrantName"].replace('-', '')
    clean = lambda x: str(x).replace('file:///', '').replace('home/redward/prod-zip-upload/data', '').replace('//', '')
    s = clean(s)
    p = clean(p)
    o = clean(o)
    sid = s.split('#')[-1]
    return json.dumps({
        'rowid': '{0}-{1}-{2}-{3}-{4}'.format(sid, dtype, ddate, cik, uri),
        'entity': entity,
        'subject': s,
        'predicate': p,
        'object': o.replace('\n', ' ').replace('\r', '')
    })

success, sids, gson = get_gson()
x=5