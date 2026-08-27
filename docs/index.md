# HELM

**Heuristic Engine for Layered Mockups.** A ten-prompt framework for turning client data into eye-catching, functional, Claude Code friendly interactive dashboards styled in science-fiction design languages.

HELM exists because fictional user interfaces are the most effective communication design under time compression ever produced. A film screen has one second to read as complex and clear. Stripped of the tropes that make screen UIs anti-usable in real products, that discipline is exactly what an executive dashboard needs.

![HELM starter render](assets/helm-starter.png)

## What ships in this repository

| Layer | Where | What it does |
|---|---|---|
| Ten-prompt system | `prompts/` | Master prompt plus SP-1 through SP-10: profile, intent, style, layout, components, build, motion, QA, snapshot, gate |
| Catalog of 15 languages | `data/canonical/catalog.json` | Original design languages with documented lineage, token sets, motion grammar |
| Generated tokens | `tokens/*.css` | One CSS custom-property file per language, drift-gated against canonical |
| Agent scaffold | `.claude/` | CADRE pattern: four tool-restricted subagents, six slash commands, one skill |
| Starter build | `examples/helm-starter/` | A Tactical HUD dashboard on labeled SYNTHETIC data with its own Claude Code scaffold |
| Templates | `templates/` | What every client build inherits |
| Validators | `tools/` | Schema, count laws, cross-references, contrast floors, drift, em-dash sweep |

## The three things HELM refuses to do

1. **Reproduce a protected work.** Lineage is a study reference. The build uses abstracted grammar only. Nothing shipped is recognizable as a specific franchise screen.
2. **Fabricate data to fill a zone.** Empty is honest. Synthetic is labeled. Ambient is marked decorative.
3. **Ship a dashboard the client cannot regenerate.** Every build carries `CLAUDE.md`, a skill, and a regeneration prompt.

## Start here

New to the framework? Read [About HELM](about.md) first.

- New to the framework: [Getting started](guide/getting-started.md)
- Picking a look: [The HELM Catalog](catalog/index.md) and [Matching logic](reference/matching-logic.md)
- Running it in Claude Code: [Claude Code integration](claude-code/index.md)
- Understanding the trade-offs: [Narrative Tax Register](reference/narrative-tax.md)
- Selling it: [Commercial architecture](guide/commercial.md)

*Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
