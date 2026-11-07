"""Add road distance, drive time and main roads from the hub to every place (OSRM, car profile).

Also adds the 5 nearest other places (straight line) for internal linking.
"""

import json
import math
import re
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "tools" / "cache"
HUB = (41.510060381449215, 12.950756550932178)
UA = "consorziologistico-site-builder/1.0 (+https://consorziologistico.it)"


def osrm(lat, lon):
    key = CACHE / f"osrm_{lat:.5f}_{lon:.5f}.json"
    if key.exists():
        return json.loads(key.read_text(encoding="utf-8"))
    url = (
        "https://router.project-osrm.org/route/v1/driving/"
        f"{HUB[1]},{HUB[0]};{lon},{lat}?overview=false&steps=true"
    )
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.loads(r.read().decode("utf-8"))
            key.write_text(json.dumps(data), encoding="utf-8")
            time.sleep(1.0)
            return data
        except Exception as e:  # noqa: BLE001
            print("retry", attempt, e)
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(url)


def norm_ref(ref: str) -> str:
    ref = ref.split(";")[0].strip().replace(" ", "")
    return ref


def haversine(a, b):
    r = 6371.0
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def main():
    path = ROOT / "data" / "places.json"
    places = json.loads(path.read_text(encoding="utf-8"))
    for p in places:
        data = osrm(p["lat"], p["lon"])
        route = data["routes"][0]
        by_ref = defaultdict(float)
        by_name = defaultdict(float)
        for leg in route["legs"]:
            for st in leg["steps"]:
                if st.get("ref"):
                    by_ref[norm_ref(st["ref"])] += st["distance"]
                elif st.get("name"):
                    by_name[st["name"]] += st["distance"]
        roads = [r for r, d in sorted(by_ref.items(), key=lambda kv: -kv[1]) if d > 1500][:4]
        named = [n for n, d in sorted(by_name.items(), key=lambda kv: -kv[1]) if d > 1500 and not re.match(r"^\d", n)][:3]
        p["road_km"] = round(route["distance"] / 1000, 1)
        p["drive_min"] = round(route["duration"] / 60)
        p["air_km"] = round(haversine(HUB, (p["lat"], p["lon"])), 1)
        p["roads"] = roads
        p["road_names"] = named
    for p in places:
        others = sorted(
            (o for o in places if o is not p),
            key=lambda o: haversine((p["lat"], p["lon"]), (o["lat"], o["lon"])),
        )
        p["nearby"] = [o["slug"] for o in others[:6]]
    path.write_text(json.dumps(places, ensure_ascii=False, indent=1), encoding="utf-8")
    for p in sorted(places, key=lambda x: x["road_km"]):
        print(f'{p["name"]:28} {p["road_km"]:6} km {p["drive_min"]:4} min  {",".join(p["roads"])}  | {",".join(p["road_names"])}')


if __name__ == "__main__":
    main()
