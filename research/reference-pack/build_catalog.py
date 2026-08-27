from __future__ import annotations

import base64
import csv
import html
import io
import os
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
IMAGES = ROOT / "images"
OUT = ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

PDF_PATH = OUT / "HELM_SciFi_Dashboard_Visual_Catalog.pdf"
HTML_PATH = OUT / "HELM_SciFi_Dashboard_Visual_Catalog.html"

NAVY = "#07111F"
NAVY_2 = "#0C1A2C"
NAVY_3 = "#10233A"
ICE = "#DDEBFA"
TEXT = "#B9CCE2"
MUTED = "#7E98B5"
COBALT = "#1B63D8"
CYAN = "#62C9FF"
ORANGE = "#FF7A36"
GREEN = "#61D79A"
RED = "#FF5F62"


STYLES = [
    {
        "name": "Command-Console",
        "lineage": "LCARS and the starship status-grid lineage",
        "fit": "Calm monitoring across many systems",
        "palette": "Near-black, pastel system blocks, one active accent",
        "type": "Condensed labels with a clear body sans",
        "hierarchy": "Rounded elbow frames, sweeping bars, grouped zones",
        "motion": "Instant state changes, little ambient movement",
        "risk": "Too many colors or narrow labels at distance",
        "assets": ["command_console_lcars_01", "command_console_lcars_02"],
    },
    {
        "name": "Tactical HUD",
        "lineage": "Iron Man helmet HUD and holographic workshop",
        "fit": "Live telemetry with one critical number",
        "palette": "Warm amber for operator state, cyan for outside data",
        "type": "Condensed technical sans and tabular numbers",
        "hierarchy": "Reticles, radar arcs, gyroscopic rings",
        "motion": "Ring start-up, snap-to-target, short alert flare",
        "risk": "Decoration can bury the central reading",
        "assets": ["tactical_hud_ironman_01", "tactical_hud_ironman_02"],
    },
    {
        "name": "Industrial Terminal",
        "lineage": "Alien ship computer and hard-SF laboratory screens",
        "fit": "Logs, events, audits, text-heavy status",
        "palette": "Green or amber phosphor, black ground, hazard color",
        "type": "Block monospace on a character-cell grid",
        "hierarchy": "Text tables, boxed readouts, cursor, pictograms",
        "motion": "Line-by-line reveal and cursor blink",
        "risk": "Weak chart language and an impersonal tone",
        "assets": ["industrial_terminal_alien", "industrial_terminal_andromeda"],
    },
    {
        "name": "Vector-Wireframe",
        "lineage": "Star Wars targeting computers and early TRON screens",
        "fit": "Sparse geometry, trajectory, archival time series",
        "palette": "Monochrome green or orange linework on black",
        "type": "Minimal labels with numeric readouts",
        "hierarchy": "Converging lines, wireframes, reticles, countdown",
        "motion": "Slow line draw and steady tick",
        "risk": "Poor magnitude encoding when fills are absent",
        "assets": ["vector_wireframe_starwars", "vector_wireframe_tron"],
    },
    {
        "name": "Gestural Holographic",
        "lineage": "Minority Report Pre-Crime screen grammar",
        "fit": "Investigation, drill-down, relationship work",
        "palette": "Ghost blue-white layers with one warm accent",
        "type": "Sparse clinical sans",
        "hierarchy": "Floating panes, object-like video, depth stacking",
        "motion": "Grab, slide, toss, parallax, elastic stop",
        "risk": "Transparent-screen glare and arm fatigue",
        "assets": ["gestural_minority_01", "gestural_minority_02"],
    },
    {
        "name": "Hard-Realism Tactical",
        "lineage": "The Expanse faction-coded ship systems",
        "fit": "Multi-unit operations and plausible enterprise use",
        "palette": "Restrained unit palettes on dark grounds",
        "type": "Glove-legible technical sans and clean telemetry",
        "hierarchy": "Faction color grammar and clear system zones",
        "motion": "Grounded physical easing with little theater",
        "risk": "Can look generic without a strong faction grammar",
        "assets": ["hard_realism_expanse_01", "hard_realism_expanse_02"],
    },
    {
        "name": "NASA-Utilitarian",
        "lineage": "Interstellar live spacecraft screens and HAL-era telemetry",
        "fit": "Engineering, mission status, precision audiences",
        "palette": "Low-chroma greens and ambers with system accents",
        "type": "Utility monospace, short system codes, plain headers",
        "hierarchy": "Telemetry cells, orbital diagrams, dense grids",
        "motion": "Steady refresh without glow",
        "risk": "Low spectacle can feel flat in sales settings",
        "assets": ["nasa_interstellar_01", "nasa_interstellar_02"],
    },
    {
        "name": "Sonar-Surveillance",
        "lineage": "The Dark Knight city-wide sonar mapping",
        "fit": "Security, anomaly, network, threat monitoring",
        "palette": "Near-monochrome green or blue on black",
        "type": "Monospace terminal labels",
        "hierarchy": "Point clouds, wireframe space, scan fields",
        "motion": "Sweep reveal, slow pulse, sonar ping",
        "risk": "The visual language carries an ethical surveillance mood",
        "assets": ["sonar_dark_knight", "sonar_mission_impossible"],
    },
    {
        "name": "Neuro-Medical",
        "lineage": "Doctor Strange medical screens grounded in science fact",
        "fit": "Clinical, anatomical, regulated, QA data",
        "palette": "Clinical blue-white with anatomical color coding",
        "type": "Clean medical sans",
        "hierarchy": "Volumetric regions, orthographic panels, isolated anatomy",
        "motion": "Precise and slow, with little ambient movement",
        "risk": "Cold tone and limited brand personality",
        "assets": ["neuro_doctor_strange_01", "neuro_doctor_strange_02"],
    },
    {
        "name": "Corporate-Liner",
        "lineage": "Passengers public terminals and luxury starliner systems",
        "fit": "Public information, wayfinding, onboarding",
        "palette": "Warm gold, clean white, alert red in crisis",
        "type": "Elegant brand-forward sans",
        "hierarchy": "Concierge cards, cutaways, large friendly numbers",
        "motion": "Smooth and generous easing",
        "risk": "Over-simplification can make expert data feel childish",
        "assets": ["corporate_passengers_01", "corporate_passengers_02"],
    },
    {
        "name": "Tabletop-Motion",
        "lineage": "Quantum of Solace evidence table and The Island desk",
        "fit": "Joint review, evidence rooms, deal rooms",
        "palette": "Flat geometric color and strong type",
        "type": "Bold geometric sans",
        "hierarchy": "Cards as physical objects with cross-reference lines",
        "motion": "Lag, elasticity, object shuffle",
        "risk": "Motion can slow readers who need fast scanning",
        "assets": ["tabletop_quantum", "tabletop_island"],
    },
    {
        "name": "Neon-Grid",
        "lineage": "TRON, Mute, and Blade Runner 2049 screen language",
        "fit": "Entertainment, gaming, nightlife, high-energy moments",
        "palette": "Black void with cyan, magenta, yellow glow",
        "type": "Geometric circuit-style display faces",
        "hierarchy": "Glowing grids, circuit traces, ribbon paths",
        "motion": "Trail, afterglow, pulse",
        "risk": "Glow cuts contrast and causes fatigue",
        "assets": ["neon_bladerunner_01", "neon_bladerunner_02"],
    },
    {
        "name": "Monochrome-Blueprint",
        "lineage": "Matrix Reloaded Zion dock-control drawings",
        "fit": "Engineering, facilities, restraint-first brands",
        "palette": "Greyscale with one alarm accent",
        "type": "Technical drafting sans",
        "hierarchy": "Blueprint linework and symbol-only controls",
        "motion": "Minimal",
        "risk": "Symbol-only controls demand training",
        "assets": ["monochrome_matrix_01", "monochrome_matrix_02"],
    },
    {
        "name": "Diegetic Wearable",
        "lineage": "Dead Space suit status and in-world holograms",
        "fit": "Wearables, mobile status, in-place feedback",
        "palette": "Cyan glow on a dark industrial ground",
        "type": "Thin holographic sans with few numbers",
        "hierarchy": "Body status strip, projected panels, locator trail",
        "motion": "Summoned panels without pausing the scene",
        "risk": "Three-dimensional maps are weak navigation tools",
        "assets": ["diegetic_deadspace_01", "diegetic_deadspace_02"],
    },
    {
        "name": "Retro-Forward",
        "lineage": "Rogue One designed against the 1976 film grammar",
        "fit": "Heritage, museums, archives, long time horizons",
        "palette": "One key color per screen, no tonal shading",
        "type": "Low-resolution 1970s-style script",
        "hierarchy": "Analog vector lines, blueprints, physical switches",
        "motion": "Line draw, CRT flicker, relay click",
        "risk": "Low resolution limits density and accessibility",
        "assets": ["retro_rogueone_01", "retro_rogueone_02"],
    },
]


SUPPLEMENT_ASSETS = [
    "supp_justice_league",
    "supp_independence_day",
    "supp_wall_e_01",
    "supp_wall_e_02",
    "supp_life_01",
    "supp_life_02",
    "supp_mute",
    "supp_cabin",
    "supp_mission_impossible",
    "supp_bladerunner_ksp",
    "supp_hal9000",
    "supp_doctor_strange_maxon",
    "supp_the_island_ops",
]


def load_assets():
    with (ROOT / "assets.tsv").open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    return rows, {row["slug"]: row for row in rows}


def load_coverage():
    with (ROOT / "coverage.csv").open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def register_fonts():
    font_dir = Path("/usr/share/fonts/truetype/dejavu")
    pdfmetrics.registerFont(TTFont("DejaVu", str(font_dir / "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuBold", str(font_dir / "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuCond", str(font_dir / "DejaVuSansMono.ttf")))


def c(hex_value):
    from reportlab.lib.colors import HexColor
    return HexColor(hex_value)


def fit_image(path: Path, x, y, w, h):
    with Image.open(path) as im:
        iw, ih = im.size
    ratio = min(w / iw, h / ih)
    dw, dh = iw * ratio, ih * ratio
    return x + (w - dw) / 2, y + (h - dh) / 2, dw, dh


def wrap_text(text, font, size, max_width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        trial = word if not line else f"{line} {word}"
        if pdfmetrics.stringWidth(trial, font, size) <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def short_url(url):
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    tail = path.split("/")[-1] if path else ""
    if len(tail) > 24:
        tail = tail[:21] + "..."
    return parsed.netloc.replace("www.", "") + ("/" + tail if tail else "")


def draw_header(pdf, page_no, title, subtitle=None):
    width, height = landscape(letter)
    pdf.setFillColor(c(NAVY))
    pdf.rect(0, 0, width, height, stroke=0, fill=1)
    pdf.setFillColor(c(COBALT))
    pdf.rect(0, height - 9, width, 9, stroke=0, fill=1)
    pdf.setFillColor(c(ICE))
    pdf.setFont("DejaVuBold", 20)
    pdf.drawString(34, height - 43, title)
    if subtitle:
        pdf.setFillColor(c(MUTED))
        pdf.setFont("DejaVu", 8.7)
        pdf.drawString(35, height - 58, subtitle)
    pdf.setFillColor(c(MUTED))
    pdf.setFont("DejaVuCond", 7)
    pdf.drawRightString(width - 26, 18, f"BHIL / HELM  |  VISUAL REFERENCE  |  {page_no:02d}")


def draw_image_card(pdf, asset, x, y, w, h, index):
    pdf.setFillColor(c(NAVY_2))
    pdf.roundRect(x, y, w, h, 7, stroke=0, fill=1)
    inner = 8
    image_h = h - 38
    img_path = IMAGES / f"{asset['slug']}.jpg"
    ix, iy, iw, ih = fit_image(img_path, x + inner, y + 28, w - 2 * inner, image_h - 2)
    pdf.setFillColor(c("#02070D"))
    pdf.rect(x + inner, y + 28, w - 2 * inner, image_h, stroke=0, fill=1)
    pdf.drawImage(str(img_path), ix, iy, iw, ih, preserveAspectRatio=True, mask="auto")
    pdf.setFillColor(c(CYAN))
    pdf.setFont("DejaVuBold", 7.8)
    pdf.drawString(x + 10, y + 16, f"{index:02d}  {asset['example']}")
    pdf.setFillColor(c(MUTED))
    pdf.setFont("DejaVuCond", 6.5)
    source_label = short_url(asset["source_url"])
    pdf.drawRightString(x + w - 10, y + 16, source_label)
    pdf.linkURL(asset["source_url"], (x + w - 170, y + 10, x + w - 8, y + 25), relative=0)


def build_pdf(rows, asset_map, coverage):
    register_fonts()
    width, height = landscape(letter)
    pdf = canvas.Canvas(str(PDF_PATH), pagesize=(width, height))
    pdf.setTitle("HELM Sci-Fi Dashboard Visual Catalog")
    pdf.setAuthor("Barry Hurd Intelligence Lab")
    page = 1

    pdf.setFillColor(c(NAVY))
    pdf.rect(0, 0, width, height, stroke=0, fill=1)
    pdf.setFillColor(c(COBALT))
    pdf.rect(0, height - 12, width, 12, stroke=0, fill=1)
    pdf.setFillColor(c(CYAN))
    pdf.setFont("DejaVuBold", 10)
    pdf.drawString(40, height - 57, "BARRY HURD INTELLIGENCE LAB / HELM")
    pdf.setFillColor(c(ICE))
    pdf.setFont("DejaVuBold", 31)
    pdf.drawString(40, height - 112, "SCI-FI DASHBOARD")
    pdf.drawString(40, height - 149, "VISUAL REFERENCE CATALOG")
    pdf.setFillColor(c(TEXT))
    pdf.setFont("DejaVu", 12)
    pdf.drawString(42, height - 180, "15 style languages  |  43 sourced visuals  |  47 named examples")
    cover_slugs = [
        "command_console_lcars_01",
        "tactical_hud_ironman_01",
        "gestural_minority_01",
        "hard_realism_expanse_01",
        "neuro_doctor_strange_01",
        "retro_rogueone_01",
    ]
    x0, y0 = 40, 64
    card_w, card_h, gap = 230, 112, 9
    for i, slug in enumerate(cover_slugs):
        row, col = divmod(i, 3)
        x = x0 + col * (card_w + gap)
        y = y0 + (1 - row) * (card_h + gap)
        pdf.setFillColor(c(NAVY_2))
        pdf.roundRect(x, y, card_w, card_h, 6, stroke=0, fill=1)
        img_path = IMAGES / f"{slug}.jpg"
        ix, iy, iw, ih = fit_image(img_path, x + 3, y + 3, card_w - 6, card_h - 6)
        pdf.drawImage(str(img_path), ix, iy, iw, ih, preserveAspectRatio=True, mask="auto")
    pdf.setFillColor(c(MUTED))
    pdf.setFont("DejaVuCond", 7)
    pdf.drawRightString(width - 26, 18, "RESEARCH EDITION  |  AUGUST 2026")
    pdf.showPage()
    page += 1

    draw_header(pdf, page, "How to read this catalog", "A research board for dashboard art direction, not a licensed asset library")
    sections = [
        ("SOURCE ORDER", "Studio or designer portfolio, named interview, specialist archive, then a film-still source."),
        ("IMAGE STATUS", "Each visual is a study reference with its source page listed. Rights stay with the credited owner."),
        ("STYLE BINDING", "Each HELM language has a native use, a hierarchy pattern, a motion pattern, and a known cost."),
        ("PRACTICAL TEST", "Judge a screen at three scales: room distance, laptop distance, and a cropped mobile view."),
        ("COLOR RULE", "Color marks system group or state. It should not act as decoration across every panel."),
        ("DENSITY RULE", "Dense screens need a clear focal reading. Ambient data belongs outside the main task zone."),
    ]
    left, top = 46, height - 96
    box_w, box_h = 340, 118
    for i, (label, body) in enumerate(sections):
        r, col = divmod(i, 2)
        x = left + col * (box_w + 18)
        y = top - r * (box_h + 16) - box_h
        pdf.setFillColor(c(NAVY_2))
        pdf.roundRect(x, y, box_w, box_h, 8, stroke=0, fill=1)
        pdf.setFillColor(c(CYAN if i < 3 else GREEN))
        pdf.setFont("DejaVuBold", 9)
        pdf.drawString(x + 16, y + box_h - 26, label)
        pdf.setFillColor(c(TEXT))
        pdf.setFont("DejaVu", 10.2)
        yy = y + box_h - 47
        for line in wrap_text(body, "DejaVu", 10.2, box_w - 32):
            pdf.drawString(x + 16, yy, line)
            yy -= 15
    pdf.setFillColor(c(MUTED))
    pdf.setFont("DejaVuCond", 7.5)
    pdf.drawString(47, 39, "The screenshots are suitable for internal study, mood boards, and design briefs. Ask the owner before public redistribution.")
    pdf.showPage()
    page += 1

    draw_header(pdf, page, "HELM style map", "Fifteen visual languages arranged by native dashboard use")
    headers = ["#", "Language", "Native use", "Primary visual device", "Main risk"]
    col_x = [38, 62, 205, 420, 640]
    col_w = [22, 140, 210, 215, 120]
    y = height - 86
    pdf.setFillColor(c(COBALT))
    pdf.rect(34, y - 19, width - 68, 24, stroke=0, fill=1)
    pdf.setFillColor(c(ICE))
    pdf.setFont("DejaVuBold", 7.5)
    for x, label in zip(col_x, headers):
        pdf.drawString(x, y - 11, label)
    y -= 25
    for i, style in enumerate(STYLES, 1):
        row_h = 31
        pdf.setFillColor(c(NAVY_2 if i % 2 else NAVY_3))
        pdf.rect(34, y - row_h + 2, width - 68, row_h, stroke=0, fill=1)
        vals = [str(i), style["name"], style["fit"], style["hierarchy"], style["risk"]]
        for j, (x, value) in enumerate(zip(col_x, vals)):
            pdf.setFillColor(c(CYAN if j == 1 else TEXT))
            pdf.setFont("DejaVuBold" if j == 1 else "DejaVu", 6.9)
            lines = wrap_text(value, "DejaVuBold" if j == 1 else "DejaVu", 6.9, col_w[j])[:2]
            for li, line in enumerate(lines):
                pdf.drawString(x, y - 10 - li * 9, line)
        y -= row_h
    pdf.showPage()
    page += 1

    asset_counter = 1
    for style_index, style in enumerate(STYLES, 1):
        draw_header(pdf, page, f"{style_index:02d}  {style['name']}", style["lineage"])
        left_x, panel_y, left_w = 38, 72, 225
        pdf.setFillColor(c(NAVY_2))
        pdf.roundRect(left_x, panel_y, left_w, height - 150, 8, stroke=0, fill=1)
        blocks = [
            ("BEST FIT", style["fit"], CYAN),
            ("PALETTE", style["palette"], COBALT),
            ("TYPE", style["type"], GREEN),
            ("HIERARCHY", style["hierarchy"], ORANGE),
            ("MOTION", style["motion"], CYAN),
            ("COST", style["risk"], RED),
        ]
        yy = height - 96
        for label, body, color in blocks:
            pdf.setFillColor(c(color))
            pdf.setFont("DejaVuBold", 7.5)
            pdf.drawString(left_x + 14, yy, label)
            yy -= 14
            pdf.setFillColor(c(TEXT))
            pdf.setFont("DejaVu", 8.2)
            for line in wrap_text(body, "DejaVu", 8.2, left_w - 28):
                pdf.drawString(left_x + 14, yy, line)
                yy -= 11
            yy -= 10
        image_x, image_w = 280, width - 318
        image_h = (height - 170) / 2
        for slot, slug in enumerate(style["assets"]):
            asset = asset_map[slug]
            y = height - 86 - (slot + 1) * image_h - slot * 12
            draw_image_card(pdf, asset, image_x, y, image_w, image_h - 2, asset_counter)
            asset_counter += 1
        pdf.showPage()
        page += 1

    for part, slugs in enumerate([SUPPLEMENT_ASSETS[:7], SUPPLEMENT_ASSETS[7:]], 1):
        draw_header(pdf, page, f"Supplemental examples {part}", "Additional references named in the codex and addenda")
        cols, rows_count = 3, 3
        gap = 10
        x0, y0 = 38, 62
        card_w = (width - 76 - gap * (cols - 1)) / cols
        card_h = (height - 142 - gap * (rows_count - 1)) / rows_count
        for i, slug in enumerate(slugs):
            r, col = divmod(i, cols)
            x = x0 + col * (card_w + gap)
            y = height - 82 - (r + 1) * card_h - r * gap
            draw_image_card(pdf, asset_map[slug], x, y, card_w, card_h, asset_counter)
            asset_counter += 1
        pdf.showPage()
        page += 1

    per_page = 16
    for offset in range(0, len(coverage), per_page):
        draw_header(pdf, page, "Coverage ledger", "Every production or interface named in the four source files")
        chunk = coverage[offset: offset + per_page]
        y = height - 82
        pdf.setFillColor(c(COBALT))
        pdf.rect(31, y - 18, width - 62, 22, stroke=0, fill=1)
        pdf.setFillColor(c(ICE))
        pdf.setFont("DejaVuBold", 7)
        pdf.drawString(38, y - 10, "EXAMPLE")
        pdf.drawString(305, y - 10, "STYLE")
        pdf.drawString(463, y - 10, "VISUAL")
        pdf.drawString(518, y - 10, "BEST SOURCE")
        y -= 25
        for i, row in enumerate(chunk):
            pdf.setFillColor(c(NAVY_2 if i % 2 else NAVY_3))
            pdf.rect(31, y - 28, width - 62, 30, stroke=0, fill=1)
            pdf.setFillColor(c(TEXT))
            pdf.setFont("DejaVu", 7.1)
            ex = row["example"]
            if len(ex) > 43:
                ex = ex[:40] + "..."
            pdf.drawString(38, y - 10, ex)
            pdf.setFillColor(c(CYAN))
            pdf.drawString(305, y - 10, row["closest_HELM_language"][:25])
            visual = row["visual_collected"]
            pdf.setFillColor(c(GREEN if visual == "Yes" else ORANGE if visual == "Partial" else MUTED))
            pdf.drawString(463, y - 10, visual.upper())
            pdf.setFillColor(c(TEXT))
            label = short_url(row["best_verified_source"])
            pdf.drawString(518, y - 10, label[:39])
            pdf.linkURL(row["best_verified_source"], (515, y - 18, width - 35, y), relative=0)
            pdf.setFillColor(c(MUTED))
            pdf.setFont("DejaVuCond", 6.1)
            note = row["status_note"]
            if len(note) > 98:
                note = note[:95] + "..."
            pdf.drawString(38, y - 21, note)
            y -= 31
        pdf.showPage()
        page += 1

    per_page = 15
    for offset in range(0, len(rows), per_page):
        draw_header(pdf, page, "Image source index", "Direct links are clickable in the PDF")
        chunk = rows[offset: offset + per_page]
        y = height - 82
        for i, row in enumerate(chunk, offset + 1):
            pdf.setFillColor(c(NAVY_2 if i % 2 else NAVY_3))
            pdf.roundRect(34, y - 30, width - 68, 32, 4, stroke=0, fill=1)
            pdf.setFillColor(c(CYAN))
            pdf.setFont("DejaVuBold", 7.2)
            pdf.drawString(43, y - 9, f"{i:02d}")
            pdf.setFillColor(c(ICE))
            pdf.drawString(68, y - 9, row["example"][:52])
            pdf.setFillColor(c(MUTED))
            pdf.setFont("DejaVuCond", 6.3)
            pdf.drawString(68, y - 20, row["source_tier"])
            pdf.setFillColor(c(TEXT))
            pdf.setFont("DejaVuCond", 6.8)
            label = short_url(row["source_url"])
            pdf.drawRightString(width - 43, y - 9, label)
            pdf.linkURL(row["source_url"], (width - 245, y - 22, width - 40, y), relative=0)
            y -= 35
        pdf.showPage()
        page += 1

    pdf.save()


def image_data_uri(path: Path):
    with Image.open(path) as im:
        im = im.convert("RGB")
        im.thumbnail((1200, 800))
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=84, method=6)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("ascii")


def build_html(rows, asset_map, coverage):
    style_cards = []
    for i, style in enumerate(STYLES, 1):
        images_html = []
        for slug in style["assets"]:
            a = asset_map[slug]
            data = image_data_uri(IMAGES / f"{slug}.jpg")
            images_html.append(
                f'<figure><img src="{data}" alt="{html.escape(a["example"])}">'
                f'<figcaption><b>{html.escape(a["example"])}</b>'
                f'<a href="{html.escape(a["source_url"])}">{html.escape(short_url(a["source_url"]))}</a></figcaption></figure>'
            )
        facts = [
            ("Best fit", style["fit"]),
            ("Palette", style["palette"]),
            ("Type", style["type"]),
            ("Hierarchy", style["hierarchy"]),
            ("Motion", style["motion"]),
            ("Cost", style["risk"]),
        ]
        facts_html = "".join(f'<dt>{html.escape(k)}</dt><dd>{html.escape(v)}</dd>' for k, v in facts)
        style_cards.append(
            f'<section class="style" id="style-{i}"><div class="style-head"><span>{i:02d}</span>'
            f'<div><h2>{html.escape(style["name"])}</h2><p>{html.escape(style["lineage"])}</p></div></div>'
            f'<div class="style-grid"><dl>{facts_html}</dl><div class="shots">{"".join(images_html)}</div></div></section>'
        )

    supplements = []
    for slug in SUPPLEMENT_ASSETS:
        a = asset_map[slug]
        data = image_data_uri(IMAGES / f"{slug}.jpg")
        supplements.append(
            f'<figure><img src="{data}" alt="{html.escape(a["example"])}">'
            f'<figcaption><b>{html.escape(a["example"])}</b><a href="{html.escape(a["source_url"])}">source</a></figcaption></figure>'
        )

    coverage_rows = []
    for row in coverage:
        coverage_rows.append(
            "<tr>"
            f'<td>{html.escape(row["example"])}</td>'
            f'<td>{html.escape(row["closest_HELM_language"])}</td>'
            f'<td><span class="status {row["visual_collected"].lower()}">{html.escape(row["visual_collected"])}</span></td>'
            f'<td><a href="{html.escape(row["best_verified_source"])}">{html.escape(short_url(row["best_verified_source"]))}</a></td>'
            f'<td>{html.escape(row["status_note"])}</td>'
            "</tr>"
        )

    nav = "".join(f'<a href="#style-{i}">{i:02d} {html.escape(s["name"])}</a>' for i, s in enumerate(STYLES, 1))
    css = f"""
    :root{{--navy:{NAVY};--navy2:{NAVY_2};--navy3:{NAVY_3};--ice:{ICE};--text:{TEXT};--muted:{MUTED};--cobalt:{COBALT};--cyan:{CYAN};--green:{GREEN};--orange:{ORANGE};}}
    *{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{margin:0;background:var(--navy);color:var(--text);font:15px/1.45 Arial,sans-serif}}
    a{{color:var(--cyan);text-decoration:none}} a:hover{{text-decoration:underline}} header{{padding:70px max(5vw,34px) 48px;border-top:10px solid var(--cobalt);background:linear-gradient(135deg,#07111f,#102845)}}
    .kicker{{color:var(--cyan);font-weight:800;letter-spacing:.14em;font-size:12px}} h1{{color:var(--ice);font-size:clamp(36px,6vw,72px);line-height:.96;margin:18px 0}} header p{{font-size:18px;max-width:800px}}
    nav{{position:sticky;top:0;z-index:5;display:flex;gap:8px;overflow:auto;padding:10px 4vw;background:#07111ff2;border-bottom:1px solid #1b3755}} nav a{{white-space:nowrap;background:var(--navy2);padding:7px 10px;border-radius:16px;font-size:12px}}
    main{{max-width:1500px;margin:auto;padding:42px 4vw}} .note{{background:var(--navy2);border-left:4px solid var(--cobalt);padding:18px 22px;border-radius:8px;margin-bottom:32px}}
    .style{{background:var(--navy2);border:1px solid #19334f;border-radius:16px;padding:24px;margin:0 0 28px;box-shadow:0 18px 60px #0003}}
    .style-head{{display:flex;gap:18px;align-items:center;margin-bottom:22px}} .style-head>span{{font-size:34px;color:var(--cyan);font-weight:900}} h2{{color:var(--ice);margin:0;font-size:28px}} .style-head p{{margin:3px 0;color:var(--muted)}}
    .style-grid{{display:grid;grid-template-columns:minmax(260px,.75fr) 2fr;gap:22px}} dl{{margin:0;background:var(--navy3);padding:18px;border-radius:10px}} dt{{color:var(--cyan);font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.1em;margin-top:11px}} dt:first-child{{margin-top:0}} dd{{margin:2px 0 0;color:var(--text)}}
    .shots{{display:grid;grid-template-columns:1fr 1fr;gap:12px}} figure{{margin:0;background:#02070d;border-radius:10px;overflow:hidden}} figure img{{display:block;width:100%;height:260px;object-fit:contain;background:#02070d}} figcaption{{display:flex;justify-content:space-between;gap:12px;padding:9px 11px;font-size:12px;background:#0c1a2c}}
    .gallery{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}} .gallery figure img{{height:210px}}
    h3{{color:var(--ice);font-size:28px;margin:48px 0 18px}} .table-wrap{{overflow:auto;border:1px solid #19334f;border-radius:10px}} table{{border-collapse:collapse;width:100%;min-width:1100px;background:var(--navy2)}} th{{position:sticky;top:45px;background:var(--cobalt);color:white;text-align:left;padding:10px;font-size:12px}} td{{border-bottom:1px solid #18314c;padding:9px 10px;vertical-align:top;font-size:12px}} .status{{padding:4px 8px;border-radius:12px;background:#203348}} .status.yes{{color:#00180d;background:var(--green)}} .status.partial{{color:#211000;background:var(--orange)}} footer{{padding:34px 4vw;color:var(--muted);border-top:1px solid #19334f}}
    @media(max-width:900px){{.style-grid{{grid-template-columns:1fr}}.shots,.gallery{{grid-template-columns:1fr}}figure img,.gallery figure img{{height:auto}}}}
    """
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>HELM Sci-Fi Dashboard Visual Catalog</title><style>{css}</style></head><body>
    <header><div class="kicker">BARRY HURD INTELLIGENCE LAB / HELM</div><h1>SCI-FI DASHBOARD<br>VISUAL REFERENCE</h1><p>Fifteen style languages, 43 sourced visuals, and a coverage ledger for every interface named in the four research files.</p></header>
    <nav>{nav}</nav><main><div class="note"><b>Study reference.</b> Images stay with their credited owners. Use the catalog for internal research, mood boards, and design briefs. Ask the owner before public redistribution.</div>
    {''.join(style_cards)}<h3>Supplemental examples</h3><div class="gallery">{''.join(supplements)}</div>
    <h3>Coverage ledger</h3><div class="table-wrap"><table><thead><tr><th>Example</th><th>HELM language</th><th>Visual</th><th>Best source</th><th>Research note</th></tr></thead><tbody>{''.join(coverage_rows)}</tbody></table></div></main>
    <footer>BHIL / HELM visual research catalog, August 2026</footer></body></html>"""
    HTML_PATH.write_text(doc, encoding="utf-8")


def main():
    rows, asset_map = load_assets()
    coverage = load_coverage()
    build_pdf(rows, asset_map, coverage)
    build_html(rows, asset_map, coverage)
    print(PDF_PATH)
    print(HTML_PATH)


if __name__ == "__main__":
    main()
