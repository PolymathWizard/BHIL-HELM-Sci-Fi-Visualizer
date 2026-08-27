<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Vector-Wireframe

`L04` · `vector-wireframe` · taxonomy: **hud-ar** · lineage decade: 1970s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 1977 trench-run briefing and cockpit targeting computer |
| Palette logic | Monochrome green or orange line on black; no fills |
| Type stack | Minimal; numeric readouts only |
| Shipped faces (open license, category matches) | display Orbitron · body Share Tech Mono · mono Share Tech Mono |
| Hierarchy device | Wireframe geometry, converging reticle, countdown |
| Motion grammar | Slow line-draw; steady tick |
| Sound cue | Single tone per tick |
| Native strength | Long time-series, retro-archival, austerity |
| Native weakness | No area encoding; hard to show magnitude |
| Radius | none |
| Glow token | none |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/vector-wireframe.css`.

| Token | Hex |
|---|---|
| --bg-void | #000000 |
| --bg-panel | #000000 |
| --bg-panel-raised | #030603 |
| --text-primary | #7DFF9A |
| --text-secondary | #4FBF6A |
| --text-muted | #2A6B3A |
| --accent-primary | #7DFF9A |
| --accent-secondary | #FFA24A |
| --state-nominal | #7DFF9A |
| --state-caution | #FFA24A |
| --state-critical | #FF6A4A |
| --state-offline | #2A2A2A |
| --border | #3FBF5A |

Swatch family: `#7DFF9A` `#FFA24A`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 1000ms |
| --motion-arrival | 400ms |
| --motion-ease | linear |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle vector-wireframe
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
