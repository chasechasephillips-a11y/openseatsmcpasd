import csv, os, statistics as st, json, random, math
from parse import parse
R="/home/user/openseatsmcpasd/research_notes/MCPASD referendum 2026 vs 2022/"
ECON={"City of Middleton":.04,"Town of Middleton":.08,"Village of Cross Plains":.03,"Town of Cross Plains":.04,"Town of Springfield":-.02,"City of Madison":.04,"Town of Berry":-.06,"Town of Westport":.09}
R25=101_150_743/11_729_700_033*1000          # 2025-26 equalized rate (DPI), per $1,000
R26F=101_150_743/13_060_000_000*1000         # 2026-27 if levy flat, on DOR 2026 TID-out base
R26U=R26F*1.08                                # 2026-27 if levy +8%
samp=list(csv.DictReader(open("sample.csv")))
recs=[]
for r in samp:
    fn=f"pages/{r['parcel']}.html"
    if not os.path.exists(fn): continue
    d=parse(fn)
    if not d or 'G1' not in d['classes']: continue
    A=d['assessed']; tx=d['tax']
    if 2025 not in A or 2026 not in A or 2025 not in tx or 2022 not in tx or not A[2025]: continue
    unit=r['unit']; muni=r['muni']
    if unit.startswith('C Madison'): unit='Madison wards (MCPASD part)'
    net=lambda y: tx[y]['taxes']-tx[y]['lottery']-tx[y]['firstdollar']
    rec=dict(parcel=r['parcel'],unit=unit,muni=muni,a25=A[2025],a26=A[2026],mv25=d['efmv'].get(2025),
             jump=A[2026]/A[2025]-1, bill22=net(2022), bill25=net(2025),
             school25_net=d['school_net'] if d['school_year']==2025 else None,
             slc25=d['slc_2025'], mixed=len(d['classes'])>1, mv22=d['efmv'].get(2022))
    rec['newbuild']= bool(rec['mv22'] and rec['mv25'] and rec['mv25']/rec['mv22']>1.6) or rec['bill22']<0.6*rec['bill25']
    recs.append(rec)
# Madison: city open data (2026 vs 2025 assessments); ratio ~0.97 assumed for market value
for x in json.load(open("madison_parcels.json")):
    if x['PropertyClass']!='Residential' or not x['CurrentTotal'] or not x['PreviousTotal']: continue
    recs.append(dict(parcel=x['Parcel'],unit='Madison wards (MCPASD part)',muni='City of Madison',a25=x['PreviousTotal'],a26=x['CurrentTotal'],
        mv25=x['PreviousTotal']/0.97, jump=x['CurrentTotal']/x['PreviousTotal']-1, bill22=None, bill25=None, school25_net=None, slc25=None, newbuild=False, madison=True))
# revaluation regime by municipality, from the sample itself
reg={}
for m in ECON:
    j=[x['jump'] for x in recs if x['muni']==m]
    if not j: continue
    med=st.median(j)
    reg[m]=('revalued' if med>0.15 else 'unchanged' if abs(med)<0.02 else 'annual update', med, len(j))
# value-weighted mean notice change per municipality (sample), used to keep each muni's total on DOR's market estimate
jbar={}
for m in ECON:
    xs=[x for x in recs if x['muni']==m]
    if xs: jbar[m]=sum(x['a26'] for x in xs)/sum(x['a25'] for x in xs)-1
for x in recs:
    # market value moves with DOR's residential economic change for the muni; a home's share within the muni moves with its notice vs the muni average
    x['mv26']= x['mv25']*(1+ECON[x['muni']])*(1+x['jump'])/(1+jbar[x['muni']]) if x['mv25'] else None
    g25=None
    if x['school25_net'] is not None and x['slc25'] is not None: g25=x['school25_net']+x['slc25']
    elif x.get('madison'): g25=x['mv25']*R25/1000
    if g25 and x['mv26']:
        x['school25_gross']=g25
        x['school26_flat']=g25*(x['mv26']/x['mv25'])*(R26F/R25)
        x['school26_up8']=g25*(x['mv26']/x['mv25'])*(R26U/R25)
json.dump(recs, open("parcel_results.json","w"))
print("usable homes",len(recs)); print('jbar',{k:round(v*100,1) for k,v in jbar.items()}); print({k:(v[0],round(v[1]*100,1),v[2]) for k,v in reg.items()})
print("rates", round(R25,3), round(R26F,3), round(R26U,3))
