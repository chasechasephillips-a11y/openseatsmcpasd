"""Pull Dane County tract and block-group rows from the Census Bureau's ACS 2020-2024 5-year
table-based summary files (www2.census.gov, no key) using small HTTP range requests:
binary-search the sorted GEO_ID column, then read only the Dane County chunk.
Run order (scratchpad paths; nothing here writes to the repository except analyze.py's CSV):
  python3 -I acs_sf_fetch.py $SCRATCH/levers/dl/acs_sf b15003 b19001 b19013 c17002 b25038 b14002 b25034 b25091
  python3 -I gis_fetch.py $SCRATCH/levers/dl/gis          # blocks, madison, landuse, farmbldg, schools
  python3 build_units.py                                  # writes $SCRATCH/levers/units_new.json
  python3 analyze.py                                      # writes new_variables_by_ward.csv and $SCRATCH/levers/results.json"""
import urllib.request, time, sys, os
BASE = "https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-%s.dat"
OUT = sys.argv[1]; TABLES = sys.argv[2:]
def rng(url, a, b):
    for t in range(4):
        try:
            req = urllib.request.Request(url, headers={"Range": f"bytes={a}-{b}", "User-Agent": "research-script"})
            return urllib.request.urlopen(req, timeout=120).read().decode("latin-1")
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(5 * (t + 1))
    raise SystemExit("failed")
def size(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "research-script"})
    return int(urllib.request.urlopen(req, timeout=60).headers["Content-Length"])
def first_geo(url, pos):
    txt = rng(url, pos, pos + 6000); i = txt.find("\n")
    line = txt[i + 1:].split("\n")[0]
    return line.split("|")[0], pos + i + 1
def locate(url, n, key):   # largest offset whose next line's GEO_ID < key
    lo, hi = 0, n
    while hi - lo > 60000:
        mid = (lo + hi) // 2; g, _ = first_geo(url, mid); time.sleep(0.7)
        if g < key: lo = mid
        else: hi = mid
    return lo
for t in TABLES:
    url = BASE % t; n = size(url); header = rng(url, 0, 4000).split("\n")[0]
    rows = []
    for key in ("1400000US55025", "1500000US55025"):
        pos = locate(url, n, key); buf = ""
        while True:
            buf += rng(url, pos, pos + 199999); pos += 200000; time.sleep(0.7)
            lines = buf.split("\n")
            got = [l for l in lines[1:-1] if l.startswith(key)]
            last = lines[-2].split("|")[0] if len(lines) > 2 else ""
            if last > key + "z" or pos >= n: break
        rows += got
    with open(os.path.join(OUT, t + ".psv"), "w") as fh: fh.write(header + "\n" + "\n".join(sorted(set(rows))) + "\n")
    print(t, "bytes", n, "tracts", sum(r.startswith("1400000") for r in set(rows)), "bgs", sum(r.startswith("1500000") for r in set(rows)))
    time.sleep(2)
