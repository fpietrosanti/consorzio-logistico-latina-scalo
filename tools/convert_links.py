"""Convert Italian internal Markdown links (/servizi/stoccaggio/) to language-aware Hugo refs
({{< relref "/servizi/stoccaggio" >}}) so translated pages link to their own language.

Usage: python tools/convert_links.py [--check]
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IT = ROOT / "content" / "it"
ALIASES = {
    "/settori/e-commerce/": "/settori/ecommerce/",
    "/settori/gdo/": "/settori/gdo-retail/",
    "/settori/tessile/": "/settori/tessile-moda/",
    "/servizi/3pl/": "/servizi/logistica-3pl/",
    "/servizi/movimentazione/": "/servizi/handling/",
    "/faq/": "/domande-frequenti/",
    "/contatti/": "/#contatti",
}


def url_map():
    m = {"/": "/"}
    for f in IT.rglob("*.md"):
        rel = f.relative_to(IT).as_posix()
        path = "/" + rel[:-3]
        if path.endswith("/_index"):
            path = path[: -len("/_index")] or "/"
        txt = f.read_text(encoding="utf-8")
        mu = re.search(r'^url:\s*"?([^"\n]+)"?\s*$', txt, re.M)
        url = mu.group(1).strip() if mu else (path.rstrip("/") + "/")
        m[url] = path
    return m


LINK = re.compile(r"\]\((/[^)\s]*)\)")


def main(check_only=False):
    m = url_map()
    bad = []
    for f in IT.rglob("*.md"):
        txt = f.read_text(encoding="utf-8")
        if "layout: \"place\"" in txt:
            continue

        def repl(mo):
            target = mo.group(1)
            target = ALIASES.get(target, target)
            base, _, frag = target.partition("#")
            if base == "" or base == "/":
                path = "/"
            else:
                if not base.endswith("/"):
                    base += "/"
                path = m.get(base)
            if path is None:
                bad.append((f.relative_to(ROOT).as_posix(), mo.group(1)))
                return mo.group(0)
            anchor = f"#{frag}" if frag else ""
            return f']({{{{< relref "{path}" >}}}}{anchor})'

        new = LINK.sub(repl, txt)
        if new != txt and not check_only:
            f.write_text(new, encoding="utf-8")
    for b in sorted(set(bad)):
        print("UNRESOLVED", *b)
    print("unresolved:", len(set(bad)))


if __name__ == "__main__":
    main("--check" in sys.argv)
