"""Test new neighborhood variables against the 2026 MCPASD referendum vote.
Outcome: Yes % in the 19 reporting units with 100+ referendum votes (12 with tax-bill history),
weighted by referendum votes. For each variable: raw weighted r with Yes, partial r holding the
Democratic governor share constant (plus leave-one-out range), partial r holding Dem share and
bill growth (n = 12), Yes in the top vs. bottom third, r with roll-off and with the Democratic-ticket
No share, the same-party-lean slope, and r with the 2022-to-2026 change in Yes (17 comparison units).
Writes new_variables_by_ward.csv (ward-level aggregates only) and levers/results.json."""
import csv, json, math, os, collections
import numpy as np
S = os.environ.get("SCRATCH", "/tmp/claude-0/-home-user-openseatsmcpasd/32ddd594-28a3-57de-8c13-227f23b7fc20/scratchpad/")
L = S + "levers/"
R = "/home/user/openseatsmcpasd/research_notes/MCPASD referendum 2026 vs 2022/"
O = "/home/user/openseatsmcpasd/research_notes/MCPASD referendum Yes and No levers/"
new = json.load(open(L + "units_new.json"))
yd = {r["reporting_unit"]: r for r in csv.DictReader(open(R + "yes_drivers_by_ward.csv"))}
p26 = {r["reporting_unit"]: r for r in csv.DictReader(open(R + "partisan_by_ward_2026.csv"))}
w26 = {r["reporting_unit"]: r for r in csv.DictReader(open(R + "ward_results_2026.csv"))}
chg = {r["unit"]: r for r in csv.DictReader(open(R + "ward_change.csv")) if r["level"] == "comparison_unit"}
fl = lambda v: float(v) if v not in ("", None) else None
rows = []
for u, d in yd.items():
    p, w, n = p26[u], w26[u], new.get(u, {})
    cu = w["comparison_unit"]; c = chg[cu]
    dem = fl(d["dem_gov_pct"]); yes = fl(d["yes_pct"])
    r = dict(unit=u, votes=int(d["ref_votes"]), yes=yes, dem=dem, split=p["split_unit"] == "yes", comp=cu,
        floor=100 * (dem - yes) / dem, rolloff=fl(w["rolloff_pct"]),
        hhk=fl(d["households_with_kids_pct_2020"]), bph=fl(d["ballots_per_household"]), senior=fl(d["age65plus_pct_2020"]),
        apt=fl(d["apartment_share_pct"]), ref26=fl(d["ref2026_4yr_cost_median_home"]), bill25=fl(d["median_bill_2025"]),
        billusd=fl(d["median_bill_change_2022_25_usd"]), billpct=fl(d["median_bill_change_2022_25_pct"]), notice=fl(d["median_notice_change_pct"]),
        # election-based new variables
        yes22=fl(c["yes_pct_2022"]), yes_chg=fl(c["chg_yes_pct_pts"]),
        turnout_chg=100 * (float(c["ballots_cast_unit_2026"]) / float(c["ballots_cast_unit_2022"]) - 1) if fl(c["ballots_cast_unit_2022"]) else None,
        refvotes_chg=100 * (float(c["ref_votes_2026"]) / float(c["ref_votes_2022"]) - 1) if fl(c["ref_votes_2022"]) else None,
        sr1=fl(p["sr1_no_pct"]), sr2=fl(p["sr2_no_pct"]), sr3=fl(p["sr3_no_pct"]),
        veto_defect=dem - fl(p["sr1_no_pct"]),
        split_ag=dem - fl(p["ag_dem_2party_pct"]), split_tre=dem - fl(p["tre_dem_2party_pct"]),
        bpa=int(w["ballots_with_question"]) / n["adults"] if n.get("adults") else None,
        # census / ACS / parcel / GIS variables (MCPASD part of each unit)
        ba=n.get("ba_plus_pct"), inc=(n.get("median_hh_income") or 0) / 1000 or None, pov=n.get("poverty_pct"),
        moved=n.get("moved_2020_plus_pct"), ownmoved=n.get("owner_moved_2020_plus_pct"), newhomes=n.get("lu_new_pct"),
        built10=n.get("built_2010_plus_pct"), priv=n.get("private_k12_pct"), poc=n.get("poc_pct"), asian=n.get("asian_pct"),
        hisp=n.get("hisp_pct"), dens=math.log10(n["hh_per_km2"]) if n.get("hh_per_km2") else None,
        dist=n.get("dist_any_km"), distel=n.get("dist_elem_km"), burden=n.get("owner_cost_burden30_pct"))
    rows.append(r)
def wm(a, w): return sum(x * y for x, y in zip(a, w)) / sum(w)
def wc(a, b, w):
    ma, mb = wm(a, w), wm(b, w)
    den = math.sqrt(sum(y * (x - ma) ** 2 for x, y in zip(a, w)) * sum(y * (z - mb) ** 2 for z, y in zip(b, w)))
    return sum(y * (x - ma) * (z - mb) for x, z, y in zip(a, b, w)) / den if den else float("nan")
def wresid(y, X, w):   # residual of y after weighted least squares on the columns of X (with intercept)
    X = np.column_stack([np.ones(len(y))] + [np.asarray(c, float) for c in X]); W = np.sqrt(np.asarray(w, float))
    beta, *_ = np.linalg.lstsq(X * W[:, None], np.asarray(y, float) * W, rcond=None)
    return list(np.asarray(y, float) - X @ beta)
def partial(rr, k, ctrl=("dem",), out="yes"):
    w = [r["votes"] for r in rr]; C = [[r[c] for r in rr] for c in ctrl]
    ex, ey = wresid([r[k] for r in rr], C, w), wresid([r[out] for r in rr], C, w)
    b = sum(x * y * v for x, y, v in zip(ex, ey, w)) / sum(x * x * v for x, v in zip(ex, w))
    return wc(ex, ey, w), b
def wsd(a, w):
    m = wm(a, w); return math.sqrt(sum(y * (x - m) ** 2 for x, y in zip(a, w)) / sum(w))
VARS = [  # key, label, group
    ("dem", "Democratic governor share", "existing"), ("billpct", "Tax bill growth 2022-25, %", "existing"),
    ("billusd", "Tax bill growth 2022-25, $", "existing"), ("bill25", "2025 tax bill, median home ($)", "existing"),
    ("ref26", "Referendum 4-yr cost, median home ($)", "existing"), ("hhk", "Households with kids, %", "existing"),
    ("bph", "Ballots per household (turnout)", "earlier"), ("senior", "Residents 65+, %", "earlier"),
    ("apt", "Apartment share of housing, %", "earlier"), ("notice", "2026 assessment notice jump, %", "earlier"),
    ("ba", "Adults 25+ with BA or more, %", "new"), ("inc", "Median household income ($000)", "new"),
    ("pov", "Poverty rate, %", "new"), ("moved", "Householders moved in 2020 or later, %", "new"),
    ("ownmoved", "Owners moved in 2020 or later, % of owners", "new"), ("newhomes", "Homes on land undeveloped in 2015, %", "new"),
    ("built10", "Housing built 2010 or later (ACS), %", "new"), ("priv", "K-12 kids in private or home school, %", "new"),
    ("poc", "People of color (2020), %", "new"), ("asian", "Asian (2020), %", "new"), ("hisp", "Hispanic (2020), %", "new"),
    ("yes22", "2022 referendum Yes, %", "new"), ("turnout_chg", "Ballots cast, change 2022-26, %", "new"),
    ("refvotes_chg", "Referendum votes, change 2022-26, %", "new"), ("rolloff", "Roll-off (skipped the question), %", "new"),
    ("bpa", "2026 ballots per 2020 adult", "new"),
    ("sr1", "No on partial-veto amendment, %", "new"), ("sr2", "No on worship amendment, %", "new"),
    ("sr3", "No on anti-discrimination amendment, %", "new"), ("veto_defect", "Dem share minus No on partial veto, pts", "new"),
    ("split_ag", "Governor minus AG Dem share, pts", "new"), ("split_tre", "Governor minus treasurer Dem share, pts", "new"),
    ("dist", "Distance to nearest MCPASD school, km", "new"), ("distel", "Distance to nearest elementary, km", "new"),
    ("dens", "Households per km2 (log10)", "new"), ("burden", "Owners paying 30%+ of income on housing, %", "new")]
TOTAL = sum(r["votes"] for r in rows)
# comparison-unit table for the change outcome (Town of Middleton's three 2026 units are one 2022 unit)
cg = collections.defaultdict(list)
for r in rows: cg[r["comp"]].append(r)
crow = []
for cu, rs in cg.items():
    v = sum(r["votes"] for r in rs); c = dict(unit=cu, votes=v)
    for k in [x[0] for x in VARS] + ["yes", "yes_chg"]:
        xs = [(r[k], r["votes"]) for r in rs if r.get(k) is not None]
        c[k] = sum(a * b for a, b in xs) / sum(b for a, b in xs) if xs else None
    crow.append(c)
res = []
for k, lab, grp in VARS:
    rr = [r for r in rows if r.get(k) is not None]; w = [r["votes"] for r in rr]; n = len(rr)
    raw = wc([r[k] for r in rr], [r["yes"] for r in rr], w)
    o = dict(k=k, label=lab, group=grp, n=n, raw=raw, sd=wsd([r[k] for r in rr], w), mean=wm([r[k] for r in rr], w))
    o["r_rolloff"] = wc([r[k] for r in rr], [r["rolloff"] for r in rr], w) if k != "rolloff" else None
    o["r_floor"] = wc([r[k] for r in rr], [r["floor"] for r in rr], w)
    s = sorted(rr, key=lambda r: r[k]); t = max(3, n // 3)
    pool = lambda g: sum(r["yes"] * r["votes"] for r in g) / sum(r["votes"] for r in g)
    o["lo3"], o["hi3"], o["t"] = pool(s[:t]), pool(s[-t:]), t
    if k != "dem":
        o["partial"], o["slope"] = partial(rr, k)
        loo = [partial([r for r in rr if r is not x], k)[0] for x in rr]; o["loo_min"], o["loo_max"] = min(loo), max(loo)
        o["margin_per_1000_per_sd"] = 20 * o["slope"] * o["sd"]
        ns = [r for r in rr if not r["split"]]
        o["partial_nonsplit"] = partial(ns, k)[0] if len(ns) >= 6 else None; o["n_nonsplit"] = len(ns)
        rb = [r for r in rr if r.get("billpct") is not None]
        if k not in ("billpct", "billusd", "bill25") and len(rb) >= 8: o["partial_dem_bill"] = partial(rb, k, ("dem", "billpct"))[0]; o["n_bill"] = len(rb)
        o["partial_floor"] = partial(rr, k, out="floor")[0]
    cr = [c for c in crow if c.get(k) is not None and c.get("yes_chg") is not None and k not in ("yes22",)]
    if k == "yes22": cr = [c for c in crow if c.get("yes_chg") is not None]
    cw = [c["votes"] for c in cr]
    o["n_chg"] = len(cr); o["r_chg"] = wc([c[k] for c in cr], [c["yes_chg"] for c in cr], cw)
    o["partial_chg"] = partial(cr, k, out="yes_chg")[0] if k != "dem" else None
    res.append(o)
def f(x, p=2): return "" if x is None or (isinstance(x, float) and math.isnan(x)) else (f"{x:+.{p}f}" if p == 2 else f"{x:.{p}f}")
print(f"{'variable':44} n  raw   part  LOO-range     part|dem+bill nonsplit  bot3  top3  r_roll r_flr  chg_r chg_part  mrg/1k/SD")
for o in res:
    print(f"{o['label'][:44]:44} {o['n']:2} {f(o['raw'])} {f(o.get('partial'))} [{f(o.get('loo_min'))},{f(o.get('loo_max'))}] {f(o.get('partial_dem_bill')):>6} {f(o.get('partial_nonsplit')):>6}  {o['lo3']:4.1f}  {o['hi3']:4.1f}  {f(o['r_rolloff']):>5} {f(o['r_floor'])}  {f(o['r_chg'])} {f(o.get('partial_chg')):>6}  {f(o.get('margin_per_1000_per_sd'),0):>5}  sd {o['sd']:.2f} slope {f(o.get('slope'))}")
json.dump(dict(results=res, rows=rows, comparison_rows=crow, total_votes=TOTAL), open(L + "results.json", "w"), indent=0, default=str)
# ---- ward-level CSV (aggregates only; all 2026 units that carried the question and have 2020 households in MCPASD)
cols = [("reporting_unit", None), ("in_19_unit_analysis", None), ("split_unit", None), ("comparison_unit_2022", None),
    ("ref_votes_2026", None), ("yes_pct_2026", 1), ("dem_gov_pct_2026", 1), ("dem_ticket_no_pct", 1), ("rolloff_pct_2026", 1),
    ("yes_pct_2022_comparison_unit", 1), ("yes_change_pts_comparison_unit", 1), ("ballots_cast_change_pct_comparison_unit", 1),
    ("ref_votes_change_pct_comparison_unit", 1), ("ballots_per_2020_adult_2026", 2),
    ("no_partial_veto_amend_pct", 1), ("no_worship_amend_pct", 1), ("no_antidiscrimination_amend_pct", 1), ("dem_minus_no_partial_veto_pts", 1),
    ("gov_minus_ag_dem_pts", 1), ("gov_minus_treasurer_dem_pts", 1),
    ("population_2020", 0), ("adults_18plus_2020", 0), ("households_2020", 0), ("housing_units_2020", 0),
    ("people_of_color_pct_2020", 1), ("asian_pct_2020", 1), ("hispanic_pct_2020", 1), ("black_pct_2020", 1),
    ("ba_plus_pct_acs", 1), ("ba_plus_moe", 1), ("median_hh_income_acs", -3), ("poverty_pct_acs", 1), ("poverty_moe", 1),
    ("householders_moved_2020plus_pct_acs", 1), ("householders_moved_2020plus_moe", 1), ("owners_moved_2020plus_pct_acs", 1),
    ("private_or_home_k12_pct_acs", 1), ("private_or_home_k12_moe", 1), ("built_2010plus_pct_acs", 1), ("built_2010plus_moe", 1),
    ("owner_cost_burden30_pct_acs", 1), ("homes_counted_parcels", 0), ("homes_on_land_undeveloped_2015_pct", 1),
    ("madison_dwelling_units_built_2015plus_pct", 1), ("households_per_km2", 0), ("dist_nearest_school_km", 2), ("dist_nearest_elementary_km", 2),
    ("households_with_kids_pct_2020", 1), ("median_bill_2025", 0), ("bill_change_2022_25_pct", 1), ("bill_change_2022_25_usd", 0), ("ref2026_4yr_cost_median_home", 0)]
yd_units = set(yd)
out = []
for u in sorted(w26, key=lambda x: (x not in yd_units, x)):
    w = w26[u]; n = new.get(u)
    if not n or n.get("hh", 0) < 1 or not w["ref_votes"] or int(w["ref_votes"]) == 0: continue
    p = p26.get(u, {}); c = chg.get(w["comparison_unit"], {}); r = next((x for x in rows if x["unit"] == u), {})
    dem = fl(p.get("gov_dem_2party_pct")); yes = fl(w["yes_pct"])
    v = dict(reporting_unit=u, in_19_unit_analysis="yes" if u in yd_units else "no (under 100 votes)", split_unit=p.get("split_unit"),
        comparison_unit_2022=w["comparison_unit"], ref_votes_2026=int(w["ref_votes"]), yes_pct_2026=yes, dem_gov_pct_2026=dem,
        dem_ticket_no_pct=100 * (dem - yes) / dem if dem and yes is not None else None, rolloff_pct_2026=fl(w["rolloff_pct"]),
        yes_pct_2022_comparison_unit=fl(c.get("yes_pct_2022")), yes_change_pts_comparison_unit=fl(c.get("chg_yes_pct_pts")),
        ballots_cast_change_pct_comparison_unit=100 * (float(c["ballots_cast_unit_2026"]) / float(c["ballots_cast_unit_2022"]) - 1) if fl(c.get("ballots_cast_unit_2022")) else None,
        ref_votes_change_pct_comparison_unit=100 * (float(c["ref_votes_2026"]) / float(c["ref_votes_2022"]) - 1) if fl(c.get("ref_votes_2022")) else None,
        ballots_per_2020_adult_2026=int(w["ballots_with_question"]) / n["adults"] if n.get("adults") else None,
        no_partial_veto_amend_pct=fl(p.get("sr1_no_pct")), no_worship_amend_pct=fl(p.get("sr2_no_pct")), no_antidiscrimination_amend_pct=fl(p.get("sr3_no_pct")),
        dem_minus_no_partial_veto_pts=dem - fl(p["sr1_no_pct"]) if dem else None,
        gov_minus_ag_dem_pts=dem - fl(p["ag_dem_2party_pct"]) if dem else None, gov_minus_treasurer_dem_pts=dem - fl(p["tre_dem_2party_pct"]) if dem else None,
        population_2020=n.get("pop"), adults_18plus_2020=n.get("adults"), households_2020=n.get("hh"), housing_units_2020=n.get("hu"),
        people_of_color_pct_2020=n.get("poc_pct"), asian_pct_2020=n.get("asian_pct"), hispanic_pct_2020=n.get("hisp_pct"), black_pct_2020=n.get("black_pct"),
        ba_plus_pct_acs=n.get("ba_plus_pct"), ba_plus_moe=n.get("ba_plus_moe"), median_hh_income_acs=n.get("median_hh_income"),
        poverty_pct_acs=n.get("poverty_pct"), poverty_moe=n.get("poverty_moe"),
        householders_moved_2020plus_pct_acs=n.get("moved_2020_plus_pct"), householders_moved_2020plus_moe=n.get("moved_2020_plus_moe"),
        owners_moved_2020plus_pct_acs=n.get("owner_moved_2020_plus_pct"),
        private_or_home_k12_pct_acs=n.get("private_k12_pct"), private_or_home_k12_moe=n.get("private_k12_moe"),
        built_2010plus_pct_acs=n.get("built_2010_plus_pct"), built_2010plus_moe=n.get("built_2010_plus_moe"),
        owner_cost_burden30_pct_acs=n.get("owner_cost_burden30_pct"), homes_counted_parcels=n.get("lu_homes"), homes_on_land_undeveloped_2015_pct=n.get("lu_new_pct"),
        madison_dwelling_units_built_2015plus_pct=n.get("mad_du_2015_pct"), households_per_km2=n.get("hh_per_km2"),
        dist_nearest_school_km=n.get("dist_any_km"), dist_nearest_elementary_km=n.get("dist_elem_km"),
        households_with_kids_pct_2020=r.get("hhk"), median_bill_2025=r.get("bill25"), bill_change_2022_25_pct=r.get("billpct"),
        bill_change_2022_25_usd=r.get("billusd"), ref2026_4yr_cost_median_home=r.get("ref26"))
    out.append(v)
os.makedirs(O, exist_ok=True)
with open(O + "new_variables_by_ward.csv", "w", newline="") as fh:
    wr = csv.writer(fh); wr.writerow([c for c, _ in cols])
    for v in out:
        line = []
        for c, p in cols:
            x = v.get(c)
            if x is None or (isinstance(x, float) and math.isnan(x)): line.append("")
            elif p is None: line.append(x)
            elif p == -3: line.append(int(round(x, -3)))
            elif p == 0: line.append(int(round(x)))
            else: line.append(round(x, p))
        wr.writerow(line)
print("wrote", len(out), "rows; total votes in 19 units", TOTAL)
# ---- diagnostics: overlap, multi-control partials, tract-level robustness, targeting value
for k in ("ba_tract", "priv_tract", "moved_tract"):
    for r in rows: r[k] = new.get(r["unit"], {}).get(k + "_pct")
print("\nTract-level robustness (partial r | Dem):", {k: round(partial(rows, k)[0], 2) for k in ("ba_tract", "priv_tract", "moved_tract")},
      "raw:", {k: round(wc([r[k] for r in rows], [r["yes"] for r in rows], [r["votes"] for r in rows]), 2) for k in ("ba_tract", "priv_tract", "moved_tract")})
KEY = ["dem", "ba", "inc", "ref26", "billpct", "yes22", "priv", "hisp", "asian", "bpa", "turnout_chg", "newhomes", "built10", "moved", "ownmoved", "distel", "sr1", "hhk", "apt"]
print("\nWeighted r matrix (pairwise available units):"); print(" " * 12 + "".join(f"{k[:7]:>8}" for k in KEY))
for a in KEY:
    line = f"{a[:11]:12}"
    for b in KEY:
        rr = [r for r in rows if r.get(a) is not None and r.get(b) is not None]
        line += f"{wc([r[a] for r in rr], [r[b] for r in rr], [r['votes'] for r in rr]):8.2f}"
    print(line)
print("\nPartial r with Yes holding Dem plus one more control (n = 19):")
for k in ["ba", "inc", "ref26", "yes22", "priv", "hisp", "asian", "bpa", "turnout_chg", "newhomes", "built10", "moved", "ownmoved", "hhk", "distel", "sr1"]:
    line = f"  {k:12}"
    for c in ["ba", "inc", "ref26", "bpa", "yes22"]:
        if c == k: line += f"{'':>14}"; continue
        line += f"  |dem+{c:6}{partial(rows, k, ('dem', c))[0]:+.2f}"
    print(line)
print("\nLeave-one-out range of partial r | Dem + bill growth (n = 12):")
rb = [r for r in rows if r.get("billpct") is not None]
for k in ["ba", "inc", "ref26", "yes22", "priv", "moved", "ownmoved", "newhomes", "built10", "bpa", "turnout_chg", "hisp", "asian", "distel", "hhk"]:
    loo = [partial([r for r in rb if r is not x], k, ("dem", "billpct"))[0] for x in rb]
    print(f"  {k:12} {partial(rb, k, ('dem', 'billpct'))[0]:+.2f}  [{min(loo):+.2f}, {max(loo):+.2f}]")
print("\nTargeting: Yes and margin per 1,000 voters from the top vs bottom third of units; minimum Dem-ticket No voters in each third")
for o in res:
    k = o["k"]; rr = sorted([r for r in rows if r.get(k) is not None], key=lambda r: r[k]); t = o["t"]
    fl_n = lambda g: sum(max(0.0, r["votes"] * (r["dem"] - r["yes"]) / 100) for g_ in [g] for r in g_)
    o["margin1000_top"], o["margin1000_bot"] = 1000 * (2 * o["hi3"] / 100 - 1), 1000 * (2 * o["lo3"] / 100 - 1)
    o["floor_votes_top"], o["floor_votes_bot"] = fl_n(rr[-t:]), fl_n(rr[:t])
    o["units_top"], o["units_bot"] = [r["unit"] for r in rr[-t:]], [r["unit"] for r in rr[:t]]
    print(f"  {o['label'][:44]:44} top {o['hi3']:4.1f}% ({o['margin1000_top']:+4.0f}/1k, DemNo>={o['floor_votes_top']:4.0f})  bottom {o['lo3']:4.1f}% ({o['margin1000_bot']:+4.0f}/1k, DemNo>={o['floor_votes_bot']:4.0f})  partial r with DemNo {f(o.get('partial_floor'))}")
json.dump(dict(results=res, rows=rows, comparison_rows=crow, total_votes=TOTAL), open(L + "results.json", "w"), indent=0, default=str)
