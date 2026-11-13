import json, csv, os, statistics as st, collections
from parse import parse
recs=json.load(open("parcel_results.json"))
samp={r['parcel']:r for r in csv.DictReader(open("sample.csv"))}
EQ={2023:9_997_047_300,2024:10_960_114_809,2025:11_729_700_033,2026:13_060_000_000}
RATE={2022:8.89,2025:8.62}
REF22={2023:7_345_000,2024:13_790_000,2025:19_435_000,2026:24_900_000}   # levy year (Dec bill year) -> 2022 referendum amount
REF26_TOTAL=118_500_000; REF26_NEW=18_900_000
# enrich AccessDane homes with assessment history + efmv history
for x in recs:
    if x.get('madison'): continue
    d=parse(f"pages/{x['parcel']}.html")
    x['efmv']={int(k):v for k,v in d['efmv'].items()}
    x['school22_gross_est']= x['school25_gross']*(x['efmv'].get(2022) or 0)/x['mv25']*(RATE[2022]/RATE[2025]) if x.get('school25_gross') and x['efmv'].get(2022) and x['mv25'] else None
    # 2022 referendum cost actually paid by this home, Dec 2023-Dec 2026 bills (2026 uses estimated 2026 value)
    mv={2023:x['efmv'].get(2023),2024:x['efmv'].get(2024),2025:x['mv25'],2026:x['mv26']}
    x['ref22_paid']= sum(REF22[y]*mv[y]/EQ[y] for y in REF22) if all(mv.values()) else None
for x in recs:
    if x.get('mv26'):
        x['ref26_total']=REF26_TOTAL*x['mv26']/EQ[2026]; x['ref26_new']=REF26_NEW*x['mv26']/EQ[2026]
    x['notice_usd']=x['a26']-x['a25']
# homes per area: likely-home parcels x residential share in the sample
pu=list(csv.DictReader(open("parcels_units.csv")))
g1=collections.defaultdict(lambda:[0,0])
for pn,r in samp.items():
    if r['muni']=='City of Madison': continue
    fn=f"pages/{pn}.html"
    if not os.path.exists(fn): continue
    d=parse(fn)
    if not d: continue
    g1[r['muni']][1]+=1; g1[r['muni']][0]+= 'G1' in d['classes']
share={m:v[0]/v[1] for m,v in g1.items()}
mad_res=sum(1 for x in json.load(open("madison_parcels.json")) if x['PropertyClass']=='Residential')
def likely(sel): return sum(1 for r in sel if int(r['imp'])>=60000 and int(r['land'])+int(r['imp'])<2500000)
areas=[("City of Middleton","Wards 1–4",lambda x:x['unit']=="C Middleton Wds 1-4",lambda r:r['unit']=="C Middleton Wds 1-4"),
("City of Middleton","Wards 5–8, 21",lambda x:x['unit']=="C Middleton Wds 5-8, 21",lambda r:r['unit']=="C Middleton Wds 5-8, 21"),
("City of Middleton","Wards 9–13, 19, 22, 24",lambda x:x['unit']=="C Middleton Wds 9-13,19,22,24",lambda r:r['unit']=="C Middleton Wds 9-13,19,22,24"),
("City of Middleton","Wards 14–18",lambda x:x['unit']=="C Middleton Wds 14-18",lambda r:r['unit']=="C Middleton Wds 14-18"),
("Town of Middleton","All wards",lambda x:x['muni']=="Town of Middleton",lambda r:r['muni']=="Town of Middleton"),
("Village of Cross Plains","Wards 1–6",lambda x:x['unit']=="V Cross Plains Wds 1-6",lambda r:r['unit']=="V Cross Plains Wds 1-6"),
("Madison","MCPASD wards",lambda x:x['unit'].startswith('Madison'),None),
("Town of Springfield","MCPASD part",lambda x:x['unit']=="T Springfield Wds 1-4",lambda r:r['unit']=="T Springfield Wds 1-4"),
("Town of Cross Plains","MCPASD part",lambda x:x['unit']=="T Cross Plains Wds 1-2",lambda r:r['unit']=="T Cross Plains Wds 1-2"),
("Town of Berry","MCPASD part",lambda x:x['unit']=="T Berry Wds 1-2",lambda r:r['unit']=="T Berry Wds 1-2"),
("Town of Westport","MCPASD part",lambda x:x['unit']=="T Westport Wds 1-5",lambda r:r['unit']=="T Westport Wds 1-5")]
med=lambda v:(st.median(v) if v else None); mean=lambda v:(st.mean(v) if v else None)
out=[]
for place,sub,fx,fr in areas:
    xs=[x for x in recs if fx(x)]
    if fr: sel=[r for r in pu if fr(r)]; muni=sel[0]['muni']; homes=round(likely(sel)*share[muni])
    else: homes=mad_res
    bx=[x for x in xs if x.get('bill22') and not x.get('newbuild')]
    sx=[x for x in xs if x.get('school25_gross')]
    o=dict(place=place,sub=sub,homes=homes,
      a25=med([x['a25'] for x in xs]), a26=med([x['a26'] for x in xs]), notice_usd=med([x['notice_usd'] for x in xs]),
      bill22=med([x['bill22'] for x in bx]), bill25=med([x['bill25'] for x in bx]), bill_chg=med([x['bill25']-x['bill22'] for x in bx]),
      school25_net=med([x['school25_net'] for x in xs if x.get('school25_net')]),
      school_share=med([x['school25_net']/x['bill25'] for x in xs if x.get('school25_net') and x.get('bill25')]),
      school_chg_22_25=med([x['school25_gross']-x['school22_gross_est'] for x in sx if x.get('school22_gross_est') and not x.get('newbuild')]),
      mv26=med([x['mv26'] for x in xs if x.get('mv26')]),
      ref26_total=med([x['ref26_total'] for x in xs if x.get('ref26_total')]), ref26_new=med([x['ref26_new'] for x in xs if x.get('ref26_new')]),
      ref22_paid=med([x['ref22_paid'] for x in xs if x.get('ref22_paid')]),
      tot_bill_chg=(mean([x['bill25']-x['bill22'] for x in bx])*homes if bx else None),
      tot_school25=(mean([x['school25_gross'] for x in sx])*homes if sx else None),
      tot_ref26=(mean([x['ref26_total'] for x in xs if x.get('ref26_total')])*homes))
    out.append(o)
json.dump(out,open("costs.json","w"),indent=0)
print("residential share in sample:",{k:round(v,2) for k,v in share.items()})
tot=sum(o['homes'] for o in out); print("homes total", tot, "(+ Village Wd 7 and others not shown)")
for o in out:
    f=lambda v,d=0: '' if v is None else f"{v:,.{d}f}"
    print(f"{o['place'][:18]:18} {o['sub'][:14]:14} homes {o['homes']:5} | assessed {f(o['a25'])}->{f(o['a26'])} (+{f(o['notice_usd'])}) | bill {f(o['bill22'])}->{f(o['bill25'])} (+{f(o['bill_chg'])}) | school25 {f(o['school25_net'])} share {f((o['school_share'] or 0)*100,0)}% school22-25 +{f(o['school_chg_22_25'])} | ref26 4yr {f(o['ref26_total'])} new {f(o['ref26_new'])} | ref22 paid {f(o['ref22_paid'])} | totals: extra/yr {f((o['tot_bill_chg'] or 0)/1e6,2)}M school25 {f((o['tot_school25'] or 0)/1e6,1)}M ref26 {f(o['tot_ref26']/1e6,1)}M")
