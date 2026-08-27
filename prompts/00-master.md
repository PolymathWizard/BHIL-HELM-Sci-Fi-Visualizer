# Master Prompt: HELM Dashboard Brief and Mockup

*Prompt Zero for the HELM stack. Generates a complete first-pass HELM Dashboard Brief and a working single-file mockup in one pass. The ten supporting prompts deepen, restyle, and harden each layer.*

## Prompt metadata

| Field | Detail |
|---|---|
| Framework | HELM (Heuristic Engine for Layered Mockups) |
| Writing type | Design brief plus functional artifact plus agent scaffold |
| Purpose | Turn client data and inputs into an eye-catching, functional, Claude Code friendly interactive dashboard styled in a science-fiction design language, without paying more narrative tax than the reader can afford |
| Target audience | Fractional CDOs, intelligence analysts, product and ops leaders, and the Claude Code instance that will own the artifact afterward |
| Tone | Precise, production-ready, cinematic where it serves the decision |
| Key variables | `[Client / Engagement]`, `[Data Sources]`, `[Reader and Decision]`, `[Style Intent]`, `[Deployment Target]`, `[Constraints]` |

## Operating principles (non-negotiable)

1. **The dashboard serves a decision, not a mood.** Name the reader, the seconds they have, and the decision the screen must move. Style is selected after that, never before.
2. **Lineage, not reproduction.** Carry the feel through abstracted grammar. No franchise names, logos, wordmarks, glyph systems, licensed fonts, or copied frames appear in any deliverable. The output must not be recognizable as a specific protected work.
3. **Pay the narrative tax knowingly.** Every trope trades usability for storytelling. Make each trade explicit in the Narrative Tax Register and dial density, transparency, and motion back to what the reader can use.
4. **Real data or labeled placeholders.** Bind to client data or to clearly flagged SYNTHETIC rows. Decorative noise lives only in zones marked `data-decorative="true"`.
5. **Claude Code is the deployment target.** Ship a single-file artifact plus `CLAUDE.md`, a skill file, and a regeneration prompt so the client's own Claude Code instance can extend, restyle, and re-bind without HELM in the loop.
6. **Evidence classification is non-optional.** Every rendered data claim and every lineage claim carries VERIFIED / CORROBORATED / UNCORROBORATED / INFERENCE / STATED. Client KPIs and targets enter as STATED until reconciled.
7. **No silent correction.** Gaps, contradictions, contrast failures, and withheld IP elements surface in the QA log.

## Intake (confirm all six before building)

| Variable | Ask for | Default if unstated |
|---|---|---|
| `[Client / Engagement]` | Who the dashboard is for and the REF code | Required |
| `[Data Sources]` | CSV, JSON, spreadsheet, database extract, or a narrative of what exists | Required; narrative only triggers SYNTHETIC mode |
| `[Reader and Decision]` | Who looks, in what setting, deciding what | Required |
| `[Style Intent]` | A catalog language, a mood, or "recommend" | "recommend" |
| `[Deployment Target]` | Claude artifact preview / standalone HTML / React in an existing repo / Claude Code project scaffold | standalone HTML |
| `[Constraints]` | Brand colors that must survive, accessibility level, motion tolerance, screen size | WCAG 2.1 AA, motion tolerant, 16:10 laptop |

## Procedure

1. Confirm intake. If `[Data Sources]` is narrative only, announce SYNTHETIC mode and state assumptions before any row is generated.
2. Run SP-1 at full depth. Produce the Data Register before any style discussion.
3. Run SP-2. Fix the reader, the seconds, the decision, the density budget, and the alert hierarchy.
4. Run SP-3. If `[Style Intent]` is "recommend", apply the matching table to the SP-1 data shape and propose two candidates with rationale. Produce the lineage card and the Narrative Tax Register. Map any mandatory brand colors into the language's accent role and log the contrast implications.
5. Run SP-4 and SP-5. Zone map, hierarchy spec, tokens, component contract.
6. Run SP-6. Build the artifact and the Claude Code scaffold. CDN-only dependencies from cdnjs, no browser storage, no external asset calls, data embedded as a JSON constant or loaded from a clearly named local file, every rendered number traceable to a Data Register field, a single `renderState()` function.
7. Run SP-7. Interaction and motion within the language's grammar; `prefers-reduced-motion` honored.
8. Run SP-8. Contrast matrix, fidelity spot-check, keyboard test, IP checklist. Log every finding.
9. Run SP-10. Issue SHIP / HOLD / REWORK.
10. After each prompt, ask whether to continue or refine. Carry forward the artifacts listed in the handoff table.

## Output format

---

**[Client] HELM Dashboard Brief**
*Version 1.0 | Draft | [Date] | Style: [Language] | Target: [Deployment] | REF [code]*

**1. Executive Read**
One paragraph: the reader, the decision, the seconds available, the selected style and why it fits the data shape, the three most consequential design trades made, and the disposition.

**2. Data Register**

| Field | Type | Source | Quality | Role (KPI / dimension / context) | Evidence class |
|---|---|---|---|---|---|

**3. Decision Map**

| Reader | Setting | Seconds to first read | Decision supported | Primary metric | Density budget |
|---|---|---|---|---|---|

**4. Style Language Selection**
Lineage card for the selected language plus the Narrative Tax Register:

| Trope carried | Usability cost | Narrative benefit | HELM setting (keep / dial back / remove) |
|---|---|---|---|

**5. Zone Map and Hierarchy**
Named zones with priority order, alert taxonomy, breakpoints, reading path.

**6. Component Contract and Tokens**
Design tokens (color, type, spacing, motion) and the component list with props.

**7. Built Artifact**
Filename, dependencies with pinned CDN versions, data-binding method, regeneration prompt.

**8. Claude Code Scaffold**
`CLAUDE.md`, skill file, and the three standing commands (rebind, restyle, add-panel).

**9. QA Log**
Contrast results per token pair, data-to-render checks, motion fallback, IP cleanliness.

**10. Disposition**
SHIP / HOLD / REWORK with reasons.

**Appendix A** Evidence Register · **Appendix B** Withheld Elements (IP) · **Appendix C** Regeneration Prompt

---

## Handoff table (what each prompt carries forward)

| From | Carries forward |
|---|---|
| SP-1 | Data Register (fields, types, quality, KPIs, hierarchy, evidence class) and data shape |
| SP-2 | Decision Map and density budget |
| SP-3 | Selected language, lineage card, Narrative Tax Register |
| SP-4 | Zone map and hierarchy spec |
| SP-5 | Component contract and design tokens |
| SP-6 | Built artifact plus Claude Code scaffold |
| SP-7 | Interaction and motion spec |
| SP-8 | QA log (accessibility, fidelity, IP) |
| SP-9 | HELM Snapshot (standalone door-opener) |
| SP-10 | SHIP / HOLD / REWORK disposition |

## Gates the master pass must clear

- Every headline metric is VERIFIED or CORROBORATED, or its class label is visible on screen.
- No open critical QA findings.
- IP checklist passes on every item.
- Artifact runs from a clean directory with only cdnjs dependencies.
- The scaffold regenerates the artifact.
- Appendix B lists every element withheld and why.
- No reader could mistake an ambient zone for signal.

## Claude Code invocation

```
/helm brief --client "[Client]" --data data/source.json --reader "[reader]" --style recommend --target html
```

The `helm` skill in `.claude/skills/helm/SKILL.md` maps this command to the procedure above and delegates SP-1 through SP-8 to the CADRE subagents in `.claude/agents/`.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
