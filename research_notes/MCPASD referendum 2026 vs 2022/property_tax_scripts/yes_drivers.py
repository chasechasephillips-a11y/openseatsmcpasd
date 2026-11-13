"""What went with a Yes vote: unit-level variables, weighted raw and partial correlations,
and Yes in the top vs bottom third of units for each variable. Writes yes_drivers_by_ward.csv."""
import csv, json, math, statistics as st, collections, os
R = "/home/user/openseatsmcpasd/research_notes/MCPASD referendum 2026 vs 2022/"
S = os.environ.get("SCRATCH", "/tmp/claude-0/-home-user-openseatsmcpasd/32ddd594-28a3-57de-8c13-227f23b7fc20/scratchpad/")
EQ26, REF26 = 13_060_000_000, 118_500_000
drv = list(csv.DictReader(open(R + "drivers_by_ward.csv")))
hhk = {r["reporting_unit"]: float(r["pct"]) for r in csv.DictReader(open(R + "households_with_kids_by_ward.csv"))}
recs = json.load(open(S + "parcels/parcel_results.json"))
mad = json.load(open(S + "parcels/madison_all.json"))
# Madison: scale each ward's median 2026 assessment by the sample's mv26/a26 ratio
mx = [x for x in recs if x.get("madison") and x.get("mv26") and x.get("a26")]
k_mad = st.median([x["mv26"] / x["a26"] for x in mx])
mw = collections.defaultdict(list)
for x in mad:
    if x["PropertyClass"] == "Residential" and x["CurrentTotal"] and x["Ward"]:
        mw["C Madison Wd %03d" % int(x["Ward"])].append(x["CurrentTotal"])
units = collections.defaultdict(list)
for x in recs:
    if not x.get("madison"): units[x["unit"]].append(x)
rows = []
for d in drv:
    u = d["reporting_unit"]; f = lambda k: float(d[k]) if d[k] not in ("", None) else None
    r = dict(unit=u, votes=int(d["ref_votes"]), yes=f("yes_pct"), dem=f("dem_gov_pct"), resid=f("yes_vs_partisan_expectation"),
             hhk=hhk.get(u), senior=f("age65plus_pct_2020"), apt=f("apartment_share_pct"),
             bph=f("ballots_per_household"), notice=f("median_notice_change_pct"), billpct=f("median_bill_change_2022_25_pct"))
    if u.startswith("C Madison"):
        r["ref26"] = REF26 * st.median(mw[u]) * k_mad / EQ26; r["bill25"] = r["billusd"] = None
    else:
        xs = units[u]; bx = [x for x in xs if x.get("bill22") and not x.get("newbuild")]
        r["ref26"] = REF26 * st.median([x["mv26"] for x in xs if x.get("mv26")]) / EQ26
        r["bill25"] = st.median([x["bill25"] for x in bx]); r["billusd"] = st.median([x["bill25"] - x["bill22"] for x in bx])
    rows.append(r)
def wm(a, w): return sum(x * y for x, y in zip(a, w)) / sum(w)
def wc(a, b, w):
    ma, mb = wm(a, w), wm(b, w)
    return sum(y * (x - ma) * (z - mb) for x, z, y in zip(a, b, w)) / math.sqrt(sum(y * (x - ma) ** 2 for x, y in zip(a, w)) * sum(y * (z - mb) ** 2 for z, y in zip(b, w)))
def wr(a, c, w):
    mc, ma = wm(c, w), wm(a, w); b = sum(y * (x - mc) * (z - ma) for x, z, y in zip(c, a, w)) / sum(y * (x - mc) ** 2 for x, y in zip(c, w))
    return [z - (ma + b * (x - mc)) for x, z in zip(c, a)]
VARS = [("dem", "Democratic vote share"), ("hhk", "Households with kids"), ("bph", "Turnout (ballots per household)"),
        ("senior", "Residents 65 and older"), ("apt", "Homes that are apartments"), ("ref26", "Referendum cost, median home"),
        ("bill25", "2025 tax bill, median home"), ("billusd", "Tax bill increase since 2022 ($)"),
        ("billpct", "Tax bill increase since 2022 (%)"), ("notice", "2026 assessment notice jump")]
out = []
for k, lab in VARS:
    rr = [r for r in rows if r.get(k) is not None]; w = [r["votes"] for r in rr]
    raw = wc([r[k] for r in rr], [r["yes"] for r in rr], w)
    part = None if k == "dem" else wc(wr([r[k] for r in rr], [r["dem"] for r in rr], w), wr([r["yes"] for r in rr], [r["dem"] for r in rr], w), w)
    s = sorted(rr, key=lambda r: r[k]); t = max(3, len(s) // 3)
    pool = lambda g: sum(r["yes"] * r["votes"] for r in g) / sum(r["votes"] for r in g)
    out.append(dict(k=k, l=lab, r=round(raw, 2), p=None if part is None else round(part, 2), n=len(rr), lo=round(pool(s[:t]), 1), hi=round(pool(s[-t:]), 1), t=t))
    print(f"{lab:36} raw {raw:+.2f}  partial {'' if part is None else f'{part:+.2f}'}  n={len(rr)}  bottom {t}: {pool(s[:t]):.1f}%  top {t}: {pool(s[-t:]):.1f}%")
json.dump(dict(vars=out, rows=rows), open(S + "renters/yes_drivers.json", "w"), indent=0)
with open(R + "yes_drivers_by_ward.csv", "w", newline="") as fh:
    cols = ["unit", "votes", "yes", "dem", "resid", "hhk", "bph", "senior", "apt", "ref26", "bill25", "billusd", "billpct", "notice"]
    wtr = csv.writer(fh); wtr.writerow(["reporting_unit", "ref_votes", "yes_pct", "dem_gov_pct", "yes_vs_partisan_expectation", "households_with_kids_pct_2020",
        "ballots_per_household", "age65plus_pct_2020", "apartment_share_pct", "ref2026_4yr_cost_median_home", "median_bill_2025", "median_bill_change_2022_25_usd",
        "median_bill_change_2022_25_pct", "median_notice_change_pct"])
    for r in rows: wtr.writerow([("" if r.get(c) is None else (round(r[c]) if c in ("ref26", "bill25", "billusd") else r[c])) for c in cols])
for r in sorted(rows, key=lambda r: -r["ref26"]): print(f"{r['unit']:30} yes {r['yes']:5.1f} dem {r['dem']:4.1f} resid {r['resid']:+5.1f} ref26 {r['ref26']:7.0f} bill25 {r['bill25'] or 0:7.0f} billusd {r['billusd'] or 0:6.0f} hhk {r['hhk']}")
