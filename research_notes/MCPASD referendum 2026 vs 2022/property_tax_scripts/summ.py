import json, csv, statistics as st, random, math
R="/home/user/openseatsmcpasd/research_notes/MCPASD referendum 2026 vs 2022/"
recs=json.load(open("parcel_results.json"))
order=["C Middleton Wds 1-4","C Middleton Wds 5-8, 21","C Middleton Wds 9-13,19,22,24","C Middleton Wds 14-18",
"T Middleton Wds 1, 3-4","T Middleton Wd 2, 4A","T Middleton Wds 5-8","V Cross Plains Wds 1-6","V Cross Plains Wd 7",
"Madison wards (MCPASD part)","T Springfield Wds 1-4","T Cross Plains Wds 1-2","T Berry Wds 1-2","T Westport Wds 1-5"]
# votes 2026 by unit, partisan
pv=list(csv.DictReader(open(R+"partisan_by_ward_2026.csv")))
votes={}
for x in pv:
    u='Madison wards (MCPASD part)' if x['reporting_unit'].startswith('C Madison') else x['reporting_unit'].replace('T Middleton Wd 2, 4A','T Middleton Wd 2, 4A')
    v=votes.setdefault(u,dict(yes=0,no=0,dem_w=0.0))
    y,n=int(x['ref_yes']),int(x['ref_no']); v['yes']+=y; v['no']+=n; v['dem_w']+=(y+n)*float(x['gov_dem_2party_pct'] or 0)
for u,v in votes.items(): v['tot']=v['yes']+v['no']; v['yes_pct']=100*v['yes']/v['tot']; v['dem']=v['dem_w']/v['tot']
# 2022->2026 change by comparison unit
wc=list(csv.DictReader(open(R+"ward_change.csv")))
chg={}
for x in wc:
    if x['level']!='comparison_unit' or not x['yes_pct_2022'] or not x['yes_pct_2026']: continue
    chg[x['unit']]=dict(d=float(x['chg_yes_pct_pts']), dno=int(x['chg_no']), y22=float(x['yes_pct_2022']), y26=float(x['yes_pct_2026']))
mad=[x for x in wc if x['level']=='municipality' and x['municipality']=='City of Madison'][0]
chg['Madison wards (MCPASD part)']=dict(d=float(mad['chg_yes_pct_pts']),dno=int(mad['chg_no']))
tm=[x for x in wc if x['level']=='municipality' and x['municipality']=='Town of Middleton'][0]
cmap={"C Middleton Wds 1-4":"C Middleton Wds 1-4","C Middleton Wds 5-8, 21":"C Middleton Wds 5-8 (+21)","C Middleton Wds 9-13,19,22,24":"C Middleton Wds 9-13,19 (+22,+24)","C Middleton Wds 14-18":"C Middleton Wds 14-18","V Cross Plains Wds 1-6":"V Cross Plains Wds 1-6","T Springfield Wds 1-4":"T Springfield Wds 1-4","T Cross Plains Wds 1-2":"T Cross Plains Wds 1-2","T Berry Wds 1-2":"T Berry Wds 1-2","T Westport Wds 1-5":"T Westport Wds 1-5","Madison wards (MCPASD part)":"Madison wards (MCPASD part)"}
def find(key):
    for k in chg:
        if k.replace(' ','').startswith(key.replace(' ','')[:18]): return chg[k]
    return None
med=lambda a: st.median(a) if a else None
out=[]
tv=[votes[u] for u in votes if u.startswith('T Middleton') and votes[u]['tot']]
votes['Town of Middleton (all)']=dict(tot=sum(v['tot'] for v in tv), yes_pct=sum(v['yes'] for v in tv)/sum(v['tot'] for v in tv)*100, dem=sum(v['dem']*v['tot'] for v in tv)/sum(v['tot'] for v in tv))
for u in order+['Town of Middleton (all)']:
    xs=[x for x in recs if x['unit']==u] if u!='Town of Middleton (all)' else [x for x in recs if x['muni']=='Town of Middleton']
    if not xs: continue
    s=[x for x in xs if x.get('school25_gross')]
    bx=[x for x in xs if x.get('bill22') and not x.get('newbuild')]
    rnd=random.Random(1); boots=[]
    for _ in range(400):
        b=[rnd.choice(xs)['jump'] for _ in xs]; boots.append(st.median(b))
    boots.sort()
    row=dict(unit=u, homes=len(xs), mv25=med([x['mv25'] for x in xs if x['mv25']]),
        notice_jump=100*med([x['jump'] for x in xs]), jump_lo=100*boots[10], jump_hi=100*boots[389],
        bill22=med([x['bill22'] for x in bx]), bill25=med([x['bill25'] for x in bx]),
        bill_chg_pct=(100*med([x['bill25']/x['bill22']-1 for x in bx]) if bx else None),
        bill_chg_usd=med([x['bill25']-x['bill22'] for x in bx]),
        school25=med([x['school25_gross'] for x in s]),
        school26_flat_usd=med([x['school26_flat']-x['school25_gross'] for x in s]),
        school26_up8_usd=med([x['school26_up8']-x['school25_gross'] for x in s]),
        school26_flat_pct=100*med([x['school26_flat']/x['school25_gross']-1 for x in s]),
        school26_up8_pct=100*med([x['school26_up8']/x['school25_gross']-1 for x in s]))
    v=votes.get(u,{}); row.update(ref_votes=v.get('tot'), yes26=v.get('yes_pct'), dem26=v.get('dem'))
    row['resid26']= v['yes_pct']-(7.0+0.69*v['dem']) if v else None
    c=None
    if u in cmap: c=find(cmap[u]) if u!='Madison wards (MCPASD part)' else chg[u]
    if u.startswith('T Middleton') or u.startswith('Town of Middleton'): c=dict(d=float(tm['chg_yes_pct_pts']),dno=int(tm['chg_no']),note='whole town')
    row['yes_chg_pts']=c['d'] if c else None; row['no_chg']=c['dno'] if c else None
    out.append(row)
with open("unit_summary.csv","w",newline="") as fh:
    w=csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for r in out:
    print(f"{r['unit'][:30]:30} n={r['homes']:3} MV25={r['mv25'] or 0:>9,.0f} notice {r['notice_jump']:+6.1f}% [{r['jump_lo']:+.0f},{r['jump_hi']:+.0f}]  bill22->25 {(r['bill_chg_pct'] or 0):+5.1f}% ({(r['bill_chg_usd'] or 0):+,.0f}) nb={len([1 for _ in range(0)])}  school25 {r['school25'] or 0:,.0f}  2026 school {r['school26_flat_usd'] or 0:+,.0f}/{r['school26_up8_usd'] or 0:+,.0f}  yes26 {r['yes26'] or 0:.1f} resid {r['resid26'] or 0:+.1f} dYes {r['yes_chg_pts']} dNo {r['no_chg']}")
# weighted correlations across units
def wcorr(a,b,w):
    W=sum(w); ma=sum(x*y for x,y in zip(a,w))/W; mb=sum(x*y for x,y in zip(b,w))/W
    cov=sum(y*(x-ma)*(z-mb) for x,z,y in zip(a,b,w)); va=sum(y*(x-ma)**2 for x,y in zip(a,w)); vb=sum(y*(z-mb)**2 for z,y in zip(b,w))
    return cov/math.sqrt(va*vb)
for xk in ['notice_jump','bill_chg_pct','school26_flat_usd']:
    for yk in ['resid26','yes_chg_pts']:
        rr=[r for r in out if r.get(xk) is not None and r.get(yk) is not None and r.get('ref_votes')]
        if yk=='yes_chg_pts': rr=[r for r in rr if not r['unit'].startswith('T Middleton') and r['unit']!='V Cross Plains Wd 7']
        else: rr=[r for r in rr if r['unit']!='Town of Middleton (all)']
        print(xk, 'vs', yk, 'n',len(rr), 'weighted r', round(wcorr([r[xk] for r in rr],[r[yk] for r in rr],[r['ref_votes'] for r in rr]),2))
