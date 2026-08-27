<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Diegetic Wearable

`L14` · `diegetic-wearable` · taxonomy: **hud-ar** · lineage decade: 2000s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 2008 survival-horror suit interface; body-worn status strip |
| Palette logic | Cyan glow on dark industrial; single-hue |
| Type stack | Thin holographic sans; minimal numerals |
| Shipped faces (open license, category matches) | display Titillium Web · body Titillium Web · mono Share Tech Mono |
| Hierarchy device | Status strip on the body of the layout; floor-projected locator trail |
| Motion grammar | Summoned panels; no pause |
| Sound cue | Soft projection hum |
| Native strength | Mobile, wearable, in-context status |
| Native weakness | Diegetic 3D maps fail at navigation |
| Radius | small |
| Glow token | yes, single box-shadow, never on text |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/diegetic-wearable.css`.

| Token | Hex |
|---|---|
| --bg-void | #060A0C |
| --bg-panel | #0C1418 |
| --bg-panel-raised | #122026 |
| --text-primary | #DDF8FF |
| --text-secondary | #8FD0DE |
| --text-muted | #4E7C88 |
| --accent-primary | #5CE1FF |
| --accent-secondary | #C7F5FF |
| --state-nominal | #5CE1FF |
| --state-caution | #FFD15C |
| --state-critical | #FF5C7A |
| --state-offline | #2F4148 |
| --border | #1E3A44 |

Swatch family: `#5CE1FF`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 600ms |
| --motion-arrival | 250ms |
| --motion-ease | cubic-bezier(.2,.8,.2,1) |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle diegetic-wearable
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
