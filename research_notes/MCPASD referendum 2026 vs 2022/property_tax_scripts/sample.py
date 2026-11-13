import csv, random, time, urllib.request, os, sys
random.seed(20261112)
rows=list(csv.DictReader(open("parcels_units.csv")))
quota={"C Middleton Wds 1-4":50,"C Middleton Wds 5-8, 21":50,"C Middleton Wds 9-13,19,22,24":50,"C Middleton Wds 14-18":50,
"T Middleton Wds 1, 3-4":40,"T Middleton Wd 2, 4A":40,"T Middleton Wds 5-8":40,"V Cross Plains Wds 1-6":50,"V Cross Plains Wd 7":25,
"T Berry Wds 1-2":25,"T Cross Plains Wds 1-2":25,"T Springfield Wds 1-4":30,"T Westport Wds 1-5":20}
samp=[]
for u,n in quota.items():
    pool=[r for r in rows if r['unit']==u and int(r['imp'])>=60000 and int(r['land'])+int(r['imp'])<2500000]
    samp+=[dict(r) for r in random.sample(pool, min(n,len(pool)))]
mad=[r for r in rows if (r['unit'] or '').startswith('C Madison')]
samp+=[dict(r) for r in random.sample(mad, min(90,len(mad)))]
with open("sample.csv","w",newline="") as fh:
    w=csv.DictWriter(fh, fieldnames=list(samp[0].keys())); w.writeheader(); w.writerows(samp)
