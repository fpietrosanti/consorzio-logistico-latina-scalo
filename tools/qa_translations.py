"""Quality checks for translated content against the Italian source.

Checks per file: front matter parses, same relref targets, same fixed keys, url prefix, description length,
FAQ count, forbidden words. Also validates i18n TOML keys/placeholders and profiles JSON.
Usage: python tools/qa_translations.py [lang ...]
"""

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IT = ROOT / "content" / "it"
FIXED = ("layout", "weight", "image", "date", "area", "subarea", "place")
REF = re.compile(r'relref "([^"]+)"')
PH = re.compile(r"\{\{\s*\.\w+\s*\}\}")


def front(text):
    m = re.match(r"^---\n(.*?)\n---\n", text.replace("\r\n", "\n"), re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).split("\n"):
        mm = re.match(r"^(\w+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"')
    fm["_faq"] = len(re.findall(r"^\s*-\s*q:", m.group(1), re.M))
    return fm, text[m.end():]


def main(langs):
    cfg = json.loads((ROOT / "tools" / "langs.json").read_text(encoding="utf-8"))
    langs = langs or [k for k in cfg if k != "it"]
    it_i18n = tomllib.loads((ROOT / "i18n" / "it.toml").read_text(encoding="utf-8"))
    problems = 0
    for lang in langs:
        issues = []
        p = ROOT / "i18n" / f"{lang}.toml"
        if p.exists():
            try:
                t = tomllib.loads(p.read_text(encoding="utf-8"))
                for k, v in it_i18n.items():
                    if k not in t:
                        issues.append(f"i18n missing key {k}")
                    elif sorted(PH.findall(str(v)).__iter__()) != sorted(PH.findall(str(t[k]))):
                        issues.append(f"i18n placeholder mismatch {k}")
            except Exception as e:  # noqa: BLE001
                issues.append(f"i18n TOML error {e}")
        pp = ROOT / "data" / "profiles" / f"{lang}.json"
        if pp.exists():
            try:
                d = json.loads(pp.read_text(encoding="utf-8"))
                if len(d) != 102:
                    issues.append(f"profiles {len(d)}/102")
            except Exception as e:  # noqa: BLE001
                issues.append(f"profiles JSON error {e}")
        for src in IT.rglob("*.md"):
            rel = src.relative_to(IT).as_posix()
            stext = src.read_text(encoding="utf-8")
            if 'layout: "place"' in stext or rel == "crediti.md":
                continue
            dst = ROOT / "content" / lang / rel
            if not dst.exists():
                continue
            dtext = dst.read_text(encoding="utf-8")
            sfm, sbody = front(stext)
            dfm, dbody = front(dtext)
            if dfm is None:
                issues.append(f"{rel}: no front matter")
                continue
            for k in FIXED:
                if sfm.get(k) != dfm.get(k):
                    issues.append(f"{rel}: {k} {sfm.get(k)!r} != {dfm.get(k)!r}")
            if sorted(REF.findall(sbody)) != sorted(REF.findall(dbody)):
                issues.append(f"{rel}: relref mismatch")
            if sfm["_faq"] != dfm["_faq"]:
                issues.append(f"{rel}: faq {dfm['_faq']}/{sfm['_faq']}")
            url = dfm.get("url", "")
            if rel != "_index.md" and not url.startswith(f"/{lang}/"):
                issues.append(f"{rel}: url {url!r}")
            if len(dfm.get("description", "")) > 170:
                issues.append(f"{rel}: description {len(dfm['description'])} chars")
            if re.search(r"transitalia", dtext, re.I):
                issues.append(f"{rel}: FORBIDDEN Transitalia")
        problems += len(issues)
        print(f"{lang}: {'OK' if not issues else str(len(issues)) + ' issues'}")
        for i in issues[:15]:
            print("   ", i)
    print("total issues:", problems)


if __name__ == "__main__":
    main(sys.argv[1:])
