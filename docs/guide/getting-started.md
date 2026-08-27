# Getting started

## Prerequisites

- Python 3.10 or later (stdlib only for every tool)
- Claude Code, for the agent scaffold
- A browser, for the artifact

No package installs are required to run the validators or the starter dashboard.

## Five-minute tour

```
git clone https://github.com/PolymathWizard/BHIL-HELM
cd BHIL-HELM
python3 tools/validate.py          # canonical data passes its laws
python3 tools/contrast.py tactical-hud
open examples/helm-starter/dashboard.html
```

The starter renders a fulfillment-network decision surface in the Tactical HUD language on labeled SYNTHETIC data. Hover a Support metric for its secondary value, tab through the controls, switch the trailing window, and emulate reduced motion to watch the boot and ambient motion switch off.

## Running a build

Open Claude Code at the repository root and run:

```
/helm brief
```

The skill confirms six intake values (client and REF, data sources, reader and decision, style intent, deployment target, constraints), creates `engagements/<REF>/`, and delegates in order to `helm-profiler`, `helm-stylist`, `helm-builder`, and `helm-qa`. After each stage it asks whether to continue or refine.

The engagement directory is gitignored. The output is a brief in the master prompt's format plus a single-file artifact and its scaffold.

## Running one stage

| Command | Stage |
|---|---|
| `/helm profile data/source.csv` | SP-1 Data Register |
| `/helm style recommend` | SP-3 language selection |
| `/helm build --target html` | SP-6 artifact plus scaffold |
| `/helm qa dashboard.html` | SP-8 QA log |
| `/gate` | SP-10 disposition, fresh context |

## Maintaining a shipped dashboard

Inside the engagement directory the client's Claude Code has its own skill with three standing commands: `/rebind <file>`, `/restyle <language>`, `/add-panel <zone> <field>`. See [Standing commands](../claude-code/commands.md).

## Editing the catalog

`data/canonical/` is the source of truth. Edit there, then:

```
python3 tools/validate.py
python3 tools/build_tokens.py
python3 tools/build_docs.py
python3 tools/check_drift.py
```

CI runs the same sequence and fails on drift.
