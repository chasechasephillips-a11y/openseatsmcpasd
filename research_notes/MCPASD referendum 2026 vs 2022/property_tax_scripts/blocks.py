import json, urllib.request, urllib.parse, time, sys
def q(url, params):
    out=[]; off=0
    while True:
        p=dict(params, f="json", resultOffset=off, resultRecordCount=2000)
        for t in range(5):
            try: d=json.load(urllib.request.urlopen(url+"/query?"+urllib.parse.urlencode(p), timeout=180)); break
            except Exception as e: print("retry",e,file=sys.stderr); time.sleep(4*(t+1))
        if 'error' in d: print(d); raise SystemExit
        fs=d.get('features',[]); out+=fs; off+=len(fs)
        if len(fs)<2000 and not d.get('exceededTransferLimit'): break
    return out
env=json.dumps({"xmin":-89.68,"ymin":43.02,"xmax":-89.40,"ymax":43.20,"spatialReference":{"wkid":4326}})
B="https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Census_2020_Redistricting_Blocks/FeatureServer/0"
bl=q(B, {"where":"GEOID LIKE '55025%'","geometry":env,"geometryType":"esriGeometryEnvelope","inSR":4326,"spatialRel":"esriSpatialRelIntersects","outFields":"GEOID,P0010001,H0010001,H0010002,H0010003","outSR":4326,"returnGeometry":"true","geometryPrecision":6})
json.dump(bl, open("blocks.json","w")); print("blocks",len(bl))
G="https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Census_2020_DHC_Housing_Units/FeatureServer/4"
bg=q(G, {"where":"GEOID LIKE '55025%'","outFields":"GEOID,H0010001,H0030002,H0040004,H004_calc_numOwn","returnGeometry":"false"})
json.dump(bg, open("bgs.json","w")); print("block groups",len(bg))
