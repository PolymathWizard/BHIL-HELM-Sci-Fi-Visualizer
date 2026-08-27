<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Industrial Terminal

`L03` · `industrial-terminal` · taxonomy: **command-control** · lineage decade: 1970s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 1979 commercial-towship computer and its hazard signage |
| Palette logic | Green or amber phosphor on pure black; hazard codes in red/yellow/blue |
| Type stack | Blocky monospace; character-cell grid |
| Shipped faces (open license, category matches) | display VT323 · body IBM Plex Mono · mono IBM Plex Mono |
| Hierarchy device | Text grids, blinking cursor, boxed readouts, pictogram wayfinding |
| Motion grammar | Line-by-line reveal; cursor blink; no smoothing |
| Sound cue | Heavy mechanical click; low hum |
| Native strength | Logs, audit trails, dense text |
| Native weakness | Cold and impersonal; no chart vocabulary |
| Radius | none |
| Glow token | none |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/industrial-terminal.css`.

| Token | Hex |
|---|---|
| --bg-void | #000000 |
| --bg-panel | #050805 |
| --bg-panel-raised | #0A120A |
| --text-primary | #9CFF8A |
| --text-secondary | #5FBF52 |
| --text-muted | #2F6B2A |
| --accent-primary | #9CFF8A |
| --accent-secondary | #FFC35A |
| --state-nominal | #9CFF8A |
| --state-caution | #FFC35A |
| --state-critical | #FF5C5C |
| --state-offline | #3A3A3A |
| --border | #1F4D1B |

Swatch family: `#9CFF8A` `#FFC35A` `#FF5C5C` `#5CA8FF`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 1200ms |
| --motion-arrival | 0ms |
| --motion-ease | steps(1, end) |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle industrial-terminal
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
