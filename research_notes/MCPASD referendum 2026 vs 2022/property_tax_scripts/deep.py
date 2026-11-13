import json, csv, collections, statistics as st, math, sys
sys.path.insert(0,"../parcels")
from shapely.geometry import Polygon
from shapely.strtree import STRtree
from shapely.ops import unary_union
from shapely.validation import make_valid
R="/home/user/openseatsmcpasd/research_notes/MCPASD referendum 2026 vs 2022/"
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
ages=json.load(open("blocks_age.json")); bga=json.load(open("bg_age.json")); bgt={b['attributes']['GEOID']:b['attributes'] for b in json.load(open("bgs.json"))}
blocks=json.load(open("blocks.json"))
D=collections.defaultdict(lambda: collections.Counter())
for b in blocks:
    a=b['attributes']
    try: g=geom(b['geometry'])
    except Exception: continue
    pt=g.representative_point()
    if not mc.contains(pt): continue
    hits=[i for i in wt.query(pt) if wg[i].contains(pt)]
    if not hits: continue
    u=wu[hits[0]]; ag=ages.get(a['GEOID'],{}); pop=ag.get('P0010001') or 0; adults=ag.get('P0030001') or 0; kids=max(0,pop-adults)
    bg=bga.get(a['GEOID'][:12],{})
    k517=sum(bg.get(k) or 0 for k in ('P0120004','P0120005','P0120006','P0120028','P0120029','P0120030'))
    lt18=bg.get('P012_calc_numLT18') or 0; bgpop=(bg.get('P0150001') or 0) or 1
    r517=k517/lt18 if lt18 else 0; r65=(bg.get('P012_calc_numGE65') or 0)/bgpop
    t=bgt.get(a['GEOID'][:12],{}); rr=(t.get('H0040004') or 0)/t['H0030002'] if t.get('H0030002') else 0
    d=D[u]; d['pop']+=pop; d['kids']+=kids; d['school']+=kids*r517; d['senior']+=pop*r65; d['hh']+=a['H0010002'] or 0; d['units']+=a['H0010001'] or 0; d['renters']+=(a['H0010002'] or 0)*rr
json.dump({k:dict(v) for k,v in D.items()}, open("demo_by_unit.json","w"))
tot=collections.Counter()
for v in D.values(): tot.update(v)
print("DISTRICT 2020: pop %d, under-18 %d (%.0f%%), school-age 5-17 ~%d, 65+ ~%d (%.0f%%), households %d" % (tot['pop'],tot['kids'],100*tot['kids']/tot['pop'],tot['school'],tot['senior'],100*tot['senior']/tot['pop'],tot['hh']))
