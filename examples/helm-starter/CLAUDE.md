# Northline Fulfillment Dashboard: HELM build (starter example)

Purpose: the operations director decides whether to reallocate carriers before the 14:00 cutoff, in 3 to 5 seconds, from a wall display.

Data: `data/source.json` embedded as `HELM_DATA` in `dashboard.html`. Schema in `data/register.json`. Every row is SYNTHETIC. STATED fields: `on_time_target`. INFERENCE fields: `avg_dock_wait`, thresholds.

Style: `tokens/tactical-hud.css` (HELM L02). Original design language only. Never introduce franchise names, logos, glyph systems, or licensed or fan-recreation fonts.

Components: Ring Gauge (Prime), Headline Metric x4 with Sparkline (Support), Trend Chart with Filter Rail (Context), Status Pill x5 (Status Rail), Ambient Ticker (Stream, `data-decorative="true"`).

Zones and density: Prime 1, Support 4, Context 1, Status Rail 5, Stream 1 (decorative). Wall budget respected.

Commands: `/rebind <file>` · `/restyle <language>` · `/add-panel <zone> <field>`

QA: run contrast and fidelity checks before any commit (see `../../prompts/sp-08-accessibility-fidelity-qa.md`). Chart.js 4.4.1 pinned from cdnjs; an inline SVG fallback renders if the CDN is unreachable and logs a console warning.

Run: open `dashboard.html` from `file://`. No build step.
