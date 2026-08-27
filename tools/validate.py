#!/usr/bin/env python3
"""HELM canonical validator. Stdlib only.

Enforces:
  - a minimal JSON Schema subset (type, required, enum, const, pattern, minItems,
    maxItems, minimum, maximum, additionalProperties, properties, items)
  - framework count laws (15 languages, 12 tropes, 5 tiers, 11 rules, 14 components)
  - cross-references (matching.first_fit / alternate resolve to catalog slugs;
    lineage.maps_to resolves; every language reachable from matching or the
    documented override list)
  - contrast floors per language (text on panel >= 4.5:1, text_secondary on panel
    >= 4.5:1, state colors on panel >= 3:1) with a documented exception file

Exit 0 on pass, 1 on any failure. Never silently corrects.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / "data" / "canonical"
SCHEMAS = ROOT / "data" / "schemas"
EXCEPTIONS = ROOT / "data" / "canonical" / "contrast_exceptions.json"

errors = []


def err(msg):
    errors.append(msg)


# ---------- minimal schema engine ----------
def check(inst, schema, path="$"):
    t = schema.get("type")
    if t:
        ok = {
            "object": isinstance(inst, dict),
            "array": isinstance(inst, list),
            "string": isinstance(inst, str),
            "integer": isinstance(inst, int) and not isinstance(inst, bool),
            "boolean": isinstance(inst, bool),
            "number": isinstance(inst, (int, float)) and not isinstance(inst, bool),
        }.get(t, True)
        if not ok:
            err(f"{path}: expected {t}")
            return
    if "const" in schema and inst != schema["const"]:
        err(f"{path}: expected const {schema['const']!r}, got {inst!r}")
    if "enum" in schema and inst not in schema["enum"]:
        err(f"{path}: {inst!r} not in {schema['enum']}")
    if "pattern" in schema and isinstance(inst, str) and not re.match(schema["pattern"], inst):
        err(f"{path}: {inst!r} fails pattern {schema['pattern']}")
    if isinstance(inst, (int, float)) and not isinstance(inst, bool):
        if "minimum" in schema and inst < schema["minimum"]:
            err(f"{path}: {inst} < minimum {schema['minimum']}")
        if "maximum" in schema and inst > schema["maximum"]:
            err(f"{path}: {inst} > maximum {schema['maximum']}")
    if isinstance(inst, dict):
        for r in schema.get("required", []):
            if r not in inst:
                err(f"{path}: missing required '{r}'")
        props = schema.get("properties", {})
        for k, v in inst.items():
            if k in props:
                check(v, props[k], f"{path}.{k}")
            elif schema.get("additionalProperties") is False and k != "$schema":
                err(f"{path}: unexpected property '{k}'")
    if isinstance(inst, list):
        if "minItems" in schema and len(inst) < schema["minItems"]:
            err(f"{path}: {len(inst)} items < minItems {schema['minItems']}")
        if "maxItems" in schema and len(inst) > schema["maxItems"]:
            err(f"{path}: {len(inst)} items > maxItems {schema['maxItems']}")
        if "items" in schema:
            for i, it in enumerate(inst):
                check(it, schema["items"], f"{path}[{i}]")


# ---------- contrast ----------
def _lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexcol):
    h = hexcol.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def load(name):
    return json.loads((CANON / f"{name}.json").read_text())


def main():
    files = ["catalog", "tropes", "evidence_tiers", "matching", "components", "lineage_register"]
    data = {}
    for f in files:
        try:
            data[f] = load(f)
        except Exception as e:  # noqa: BLE001
            err(f"{f}.json: unreadable ({e})")
            continue
        schema = json.loads((SCHEMAS / f"{f}.schema.json").read_text())
        check(data[f], schema, f)

    if errors:
        report()
        return 1

    # count laws (belt and braces beyond schema)
    laws = {"catalog": ("languages", 15), "tropes": ("tropes", 12), "evidence_tiers": ("tiers", 5),
            "matching": ("rules", 11), "components": ("components", 14)}
    for f, (key, n) in laws.items():
        got = len(data[f][key])
        if got != n:
            err(f"count law: {f}.{key} has {got}, law says {n}")
        if data[f].get("count_law") != n:
            err(f"count law: {f}.count_law declares {data[f].get('count_law')}, law says {n}")

    # uniqueness
    langs = data["catalog"]["languages"]
    slugs = [l["slug"] for l in langs]
    ids = [l["id"] for l in langs]
    for label, seq in (("slug", slugs), ("id", ids)):
        dupes = {x for x in seq if seq.count(x) > 1}
        if dupes:
            err(f"catalog: duplicate {label}s {sorted(dupes)}")
    if ids != [f"L{i:02d}" for i in range(1, 16)]:
        err("catalog: language ids must run L01..L15 in order")

    # evidence tier order
    tiers = [t["tier"] for t in data["evidence_tiers"]["tiers"]]
    if tiers != ["VERIFIED", "CORROBORATED", "UNCORROBORATED", "INFERENCE", "STATED"]:
        err(f"evidence_tiers: order must be fixed, got {tiers}")

    # cross refs
    slugset = set(slugs)
    reached = set()
    for r in data["matching"]["rules"]:
        for k in ("first_fit", "alternate"):
            if r[k] not in slugset:
                err(f"matching {r['id']}.{k}: '{r[k]}' is not a catalog slug")
            reached.add(r[k])
    overrides = {"monochrome-blueprint", "diegetic-wearable", "retro-forward"}
    unreached = slugset - reached - overrides
    if unreached:
        err(f"matching: languages unreachable and not in override list: {sorted(unreached)}")
    for e in data["lineage_register"]["entries"]:
        if e["maps_to"] not in slugset:
            err(f"lineage {e['id']}.maps_to: '{e['maps_to']}' is not a catalog slug")

    # decorative rule
    for c in data["components"]["components"]:
        if c["name"] == "Ambient Ticker" and not c["decorative_only"]:
            err("components: Ambient Ticker must be decorative_only")

    # contrast floors
    exc = {}
    if EXCEPTIONS.exists():
        exc = {(x["language"], x["pair"]): x for x in json.loads(EXCEPTIONS.read_text())["exceptions"]}
    for l in langs:
        t = l["tokens"]
        light_panel = luminance(t["panel"]) > 0.5
        pairs = [("text", "panel", 4.5), ("text_secondary", "panel", 4.5),
                 ("nominal", "panel", 3.0), ("caution", "panel", 3.0), ("critical", "panel", 3.0),
                 ("accent", "panel", 3.0)]
        if not light_panel:
            pairs.append(("text", "void", 4.5))  # dark languages set text directly on void
        for fg, bg, floor in pairs:
            ratio = contrast(t[fg], t[bg])
            key = (l["slug"], f"{fg}/{bg}")
            if ratio < floor and key not in exc:
                err(f"contrast {l['slug']} {fg} on {bg}: {ratio:.2f} < {floor} (no logged exception)")

    report()
    return 1 if errors else 0


def report():
    if errors:
        print(f"HELM validate: FAIL ({len(errors)} finding{'s' if len(errors) != 1 else ''})")
        for e in errors:
            print("  -", e)
    else:
        print("HELM validate: PASS (15 languages, 12 tropes, 5 tiers, 11 rules, 14 components, contrast floors held)")


if __name__ == "__main__":
    sys.exit(main())
