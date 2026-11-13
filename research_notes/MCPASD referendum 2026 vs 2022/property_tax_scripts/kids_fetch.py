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
bl=q(B, {"where":"GEOID LIKE '55025%'","geometry":env,"geometryType":"esriGeometryEnvelope","inSR":4326,"spatialRel":"esriSpatialRelIntersects","outFields":"GEOID,P0010001,P0030001","returnGeometry":"false"})
json.dump({b['attributes']['GEOID']:b['attributes'] for b in bl}, open("blocks_age.json","w")); print("blocks",len(bl))
G="https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_Census_2020_DHC_Age_and_Sex/FeatureServer/4"
f="GEOID,H0030002,P012_calc_numLT18,P012_calc_numGE65,P0120004,P0120005,P0120006,P0120028,P0120029,P0120030,P0130001,P0150002,P0150001"
bg=q(G, {"where":"GEOID LIKE '55025%'","outFields":f,"returnGeometry":"false"})
json.dump({b['attributes']['GEOID']:b['attributes'] for b in bg}, open("bg_age.json","w")); print("bgs",len(bg))
