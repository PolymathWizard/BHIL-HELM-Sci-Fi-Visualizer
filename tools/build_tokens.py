#!/usr/bin/env python3
"""Generate tokens/<slug>.css for every catalog language. Stdlib only.

tokens/*.css are DERIVED. Edit data/canonical/catalog.json, then re-run.
CI drift gate (check_drift.py) fails if the generated files differ from committed ones.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "canonical" / "catalog.json"
OUT = ROOT / "tokens"

RADIUS = {"none": "0", "small": "4px", "medium": "10px", "large": "18px", "elbow": "22px 0 0 22px"}
HEADER = "/* HELM token set: {name} ({id}). DERIVED from data/canonical/catalog.json. Do not hand edit. */\n"


def css_for(lang):
    t = lang["tokens"]
    f = lang["type_fonts"]
    m = lang["motion"]
    glow = f"0 0 18px color-mix(in srgb, {t['accent']} 55%, transparent)" if lang["glow"] else "none"
    lines = [HEADER.format(name=lang["name"], id=lang["id"]), ":root {",
             f"  --helm-language: \"{lang['slug']}\";",
             "  /* background layers */",
             f"  --bg-void: {t['void']};", f"  --bg-panel: {t['panel']};", f"  --bg-panel-raised: {t['panel_raised']};",
             "  /* text */",
             f"  --text-primary: {t['text']};", f"  --text-secondary: {t['text_secondary']};", f"  --text-muted: {t['text_muted']};",
             "  /* accent */",
             f"  --accent-primary: {t['accent']};", f"  --accent-secondary: {t['accent_2']};",
             "  /* alert states: nominal / caution / critical / offline */",
             f"  --state-nominal: {t['nominal']};", f"  --state-caution: {t['caution']};",
             f"  --state-critical: {t['critical']};", f"  --state-offline: {t['offline']};",
             "  /* structure */",
             f"  --border: {t['border']};", "  --border-weight: 1px;", "  --border-weight-strong: 3px;",
             f"  --radius: {RADIUS[lang['radius']]};",
             f"  --glow: {glow};",
             "  /* type stack (open-license category faces; never screen originals) */",
             f"  --font-display: \"{f['display']}\", system-ui, sans-serif;",
             f"  --font-body: \"{f['body']}\", system-ui, sans-serif;",
             f"  --font-mono: \"{f['mono']}\", ui-monospace, monospace;",
             "  /* spacing scale */",
             "  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-6: 24px; --space-8: 32px;",
             "  /* motion */",
             f"  --motion-boot: {m['boot_ms']}ms;", f"  --motion-arrival: {m['arrival_ms']}ms;", f"  --motion-ease: {m['ease']};",
             "}", "",
             "@media (prefers-reduced-motion: reduce) {",
             "  :root { --motion-boot: 0ms; --motion-arrival: 0ms; }",
             "}", ""]
    return "\n".join(lines)


def build():
    cat = json.loads(CATALOG.read_text())
    OUT.mkdir(exist_ok=True)
    written = []
    for lang in cat["languages"]:
        p = OUT / f"{lang['slug']}.css"
        p.write_text(css_for(lang))
        written.append(p.name)
    return written


if __name__ == "__main__":
    for n in build():
        print("wrote tokens/" + n)
