<!-- DERIVED copy of prompts/sp-09-helm-snapshot.md by tools/sync_prompts.py. Edit the source in prompts/. -->

# SP-09: HELM Snapshot

*Standalone paid diagnostic. One file, one screen, one language, one readout. The door-opener SKU.*

## Goal

Show a prospect what their data looks like as a command surface in a single session, and make the case for the full build honestly.

## Inputs

| Input | Form |
|---|---|
| One client file | CSV or spreadsheet, at most 2,000 rows |
| Prospect name and context | For the readout header |

## Procedure

1. Run SP-1 at summary depth. Pick one headline metric and three support metrics.
2. Select one language via the SP-3 matching table. Record the alternate but do not build it.
3. Build one 16:9 screen with Prime, Support, Context, and Status Rail zones only. No Stream, no Control.
4. Write the two-page readout: what the data can and cannot honestly show; the language chosen and why; the three trades made; what a full HELM build would add.
5. Deliver the screen as a single HTML file and the readout as a BHIL-branded document (use the `bhil-docx` skill).

## Output contract

- **One-screen dashboard** (`snapshot.html`)
- **HELM Snapshot Readout** (two pages, branded)
- **Upsell path**: Snapshot to Core Build, with the specific zones and commands the client gains

## Gates

- The screen carries the same evidence labels as a full build.
- The readout names at least one thing the data cannot support.
- No scaffold is shipped with a Snapshot; that is the Core Build differentiator.

## Claude Code handoff

Subagent: `helm-builder` (see `.claude/agents/helm-builder.md`). Command: `/helm snapshot data/prospect.csv`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
