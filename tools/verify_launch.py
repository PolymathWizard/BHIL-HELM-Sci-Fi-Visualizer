#!/usr/bin/env python3
"""Verify every GitHub description option in launch/github-description.md is <= 350 chars. Stdlib only."""
import re
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
txt = (ROOT / "launch" / "github-description.md").read_text()
blocks = re.findall(r"## Option ([A-C])[^\n]*\n\n(.+?)\n\nRationale", txt, re.S)
bad = 0
for letter, desc in blocks:
    n = len(desc.strip())
    ok = n <= 350
    bad += not ok
    print(f"Option {letter}: {n} chars {'OK' if ok else 'OVER'}")
sys.exit(1 if bad or len(blocks) != 3 else 0)
