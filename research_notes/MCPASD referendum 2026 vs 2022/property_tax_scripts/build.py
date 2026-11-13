import json, csv, statistics as st, math, collections
R="/home/user/openseatsmcpasd/research_notes/MCPASD referendum 2026 vs 2022/"
recs=json.load(open("parcels/parcel_results.json"))
ren=json.load(open("renters/renters_by_unit.json"))
p26={r['reporting_unit']:r for r in csv.DictReader(open(R+"partisan_by_ward_2026.csv"))}
w26={r['reporting_unit']:r for r in csv.DictReader(open(R+"ward_results_2026.csv"))}
p22=list(csv.DictReader(open(R+"partisan_by_ward_2022.csv")))
# enrich school 2022 estimate (needs efmv 2022) -> recompute from pages
import sys; sys.path.insert(0,"parcels"); from parse import parse
for x in recs:
    if x.get('madison') or not x.get('school25_gross'): continue
    d=parse(f"parcels/pages/{x['parcel']}.html"); mv22=d['efmv'].get(2022)
    x['s22']= x['school25_gross']*mv22/x['mv25']*(8.89/8.62) if mv22 and x['mv25'] else None
    t=d['tax'].get(2025,{}).get('taxes'); x['taxes25']=t
AREAS=[("City of Middleton","Wards 1–4",["C Middleton Wds 1-4"],["C Middleton Wds 1-4"],lambda x:x['unit']=="C Middleton Wds 1-4"),
("City of Middleton","Wards 5–8, 21",["C Middleton Wds 5-8, 21"],["C Middleton Wds 5-8","C Middleton Wd 21"],lambda x:x['unit']=="C Middleton Wds 5-8, 21"),
("City of Middleton","Wards 9–13, 19, 22, 24",["C Middleton Wds 9-13,19,22,24"],["C Middleton Wds 9-13, 19","C Middleton Wd 22"],lambda x:x['unit']=="C Middleton Wds 9-13,19,22,24"),
("City of Middleton","Wards 14–18",["C Middleton Wds 14-18"],["C Middleton Wds 14-18"],lambda x:x['unit']=="C Middleton Wds 14-18"),
("Town of Middleton","Wards 1, 3–4",["T Middleton Wds 1, 3-4"],None,lambda x:x['unit']=="T Middleton Wds 1, 3-4"),
("Town of Middleton","Wards 2, 4A",["T Middleton Wd 2, 4A"],None,lambda x:x['unit']=="T Middleton Wd 2, 4A"),
("Town of Middleton","Wards 5–8",["T Middleton Wds 5-8"],None,lambda x:x['unit']=="T Middleton Wds 5-8"),
("Village of Cross Plains","Wards 1–6",["V Cross Plains Wds 1-6"],["V Cross Plains Wds 1-6"],lambda x:x['unit']=="V Cross Plains Wds 1-6"),
("Madison","MCPASD wards",[k for k in p26 if k.startswith("C Madison")],[r['reporting_unit'] for r in p22 if r['reporting_unit'].startswith("C Madison")],lambda x:x['unit'].startswith('Madison')),
("Town of Springfield","MCPASD part",["T Springfield Wds 1-4"],["T Springfield Wds 1-4"],lambda x:x['unit']=="T Springfield Wds 1-4"),
("Town of Cross Plains","MCPASD part",["T Cross Plains Wds 1-2"],["T Cross Plains Wds 1-2"],lambda x:x['unit']=="T Cross Plains Wds 1-2"),
("Town of Berry","MCPASD part",["T Berry Wds 1-2"],["T Berry Wds 1-2"],lambda x:x['unit']=="T Berry Wds 1-2"),
("Town of Westport","MCPASD part",["T Westport Wds 1-5"],["T Westport Wds 1-5"],lambda x:x['unit']=="T Westport Wds 1-5")]
p22u={r['reporting_unit']:r for r in p22}
print([k for k in p22u if 'Middleton' in k])
def agg_vote(units, src):
    y=n=0; dw=0.0
    for u in units:
        r=src.get(u)
        if not r: continue
        yy,nn=int(r['ref_yes']),int(r['ref_no']); y+=yy; n+=nn; dw+=(yy+nn)*float(r['gov_dem_2party_pct'] or 0)
    if y+n==0: return None
    return dict(yes=100*y/(y+n), dem=dw/(y+n), votes=y+n)
med=lambda v:(st.median(v) if v else None)
out=[]
for place,sub,u26,u22,fx in AREAS:
    v=agg_vote(u26,p26); v22=agg_vote(u22,p22u) if u22 else None
    rr=[ren[u] for u in u26 if u in ren]; units=sum(r['units'] for r in rr); occ=sum(r['occ'] for r in rr); apt=sum(r['apt_est'] for r in rr); rent=sum(r['renters'] for r in rr)
    wq=sum(int(w26[u]['ballots_with_question']) for u in u26 if u in w26); ro=sum(int(w26[u]['rolloff']) for u in u26 if u in w26)
    xs=[x for x in recs if fx(x)]
    sch_share_home=med([x['school25_net']/x['bill25'] for x in xs if x.get('school25_net') and x.get('bill25')])
    sch_share_rent=med([x['school25_net']/x['taxes25'] for x in xs if x.get('school25_net') and x.get('taxes25')])
    sch_inc=med([x['school25_gross']/x['s22']-1 for x in xs if x.get('s22') and not x.get('newbuild')])
    floor26=100*(v['dem']-v['yes'])/v['dem']; floor22=100*(v22['dem']-v22['yes'])/v22['dem'] if v22 else None
    out.append(dict(place=place,sub=sub,votes=v['votes'],yes=round(v['yes'],1),dem=round(v['dem'],1),resid=round(v['yes']-(7.0+0.69*v['dem']),1),
        floor26=round(floor26,1),floor22=(round(floor22,1) if floor22 is not None else None),
        units=units,occ=occ,apt=apt,aptShare=round(100*apt/units,0) if units else None,renters=round(rent),renterShare=round(100*rent/occ) if occ else None,
        rolloff=round(100*ro/wq,1) if wq else None, ballotsPerHH=round(wq/occ,2) if occ else None,
        schHome=round(100*sch_share_home) if sch_share_home else None, schRent=round(100*sch_share_rent) if sch_share_rent else None,
        schInc=round(100*sch_inc,1) if sch_inc is not None else None))
json.dump(out,open("renters/areas.json","w"),indent=0,ensure_ascii=False)
for o in out: print(f"{o['place'][:18]:18} {o['sub'][:16]:16} votes {o['votes']:5} yes {o['yes']} dem {o['dem']} resid {o['resid']:+} floor {o['floor22']}->{o['floor26']} | units {o['units']} apt {o['aptShare']}% renters {o['renterShare']}% rolloff {o['rolloff']} ballots/HH {o['ballotsPerHH']} | school share home {o['schHome']}% rent {o['schRent']}% school inc {o['schInc']}%")
def wc(a,b,w):
    W=sum(w); ma=sum(x*y for x,y in zip(a,w))/W; mb=sum(x*y for x,y in zip(b,w))/W
    return sum(y*(x-ma)*(z-mb) for x,z,y in zip(a,b,w))/math.sqrt(sum(y*(x-ma)**2 for x,y in zip(a,w))*sum(y*(z-mb)**2 for z,y in zip(b,w)))
def r(xk,yk,rows=None):
    rows=[o for o in (rows or out) if o.get(xk) is not None and o.get(yk) is not None]
    return len(rows), round(wc([o[xk] for o in rows],[o[yk] for o in rows],[o['votes'] for o in rows]),2)
for xk,yk in [('aptShare','resid'),('aptShare','floor26'),('aptShare','rolloff'),('aptShare','yes'),('aptShare','ballotsPerHH'),('schInc','floor26'),('schInc','resid'),('schInc','yes')]:
    print(xk,'vs',yk, r(xk,yk))
fc=[dict(o, fchg=o['floor26']-o['floor22']) for o in out if o['floor22'] is not None]
print('schInc vs floor change', r('schInc','fchg',fc), 'aptShare vs floor change', r('aptShare','fchg',fc))
