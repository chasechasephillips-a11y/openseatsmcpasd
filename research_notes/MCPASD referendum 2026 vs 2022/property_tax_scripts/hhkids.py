import json, collections
from shapely.geometry import Polygon
from shapely.strtree import STRtree
from shapely.ops import unary_union
from shapely.validation import make_valid
def geom(g):
    u=None
    for r in g['rings']:
        if len(r)<4: continue
        p=make_valid(Polygon(r)); u=p if u is None else u.symmetric_difference(p)
    return make_valid(u)
src=open("../parcels/assign.py").read(); ns={}; exec(src[src.index("def unit("):src.index("wg=[]; wu=[]")], ns); unit=ns['unit']
W=json.load(open("../parcels/wards.json")); wg=[]; wu=[]
for f in W:
    try: g=geom(f['geometry'])
    except Exception: continue
    wg.append(g); wu.append(unit(f['attributes']['NAME'], f['attributes']['WardNumber']))
wt=STRtree(wg)
mc=unary_union([geom(x['geometry']) for x in json.load(open("../acs/schooldists.json")) if x['attributes']['SchoolID']=='3549'])
bg=json.load(open("bg_hhkids.json")); D=collections.defaultdict(lambda: collections.Counter())
for b in json.load(open("blocks.json")):
    a=b['attributes']
    try: g=geom(b['geometry'])
    except Exception: continue
    pt=g.representative_point()
    if not mc.contains(pt): continue
    hits=[i for i in wt.query(pt) if wg[i].contains(pt)]
    if not hits: continue
    x=bg.get(a['GEOID'][:12],{}); rate=(x.get('H015_calc_numChild') or 0)/x['H0030002'] if x.get('H0030002') else 0
    d=D[wu[hits[0]]]; d['hh']+=a['H0010002'] or 0; d['hhkids']+=(a['H0010002'] or 0)*rate
json.dump({k:dict(v) for k,v in D.items()}, open("hhkids_by_unit.json","w"))
T=collections.Counter(); [T.update(v) for v in D.values()]
print("district est households with kids", round(T['hhkids']), "of", T['hh'], f"{T['hhkids']/T['hh']:.1%}")
for u,v in sorted(D.items(), key=lambda kv:-kv[1]['hhkids']):
    if v['hh']>100: print(f"{u:32} households {v['hh']:5}  with kids ~{v['hhkids']:5.0f}  {v['hhkids']/v['hh']:.0%}")
