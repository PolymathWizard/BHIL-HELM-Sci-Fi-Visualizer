<!-- DERIVED copy of prompts/sp-06-functional-mockup-build.md by tools/sync_prompts.py. Edit the source in prompts/. -->

# SP-06: Functional Mockup Build

*Ship a working single-file dashboard bound to real data, plus the scaffold that lets the client's Claude Code instance own it.*

## Goal

A dashboard the client cannot regenerate in Claude Code is a screenshot, not a deliverable.

## Inputs

| Input | Form |
|---|---|
| SP-1 Data Register and data file | `data/<source>.json` |
| SP-4 zone map | Zones and priorities |
| SP-5 tokens and component contract | Token file and component list |
| `[Deployment Target]` | html / jsx / artifact / scaffold |
| Template | `templates/dashboard.template.html` or `.jsx` |

## Procedure

1. Build a single `.html` (vanilla plus Chart.js or D3 from cdnjs) or a single `.jsx` (React plus Recharts, Tailwind core classes only) per target.
2. Rules: no localStorage or sessionStorage; no external image or font hotlinks beyond cdnjs; data embedded as a JSON constant or loaded from a clearly named local file; every rendered number traceable to a Data Register field; ambient zones marked `data-decorative="true"`; one `renderState()` function.
3. Include a boot sequence at or below 1.2 s, skippable, disabled under `prefers-reduced-motion`.
4. Write `CLAUDE.md` from `templates/CLAUDE.md.template`: purpose, data schema, token file location, component list, the three standing commands, and the IP rule.
5. Write `.claude/skills/helm-dashboard/SKILL.md` so the client can invoke restyle and add-panel.
6. Write `REGENERATE.md`: the exact prompt that rebuilds the artifact from the Data Register and tokens.
7. Pin every CDN dependency by version.
8. Run the artifact from a clean directory and confirm it renders with no console errors.

## Output contract

- **Artifact file** (`dashboard.html` or `dashboard.jsx`)
- **Scaffold files**: `CLAUDE.md`, `.claude/skills/helm-dashboard/SKILL.md`, `REGENERATE.md`
- **Dependency list** with pinned cdnjs versions
- **How to run in Claude Code**: five lines or fewer

## Gates

- The artifact opens from `file://` with no build step.
- `grep -c data-decorative` equals the number of ambient components in SP-5.
- The regeneration prompt reproduces a structurally identical artifact.

## Claude Code handoff

Subagent: `helm-builder` (see `.claude/agents/helm-builder.md`). Command: `/helm build --target html`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
