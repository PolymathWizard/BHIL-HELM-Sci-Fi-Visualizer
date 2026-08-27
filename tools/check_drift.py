#!/usr/bin/env python3
"""Drift gate: regenerate derived artifacts to a temp dir and diff against committed.
Fails (exit 1) on any difference. Stdlib only."""
import difflib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tokens  # noqa: E402
import build_docs  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
bad = 0
cat = json.loads(build_tokens.CATALOG.read_text())
for lang in cat["languages"]:
    committed = ROOT / "tokens" / f"{lang['slug']}.css"
    fresh = build_tokens.css_for(lang)
    if not committed.exists() or committed.read_text() != fresh:
        bad += 1
        print(f"DRIFT tokens/{lang['slug']}.css")
for rel, fresh in build_docs.render_all().items():
    committed = ROOT / rel
    if not committed.exists() or committed.read_text() != fresh:
        bad += 1
        print(f"DRIFT {rel}")
        if committed.exists():
            for line in list(difflib.unified_diff(committed.read_text().splitlines(), fresh.splitlines(), lineterm=""))[:20]:
                print("   ", line)
print("drift gate:", "FAIL" if bad else "PASS (derived artifacts match canonical)")
sys.exit(1 if bad else 0)
