#!/usr/bin/env python3
"""Fail if any derived prose contains an em dash (BHIL house rule). Stdlib only.
Scans README, docs/, prompts/, launch/, CLAUDE.md, .claude/, examples/, templates/."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGETS = ["README.md", "CLAUDE.md", "CONTRIBUTING.md", "CHANGELOG.md", "docs", "prompts", "launch", ".claude", "examples", "templates"]
hits = []
for t in TARGETS:
    p = ROOT / t
    files = [p] if p.is_file() else list(p.rglob("*")) if p.exists() else []
    for f in files:
        if f.is_file() and f.suffix in {".md", ".html", ".css", ".yml", ".yaml", ".txt", ".json"}:
            for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
                if "\u2014" in line:
                    hits.append(f"{f.relative_to(ROOT)}:{i}")
if hits:
    print(f"em-dash sweep: FAIL ({len(hits)})")
    for h in hits:
        print("  -", h)
    sys.exit(1)
print("em-dash sweep: PASS")
