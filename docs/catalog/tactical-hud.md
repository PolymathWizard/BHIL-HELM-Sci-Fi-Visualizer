<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Tactical HUD

`L02` · `tactical-hud` · taxonomy: **hud-ar** · lineage decade: 2000s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 2008-era armored-suit helmet HUD and holographic workshop |
| Palette logic | Warm gold/amber/red for the operator's own state; cool cyan for external data; optical flare accent |
| Type stack | Condensed technical sans; tabular numerals |
| Shipped faces (open license, category matches) | display Saira Condensed · body Saira · mono Share Tech Mono |
| Hierarchy device | Reticle focus, radar arcs, gyroscopic rings, layered translucent panes |
| Motion grammar | Rings spin up on load; data snaps to reticle; flare on alert |
| Sound cue | Short click per state; rising tone on lock |
| Native strength | One critical number surrounded by context |
| Native weakness | Ornamental density; flares fight contrast |
| Radius | small |
| Glow token | yes, single box-shadow, never on text |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/tactical-hud.css`.

| Token | Hex |
|---|---|
| --bg-void | #07090C |
| --bg-panel | #0E1319 |
| --bg-panel-raised | #151C25 |
| --text-primary | #F6EFDF |
| --text-secondary | #C8B98F |
| --text-muted | #7D7460 |
| --accent-primary | #F2B441 |
| --accent-secondary | #4FD6E8 |
| --state-nominal | #4FD6E8 |
| --state-caution | #F2B441 |
| --state-critical | #F0553D |
| --state-offline | #4A4F58 |
| --border | #2A3340 |

Swatch family: `#F2B441` `#F0553D` `#4FD6E8`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 1200ms |
| --motion-arrival | 300ms |
| --motion-ease | cubic-bezier(.2,.8,.2,1) |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle tactical-hud
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
