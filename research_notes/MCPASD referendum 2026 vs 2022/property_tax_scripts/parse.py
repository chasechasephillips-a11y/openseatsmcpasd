import re, html, glob, os, csv, json
def money(x): return float(x.replace('$','').replace(',',''))
def parse(fn):
    s=open(fn,errors='ignore').read()
    t=html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)))
    t=re.sub(r'\s+',' ',t)
    if 'Parcel Not Found' in t: return None
    d={}
    # assessed totals by year (Valuations by Assessment Year table)
    tot={}
    for m in re.finditer(r'\b(20\d\d) Total [\d.]+ ((?:\$[\d,]+(?:\.\d\d)? ?)+)', t):
        vals=re.findall(r'\$[\d,]+(?:\.\d\d)?', m.group(2)); tot.setdefault(int(m.group(1)), money(vals[-1]))
    d['assessed']=tot
    cls=set(re.findall(r'\b2026 \d\d/\d\d/\d{4} (G\d|X\d|W\d)', t)) or set(re.findall(r'\b2025 \d\d/\d\d/\d{4} (G\d|X\d|W\d)', t))
    d['classes']=sorted(cls)
    # year header and ratio / EFMV rows
    m=re.search(r'Assessment Detail .*? Assessment Year ((?:20\d\d ?)+)', t)
    years=[int(y) for y in m.group(1).split()] if m else []
    m2=re.search(r'Average Assessment Ratio ((?:(?:N/A|[\d.]+) ?)+)', t)
    m3=re.search(r'Estimated Fair Market Value ((?:(?:N/A|\$[\d,]+) ?)+)', t)
    d['ratio']={y:(float(v) if v!='N/A' else None) for y,v in zip(years, m2.group(1).split())} if m2 else {}
    d['efmv']={y:(money(v) if v!='N/A' else None) for y,v in zip(years, m3.group(1).split())} if m3 else {}
    vd=re.search(r'Valuation Date (\d\d/\d\d/\d{4})', t); d['valdate_latest']=vd.group(1) if vd else None
    # tax bills by year
    tx={}
    for m in re.finditer(r'Tax Year (20\d\d) Assessed Land Value .*? Taxes: (\$[\d,]+\.\d\d) Lottery Credit\(-\) : (\$[\d,]+\.\d\d) First Dollar Credit\(-\): (\$[\d,]+\.\d\d)', t):
        y=int(m.group(1))
        if y not in tx: tx[y]=dict(taxes=money(m.group(2)), lottery=money(m.group(3)), firstdollar=money(m.group(4)))
    d['tax']=tx
    m=re.search(r'School Levy Tax Credit: (\$[\d,]+\.\d\d)', t); d['slc_2025']=money(m.group(1)) if m else None
    m=re.search(r'Tax Amounts for (20\d\d) Tax Year .*?MID-CR PLAINS SCHOOL DIST (\$[\d,]+\.\d\d)', t)
    d['school_year']=int(m.group(1)) if m else None; d['school_net']=money(m.group(2)) if m else None
    return d
if __name__=="__main__":
    for fn in sorted(glob.glob("pages/*.html"))[:4]:
        print(os.path.basename(fn), json.dumps(parse(fn))[:900]); print()
