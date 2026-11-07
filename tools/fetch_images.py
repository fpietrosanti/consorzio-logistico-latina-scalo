"""Download free-licence photos from Wikimedia Commons with attribution metadata.

Places: Wikidata P18 image; if missing, the Wikidata item found through Nominatim extratags;
if still missing, the closest geotagged Commons photo (manually reviewed afterwards).
Topic images (warehouses, forklifts, ports, roads...) come from tools/topic_images.json.
Output: static/img/places/<slug>.webp, static/img/topics/<key>.webp, data/images.json
"""

import html
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "tools" / "cache"
UA = "consorziologistico-site-builder/1.0 (+https://consorziologistico.it)"
FREE = re.compile(r"^(CC0|CC BY(-SA)? [0-9.]+|CC BY(-SA)?|Public domain|PD.*|GFDL.*|Attribution.*)", re.I)
BAD_WORDS = re.compile(r"(stemma|coat of arms|logo|map|mappa|locator|flag|bandiera|svg|\.pdf|blason|wappen)", re.I)


def get_json(url, key):
    path = CACHE / (re.sub(r"[^a-zA-Z0-9_.-]", "_", key)[:150] + ".json")
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.loads(r.read().decode("utf-8"))
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            time.sleep(0.3)
            return data
        except Exception as e:  # noqa: BLE001
            print("retry", attempt, e, file=sys.stderr)
            time.sleep(4 * (attempt + 1))
    raise RuntimeError(url)


def strip_html(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def commons_info(filename):
    url = (
        "https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo"
        "&iiprop=url|extmetadata|size|mime&iiurlwidth=1600&titles=" + urllib.parse.quote("File:" + filename)
    )
    data = get_json(url, "ci_" + filename)
    page = next(iter(data["query"]["pages"].values()))
    if "imageinfo" not in page:
        return None
    ii = page["imageinfo"][0]
    md = ii.get("extmetadata", {})
    lic = strip_html(md.get("LicenseShortName", {}).get("value", ""))
    return {
        "file": filename,
        "thumb": ii.get("thumburl") or ii["url"],
        "page": ii["descriptionurl"],
        "author": strip_html(md.get("Artist", {}).get("value", ""))[:120] or "Autore sconosciuto",
        "license": lic,
        "license_url": md.get("LicenseUrl", {}).get("value", ""),
        "description": strip_html(md.get("ImageDescription", {}).get("value", ""))[:300],
        "mime": ii.get("mime"),
        "width": ii.get("width"),
        "height": ii.get("height"),
    }


def acceptable(info):
    if not info or info["mime"] not in ("image/jpeg", "image/png", "image/webp"):
        return False
    if BAD_WORDS.search(info["file"]):
        return False
    if (info["width"] or 0) < 800:
        return False
    return bool(FREE.match(info["license"]))


def wikidata_image(qid):
    data = get_json(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json", "wd_ent_" + qid)
    ent = data["entities"][qid]
    claims = ent.get("claims", {}).get("P18", [])
    return claims[0]["mainsnak"]["datavalue"]["value"] if claims else None


def nominatim_qid(name):
    url = (
        "https://nominatim.openstreetmap.org/search?format=jsonv2&limit=1&extratags=1&countrycodes=it&q="
        + urllib.parse.quote(name + ", Roma")
    )
    res = get_json(url, "nomx_" + name)
    time.sleep(1.1)
    if res and res[0].get("extratags"):
        return res[0]["extratags"].get("wikidata")
    return None


def commons_geosearch(lat, lon, radius=1500):
    url = (
        "https://commons.wikimedia.org/w/api.php?action=query&format=json&list=geosearch"
        f"&gscoord={lat}|{lon}&gsradius={radius}&gslimit=40&gsnamespace=6"
    )
    data = get_json(url, f"geo_{lat:.4f}_{lon:.4f}_{radius}")
    return [g["title"][5:] for g in data.get("query", {}).get("geosearch", [])]


def download(info, dest: Path):
    if dest.exists():
        return
    req = urllib.request.Request(info["thumb"], headers={"User-Agent": UA})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                raw = r.read()
            break
        except Exception as e:  # noqa: BLE001
            print("dl retry", attempt, e, file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    else:
        raise RuntimeError(info["thumb"])
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    im.thumbnail((1600, 1000))
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, "WEBP", quality=78, method=6)
    time.sleep(0.5)


def main():
    places = json.loads((ROOT / "data" / "places.json").read_text(encoding="utf-8"))
    images_path = ROOT / "data" / "images.json"
    images = json.loads(images_path.read_text(encoding="utf-8")) if images_path.exists() else {}
    rejected = json.loads((ROOT / "tools" / "rejected_images.json").read_text(encoding="utf-8")) \
        if (ROOT / "tools" / "rejected_images.json").exists() else []

    overrides_path = ROOT / "tools" / "place_image_overrides.json"
    overrides = json.loads(overrides_path.read_text(encoding="utf-8")) if overrides_path.exists() else {}
    for p in places:
        key = "places/" + p["slug"]
        forced = overrides.get(p["slug"])
        if key in images and (not forced or images[key]["file"] == forced):
            continue
        if forced:
            info = commons_info(forced)
            dest = ROOT / "static" / "img" / f"{key}.webp"
            if dest.exists():
                dest.unlink()
            download(info, dest)
            info["source"] = "manual"
            images[key] = info
            print("OVERRIDE", p["name"], forced)
            continue
        candidates = []
        if p.get("image"):
            candidates.append(p["image"])
        if p.get("wikidata") is None and p["kind"] == "zona":
            qid = nominatim_qid(p["name"])
            if qid:
                p["wikidata"] = qid
                img = wikidata_image(qid)
                if img:
                    candidates.append(img)
        candidates += commons_geosearch(p["lat"], p["lon"])
        chosen = None
        for c in candidates:
            if c in rejected:
                continue
            info = commons_info(c)
            if acceptable(info):
                chosen = info
                break
        if not chosen:
            print("NO IMAGE", p["name"])
            continue
        download(chosen, ROOT / "static" / "img" / f"{key}.webp")
        chosen["source"] = "wikidata" if c == p.get("image") else "geosearch"
        images[key] = chosen
        print("OK", p["name"], "|", chosen["file"], "|", chosen["license"])
        images_path.write_text(json.dumps(images, ensure_ascii=False, indent=1), encoding="utf-8")

    topics_path = ROOT / "tools" / "topic_images.json"
    if topics_path.exists():
        for key, filename in json.loads(topics_path.read_text(encoding="utf-8")).items():
            k = "topics/" + key
            if k in images and images[k]["file"] == filename:
                continue
            info = commons_info(filename)
            if not acceptable(info):
                print("TOPIC REJECTED", key, filename, info and info["license"])
                continue
            dest = ROOT / "static" / "img" / f"{k}.webp"
            if dest.exists():
                dest.unlink()
            download(info, dest)
            info["source"] = "topic"
            images[k] = info
            print("TOPIC OK", key, filename, info["license"])

    images_path.write_text(json.dumps(images, ensure_ascii=False, indent=1), encoding="utf-8")
    (ROOT / "data" / "places.json").write_text(json.dumps(places, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(images), "images")


if __name__ == "__main__":
    main()
