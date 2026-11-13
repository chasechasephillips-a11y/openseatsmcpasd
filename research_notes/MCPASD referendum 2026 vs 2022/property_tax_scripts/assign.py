import json, collections, csv
from shapely.geometry import Polygon, MultiPolygon, shape
from shapely.strtree import STRtree
def geom(g):
    rings=[r for r in g['rings'] if len(r)>=4]
    polys=[Polygon(r) for r in rings]
    polys=[p.buffer(0) for p in polys]
    return max(polys, key=lambda p:p.area) if len(polys)==1 else MultiPolygon([p for p in polys if p.geom_type=='Polygon']) if all(p.geom_type=='Polygon' for p in polys) else polys[0]
W=json.load(open("wards.json"))
def unit(name, wn):
    wn=wn.strip()
    if name=="City of Middleton":
        n=int(wn)
        if 1<=n<=4: return "C Middleton Wds 1-4"
        if 5<=n<=8 or n==21: return "C Middleton Wds 5-8, 21"
        if 9<=n<=13 or n in (19,22,24): return "C Middleton Wds 9-13,19,22,24"
        if 14<=n<=18: return "C Middleton Wds 14-18"
        return "C Middleton Wds 20, 23"
    if name=="Town of Middleton":
        if wn in ("1","3","4"): return "T Middleton Wds 1, 3-4"
        if wn in ("2","4A"): return "T Middleton Wd 2, 4A"
        if wn in ("5","6","7","8"): return "T Middleton Wds 5-8"
        return "T Middleton Wd 8A"
    if name=="Village of Cross Plains": return "V Cross Plains Wd 7" if wn=="7" else "V Cross Plains Wds 1-6"
    if name=="City of Madison": return "C Madison Wd %03d"%int(wn)
    short={"Town of Berry":"T Berry Wds 1-2","Town of Cross Plains":"T Cross Plains Wds 1-2","Town of Springfield":"T Springfield Wds 1-4","Town of Westport":"T Westport Wds 1-5"}
    return short[name]
wg=[]; wu=[]
for f in W:
    try:
        g=geom(f['geometry'])
    except Exception as e:
        continue
    wg.append(g); wu.append(unit(f['attributes']['NAME'], f['attributes']['WardNumber']))
tree=STRtree(wg)
P=json.load(open("parcels.json"))
seen={}; 
for f in P:
    a=f['attributes']; pn=a['PARCELNO']
    if pn in seen or not f.get('geometry'): continue
    try: g=geom(f['geometry']); pt=g.representative_point()
    except Exception: continue
    hits=[i for i in tree.query(pt) if wg[i].contains(pt)]
    u=wu[hits[0]] if hits else None
    seen[pn]=dict(parcel=pn, muni=a['Municipality'], unit=u, land=a['Sum_LandValue'] or 0, imp=a['Sum_ImprovementValue'] or 0, addr=a['PropertyAddress'], lon=round(pt.x,6), lat=round(pt.y,6))
rows=list(seen.values())
with open("parcels_units.csv","w",newline="") as fh:
    wr=csv.DictWriter(fh, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
c=collections.Counter((r['unit']) for r in rows)
res=collections.Counter((r['unit']) for r in rows if r['imp']>=60000 and r['land']+r['imp']<2500000)
for k in sorted(c, key=lambda x:str(x)): print(str(k).ljust(32), c[k], 'likely homes', res[k])
