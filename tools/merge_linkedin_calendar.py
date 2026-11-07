"""Merge marketing/linkedin-intl/calendar.csv into marketing/linkedin-calendar.csv (idempotent).

Rows for languages that need native review (ga, mt, lv, et) get status "review" and are skipped by the scheduler
until a human changes them to "pending".
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAL = ROOT / "marketing" / "linkedin-calendar.csv"
INTL = ROOT / "marketing" / "linkedin-intl" / "calendar.csv"
REVIEW = {"ga", "mt", "lv", "et"}


def main():
    cal = list(csv.DictReader(CAL.open(encoding="utf-8")))
    ids = {r["id"] for r in cal}
    added = 0
    for r in csv.DictReader(INTL.open(encoding="utf-8")):
        rid = f"{r['lang'].upper()}-P{r['post']}"
        if rid in ids:
            continue
        cal.append({
            "id": rid, "date": r["date"], "time": r["time"], "lang": r["lang"],
            "source": f"marketing/linkedin-intl/{r['lang']}.md", "section": f"## Post {r['post']}",
            "status": "review" if r["lang"] in REVIEW else "pending", "notes": "",
        })
        added += 1
    for r in cal:
        if r["lang"] in REVIEW and r["status"] == "pending":
            r["status"] = "review"
    cal.sort(key=lambda r: (r["date"], r["time"]))
    with CAL.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "date", "time", "lang", "source", "section", "status", "notes"])
        w.writeheader()
        w.writerows(cal)
    print(f"{len(cal)} rows, {added} added")


if __name__ == "__main__":
    main()
