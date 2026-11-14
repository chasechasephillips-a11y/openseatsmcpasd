"""Build new neighborhood variables for each 2026 MCPASD reporting unit (MCPASD part only).
Inputs (read only): existing scratchpad files (renters/blocks.json geometry, acs/schooldists.json,
parcels/wards.json, parcels/parcels_units.csv) plus the new downloads in levers/dl/.
Method: every 2020 Census block whose representative point is inside MCPASD is placed in its
2026 ward/reporting unit (as hhkids.py does). Block counts (race, adults, kids, households,
land area) sum exactly. ACS 2020-24 block-group rates are applied to each block's population,
adults, kids, households or housing units (block groups nest blocks), then summed to units.
Output: levers/units_new.json (unit-level aggregates only)."""
import json, csv, math, collections, os, datetime
from shapely.geometry import Polygon, Point
from shapely.strtree import STRtree
from shapely.ops import unary_union
from shapely.validation import make_valid
S = os.environ.get("SCRATCH", "/tmp/claude-0/-home-user-openseatsmcpasd/32ddd594-28a3-57de-8c13-227f23b7fc20/scratchpad/")
L = S + "levers/"
R = "/home/user/openseatsmcpasd/research_notes/MCPASD referendum 2026 vs 2022/"
def geom(g):
    u = None
    for r in g["rings"]:
        if len(r) < 4: continue
        p = make_valid(Polygon(r)); u = p if u is None else u.symmetric_difference(p)
    return make_valid(u)
src = open(R + "property_tax_scripts/assign.py").read(); ns = {}
exec(src[src.index("def unit("):src.index("wg=[]; wu=[]")], ns); unit = ns["unit"]
W = json.load(open(S + "parcels/wards.json")); wg = []; wu = []
for f in W:
    try: g = geom(f["geometry"])
    except Exception: continue
    wg.append(g); wu.append(unit(f["attributes"]["NAME"], f["attributes"]["WardNumber"]))
wt = STRtree(wg)
def unit_of(pt):
    hits = [i for i in wt.query(pt) if wg[i].contains(pt)]
    return wu[hits[0]] if hits else None
mc = unary_union([geom(x["geometry"]) for x in json.load(open(S + "acs/schooldists.json")) if x["attributes"]["SchoolID"] == "3549"])
# ---- ACS 2020-24 block-group tables from the Census summary files
def sf(t):
    rows = {}
    with open(L + f"dl/acs_sf/{t}.psv") as fh:
        rd = csv.DictReader(fh, delimiter="|")
        for r in rd:
            g = r["GEO_ID"]
            if g.startswith("1500000US"): rows[g[9:]] = {k: (float(v) if v not in ("", None, "null") else None) for k, v in r.items() if k != "GEO_ID"}
    return rows
def sf_tract(t):
    rows = {}
    with open(L + f"dl/acs_sf/{t}.psv") as fh:
        for r in csv.DictReader(fh, delimiter="|"):
            if r["GEO_ID"].startswith("1400000US"): rows[r["GEO_ID"][9:]] = {k: (float(v) if v not in ("", None, "null") else 0.0) for k, v in r.items() if k != "GEO_ID"}
    return rows
TT = {t: sf_tract(t) for t in ("b15003", "b14002", "b25038", "b19013")}
def tract_rate(t, tr, num, den):
    r = TT[t].get(tr)
    if not r: return None
    d = sum(r[t.upper() + "_E%03d" % c] for c in den); n = sum(r[t.upper() + "_E%03d" % c] for c in num)
    return n / d if d else None
T = {t: sf(t) for t in ("b15003", "b19001", "b19013", "c17002", "b25038", "b14002", "b25034", "b25091")}
def E(t, bg, *cols, m=False):
    r = T[t].get(bg)
    if r is None: return None
    pre = t.upper() + ("_M" if m else "_E")
    return [r.get(pre + "%03d" % c) or 0.0 for c in cols]
# ACS numerators and denominators by block group: (table, numerator cols, denominator col, block weight)
ACSV = {
    "ba_plus": ("b15003", [22, 23, 24, 25], 1, "adults"),
    "poverty": ("c17002", [2, 3], 1, "pop"),
    "moved_2020_plus": ("b25038", [3, 4, 10, 11], 1, "hh"),
    "owner_moved_2020_plus": ("b25038", [3, 4], 2, "hh"),
    "private_k12": ("b14002", [9, 12, 15, 18, 33, 36, 39, 42], None, "kids"),
    "built_2010_plus": ("b25034", [2, 3], 1, "hu"),
    "built_2020_plus": ("b25034", [2], 1, "hu"),
    "owner_cost_burden30": ("b25091", [8, 9, 10, 11, 19, 20, 21, 22], None, "hh"),
}
K12_ALL = [7, 10, 13, 16, 31, 34, 37, 40]
OWN_ALL = [3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22]   # owners with costs computed
INC_BINS = [(0, 10), (10, 15), (15, 20), (20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 50), (50, 60), (60, 75), (75, 100), (100, 125), (125, 150), (150, 200), (200, 250)]
# ---- 2020 Census block counts
race = {b["GEOID"]: b for b in json.load(open(L + "dl/gis/blocks_race.json"))}
schools = json.load(open(L + "dl/gis/schools_nces.json"))
sites = {}
for s in schools: sites.setdefault((round(s["LAT"], 4), round(s["LON"], 4)), []).append(s["NAME"])
elem = [(s["LAT"], s["LON"]) for s in schools if "Elementary" in s["NAME"]]
allsites = [(la, lo) for la, lo in sites]
def km(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1]); dp = p2 - p1
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))
U = collections.defaultdict(lambda: collections.defaultdict(float))
bgw = collections.defaultdict(lambda: collections.defaultdict(float))   # block-group totals of block weights (for MOE shares)
blk_unit = {}
for b in json.load(open(S + "renters/blocks.json")):
    a = b["attributes"]; gid = a["GEOID"]
    try: g = geom(b["geometry"])
    except Exception: continue
    x = race.get(gid)
    if x is None: continue
    w = dict(pop=x["P0010001"] or 0, adults=x["P0030001"] or 0, hh=x["H0010002"] or 0, hu=x["H0010001"] or 0)
    w["kids"] = w["pop"] - w["adults"]
    for k, v in w.items(): bgw[gid[:12]][k] += v
    pt = g.representative_point()
    if not mc.contains(pt): continue
    u = unit_of(pt)
    if not u: continue
    blk_unit[gid] = u; d = U[u]; bg = gid[:12]
    for k, v in w.items(): d[k] += v
    d["nhwhite"] += x["P0020005"] or 0; d["hisp"] += x["P0020002"] or 0; d["black"] += x["P0020006"] or 0; d["asian"] += x["P0020008"] or 0
    d["aland"] += x["ALAND"] or 0
    if w["pop"]:
        c = (pt.y, pt.x)
        d["dist_any_x_pop"] += w["pop"] * min(km(c, s) for s in allsites)
        d["dist_elem_x_pop"] += w["pop"] * min(km(c, s) for s in elem)
        d["dist_mhs_x_pop"] += w["pop"] * km(c, (43.100366, -89.507643))
    for k, (t, num, den, wk) in ACSV.items():
        if den is None:
            denv = sum(E(t, bg, *(K12_ALL if t == "b14002" else OWN_ALL)) or [0])
        else:
            denv = (E(t, bg, den) or [0])[0]
        numv = sum(E(t, bg, *num) or [0])
        if denv > 0:
            d[k + "_num"] += w[wk] * numv / denv; d[k + "_den"] += w[wk]
    for k, t, num, den, wk in (("ba_tract", "b15003", [22, 23, 24, 25], [1], "adults"), ("priv_tract", "b14002", [9, 12, 15, 18, 33, 36, 39, 42], K12_ALL, "kids"),
                               ("moved_tract", "b25038", [3, 4, 10, 11], [1], "hh")):
        rt = tract_rate(t, gid[:11], num, den)
        if rt is not None: d[k + "_num"] += w[wk] * rt; d[k + "_den"] += w[wk]
    # income distribution: households in each bin
    inc = E("b19001", bg, *range(2, 18)); tot = (E("b19001", bg, 1) or [0])[0]
    if inc and tot > 0:
        for i, v in enumerate(inc): d["inc_bin_%02d" % i] += w["hh"] * v / tot
        d["inc_hh"] += w["hh"]
    med = E("b19013", bg, 1)
    if med and med[0] and med[0] > 0: d["med_bg_x_hh"] += w["hh"] * med[0]; d["med_bg_hh"] += w["hh"]
# approximate MOEs for apportioned shares: unit share of each block group = unit weight / all-block weight in that BG
moe = collections.defaultdict(lambda: collections.defaultdict(float))
ubg = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(float)))
for gid, u in blk_unit.items():
    x = race[gid]; w = dict(pop=x["P0010001"] or 0, adults=x["P0030001"] or 0, hh=x["H0010002"] or 0, hu=x["H0010001"] or 0); w["kids"] = w["pop"] - w["adults"]
    for k, v in w.items(): ubg[u][gid[:12]][k] += v
for u, bgs in ubg.items():
    for k, (t, num, den, wk) in ACSV.items():
        N = Dn = mn2 = md2 = 0.0
        for bg, ww in bgs.items():
            if not bgw[bg][wk]: continue
            f = ww[wk] / bgw[bg][wk]
            dcols = (K12_ALL if t == "b14002" else OWN_ALL) if den is None else [den]
            ne, nm = E(t, bg, *num), E(t, bg, *num, m=True); de, dm = E(t, bg, *dcols), E(t, bg, *dcols, m=True)
            if ne is None: continue
            N += f * sum(ne); Dn += f * sum(de); mn2 += f * f * sum(v * v for v in nm); md2 += f * f * sum(v * v for v in dm)
        if Dn > 0:
            p = N / Dn; inside = mn2 - p * p * md2
            moe[u][k] = 100 * math.sqrt(inside if inside > 0 else mn2 + p * p * md2) / Dn
# ---- Madison: dwelling units by year built (City assessor)
mad = json.load(open(L + "dl/gis/madison_yearbuilt.json"))
for x in mad:
    if not x["Ward"]: continue
    res = x["PropertyClass"] == "Residential" or x["PropertyUse"] == "Apartments"
    du = x["TotalDwellingUnits"] or 0
    if not res or du <= 0 or not x["YearBuilt"]: continue
    u = "C Madison Wd %03d" % int(x["Ward"])
    U[u]["mad_du"] += du; U[u]["mad_du_2015"] += du if x["YearBuilt"] >= 2015 else 0
    if x["PropertyUse"] in ("Single family", "Condominium", "2 Unit", "Condominium-Notation"):
        U[u]["mad_home"] += 1; U[u]["mad_home_2015"] += 1 if x["YearBuilt"] >= 2015 else 0
# ---- Everywhere: homes on parcels that were entirely undeveloped in Dane County's 2015 land use inventory
# A home parcel counts as "new since 2015" when at least 90% of its area was undeveloped land in 2015
# (farm fields, woods, open land, vacant subdivided lots) or under construction, the parcel is under 5 acres,
# and the 2015 undeveloped area excludes farm
# residences and farm buildings (LUCODE 811x), which are existing structures. Validated against Madison year built.
lu = json.load(open(L + "dl/gis/landuse2015_undeveloped.json")); fb = json.load(open(L + "dl/gis/landuse2015_farmbldg.json"))
def polys(fs):
    out = []
    for f in fs:
        try: out.append(geom(f["geometry"]))
        except Exception: pass
    return out
lg = polys(lu); lt = STRtree(lg); fg = polys(fb); ft = STRtree(fg)
madyb = {x["Parcel"]: x for x in mad}
PG = {}
for f in json.load(open(S + "parcels/parcels.json")):
    if f.get("geometry") and f["attributes"]["PARCELNO"] not in PG: PG[f["attributes"]["PARCELNO"]] = f["geometry"]
def undeveloped_share(pg):
    a = pg.area
    if a <= 0: return 0.0
    und = sum(pg.intersection(lg[i]).area for i in lt.query(pg))
    farm = sum(pg.intersection(fg[i]).area for i in ft.query(pg))
    return max(0.0, min(1.0, (und - farm) / a))
val = collections.Counter()
with open(S + "parcels/parcels_units.csv") as fh:
    for r in csv.DictReader(fh):
        u = r["unit"]; imp = float(r["imp"] or 0); tot = imp + float(r["land"] or 0)
        if not u or u == "None": continue
        pt = Point(float(r["lon"]), float(r["lat"]))
        if not mc.contains(pt): continue
        mx = madyb.get(r["parcel"])
        if u.startswith("C Madison"):
            if not (mx and mx["PropertyClass"] == "Residential" and (mx["YearBuilt"] or 0) > 0): continue
        elif not (imp >= 60000 and tot < 2_500_000): continue
        try: pg = geom(PG[r["parcel"]])
        except Exception: continue
        acres = pg.area * 111_000 * 81_200 / 4046.86   # degrees to m2 at about 43.1 N
        new = acres < 5 and undeveloped_share(pg) >= 0.9   # parcels of 5+ acres are farms or rural lots whose 2015 house was not mapped separately
        if mx and mx["PropertyClass"] == "Residential" and (mx["YearBuilt"] or 0) > 0:   # validation in Madison
            val[("flag_new" if new else "flag_old", "built2015+" if mx["YearBuilt"] >= 2015 else "built<2015")] += 1
        U[u]["lu_homes"] += 1; U[u]["lu_new"] += 1 if new else 0
print("Madison validation:", dict(val))
out = {}
for u, d in U.items():
    o = dict(d)
    pop, hh = d.get("pop", 0), d.get("hh", 0)
    o["nhwhite_pct"] = 100 * d["nhwhite"] / pop if pop else None
    o["poc_pct"] = 100 - o["nhwhite_pct"] if pop else None
    o["hisp_pct"] = 100 * d["hisp"] / pop if pop else None
    o["asian_pct"] = 100 * d["asian"] / pop if pop else None
    o["black_pct"] = 100 * d["black"] / pop if pop else None
    o["hh_per_km2"] = hh / (d["aland"] / 1e6) if d.get("aland") else None
    o["dist_any_km"] = d["dist_any_x_pop"] / pop if pop else None
    o["dist_elem_km"] = d["dist_elem_x_pop"] / pop if pop else None
    o["dist_mhs_km"] = d["dist_mhs_x_pop"] / pop if pop else None
    for k in ACSV:
        o[k + "_pct"] = 100 * d[k + "_num"] / d[k + "_den"] if d.get(k + "_den") else None
        o[k + "_moe"] = moe[u].get(k)
    if d.get("inc_hh"):
        bins = [d["inc_bin_%02d" % i] for i in range(16)]; half = sum(bins) / 2; c = 0
        for (lo, hi), v in zip(INC_BINS, bins):
            if c + v >= half:
                o["median_hh_income"] = 1000 * (lo + (hi - lo) * (half - c) / v); break   # linear interpolation within the bin
            c += v
        o["income_100k_plus_pct"] = 100 * sum(bins[12:]) / sum(bins)
        o["income_under50k_pct"] = 100 * sum(bins[:9]) / sum(bins)
    o["median_hh_income_bgavg"] = d["med_bg_x_hh"] / d["med_bg_hh"] if d.get("med_bg_hh") else None
    for k in ("ba_tract", "priv_tract", "moved_tract"):
        o[k + "_pct"] = 100 * d[k + "_num"] / d[k + "_den"] if d.get(k + "_den") else None
    o["mad_du_2015_pct"] = 100 * d["mad_du_2015"] / d["mad_du"] if d.get("mad_du") else None
    o["mad_home_2015_pct"] = 100 * d["mad_home_2015"] / d["mad_home"] if d.get("mad_home") else None
    o["lu_new_pct"] = 100 * d["lu_new"] / d["lu_homes"] if d.get("lu_homes") else None
    out[u] = o
json.dump(out, open(L + "units_new.json", "w"), indent=0)
for u, o in sorted(out.items(), key=lambda kv: -kv[1].get("hh", 0)):
    if o.get("hh", 0) < 50: continue
    print(f"{u:31} hh {o['hh']:5.0f} BA+ {o['ba_plus_pct'] or 0:4.1f}±{o['ba_plus_moe'] or 0:4.1f} inc {o.get('median_hh_income',0)/1000:5.0f}k pov {o['poverty_pct'] or 0:4.1f} mv20+ {o['moved_2020_plus_pct'] or 0:4.1f} priv {o['private_k12_pct'] or 0:4.1f}±{o['private_k12_moe'] or 0:4.1f} b10+ {o['built_2010_plus_pct'] or 0:4.1f} lu15+ {o['lu_new_pct'] or 0:4.1f} madDU15 {o['mad_du_2015_pct'] or 0:4.1f} poc {o['poc_pct']:4.1f} dens {o['hh_per_km2']:6.0f} dist {o['dist_any_km']:4.1f}/{o['dist_elem_km']:4.1f} burden {o['owner_cost_burden30_pct'] or 0:4.1f}")
