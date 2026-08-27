# About HELM

![HELM command surface](assets/hero/helm-hero-01-command-surface.jpg)

**HELM** stands for **Heuristic Engine for Layered Mockups**. It is a Barry Hurd Intelligence Lab framework for turning a client's data into an interactive dashboard that looks like a science-fiction command surface, reads at room distance, answers one named decision, and can be rebuilt by the client's own Claude Code session without the lab in the loop.

The name is literal. A helm is the station where the information converges and the decision gets made. The engine is heuristic because the fifteen style languages, twelve tropes, and eleven matching rules are judgments distilled from a body of film and game interface work, not a formula. The mockups are layered because every build stacks the same way: canonical data, a style language, a component contract, a functional artifact, a QA gate.

## Why science fiction

Fictional user interfaces are the most effective communication design under time compression ever made. A film screen has roughly one second to read as both complex and clear, and the studios that make them (Territory, Cantina Creative, Imaginary Forces, MK12, SPOV, BLIND, Perception, among others) have spent decades refining that grammar.

The same grammar makes real products worse when copied without editing. Screens that flash, spin, and stream ambient data are anti-usable in a room where someone has to act. HELM keeps the discipline of the one-second read and strips the twelve tropes that cost real users their attention. That trade is the whole framework.

## What HELM produces

A HELM engagement ends with a folder the client owns:

- One self-contained `dashboard.html` that opens from disk, degrades to inline SVG if its one pinned chart library is blocked, honors reduced-motion, and shape-codes every alert state so color is never the only signal.
- A `register.json` that names the reader, the setting, the seconds available, the decision question, and the data mode (live or SYNTHETIC, badged on screen).
- A CSS token file for the chosen language, generated from canonical data so it cannot drift by hand.
- A `CLAUDE.md`, a `REGENERATE.md`, and a client skill file, so the next change is a command in the client's own Claude Code session rather than a ticket back to the lab.

Every metric on screen carries an evidence label from the five-tier vocabulary shared across all BHIL frameworks: VERIFIED, CORROBORATED, UNCORROBORATED, INFERENCE, STATED. A target the client typed in is STATED. A number the engine derived is INFERENCE. The label stays attached through every restyle.

## How the pipeline runs

![The HELM pipeline from data to gate](assets/hero/helm-hero-03-pipeline.jpg)

Ten prompts, run in order, each with a gate.

| Stage | Prompts | What has to be true before the next stage |
|---|---|---|
| Profile | SP-1, SP-2 | The data is typed, the reader is named, the decision question is one sentence |
| Map | SP-3, SP-4 | One language is bound with its rule cited; the six zones have a density budget |
| Style | SP-5 | Every component has states, props, and an accessibility contract |
| Build | SP-6, SP-7 | The artifact runs from disk; motion has a purpose and a reduced-motion path |
| Ship | SP-8, SP-9, SP-10 | Contrast, keyboard, and screen-reader checks pass; the snapshot is written; a fresh-context QA agent signs off |

In Claude Code the same stages are four CADRE agents (`helm-profiler`, `helm-stylist`, `helm-builder`, `helm-qa`) with tool grants that match their job. The QA agent can only write the log and the disposition. It always runs in a fresh context so it is judging the artifact, not the conversation that produced it.

## The fifteen languages

![Layered design languages over data](assets/hero/helm-hero-02-layered-languages.jpg)

The catalog holds fifteen style languages, each with an original token set, open-license typefaces, a native use, a hierarchy pattern, a motion pattern, and a known cost. Command-Console for calm multi-system monitoring. Tactical HUD when one number matters. Industrial Terminal for logs and audits. NASA-Utilitarian for engineering audiences who distrust spectacle. Corporate-Liner for public wayfinding. Neon-Grid for the moments that are allowed to be loud. The full table is on the [catalog overview](catalog/index.md).

Three languages (Monochrome-Blueprint, Diegetic Wearable, Retro-Forward) are never selected by the matching rules. They require an explicit override, because their costs are high enough that a client should choose them on purpose.

The language names on the panel above are illustrative composites drawn for the launch imagery; the canonical names are the fifteen in the catalog.

## The operating room

![HELM in an operations setting](assets/hero/helm-hero-04-operations-room.jpg)

HELM is designed for the wall, the laptop, and the cropped phone view at the same time. Every build is judged at all three distances. The three commitments on the left of that image are the framework in six words: decision first, lineage not reproduction, evidence tagged.

## What HELM refuses to do

- **Reproduce a franchise interface.** The lineage register records which studios and productions each language descends from, and the tests fail the build if a property name enters a shipped file. Clients get the family resemblance, never the copy.
- **Ship decoration as data.** The Ambient Ticker component exists, is flagged `decorative_only`, and can never carry a metric.
- **Let a restyle strip a label.** Evidence tiers and the SYNTHETIC badge survive every language change because they live in the register, not the template.

## The research behind it

![Cover of the visual reference catalog](assets/catalog-preview.jpg)

The catalog was distilled from a study board of 43 sourced visuals across 47 named productions and interfaces, each traced to a studio portfolio, designer interview, specialist archive, or film still, in that order of preference. The board ships in `research/reference-pack/` as a 26-page PDF, a self-contained HTML page, the image set, and the two ledgers that generate them. See the [reference pack](research/reference-pack.md) page for the coverage table and the rights posture.

The machine-readable distillation is `data/canonical/lineage_register.json`. It is the only file in the canonical layer where production names appear, and every attribution in it carries an evidence tier.

## The engine, in one picture

![The HELM engine and its five facets](assets/hero/helm-hero-05-engine-map.jpg)

Reader, decision, style, components, QA. Everything else in the repository is tooling to keep those five honest: schemas with count laws, a drift gate that fails on hand edits, contrast floors checked in CI, an em-dash sweep on derived prose, and twenty regression tests that each name the bug they prevent.

## Provenance and licensing

Code, schemas, and tooling are MIT. Content, prompts, and catalog text are CC BY 4.0. The five hero panels were generated for the launch and are BHIL originals. The reference pack images are third-party study material and are not covered by either license; see the pack README.

HELM is part of the BHIL framework family, alongside CADRE (the agent pattern it runs on), QUADRA, CIPHER, PRIMER, LOCUS, and FACET (which shares its evidence-tier vocabulary). Version history is in the [changelog](https://github.com/PolymathWizard/BHIL-HELM/blob/main/CHANGELOG.md).

## Who built it

Barry Hurd, Barry Hurd Intelligence Lab. GitHub: [PolymathWizard](https://github.com/PolymathWizard). Built with Claude as the build partner, human-directed at every gate.

*Human-Directed. AI-Enabled. Commercially Tested.*
