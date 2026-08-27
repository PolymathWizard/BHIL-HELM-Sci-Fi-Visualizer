# SP-02: Narrative Intent Mapping

*Fix the reader, the seconds, and the decision before a single pixel is styled.*

## Goal

A hero screen in a film has roughly one second to land. An executive glance has three to five. Set the density budget the reader can afford, not the density the style can carry.

## Inputs

| Input | Form |
|---|---|
| `[Reader and Decision]` | Every reader class and their setting |
| SP-1 Data Register | Fields and candidate headlines |
| Zone table | `data/canonical/components.json` zones with density budgets |

## Procedure

1. Name every reader class: executive, operator, investor, board, floor, analyst.
2. For each: setting (wall at 3 meters, laptop at arm's length, phone), seconds to first read, decision supported, and what wrong looks like if they misread.
3. Set the density budget per zone from the setting: executive wall 3 to 5 objects in Prime plus Support; operator console 12 to 20; analyst workbench 20 plus.
4. State the alert hierarchy the reader must decode without a legend. Three states maximum for wall displays. Every state must be distinguishable without color alone.
5. Select the primary reader if more than one exists. The screen is built for the primary; secondary readers get a documented compromise.
6. Write the one-sentence purpose: the screen exists so that [reader] can [decide] in [seconds].

## Output contract

- **Decision Map** table: Reader | Setting | Seconds to first read | Decision supported | Primary metric | Density budget
- **Density budget per zone** for the primary reader
- **Alert hierarchy**: states, the non-color cue for each, and the threshold rule per headline metric
- **Purpose sentence**
- **Reader conflicts** and the compromise chosen

## Gates

- A wall display Prime zone holds one number and one state. Everything else is Support.
- No alert state is defined by color alone.
- The purpose sentence names a decision, not a topic.

## Claude Code handoff

Subagent: `helm-profiler` (see `.claude/agents/helm-profiler.md`). Command: `/helm intent`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
