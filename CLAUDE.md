# BHIL-HELM

HELM (Heuristic Engine for Layered Mockups) turns client data into eye-catching, functional, Claude Code friendly interactive dashboards styled in science-fiction design languages. This file is the standing brief for any Claude Code session in this repository.

## What this repo is

- A ten-prompt framework (`prompts/`) with a master prompt and SP-1 through SP-10.
- A canonical catalog of 15 original design languages (`data/canonical/catalog.json`) with generated token sets (`tokens/*.css`).
- A CADRE agent scaffold (`.claude/agents/`, `.claude/commands/`, `.claude/skills/helm/`) so the framework runs end to end from slash commands.
- A starter dashboard (`examples/helm-starter/`) bound to labeled SYNTHETIC data.
- Templates (`templates/`) that every client build inherits.

## Canonical source discipline

`data/canonical/*.json` is the single source of truth. `tokens/*.css`, `docs/catalog/*.md`, and `docs/reference/*.md` are derived. Never hand edit a derived file. Edit canonical, then run:

```
python3 tools/validate.py && python3 tools/build_tokens.py && python3 tools/build_docs.py && python3 tools/check_drift.py
```

CI fails on drift, on count-law violations (15 languages, 12 tropes, 5 tiers, 11 rules, 14 components), on contrast-floor violations without a logged exception, and on em dashes in derived prose.

## Operating rules for any session

1. Profile before styling. SP-1 always runs first on a new engagement.
2. One language per screen. Blends need an SP-3 rationale.
3. Original design language only. Never introduce franchise names, logos, wordmarks, glyph systems, or licensed or fan-recreation fonts into any file. Lineage fields are study references, not assets.
4. Every rendered number traces to a Data Register field and carries an evidence class. STATED, INFERENCE, and UNCORROBORATED render their label on screen.
5. Ambient content carries `data-decorative="true"` and lives in the Stream zone only.
6. No browser storage in artifacts. CDN dependencies from cdnjs only, pinned.
7. No silent correction. Findings go in the QA log even when fixed.
8. No em dashes in any prose this repo ships.

## Standing commands

| Command | What it does |
|---|---|
| `/helm brief` | Run the master prompt end to end on an engagement |
| `/helm profile <file>` | SP-1 only; writes `engagements/<ref>/register.json` |
| `/helm style <language\|recommend>` | SP-3; lineage card and Narrative Tax Register |
| `/helm build --target html\|jsx` | SP-6; artifact plus scaffold |
| `/helm qa <artifact>` | SP-8; contrast, fidelity, keyboard, IP |
| `/helm gate` | SP-10; SHIP / HOLD / REWORK |
| `/rebind <file>` | Swap data file, preserve layout, re-run fidelity |
| `/restyle <language>` | Swap token set, preserve bindings, re-run contrast |
| `/add-panel <zone> <field>` | Insert a component respecting the density budget |
| `/snapshot <file>` | SP-9 door-opener: one screen, two-page readout |

## Agents (CADRE pattern)

Orchestrator: the session model. Subagents in `.claude/agents/` each own a slice and are tool-restricted:

| Agent | Owns | May write |
|---|---|---|
| `helm-profiler` | SP-1, SP-2 | `engagements/<ref>/register.json`, `engagements/<ref>/decision-map.md` |
| `helm-stylist` | SP-3, SP-4 | `engagements/<ref>/style.md`, `engagements/<ref>/zones.md`, token overrides |
| `helm-builder` | SP-5, SP-6, SP-7, SP-9 | `engagements/<ref>/dashboard.*`, scaffold files |
| `helm-qa` | SP-8, SP-10 | `engagements/<ref>/qa-log.md`, `engagements/<ref>/disposition.md` |

`helm-qa` never runs in the same context that built the artifact. The gate must be issued by a fresh subagent.

## Engagements

`engagements/` is gitignored except `.gitkeep`. Each engagement lives in `engagements/<REF>/` and is never committed to this repo.

## Quality gate before any commit

```
python3 tools/validate.py
python3 tools/check_drift.py
python3 tools/em_dash_sweep.py
python3 -m pytest -q tests/
mkdocs build --strict
```

## Conventions inherited from BHIL

Dual licensing (MIT code and schemas, CC BY 4.0 content). Conventional commits scoped `helm:`. MkDocs Material with IBM Plex Sans and Mono. Brand tokens: COBALT `#1B4FD8`, NAVY `#1C1C2E`, ACCENT `#6B9EFF`. The BHIL brand tokens style this repository's documentation site; they are not a HELM dashboard language.

*Human-Directed. AI-Enabled. Commercially Tested.*
