import json, csv, collections, sys
sys.path.insert(0,"../parcels")
from shapely.geometry import Polygon, Point
from shapely.strtree import STRtree
from shapely.ops import unary_union
from shapely.validation import make_valid
def geom(g):
    u=None
    for r in g['rings']:
        if len(r)<4: continue
        p=make_valid(Polygon(r)); u=p if u is None else u.symmetric_difference(p)
    return make_valid(u)
# wards -> reporting units (reuse mapping from assign.py)
import importlib.util
spec=importlib.util.spec_from_file_location("assign_mod","../parcels/assign.py")
src=open("../parcels/assign.py").read(); unit_src=src[src.index("def unit("):src.index("wg=[]; wu=[]")]
ns={}; exec(unit_src, ns); unit=ns['unit']
W=json.load(open("../parcels/wards.json")); wg=[]; wu=[]
for f in W:
    try: g=geom(f['geometry'])
    except Exception: continue
    wg.append(g); wu.append(unit(f['attributes']['NAME'], f['attributes']['WardNumber']))
wtree=STRtree(wg)
sd=[x for x in json.load(open("../acs/schooldists.json")) if x['attributes']['SchoolID']=='3549']
mc=unary_union([geom(x['geometry']) for x in sd])
bgs={b['attributes']['GEOID']:b['attributes'] for b in json.load(open("bgs.json"))}
blocks=json.load(open("blocks.json"))
# parcels (residential-looking) per block
pu=list(csv.DictReader(open("../parcels/parcels_units.csv")))
bgeo=[]; bat=[]
for b in blocks:
    try: g=geom(b['geometry'])
    except Exception: continue
    bgeo.append(g); bat.append(b['attributes'])
btree=STRtree(bgeo)
homes_in_block=collections.Counter()
for r in pu:
    if r['muni']=='City of Madison' or (int(r['imp'])>=60000 and int(r['land'])+int(r['imp'])<2500000):
        pt=Point(float(r['lon']),float(r['lat']))
        for i in btree.query(pt):
            if bgeo[i].contains(pt): homes_in_block[bat[i]['GEOID']]+=1; break
agg=collections.defaultdict(lambda: dict(units=0,occ=0,renters=0.0,pop=0,apt_est=0))
for g,a in zip(bgeo,bat):
    pt=g.representative_point()
    if not mc.contains(pt): continue
    hits=[i for i in wtree.query(pt) if wg[i].contains(pt)]
    u=wu[hits[0]] if hits else 'unassigned'
    bg=bgs.get(a['GEOID'][:12]); rate=(bg['H0040004']/bg['H0030002']) if bg and bg['H0030002'] else 0
    d=agg[u]; d['units']+=a['H0010001'] or 0; d['occ']+=a['H0010002'] or 0; d['pop']+=a['P0010001'] or 0
    d['renters']+= (a['H0010002'] or 0)*rate
    d['apt_est']+= max(0,(a['H0010001'] or 0)-homes_in_block[a['GEOID']])
tot=dict(units=0,occ=0,renters=0,pop=0,apt_est=0)
for u in sorted(agg):
    d=agg[u]; [tot.__setitem__(k,tot[k]+d[k]) for k in tot]
    print(f"{u:32} units {d['units']:6} occ {d['occ']:6} renters~{d['renters']:7.0f} ({d['renters']/max(d['occ'],1):.0%}) apt-units~{d['apt_est']:6} pop {d['pop']}")
print("DISTRICT", {k:round(v) for k,v in tot.items()}, f"renter share {tot['renters']/tot['occ']:.0%}")
json.dump({k:dict(v) for k,v in agg.items()}, open("renters_by_unit.json","w"))
