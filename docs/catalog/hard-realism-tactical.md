<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Hard-Realism Tactical

`L06` · `hard-realism-tactical` · taxonomy: **command-control** · lineage decade: 2010s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 2015 to 2022 hard-SF ship and civic terminals; faction-coded systems |
| Palette logic | Restrained per-unit palettes on dark; utilitarian, glove-legible |
| Type stack | Clean technical sans; legible telemetry |
| Shipped faces (open license, category matches) | display Barlow Semi Condensed · body Barlow · mono Roboto Mono |
| Hierarchy device | Per-faction color grammar; swipe-to-AR handoff; transparent panels used sparingly |
| Motion grammar | Grounded, physical easing; no theatrics |
| Sound cue | Muted confirm tone |
| Native strength | Multi-unit ops, plausible enterprise use |
| Native weakness | Understated; can read as generic |
| Radius | small |
| Glow token | none |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/hard-realism-tactical.css`.

| Token | Hex |
|---|---|
| --bg-void | #0B0D10 |
| --bg-panel | #14181E |
| --bg-panel-raised | #1C222A |
| --text-primary | #EEF1F4 |
| --text-secondary | #AEB7C2 |
| --text-muted | #6F7A87 |
| --accent-primary | #5FB4E5 |
| --accent-secondary | #E0A44A |
| --state-nominal | #6FCF97 |
| --state-caution | #E0A44A |
| --state-critical | #E5605F |
| --state-offline | #4B535D |
| --border | #2C343E |

Swatch family: `#5FB4E5` `#E0A44A` `#C56A9E` `#6FCF97`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 500ms |
| --motion-arrival | 250ms |
| --motion-ease | cubic-bezier(.4,0,.2,1) |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle hard-realism-tactical
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
