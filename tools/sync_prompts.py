#!/usr/bin/env python3
"""Copy prompts/*.md into docs/prompts/ so MkDocs can serve them. Stdlib only. Derived; do not hand edit copies."""
import shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
dst = ROOT / "docs" / "prompts"
dst.mkdir(parents=True, exist_ok=True)
for p in sorted((ROOT / "prompts").glob("*.md")):
    (dst / p.name).write_text("<!-- DERIVED copy of prompts/" + p.name + " by tools/sync_prompts.py. Edit the source in prompts/. -->\n\n" + p.read_text())
    print("synced", p.name)
