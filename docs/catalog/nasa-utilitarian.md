<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# NASA-Utilitarian

`L07` · `nasa-utilitarian` · taxonomy: **command-control** · lineage decade: 2010s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 2014 deep-space mission graphics run live in-camera; 1968 monolith-era telemetry |
| Palette logic | Muted greens/ambers, low chroma; primary-block accents for system IDs |
| Type stack | Utilitarian monospace; three-letter system codes; extended geometric sans for headers |
| Shipped faces (open license, category matches) | display Michroma · body IBM Plex Sans · mono IBM Plex Mono |
| Hierarchy device | Telemetry cells, orbital diagrams, dense-but-legible grids |
| Motion grammar | Steady refresh; no glow |
| Sound cue | Quiet beep per acknowledge |
| Native strength | Trust, precision, engineering audiences |
| Native weakness | Low visual excitement |
| Radius | none |
| Glow token | none |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/nasa-utilitarian.css`.

| Token | Hex |
|---|---|
| --bg-void | #0A0C0A |
| --bg-panel | #131612 |
| --bg-panel-raised | #1B1F19 |
| --text-primary | #E6E9DF |
| --text-secondary | #B3B9A6 |
| --text-muted | #737A69 |
| --accent-primary | #A9C97A |
| --accent-secondary | #D9B458 |
| --state-nominal | #A9C97A |
| --state-caution | #D9B458 |
| --state-critical | #D96A5A |
| --state-offline | #4F544B |
| --border | #2C3129 |

Swatch family: `#A9C97A` `#D9B458` `#6FA3D9` `#D96A5A`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 400ms |
| --motion-arrival | 200ms |
| --motion-ease | linear |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle nasa-utilitarian
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
