import json, csv, statistics as st, math, collections
R="/home/user/openseatsmcpasd/research_notes/MCPASD referendum 2026 vs 2022/"
demo=json.load(open("demo_by_unit.json")); ren=json.load(open("renters_by_unit.json"))
p26={r['reporting_unit']:r for r in csv.DictReader(open(R+"partisan_by_ward_2026.csv"))}
w26={r['reporting_unit']:r for r in csv.DictReader(open(R+"ward_results_2026.csv"))}
recs=json.load(open("../parcels/parcel_results.json"))
mad=json.load(open("../parcels/madison_all.json"))
areas=json.load(open("areas.json"))  # has schInc, bill info at area level
# property by reporting unit
prop=collections.defaultdict(dict)
for u in set(x['unit'] for x in recs if not x.get('madison')):
    xs=[x for x in recs if x['unit']==u and not x.get('madison')]
    prop[u]=dict(mv=st.median([x['mv25'] for x in xs if x.get('mv25')]), notice=100*st.median([x['jump'] for x in xs]),
                 bill=100*st.median([x['bill25']/x['bill22']-1 for x in xs if x.get('bill22') and not x.get('newbuild')]))
mw=collections.defaultdict(list)
for x in mad:
    if x['PropertyClass']=='Residential' and x['CurrentTotal'] and x['PreviousTotal'] and x['Ward']: mw["C Madison Wd %03d"%int(x['Ward'])].append(x)
for u,xs in mw.items(): prop[u]=dict(mv=st.median([x['PreviousTotal']/0.97 for x in xs]), notice=100*st.median([x['CurrentTotal']/x['PreviousTotal']-1 for x in xs]), bill=None)
# school tax increase by municipality (from areas.json; City/Town/Village/towns)
muni_sch={}
for a in areas:
    if a['schInc'] is not None and a['place']!='Madison': muni_sch.setdefault(a['place'],[]).append((a['sub'],a['schInc']))
def sch_for(u):
    m={'C Middleton':'City of Middleton','T Middleton':'Town of Middleton','V Cross':'Village of Cross Plains','T Springf':'Town of Springfield','T Cross':'Town of Cross Plains','T Berry':'Town of Berry','T Westp':'Town of Westport'}
    for k,v in m.items():
        if u.startswith(k):
            if v=='Town of Middleton': return {'T Middleton Wds 1, 3-4':20.6,'T Middleton Wd 2, 4A':20.6,'T Middleton Wds 5-8':14.9}.get(u)
            return muni_sch.get(v,[(None,None)])[0][1]
    return None
rows=[]
for u,r in p26.items():
    y,n=int(r['ref_yes']),int(r['ref_no'])
    if y+n<100 or u not in demo: continue
    d=demo[u]; rn=ren.get(u,{}); pr=prop.get(u,{}); w=w26.get(u,{})
    dem=float(r['gov_dem_2party_pct']); yes=100*y/(y+n)
    rows.append(dict(unit=u, votes=y+n, split=r['split_unit']=='yes', dem=dem, yes=yes, resid=yes-(7.0+0.69*dem), floor=100*(dem-yes)/dem,
        rolloff=float(w['rolloff_pct']) if w.get('rolloff_pct') else None,
        bph=(int(w['ballots_with_question'])/d['hh']) if w.get('ballots_with_question') and d['hh'] else None,
        kids=100*d['kids']/d['pop'] if d['pop'] else None, school=100*d['school']/d['hh'] if d['hh'] else None, senior=100*d['senior']/d['pop'] if d['pop'] else None,
        apt=100*rn['apt_est']/rn['units'] if rn.get('units') else None, mv=pr.get('mv'), notice=pr.get('notice'), bill=pr.get('bill'), schInc=sch_for(u)))
json.dump(rows, open("deep_rows.json","w"), indent=0)
def wmean(a,w): return sum(x*y for x,y in zip(a,w))/sum(w)
def wcorr(a,b,w):
    ma,mb=wmean(a,w),wmean(b,w)
    return sum(y*(x-ma)*(z-mb) for x,z,y in zip(a,b,w))/math.sqrt(sum(y*(x-ma)**2 for x,y in zip(a,w))*sum(y*(z-mb)**2 for z,y in zip(b,w)))
def wresid(a,c,w):  # residual of a on c (weighted OLS)
    mc,ma=wmean(c,w),wmean(a,w); b=sum(y*(x-mc)*(z-ma) for x,z,y in zip(c,a,w))/sum(y*(x-mc)**2 for x,y in zip(c,w))
    return [z-(ma+b*(x-mc)) for x,z in zip(c,a)]
def table(rows, xs, ys, label):
    print(f"\n=== {label}: n={len(rows)} ===")
    print("driver".ljust(10), "".join(f"{y:>12}" for y in ys), "   partial r with Yes | Dem")
    for x in xs:
        rr=[r for r in rows if r.get(x) is not None]
        w=[r['votes'] for r in rr]; line=x.ljust(10)
        for y in ys:
            r2=[r for r in rr if r.get(y) is not None]
            line+=f"{wcorr([r[x] for r in r2],[r[y] for r in r2],[r['votes'] for r in r2]):>12.2f}" if len(r2)>3 else f"{'':>12}"
        if x!='dem':
            pa=wcorr(wresid([r[x] for r in rr],[r['dem'] for r in rr],w), wresid([r['yes'] for r in rr],[r['dem'] for r in rr],w), w)
            line+=f"   {pa:+.2f} (n={len(rr)})"
        print(line)
xs=['dem','kids','school','senior','apt','mv','notice','bill','schInc','bph']; ys=['yes','resid','floor','rolloff']
table(rows, xs, ys, "All 2026 reporting units with 100+ votes")
table([r for r in rows if not r['split']], xs, ys, "Units fully inside the district")
for r in sorted(rows,key=lambda r:-r['school']): print(f"{r['unit']:32} votes {r['votes']:5} kids {r['kids']:4.1f}% school-age/100HH {r['school']:5.1f} 65+ {r['senior']:4.1f}% apt {r['apt'] or 0:4.0f}% MV {r['mv'] or 0:>9,.0f} yes {r['yes']:4.1f} dem {r['dem']:4.1f} resid {r['resid']:+5.1f} floor {r['floor']:4.1f}")
