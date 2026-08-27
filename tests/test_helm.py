"""HELM regression tests. Each test names the bug it prevents."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import validate  # noqa: E402
import build_tokens  # noqa: E402
import build_docs  # noqa: E402

CAT = json.loads((ROOT / "data/canonical/catalog.json").read_text())


def run(*args):
    return subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)


def test_validator_passes_on_committed_canonical():
    r = run("tools/validate.py")
    assert r.returncode == 0, r.stdout


def test_count_law_exactly_fifteen_languages():
    # bug: a sixteenth language was appended without a matching rule or override
    assert len(CAT["languages"]) == 15


def test_language_ids_are_sequential():
    assert [l["id"] for l in CAT["languages"]] == [f"L{i:02d}" for i in range(1, 16)]


def test_evidence_tier_order_is_fixed():
    ev = json.loads((ROOT / "data/canonical/evidence_tiers.json").read_text())
    assert [t["tier"] for t in ev["tiers"]] == ["VERIFIED", "CORROBORATED", "UNCORROBORATED", "INFERENCE", "STATED"]


def test_matching_rules_resolve_to_catalog_slugs():
    slugs = {l["slug"] for l in CAT["languages"]}
    mt = json.loads((ROOT / "data/canonical/matching.json").read_text())
    for r in mt["rules"]:
        assert r["first_fit"] in slugs and r["alternate"] in slugs, r["id"]


def test_every_language_reachable_or_documented_override():
    mt = json.loads((ROOT / "data/canonical/matching.json").read_text())
    reached = {r[k] for r in mt["rules"] for k in ("first_fit", "alternate")}
    overrides = {"monochrome-blueprint", "diegetic-wearable", "retro-forward"}
    assert {l["slug"] for l in CAT["languages"]} <= reached | overrides


def test_ambient_ticker_is_decorative_only():
    co = json.loads((ROOT / "data/canonical/components.json").read_text())
    tick = next(c for c in co["components"] if c["name"] == "Ambient Ticker")
    assert tick["decorative_only"] is True


def test_contrast_floor_text_on_panel():
    # bug: a pastel text token slipped below 4.5:1 on its own panel
    for l in CAT["languages"]:
        t = l["tokens"]
        assert validate.contrast(t["text"], t["panel"]) >= 4.5, l["slug"]
        assert validate.contrast(t["text_secondary"], t["panel"]) >= 4.5, l["slug"]


def test_contrast_math_known_values():
    assert abs(validate.contrast("#FFFFFF", "#000000") - 21.0) < 0.01
    assert abs(validate.contrast("#777777", "#FFFFFF") - 4.48) < 0.02


def test_boot_never_exceeds_1200ms():
    for l in CAT["languages"]:
        assert l["motion"]["boot_ms"] <= 1200, l["slug"]


def test_tokens_derived_match_committed():
    for l in CAT["languages"]:
        p = ROOT / "tokens" / f"{l['slug']}.css"
        assert p.exists(), p
        assert p.read_text() == build_tokens.css_for(l), f"drift in {p.name}"


def test_token_css_declares_every_required_property():
    req = ["--bg-void", "--bg-panel", "--text-primary", "--accent-primary", "--state-nominal", "--state-caution",
           "--state-critical", "--state-offline", "--font-display", "--font-mono", "--motion-boot", "--motion-arrival", "--glow", "--radius"]
    for l in CAT["languages"]:
        css = (ROOT / "tokens" / f"{l['slug']}.css").read_text()
        for r in req:
            assert r + ":" in css, (l["slug"], r)
        assert "prefers-reduced-motion" in css


def test_docs_derived_match_committed():
    for rel, fresh in build_docs.render_all().items():
        assert (ROOT / rel).read_text() == fresh, f"drift in {rel}"


def test_no_em_dash_in_derived_prose():
    r = run("tools/em_dash_sweep.py")
    assert r.returncode == 0, r.stdout


def test_starter_register_validates():
    r = run("tools/validate_register.py", "examples/helm-starter/data/register.json")
    assert r.returncode == 0, r.stdout


def test_starter_artifact_rules():
    html = (ROOT / "examples/helm-starter/dashboard.html").read_text()
    # bug: browser storage crept into an artifact
    assert "localStorage" not in html and "sessionStorage" not in html
    # bug: unpinned CDN
    assert re.search(r"cdnjs\.cloudflare\.com/ajax/libs/Chart\.js/\d+\.\d+\.\d+/", html)
    assert "data-decorative=\"true\"" in html
    assert "function renderState" in html
    assert "prefers-reduced-motion" in html
    # every data-field in the artifact exists in the register
    reg = json.loads((ROOT / "examples/helm-starter/data/register.json").read_text())
    names = {f["name"] for f in reg["fields"]}
    for field in set(re.findall(r'data-field="([a-z_]+)"', html)):
        assert field in names, field
    # only cdnjs as an external origin
    for url in re.findall(r'https?://[^"\')\s]+', html):
        assert url.startswith("https://cdnjs.cloudflare.com/"), url


def test_starter_stated_headline_labeled_on_screen():
    # bug: STATED target rendered without its label
    html = (ROOT / "examples/helm-starter/dashboard.html").read_text()
    assert 'data-tier="STATED">STATED' in html


def test_template_placeholders_present():
    t = (ROOT / "templates/dashboard.template.html").read_text()
    for ph in ["CLIENT", "REF", "LANGUAGE_SLUG", "HELM_DATA_JSON", "DATA_MODE"]:
        assert "{{" + ph + "}}" in t, ph


def test_ip_cleanliness_no_franchise_names_in_shipped_files():
    # lineage_register.json is the documented study-only exception; everything else must be clean
    banned = ["lcars", "star trek", "iron man", "jarvis", "j.a.r.v.i.s", "nostromo", "weyland", "star wars", "blade runner",
              "minority report", "hal 9000", "dead space", "the expanse", "tron", "batman", "marvel", "starfleet"]
    check = list((ROOT / "tokens").glob("*.css")) + list((ROOT / "templates").iterdir()) + list((ROOT / "examples").rglob("*")) \
        + list((ROOT / "docs/catalog").glob("*.md")) + list((ROOT / ".claude").rglob("*.md")) + [ROOT / "data/canonical/catalog.json"]
    for f in check:
        if f.is_file():
            txt = f.read_text(errors="ignore").lower()
            for b in banned:
                assert not re.search(r"\b" + re.escape(b) + r"\b", txt), f"{f.relative_to(ROOT)} contains '{b}'"


def test_reference_pack_is_quarantined_with_rights_note():
    """Bug prevented: study images leaking into shipped deliverables, or the pack shipping without its rights posture."""
    pack = ROOT / "research/reference-pack"
    readme = (pack / "README.md").read_text()
    assert "Rights remain with the credited" in readme
    assert "not a shipped asset library" in readme
    names = {p.name for p in (pack / "images").glob("*.jpg")}
    assert len(names) == 43
    for d in ("examples", "templates", "tokens", "docs/assets"):
        for p in (ROOT / d).rglob("*"):
            assert p.name not in names, f"reference-pack image shipped in {p}"


def test_disclaimer_present_and_linked():
    """Bug prevented: shipping third-party study material without the intended-use and rights statement."""
    d = (ROOT / "DISCLAIMER.md").read_text()
    assert "property of their respective license holders" in d
    assert "solely for development, research, and innovation use" in d
    assert "DISCLAIMER.md" in (ROOT / "README.md").read_text()
    assert (ROOT / "docs/disclaimer.md").read_text() == d
