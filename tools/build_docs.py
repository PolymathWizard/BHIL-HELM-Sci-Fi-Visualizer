#!/usr/bin/env python3
"""Render derived documentation pages from canonical JSON. Stdlib only.

Derived pages (do not hand edit):
  docs/catalog/index.md            catalog overview table
  docs/catalog/<slug>.md           one lineage card per language (15)
  docs/reference/narrative-tax.md  trope register
  docs/reference/evidence-tiers.md tier table
  docs/reference/matching-logic.md SP-3 matching table
  docs/reference/components.md     zones + component contract
  docs/reference/lineage-register.md study-only register
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT / "data" / "canonical"
DERIVED = "<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->\n\n"


def load(n):
    return json.loads((CANON / f"{n}.json").read_text())


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out) + "\n"


def swatch_row(hexes):
    return " ".join(f"`{h}`" for h in hexes)


def catalog_index(cat):
    rows = [(l["id"], f"[{l['name']}]({l['slug']}.md)", l["taxonomy"], l["lineage_decade"], l["native_strength"], l["native_weakness"]) for l in cat["languages"]]
    body = ["# The HELM Catalog", "",
            "Fifteen original design languages with documented lineage. Each language records what a lineage of fictional interfaces did so a build can carry the feel. The build uses only the abstracted grammar: palette relationships, type categories, hierarchy device, motion grammar, sound cue. No franchise names, logos, glyph systems, licensed fonts, or copied frames appear in any deliverable.", "",
            "One language per screen. Blending is an SP-3 decision with a documented rationale.", "",
            table(["ID", "Language", "Taxonomy", "Lineage decade", "Native strength", "Native weakness"], rows), "",
            "## Interaction-paradigm overlays", "", "Apply to any language.", "",
            table(["ID", "Overlay", "Description"], [(o["id"], o["name"], o["description"]) for o in cat["overlays"]])]
    return DERIVED + "\n".join(body)


def lineage_card(l):
    t = l["tokens"]
    f = l["type_fonts"]
    m = l["motion"]
    body = [f"# {l['name']}", "", f"`{l['id']}` · `{l['slug']}` · taxonomy: **{l['taxonomy']}** · lineage decade: {l['lineage_decade']}", "",
            "## Lineage card", "",
            table(["Field", "Value"], [
                ("Lineage (study only)", l["lineage_study_only"]),
                ("Palette logic", l["palette_logic"]),
                ("Type stack", l["type_stack"]),
                ("Shipped faces (open license, category matches)", f"display {f['display']} · body {f['body']} · mono {f['mono']}"),
                ("Hierarchy device", l["hierarchy_device"]),
                ("Motion grammar", l["motion_grammar"]),
                ("Sound cue", l["sound_cue"]),
                ("Native strength", l["native_strength"]),
                ("Native weakness", l["native_weakness"]),
                ("Radius", l["radius"]),
                ("Glow token", "yes, single box-shadow, never on text" if l["glow"] else "none"),
            ]),
            "## Token set", "", f"Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/{l['slug']}.css`.", "",
            table(["Token", "Hex"], [
                ("--bg-void", t["void"]), ("--bg-panel", t["panel"]), ("--bg-panel-raised", t["panel_raised"]),
                ("--text-primary", t["text"]), ("--text-secondary", t["text_secondary"]), ("--text-muted", t["text_muted"]),
                ("--accent-primary", t["accent"]), ("--accent-secondary", t["accent_2"]),
                ("--state-nominal", t["nominal"]), ("--state-caution", t["caution"]), ("--state-critical", t["critical"]), ("--state-offline", t["offline"]),
                ("--border", t["border"]),
            ]),
            f"Swatch family: {swatch_row(l['swatches'])}", "",
            "## Motion", "", table(["Token", "Value"], [("--motion-boot", f"{m['boot_ms']}ms"), ("--motion-arrival", f"{m['arrival_ms']}ms"), ("--motion-ease", m["ease"])]),
            "Reduced motion collapses boot and arrival to 0ms.", "",
            "## Restyle in Claude Code", "", "```", f"/restyle {l['slug']}", "```", "",
            "Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.", "",
            "## IP cleanliness", "", "This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds."]
    return DERIVED + "\n".join(body) + "\n"


def tropes_page(tr):
    rows = [(t["id"], t["trope"], t["usability_cost"], t["narrative_benefit"], t["helm_default"].replace("_", " "), t["rule"]) for t in tr["tropes"]]
    body = ["# The Narrative Tax Register", "", "Every science-fiction trope trades usability for storytelling. HELM makes each trade explicit and sets a default. Applied in SP-3, re-checked in SP-8. Count law: exactly 12 tropes.", "",
            table(["ID", "Trope", "Usability cost", "Narrative benefit", "HELM default", "Rule"], rows), "",
            "A build may override a default only with a documented rationale in the SP-3 output and a matching QA line in SP-8."]
    return DERIVED + "\n".join(body) + "\n"


def evidence_page(ev):
    rows = [(t["rank"], t["tier"], t["definition"], t["helm_application"], "yes" if t["on_screen_label_required"] else "no") for t in ev["tiers"]]
    s = ev["synthetic_flag"]
    body = ["# Evidence Classification Standard", "", "The five-tier vocabulary is shared across every BHIL framework and propagates faithfully. Order is fixed. Every headline metric on a HELM screen either carries VERIFIED or CORROBORATED, or shows its class label on screen.", "",
            table(["Rank", "Tier", "Definition", "HELM application", "On-screen label required"], rows), "",
            f"## {s['label']}", "", s["definition"], "",
            "## Why this is load-bearing", "", "Claim degradation is invisible at the variant level. A hedge stripped during compression looks like confidence. Structural enforcement (the label travels with the number in the data file and the render function refuses to draw a headline without one) is the only reliable counter."]
    return DERIVED + "\n".join(body) + "\n"


def matching_page(mt, cat):
    names = {l["slug"]: l["name"] for l in cat["languages"]}
    rows = [(r["id"], r["data_shape"], r["reader_hint"], f"[{names[r['first_fit']]}](../catalog/{r['first_fit']}.md)", f"[{names[r['alternate']]}](../catalog/{r['alternate']}.md)", r["why"]) for r in mt["rules"]]
    body = ["# SP-3 Matching Logic", "", "Data shape plus reader plus decision resolves to a first-fit language and one alternate. Every fit rationale is INFERENCE and is recorded as such in the brief. Count law: exactly 11 rules.", "",
            table(["ID", "Data shape", "Reader hint", "First fit", "Alternate", "Why"], rows), "",
            "## Override languages", "", mt["unmatched_languages_note"]]
    return DERIVED + "\n".join(body) + "\n"


def components_page(co):
    zrows = [(z["id"], z["name"], z["purpose"], z["density_wall"], z["density_laptop"], z["density_workbench"]) for z in co["zones"]]
    crows = [(c["id"], c["name"], c["purpose"], c["data_shape"], ", ".join(c["props"]), ", ".join(c["states"]), "yes" if c["decorative_only"] else "no") for c in co["components"]]
    body = ["# Zones and Component Contract", "", "## Zones and density budgets", "", "The density budget is the number of distinct data objects a zone may hold for a given reader setting. Exceeding it demotes an object; it never squeezes.", "",
            table(["Zone", "Name", "Purpose", "Wall (3 m)", "Laptop", "Workbench"], zrows), "",
            f"Alert taxonomy: {' / '.join(co['alert_states'])}. Wall displays use at most three states without a legend.", "",
            "## Component contract", "", "Count law: exactly 14 components. Components marked decorative must carry `data-decorative=\"true\"` in the artifact and may never sit where a reader could mistake them for signal.", "",
            table(["ID", "Component", "Purpose", "Data shape", "Props", "States", "Decorative only"], crows)]
    return DERIVED + "\n".join(body) + "\n"


def lineage_page(lr, cat):
    names = {l["slug"]: l["name"] for l in cat["languages"]}
    rows = [(e["id"], f"{e['work']} ({e['year']})", e["interface"], e["credited"], f"[{names[e['maps_to']]}](../catalog/{e['maps_to']}.md)", e["grammar_studied"], e["attribution_evidence"]) for e in lr["entries"]]
    houses = [(h["name"], h["location"], h["principal"] or "", h["disambiguation"] or "") for h in lr["design_houses"]]
    refs = [(r["category"], r["reference"], r["why"]) for r in lr["reference_set"]]
    body = ["# Lineage Register (study only)", "", lr["note"], "",
            "## Entries", "", table(["ID", "Work", "Interface", "Credited", "HELM language", "Grammar studied", "Attribution"], rows), "",
            "Typeface attribution for every entry is UNCORROBORATED by policy; HELM specifies type categories and ships open-license faces in those categories.", "",
            "## Design houses", "", "Tracked as first-class entities because a single studio's grammar now spans many properties.", "", table(["Studio", "Location", "Principal", "Disambiguation"], houses), "",
            "## Reference set", "", table(["Category", "Reference", "Why it matters"], refs), "",
            "## Evidence note", "", "Designer identities and studio credits are CORROBORATED across multiple independent trade sources. The tablet-prior-art claim is directional only. Analysts study the source; builders never open a franchise screenshot next to the editor."]
    return DERIVED + "\n".join(body) + "\n"


def render_all():
    cat, tr, ev, mt, co, lr = (load(n) for n in ["catalog", "tropes", "evidence_tiers", "matching", "components", "lineage_register"])
    out = {"docs/catalog/index.md": catalog_index(cat)}
    for l in cat["languages"]:
        out[f"docs/catalog/{l['slug']}.md"] = lineage_card(l)
    out["docs/reference/narrative-tax.md"] = tropes_page(tr)
    out["docs/reference/evidence-tiers.md"] = evidence_page(ev)
    out["docs/reference/matching-logic.md"] = matching_page(mt, cat)
    out["docs/reference/components.md"] = components_page(co)
    out["docs/reference/lineage-register.md"] = lineage_page(lr, cat)
    return out


if __name__ == "__main__":
    for rel, text in render_all().items():
        p = ROOT / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        print("wrote", rel)
