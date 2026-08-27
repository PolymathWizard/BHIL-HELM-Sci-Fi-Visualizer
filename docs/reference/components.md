<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Zones and Component Contract

## Zones and density budgets

The density budget is the number of distinct data objects a zone may hold for a given reader setting. Exceeding it demotes an object; it never squeezes.

| Zone | Name | Purpose | Wall (3 m) | Laptop | Workbench |
|---|---|---|---|---|---|
| prime | Prime | The headline number or state | 1 | 1 | 2 |
| support | Support | Three to five secondary metrics | 3 | 5 | 8 |
| context | Context | Trend, comparison | 1 | 3 | 6 |
| stream | Stream | Live log, ticker, ambient | 0 | 1 | 2 |
| control | Control | Filters, time range | 0 | 3 | 6 |
| status_rail | Status Rail | System health | 5 | 8 | 12 |


Alert taxonomy: nominal / caution / critical / offline. Wall displays use at most three states without a legend.

## Component contract

Count law: exactly 14 components. Components marked decorative must carry `data-decorative="true"` in the artifact and may never sit where a reader could mistake them for signal.

| ID | Component | Purpose | Data shape | Props | States | Decorative only |
|---|---|---|---|---|---|---|
| C01 | Frame Panel | Zone boundary carrying the language hierarchy device | none | zone, title, priority | default, focused | no |
| C02 | Headline Metric | One number, one label, one evidence class | scalar | value, label, unit, evidence, delta | nominal, caution, critical, offline | no |
| C03 | Ring Gauge | Progress or utilization against a bound | scalar-with-bound | value, max, label, evidence | nominal, caution, critical | no |
| C04 | Bar / Segmented Bar | Categorical comparison | categorical | series, labels, evidence | default, hover | no |
| C05 | Sparkline | Compact trend beside a metric | time-series | values, window | default | no |
| C06 | Trend Chart | Full time-series with axes | time-series | series, x, y, evidence | default, hover, range-selected | no |
| C07 | Status Pill | One system, one state, readable without color | enum | label, state, shape | nominal, caution, critical, offline | no |
| C08 | Data Grid | Tabular detail with keyboard navigation | table | columns, rows, sort | default, row-focused, sorted | no |
| C09 | Log Stream | Chronological events; real events only | event-list | events, max_visible | live, paused | no |
| C10 | Radar / Polar Plot | Multi-axis profile comparison | multi-axis | axes, series | default, hover | no |
| C11 | Map Tile | Geospatial placement | geospatial | points, bounds | default, hover | no |
| C12 | Filter Rail | Time range and segment controls | none | ranges, segments | default, active | no |
| C13 | Alert Banner | Critical state announcement with shape and label | enum | message, state | hidden, caution, critical | no |
| C14 | Ambient Ticker | Atmosphere only; must carry data-decorative | none | text | scrolling, paused | yes |

