"""Report which Italian source files still lack a translation, per language and group.

Usage: python tools/translation_status.py [lang ...]
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IT = ROOT / "content" / "it"


def group_of(rel: str) -> str:
    if rel.startswith("approfondimenti/"):
        return "articoli"
    if rel.startswith("settori/") or rel.startswith("logistica/"):
        return "settori-hub"
    return "nucleo"


def sources():
    out = []
    for f in sorted(IT.rglob("*.md")):
        rel = f.relative_to(IT).as_posix()
        txt = f.read_text(encoding="utf-8")
        if 'layout: "place"' in txt or rel == "crediti.md":
            continue
        out.append(rel)
    return out


def main(langs):
    cfg = json.loads((ROOT / "tools" / "langs.json").read_text(encoding="utf-8"))
    langs = langs or [k for k in cfg if k != "it"]
    src = sources()
    total_missing = 0
    for lang in langs:
        missing = {"nucleo": [], "settori-hub": [], "articoli": []}
        for rel in src:
            if not (ROOT / "content" / lang / rel).exists():
                missing[group_of(rel)].append(rel)
        if not (ROOT / "i18n" / f"{lang}.toml").exists():
            missing["nucleo"].append("i18n")
        if not (ROOT / "data" / "profiles" / f"{lang}.json").exists():
            missing["nucleo"].append("profiles")
        n = sum(len(v) for v in missing.values())
        total_missing += n
        print(f"{lang}: {'OK' if n == 0 else n} " + " ".join(f"{g}={len(v)}" for g, v in missing.items() if v))
    print("sources:", len(src), "missing total:", total_missing)


if __name__ == "__main__":
    main(sys.argv[1:])
