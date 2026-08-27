<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Neon-Grid

`L12` · `neon-grid` · taxonomy: **public-access** · lineage decade: 1980s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 1982 computer-world interior; 2018 near-future neon city signage |
| Palette logic | Black void; cyan, magenta, yellow glow; wet-noir saturation |
| Type stack | Geometric circuit-inspired display face |
| Shipped faces (open license, category matches) | display Audiowide · body Rajdhani · mono Share Tech Mono |
| Hierarchy device | Glowing grid lines, circuit traces, ribbon paths |
| Motion grammar | Trail and afterglow; pulse |
| Sound cue | Synth sweep |
| Native strength | Energy, entertainment, gaming, nightlife |
| Native weakness | Glow destroys contrast; fatigue |
| Radius | none |
| Glow token | yes, single box-shadow, never on text |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/neon-grid.css`.

| Token | Hex |
|---|---|
| --bg-void | #05030A |
| --bg-panel | #0B0715 |
| --bg-panel-raised | #120B21 |
| --text-primary | #F3EAFF |
| --text-secondary | #C3A9F0 |
| --text-muted | #7A639E |
| --accent-primary | #3DF2FF |
| --accent-secondary | #FF3DD8 |
| --state-nominal | #3DF2FF |
| --state-caution | #FFE83D |
| --state-critical | #FF3D6E |
| --state-offline | #3A2F52 |
| --border | #2E1F4A |

Swatch family: `#3DF2FF` `#FF3DD8` `#FFE83D`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 1000ms |
| --motion-arrival | 300ms |
| --motion-ease | cubic-bezier(.2,.8,.2,1) |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle neon-grid
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
