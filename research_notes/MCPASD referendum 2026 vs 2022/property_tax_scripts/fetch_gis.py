import json, urllib.request, urllib.parse, time, sys
B="https://dcimapapps.countyofdane.com/arcgissrv/rest/services"
def q(layer, params):
    out=[]; off=0
    while True:
        p=dict(params, f="json", resultOffset=off, resultRecordCount=2000)
        url=f"{B}/{layer}/query?"+urllib.parse.urlencode(p)
        for t in range(4):
            try:
                d=json.load(urllib.request.urlopen(url, timeout=120)); break
            except Exception as e:
                print("retry",e,file=sys.stderr); time.sleep(3*(t+1))
        if 'error' in d: print(d); sys.exit(1)
        fs=d.get('features',[]); out+=fs; off+=len(fs)
        if not d.get('exceededTransferLimit') and len(fs)<2000: break
    return out
munis=["City of Middleton","Town of Middleton","Village of Cross Plains","Town of Berry","Town of Cross Plains","Town of Springfield","Town of Westport","City of Madison"]
w = q("DaneCountyBase/MapServer/18", {"where":"NAME IN (%s)"%",".join("'%s'"%m for m in munis), "outFields":"NAME,WardNumber,WardID", "outSR":4326, "returnGeometry":"true"})
json.dump(w, open("wards.json","w")); print("wards",len(w))
p = q("TaxParcels/MapServer/0", {"where":"SchoolDistrict='MID-CR PLAINS SCHOOL DIST'", "outFields":"PARCELNO,Municipality,Sum_LandValue,Sum_ImprovementValue,PropertyAddress", "outSR":4326, "returnGeometry":"true", "maxAllowableOffset":0.0002, "geometryPrecision":6})
json.dump(p, open("parcels.json","w")); print("parcel rows",len(p), "distinct", len({f['attributes']['PARCELNO'] for f in p}))
