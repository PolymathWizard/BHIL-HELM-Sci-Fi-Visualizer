<!-- DERIVED copy of prompts/sp-04-information-architecture-layout-grid.md by tools/sync_prompts.py. Edit the source in prompts/. -->

# SP-04: Information Architecture & Layout Grid

*Place every data object in a zone with a priority, so the layout itself does the hierarchy work.*

## Goal

The layout is the first legend the reader gets. Zones, priority order, and the language's hierarchy device carry meaning before any label is read.

## Inputs

| Input | Form |
|---|---|
| SP-1 Data Register | Every field |
| SP-2 density budget and alert hierarchy | Per zone |
| SP-3 selected language | Hierarchy device |
| `[Constraints]` | Screen size and canvas |

## Procedure

1. Define the canvas: 16:9 wall, 16:10 laptop, 9:16 phone. Define the grid: 12 columns for laptop and wall, 4 columns for phone.
2. Name the zones: Prime (headline number or state), Support (3 to 5 secondary metrics), Context (trend, comparison), Stream (live log or ticker, ambient), Control (filters, time range), Status Rail (system health).
3. Assign each Data Register field to exactly one zone or to "not shown". Record why for every field not shown.
4. Specify the alert taxonomy: nominal / caution / critical plus optional offline. Give each a shape or label cue.
5. Specify the reading path: Z-pattern for wall, F-pattern for laptop. Priority order follows the path.
6. Define breakpoints and what collapses at each. The Prime zone never collapses below the fold.
7. Apply the language's hierarchy device as the zone boundary treatment (elbow frames, reticle focus, panel stacks, drafting lines).

## Output contract

- **Zone map** with field assignments and priority order
- **Reading path** diagram or description
- **Alert taxonomy** table: State | Color token | Shape or label cue | Trigger rule
- **Breakpoint table**: Breakpoint | Canvas | Columns | What collapses
- **Not-shown list** with reasons

## Gates

- Every Data Register field appears exactly once in the zone map or the not-shown list.
- No zone exceeds its SP-2 density budget.
- Ambient content lands in Stream only.

## Claude Code handoff

Subagent: `helm-stylist` (see `.claude/agents/helm-stylist.md`). Command: `/helm layout`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
