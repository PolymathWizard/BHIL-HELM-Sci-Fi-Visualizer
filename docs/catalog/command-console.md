<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Command-Console

`L01` · `command-console` · taxonomy: **command-control** · lineage decade: 1980s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 1987 Federation starship computer; the tablet-precursor lineage |
| Palette logic | Near-black void; flat pastel swatch blocks (blue, violet, apricot, salmon); high-chroma accent for active only |
| Type stack | Ultra-condensed grotesque caps for labels; humanist sans for body |
| Shipped faces (open license, category matches) | display Antonio · body Nunito Sans · mono IBM Plex Mono |
| Hierarchy device | Rounded elbow frames, sweeping bars, pill buttons; color = system group |
| Motion grammar | Minimal activity; instant state flips; no ambient noise |
| Sound cue | Two-tone rising = open, reversed = close |
| Native strength | Calm status grids, many systems, no legend |
| Native weakness | Narrow all-caps at distance; too many simultaneous colors |
| Radius | elbow |
| Glow token | none |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/command-console.css`.

| Token | Hex |
|---|---|
| --bg-void | #050509 |
| --bg-panel | #101018 |
| --bg-panel-raised | #181826 |
| --text-primary | #F2F0FF |
| --text-secondary | #B9B4D6 |
| --text-muted | #7E7A99 |
| --accent-primary | #9C8CFF |
| --accent-secondary | #FFB27A |
| --state-nominal | #7FC8FF |
| --state-caution | #FFB27A |
| --state-critical | #FF7A7A |
| --state-offline | #5C5A6E |
| --border | #2B2B3C |

Swatch family: `#7FC8FF` `#C9A5FF` `#FFB27A` `#FF9E9E`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 600ms |
| --motion-arrival | 200ms |
| --motion-ease | steps(1, end) |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle command-console
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
