#!/usr/bin/env python3
"""Print the WCAG contrast matrix for one or all languages. Stdlib only.

usage: python3 tools/contrast.py [slug]
Floors: 4.5:1 body text, 3:1 large text and UI components (WCAG 2.1 AA).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import contrast  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
cat = json.loads((ROOT / "data" / "canonical" / "catalog.json").read_text())
want = sys.argv[1] if len(sys.argv) > 1 else None
PAIRS = [("text", "panel", 4.5), ("text_secondary", "panel", 4.5), ("text_muted", "panel", 3.0),
         ("accent", "panel", 3.0), ("nominal", "panel", 3.0), ("caution", "panel", 3.0),
         ("critical", "panel", 3.0), ("offline", "panel", 3.0)]
for l in cat["languages"]:
    if want and l["slug"] != want:
        continue
    print(f"\n{l['id']} {l['name']}")
    print(f"  {'pair':26} {'ratio':>6}  floor  result")
    for fg, bg, floor in PAIRS:
        r = contrast(l["tokens"][fg], l["tokens"][bg])
        flag = "PASS" if r >= floor else "FLAG"
        print(f"  {fg + ' on ' + bg:26} {r:6.2f}  {floor:>4}   {flag}")
