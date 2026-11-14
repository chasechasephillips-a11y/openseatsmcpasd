"""Fetch the public GIS inputs for the new-variable tests (writes to the scratchpad only):
2020 Census block race and adult counts (Esri Living Atlas), City of Madison parcel year built /
owner-change year / attendance schools (no names or addresses kept), Dane County 2015 land use
polygons that were undeveloped, and NCES public school locations for MCPASD (LEAID 5509510)."""
import json, urllib.request, urllib.parse, time, sys, os
OUT = sys.argv[1]
def q(url, params, page=2000, post=False):
    out = []; off = 0
    while True:
        p = dict(params, f="json", resultOffset=off, resultRecordCount=page)
        for t in range(5):
            try:
                if post:
                    d = json.load(urllib.request.urlopen(urllib.request.Request(url + "/query", data=urllib.parse.urlencode(p).encode()), timeout=240))
                else:
                    d = json.load(urllib.request.urlopen(url + "/query?" + urllib.parse.urlencode(p), timeout=240))
                break
            except Exception as e:
                print("retry", e, file=sys.stderr); time.sleep(5 * (t + 1))
        if "error" in d: print(d); raise SystemExit
        fs = d.get("features", []); out += fs; off += len(fs)
        time.sleep(1.5)
        if len(fs) < page and not d.get("exceededTransferLimit"): break
        if not fs: break
    return out
env = json.dumps({"xmin": -89.68, "ymin": 43.02, "xmax": -89.40, "ymax": 43.20, "spatialReference": {"wkid": 4326}})
geo = {"geometry": env, "geometryType": "esriGeometryEnvelope", "inSR": 4326, "spatialRel": "esriSpatialRelIntersects"}
what = sys.argv[2:] or ["blocks", "madison", "landuse", "farmbldg", "schools"]
if "blocks" in what:
    B = "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Census_2020_Redistricting_Blocks/FeatureServer/0"
    f = "GEOID,P0010001,P0020002,P0020005,P0020006,P0020008,P0030001,H0010001,H0010002,ALAND"
    bl = q(B, dict(geo, where="GEOID LIKE '55025%'", outFields=f, returnGeometry="false"))
    json.dump([x["attributes"] for x in bl], open(os.path.join(OUT, "blocks_race.json"), "w")); print("blocks", len(bl))
if "madison" in what:
    M = "https://maps.cityofmadison.com/arcgis/rest/services/Public/OPEN_DATA2/FeatureServer/0"
    f = "Parcel,PropertyClass,PropertyUse,YearBuilt,MaxConstructionYear,TotalDwellingUnits,Ward,ElementarySchool,MiddleSchool,HighSchool,OwnerOccupied,OwnerChangeDate,XCoord,YCoord"
    m = q(M, dict(where="TaxSchoolDist='3549'", outFields=f, returnGeometry="false"), page=1000)
    json.dump([x["attributes"] for x in m], open(os.path.join(OUT, "madison_yearbuilt.json"), "w")); print("madison parcels", len(m))
if "landuse" in what:
    L = "https://dcimapapps.countyofdane.com/arcgissrv/rest/services/Landuse/MapServer/14"
    lu = q(L, dict(geo, where="(DEVELOPED='N' AND GENERALIZED_LANDUSE<>'Water') OR GENERALIZED_LANDUSE='Under Construction'",
                   outFields="GENERALIZED_LANDUSE,DEVELOPED", returnGeometry="true", outSR=4326, geometryPrecision=6, maxAllowableOffset=0.00002), page=1000)
    json.dump(lu, open(os.path.join(OUT, "landuse2015_undeveloped.json"), "w")); print("landuse polys", len(lu))
if "farmbldg" in what:   # 2015 farm residences and farm buildings (coded undeveloped, but they are existing homes/structures)
    L = "https://dcimapapps.countyofdane.com/arcgissrv/rest/services/Landuse/MapServer/14"
    fb = q(L, dict(geo, where="LUCODE LIKE '811%'", outFields="LUCODE", returnGeometry="true", outSR=4326, geometryPrecision=6, maxAllowableOffset=0.00002), page=1000)
    json.dump(fb, open(os.path.join(OUT, "landuse2015_farmbldg.json"), "w")); print("farm building polys", len(fb))
if "schools" in what:
    S = "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_2324/MapServer/0"
    s = q(S, dict(where="LEAID='5509510'", outFields="NCESSCH,NAME,STREET,CITY,LAT,LON,SCHOOLYEAR", returnGeometry="false"))
    json.dump([x["attributes"] for x in s], open(os.path.join(OUT, "schools_nces.json"), "w")); print("schools", len(s))
