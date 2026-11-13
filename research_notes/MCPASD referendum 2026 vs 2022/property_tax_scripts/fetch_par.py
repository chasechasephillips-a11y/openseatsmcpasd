import csv, time, urllib.request, os
from concurrent.futures import ThreadPoolExecutor
samp=list(csv.DictReader(open("sample.csv")))
todo=[r['parcel'] for r in samp if not (os.path.exists(f"pages/{r['parcel']}.html") and os.path.getsize(f"pages/{r['parcel']}.html")>20000)]
print("todo",len(todo),flush=True)
def get(pn):
    req=urllib.request.Request("https://accessdane.danecounty.gov/"+pn, headers={"User-Agent":"Mozilla/5.0 (MCPASD referendum research; low-rate sampling)"})
    for t in range(3):
        try:
            b=urllib.request.urlopen(req, timeout=90).read(); open(f"pages/{pn}.html","wb").write(b); break
        except Exception as e: time.sleep(5*(t+1))
    time.sleep(0.5)
with ThreadPoolExecutor(3) as ex:
    for i,_ in enumerate(ex.map(get,todo)):
        if i%50==0: print(i,flush=True)
print("done",flush=True)
