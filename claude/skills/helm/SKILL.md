---
name: helm
description: Build eye-catching, functional, Claude Code friendly interactive dashboards in science-fiction design languages from client data. Use whenever the user wants to "build a dashboard", "make this data look like mission control", "starship console for our KPIs", "HUD-style report", "cyberpunk or neon dashboard", "interactive mockup of our ops data", "executive command center", "sci-fi UI", or asks for a Claude Code dashboard scaffold. Runs the HELM ten-prompt stack (profile, intent, style, layout, components, build, motion, QA, snapshot, gate) with evidence tiers and an IP-clean original-design-only rule.
---

# HELM skill

HELM turns data into a decision surface styled in one of 15 original design languages. The dashboard serves a decision, not a mood. Style is selected after the data is profiled, never before.

## Invocation map

| User says | Run |
|---|---|
| "build a dashboard", "command center", "full HELM" | `prompts/00-master.md` end to end via the four subagents |
| "what does my data support", "profile this" | `prompts/sp-01-data-input-deconstruction.md` (helm-profiler) |
| "who is this for", "wall display" | `prompts/sp-02-narrative-intent-mapping.md` (helm-profiler) |
| "which style", "recommend a look", "make it feel like a bridge" | `prompts/sp-03-style-language-selector.md` (helm-stylist) |
| "restyle to X" | `/restyle <slug>` |
| "add a panel for X" | `/add-panel <zone> <field>` |
| "swap the data" | `/rebind <file>` |
| "is it ready", "check accessibility" | `prompts/sp-08-accessibility-fidelity-qa.md` (helm-qa) |
| "ship it" | `prompts/sp-10-terminal-gate.md` (helm-qa, fresh context) |
| "quick look for a prospect" | `prompts/sp-09-helm-snapshot.md` |

## Procedure for a full build

1. Confirm six intake values: client and REF, data sources, reader and decision, style intent, deployment target, constraints. Defaults: style "recommend", target standalone HTML, WCAG 2.1 AA.
2. Create `engagements/<REF>/`. Copy the source data in as `data/source.<ext>`.
3. Delegate SP-1 and SP-2 to `helm-profiler`. Wait for `register.json` validated against `data/schemas/register.schema.json`.
4. Delegate SP-3 and SP-4 to `helm-stylist` with the data shape and the Decision Map. If intent is "recommend", the stylist applies `data/canonical/matching.json`.
5. Delegate SP-5, SP-6, SP-7 to `helm-builder`. Builder starts from `templates/dashboard.template.html`, links `tokens/<slug>.css`, embeds the data, and writes `CLAUDE.md`, `REGENERATE.md`, and the client skill from `templates/`.
6. Delegate SP-8 then SP-10 to `helm-qa` in a fresh context. Builder output is never gated by the builder.
7. Present the brief in the master prompt's output format, then the artifact.
8. After each stage, ask whether to continue or refine.

## Hard rules

- Original design language only. Never write a franchise name, logo, wordmark, glyph system, licensed font, or fan-recreation font into any deliverable. If the user names a property, translate to the nearest catalog language and say so.
- Every rendered number has a Data Register field and an evidence class. STATED, INFERENCE, and UNCORROBORATED show their label on screen.
- Ambient elements carry `data-decorative="true"` and live in Stream only.
- No localStorage or sessionStorage. Dependencies from cdnjs only, pinned.
- Reduced motion turns off boot and ambient motion.
- Sonar-Surveillance is a grammar for system and network state, never for tracking people.
- No silent correction. Log it.

## Files this skill reads

- `data/canonical/catalog.json`, `matching.json`, `tropes.json`, `components.json`, `evidence_tiers.json`
- `tokens/<slug>.css`
- `templates/*`
- `prompts/*`

## Files this skill writes

Only under `engagements/<REF>/`. Never under `data/canonical/`, `tokens/`, or `docs/`.
