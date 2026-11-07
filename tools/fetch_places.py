"""Build data/places.json: comuni of Latina province + Roma Sud comuni + Roma Sud zones.

Sources: Wikidata (ISTAT code, coords, population, elevation, image), Nominatim for Rome zones.
Idempotent: re-running refreshes the file; cached responses live in tools/cache/.
"""

import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "tools" / "cache"
CACHE.mkdir(parents=True, exist_ok=True)
UA = "consorziologistico-site-builder/1.0 (+https://consorziologistico.it)"

ROMA_SUD_COMUNI = [
    "Pomezia", "Ardea", "Anzio", "Nettuno", "Ciampino", "Marino", "Castel Gandolfo",
    "Albano Laziale", "Ariccia", "Genzano di Roma", "Lanuvio", "Velletri", "Lariano", "Nemi",
    "Rocca di Papa", "Grottaferrata", "Frascati", "Monte Porzio Catone", "Monte Compatri",
    "Rocca Priora", "Colonna", "San Cesareo", "Zagarolo", "Gallicano nel Lazio", "Palestrina",
    "Labico", "Valmontone", "Artena", "Colleferro", "Segni", "Gavignano", "Montelanico",
    "Carpineto Romano", "Gorga", "Cave", "Genazzano", "Fiumicino",
]

# Rome zones south of the centre (quartieri / zone urbanistiche / località).
ROMA_ZONE = [
    ("EUR", "EUR, Roma"),
    ("Laurentino", "Laurentina, Roma"),
    ("Ostiense", "Ostiense, Roma"),
    ("Garbatella", "Garbatella, Roma"),
    ("Torrino", "Torrino, Roma"),
    ("Spinaceto", "Spinaceto, Roma"),
    ("Trigoria", "Trigoria, Roma"),
    ("Castel Romano", "Castel Romano, Roma"),
    ("Santa Palomba", "Santa Palomba, Roma"),
    ("Tor Vergata", "Tor Vergata, Roma"),
    ("Romanina", "Romanina, Roma"),
    ("Cinecittà", "Cinecittà, Roma"),
    ("Anagnina", "Anagnina, Roma"),
    ("Tuscolano", "Tuscolano, Roma"),
    ("Appio Latino", "Appio-Latino, Roma"),
    ("Ostia", "Ostia, Roma"),
    ("Acilia", "Acilia, Roma"),
    ("Infernetto", "Infernetto, Roma"),
    ("Casal Palocco", "Casal Palocco, Roma"),
    ("Magliana", "Magliana, Roma"),
    ("Ponte Galeria", "Ponte Galeria, Roma"),
    ("Capannelle", "Capannelle, Roma"),
    ("Morena", "Morena, Roma"),
    ("Falcognana", "Falcognana, Roma"),
    ("Cecchignola", "Cecchignola, Roma"),
    ("Vitinia", "Vitinia, Roma"),
    ("Mezzocammino", "Mezzocammino, Roma"),
    ("Castel di Leva", "Castel di Leva, Roma"),
    ("Tor Bella Monaca", "Tor Bella Monaca, Roma"),
    ("Torre Angela", "Torre Angela, Roma"),
    ("Tor Sapienza", "Tor Sapienza, Roma"),
    ("Centocelle", "Centocelle, Roma"),
]


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


def http_json(url: str, cache_key: str, data: bytes | None = None, accept="application/json"):
    path = CACHE / (re.sub(r"[^a-zA-Z0-9_.-]", "_", cache_key)[:150] + ".json")
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, "Accept": accept})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                payload = json.loads(r.read().decode("utf-8"))
            path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
            return payload
        except Exception as e:  # noqa: BLE001
            print("retry", attempt, url[:100], e)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(url)


SPARQL = """
SELECT ?item ?itemLabel ?istat ?coord ?pop ?elev ?image ?itwiki WHERE {
  ?item wdt:P31 wd:Q747074; wdt:P635 ?istat; wdt:P625 ?coord.
  FILTER(STRSTARTS(?istat, "%s"))
  FILTER NOT EXISTS { ?item wdt:P576 ?dissolved }
  OPTIONAL { ?item p:P1082 ?ps. ?ps ps:P1082 ?pop; pq:P585 ?pd. }
  OPTIONAL { ?item wdt:P2044 ?elev. }
  OPTIONAL { ?item wdt:P18 ?image. }
  OPTIONAL { ?itwiki schema:about ?item; schema:isPartOf <https://it.wikipedia.org/>. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "it". }
} ORDER BY ?itemLabel DESC(?pd)
"""


def wikidata_comuni(prefix: str):
    q = SPARQL % prefix
    url = "https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(q)
    res = http_json(url, f"wd_{prefix}")
    out = {}
    for b in res["results"]["bindings"]:
        name = b["itemLabel"]["value"]
        if name in out:
            continue  # first row = most recent population (ORDER BY DESC(?pd))
        m = re.match(r"Point\(([-\d.]+) ([-\d.]+)\)", b["coord"]["value"])
        out[name] = {
            "name": name,
            "wikidata": b["item"]["value"].rsplit("/", 1)[1],
            "istat": b["istat"]["value"],
            "lat": float(m.group(2)),
            "lon": float(m.group(1)),
            "population": int(float(b["pop"]["value"])) if "pop" in b else None,
            "elevation": round(float(b["elev"]["value"])) if "elev" in b else None,
            "image": urllib.parse.unquote(b["image"]["value"].rsplit("/", 1)[1]) if "image" in b else None,
            "itwiki": b["itwiki"]["value"] if "itwiki" in b else None,
        }
    return out


def nominatim(query: str):
    url = "https://nominatim.openstreetmap.org/search?format=jsonv2&limit=1&countrycodes=it&q=" + urllib.parse.quote(query)
    cached = (CACHE / (re.sub(r"[^a-zA-Z0-9_.-]", "_", "nom_" + query)[:150] + ".json")).exists()
    res = http_json(url, "nom_" + query)
    if not cached:
        time.sleep(1.1)
    return res[0] if res else None


def main():
    places = []
    latina = wikidata_comuni("059")
    for c in sorted(latina.values(), key=lambda x: x["name"]):
        places.append({**c, "kind": "comune", "area": "latina", "province": "LT"})

    roma = wikidata_comuni("058")
    for name in ROMA_SUD_COMUNI:
        c = roma.get(name)
        if not c:
            print("MISSING comune", name)
            continue
        places.append({**c, "kind": "comune", "area": "roma-sud", "province": "RM"})

    for name, query in ROMA_ZONE:
        hit = nominatim(query)
        if not hit:
            print("MISSING zone", name)
            continue
        places.append({
            "name": name, "kind": "zona", "area": "roma-citta", "province": "RM",
            "lat": float(hit["lat"]), "lon": float(hit["lon"]),
            "osm": f'{hit["osm_type"]}/{hit["osm_id"]}', "osm_type": hit.get("type"),
            "population": None, "elevation": None, "image": None, "itwiki": None,
        })

    # Nominatim matched a bus stop in the city / a peripheral stop for these two.
    overrides = {"Castel Romano": (41.7188, 12.4441), "Tor Vergata": (41.8536, 12.6037)}
    for p in places:
        if p["name"] in overrides and p["kind"] == "zona":
            p["lat"], p["lon"] = overrides[p["name"]]
        p["slug"] = slugify(p["name"])
    slugs = [p["slug"] for p in places]
    assert len(slugs) == len(set(slugs)), "duplicate slugs"

    out = ROOT / "data" / "places.json"
    out.write_text(json.dumps(places, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(places), "places ->", out)


if __name__ == "__main__":
    main()
