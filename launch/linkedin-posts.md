# LinkedIn post variants

## Variant 1: technical authority

A film HUD has one second of screen time to read as complex and clear. That is the tightest communication-design brief in existence, and it is exactly what an executive dashboard needs.

I built HELM to carry that discipline into real data without carrying the tropes that make screen UIs unusable.

What ships:

- Ten prompts: profile the data before styling, fix the reader and the seconds, match a design language to the data shape, lay out zones with density budgets, build a single-file artifact, run accessibility and fidelity QA, gate it SHIP/HOLD/REWORK.
- 15 original design languages with documented lineage and generated token sets. Drift-gated against canonical JSON.
- A Narrative Tax Register: every sci-fi trope named with its usability cost and a default setting. Glow never touches text. Transparency caps at 15 percent. Boot sequences stay under 1.2 seconds and are skippable.
- Five-tier evidence classes on every rendered number. Client targets are STATED until reconciled, and the label renders on screen.
- A Claude Code scaffold with four tool-restricted subagents. The builder never gates its own output.

Nothing in it is recognizable as a specific franchise screen. The test suite greps for property names and fails the build if one appears.

Repo: github.com/PolymathWizard/BHIL-HELM

Human-Directed. AI-Enabled. Commercially Tested.

## Variant 2: inquiry-driving

Your ops dashboard is probably readable. Is it decidable?

Most dashboards answer "what is happening." Very few are built so that one specific reader, standing three meters from a wall, can make one specific decision in five seconds.

Science fiction solved that problem decades ago, for audiences. HELM is my framework for solving it for operators, with the data honesty a real business needs.

It starts with a question I ask every client: what decision does this screen exist to move? If the answer is "it shows our KPIs," we have work to do before anyone picks a look.

The door-opener is a HELM Snapshot: one file, one screen, one design language, and a two-page readout on what your data can and cannot honestly show.

If your team has data and no decision surface, I would like to see the file.

github.com/PolymathWizard/BHIL-HELM

Human-Directed. AI-Enabled. Commercially Tested.

## Variant 3: peer and builder ship post

Shipped: BHIL-HELM.

Sci-fi design-language dashboards, Claude Code native, built the way the rest of the BHIL family is built.

- Canonical JSON generates 15 CSS token sets and every catalog page; CI fails on drift.
- Count laws in the schema: exactly 15 languages, 12 tropes, 5 evidence tiers, 11 matching rules, 14 components. Changing one is a decision, not an accident.
- Stdlib-only validators including a WCAG contrast gate on every token pair.
- CADRE agents with per-agent tool grants: profiler cannot style, stylist cannot build, builder cannot gate, QA can only write the log.
- A starter dashboard that opens from file://, renders an inline SVG fallback if the CDN is down, and honors prefers-reduced-motion.
- 19 regression tests, each named for the bug it prevents.

MIT for code and tokens, CC BY 4.0 for prose. Fork it, restyle it, tell me what breaks.

github.com/PolymathWizard/BHIL-HELM

Human-Directed. AI-Enabled. Commercially Tested.
