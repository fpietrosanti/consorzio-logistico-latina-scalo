"""Generate per-language stub pages for every place (content/<lang>/logistica/<slug>.md)
and the photo-credits page (content/<lang>/crediti.md).

Title/description come from the i18n/<lang>.toml templates, so a language is generated only
once its i18n file exists. Re-running is idempotent (files are rewritten).
"""

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def fmt_num(x, lang):
    s = f"{x:.1f}"
    if lang in ("en", "zh", "ga", "mt"):
        return s
    return s.replace(".", ",")


def render(tpl: str, v: dict) -> str:
    return re.sub(r"\{\{\s*\.(\w+)\s*\}\}", lambda m: str(v.get(m.group(1), "")), tpl)


def yq(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def main(langs):
    places = json.loads((ROOT / "data" / "places.json").read_text(encoding="utf-8"))
    cfg = json.loads((ROOT / "tools" / "langs.json").read_text(encoding="utf-8"))
    for lang in langs:
        i18n_path = ROOT / "i18n" / f"{lang}.toml"
        if not i18n_path.exists():
            print("skip", lang, "(no i18n)")
            continue
        t = tomllib.loads(i18n_path.read_text(encoding="utf-8"))
        sec = cfg[lang]["sec"]
        prefix = "" if lang == "it" else f"/{lang}"
        outdir = ROOT / "content" / lang / "logistica"
        outdir.mkdir(parents=True, exist_ok=True)
        for p in places:
            v = {"Name": p["name"], "Prov": p["province"], "Km": fmt_num(p["road_km"], lang), "Min": p["drive_min"]}
            title = render(t["place_title_comune" if p["kind"] == "comune" else "place_title_zona"], v)
            desc = render(t["place_description_island" if p["island"] else "place_description"], v)
            body = (
                "---\n"
                f"title: {yq(title)}\n"
                f"linkTitle: {yq(p['name'])}\n"
                f"description: {yq(desc)}\n"
                f"url: {yq(f'{prefix}/{sec['logistica']}/{p['slug']}/')}\n"
                "layout: \"place\"\n"
                f"place: {yq(p['slug'])}\n"
                f"image: {yq('places/' + p['slug'])}\n"
                f"weight: {int(p['road_km'] * 10)}\n"
                "---\n"
            )
            (outdir / f"{p['slug']}.md").write_text(body, encoding="utf-8")
        credits = (
            "---\n"
            f"title: {yq(t['credits_page_title'])}\n"
            f"url: {yq(f'{prefix}/' + ('crediti' if lang == 'it' else 'credits') + '/')}\n"
            "layout: \"credits\"\n"
            "sitemap:\n  disable: true\n"
            "---\n"
        )
        (ROOT / "content" / lang / "crediti.md").write_text(credits, encoding="utf-8")
        print(lang, len(places), "place stubs")


if __name__ == "__main__":
    main(sys.argv[1:] or ["it"])
