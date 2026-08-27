# HELM Sci-Fi Dashboard Visual Reference Pack

Research edition, August 2026. This is the study board behind the HELM catalog: the visual evidence that the fifteen design languages were distilled from, with every image traced to a source page.

**This directory is study material, not a shipped asset library.** Nothing in `research/` is read by the validators, copied into tokens, or embedded in client deliverables. It exists so that anyone extending the catalog can see the lineage and check the reasoning.

## Contents

| File | What it is |
|---|---|
| `HELM_SciFi_Dashboard_Visual_Catalog.pdf` | 26-page fixed-layout catalog. One page per language, two supplemental pages, a three-page coverage ledger, and a three-page image source index. 133 clickable links. |
| `HELM_SciFi_Dashboard_Visual_Catalog.html` | The same catalog as a self-contained browser page with all 43 images embedded. |
| `images/` | 43 study-reference JPG files, named `<language>_<production>_<n>.jpg`. |
| `assets.tsv` | One row per image: slug, HELM language, example title, source page, direct image URL, source tier. |
| `coverage.csv` | 47-entry ledger. Every production or interface named in the four HELM source files, with year, closest HELM language, whether a visual was retained, the best verified source, and a status note. |
| `build_catalog.py` | The builder that renders the PDF and HTML from `assets.tsv`, `coverage.csv`, and `images/`. |
| `catalog-preview.jpg` | Cover page render used on the docs site. |

## Coverage

- 15 HELM style languages, each with two visuals
- 43 sourced visuals
- 47 named examples in the ledger, 25 with a retained visual and one partial record
- 21 named examples with no retained visual: confirmed in the source thread but no stable, attributable image was found

## Source order

Each image was collected at the highest tier available:

1. Studio or designer portfolio (the people who built the screen graphics)
2. Named designer interview
3. Specialist interface archive
4. Film still or community source

The `source_tier` column in `assets.tsv` records which tier applies. In HELM's evidence vocabulary, a first-party portfolio supports a CORROBORATED attribution claim; a film still supports the visual observation only, and any claim about who designed it stays UNCORROBORATED unless a second source names the studio.

## How this feeds the canonical layer

`data/canonical/lineage_register.json` is the machine-readable distillation of this pack. The register carries the design house, the production, the visual devices observed, and an evidence tier per attribution. The catalog entries in `data/canonical/catalog.json` reference the register by ID and carry original tokens only.

The boundary is deliberate: study the lineage here, ship original work from there. A screen built with HELM should read as the same family as its lineage without reproducing any element of it.

## Rights

The repository-wide statement is in [DISCLAIMER.md](../../DISCLAIMER.md). In short: all resources here are the property of their respective license holders, and this repository is solely for development and innovation use.

The images are study references. Rights remain with the credited studios, artists, publishers, and film or game owners. The pack is suitable for internal research, mood boards, and design briefs. Ask the owner before any public redistribution beyond that use, and do not place any of these images in a client deliverable.

If the repository owner decides to keep the stills out of the public tree, add `research/reference-pack/images/` and the two catalog files to `.gitignore`; `assets.tsv` retains every direct image URL so the pack can be rebuilt locally with `build_catalog.py`.
