<!-- DERIVED from data/canonical by tools/build_docs.py. Do not hand edit. -->

# Neuro-Medical

`L09` · `neuro-medical` · taxonomy: **investigation** · lineage decade: 2010s

## Lineage card

| Field | Value |
|---|---|
| Lineage (study only) | 2016 neurosurgical PACS-style graphics (science fact) |
| Palette logic | Clinical white/blue; anatomical color coding; red only for fail |
| Type stack | Clean medical sans |
| Shipped faces (open license, category matches) | display Inter · body Inter · mono IBM Plex Mono |
| Hierarchy device | Volumetric region isolation; orthographic panels |
| Motion grammar | Precise, slow, orthographic |
| Sound cue | None by default |
| Native strength | Clinical, QA, precision, regulated data |
| Native weakness | Cold; little brand personality |
| Radius | small |
| Glow token | none |

## Token set

Source of truth: `data/canonical/catalog.json`. Generated CSS: `tokens/neuro-medical.css`.

| Token | Hex |
|---|---|
| --bg-void | #0E1420 |
| --bg-panel | #F7FAFF |
| --bg-panel-raised | #FFFFFF |
| --text-primary | #0F1B2D |
| --text-secondary | #3E4F68 |
| --text-muted | #6E7E95 |
| --accent-primary | #1F6FE5 |
| --accent-secondary | #19A3A3 |
| --state-nominal | #1F8A5B |
| --state-caution | #B9770E |
| --state-critical | #C0392B |
| --state-offline | #8A95A5 |
| --border | #D4DEEC |

Swatch family: `#1F6FE5` `#19A3A3` `#8E5BE5`

## Motion

| Token | Value |
|---|---|
| --motion-boot | 300ms |
| --motion-arrival | 300ms |
| --motion-ease | cubic-bezier(.4,0,.2,1) |

Reduced motion collapses boot and arrival to 0ms.

## Restyle in Claude Code

```
/restyle neuro-medical
```

Swaps the token set, keeps every binding, re-runs contrast on every token pair, reports any pair below floor.

## IP cleanliness

This language is an original design language. The lineage field names a period and function so an analyst can study the source. Nothing from that source is reproduced: no name, logo, wordmark, glyph system, licensed or fan-recreation face, or frame traceable to a specific screen. Appendix B of every HELM brief records anything withheld on these grounds.
