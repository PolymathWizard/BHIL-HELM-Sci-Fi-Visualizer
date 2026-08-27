# Claude Code integration

HELM treats Claude Code as the deployment target. Two scaffolds exist: the framework scaffold in this repository, and the client scaffold every build ships.

## Framework scaffold (this repo)

```
.claude/
├── settings.json              permissions: ask before writing canonical, tokens, or derived docs
├── skills/helm/SKILL.md       invocation map, procedure, hard rules
├── agents/
│   ├── helm-profiler.md       SP-1, SP-2
│   ├── helm-stylist.md        SP-3, SP-4
│   ├── helm-builder.md        SP-5, SP-6, SP-7, SP-9
│   └── helm-qa.md             SP-8, SP-10 (fresh context only)
└── commands/
    ├── helm.md                /helm <stage>
    ├── rebind.md              /rebind <file>
    ├── restyle.md             /restyle <language>
    ├── add-panel.md           /add-panel <zone> <field>
    ├── snapshot.md            /snapshot <file>
    └── gate.md                /gate
```

`CLAUDE.md` at the root is the standing brief. It states the canonical-source discipline, the seven operating rules, the command table, and the agent table.

## CADRE pattern

The session model orchestrates. Four subagents each own a slice of the stack and are tool-restricted at the frontmatter level: the profiler cannot style, the stylist cannot build, the builder cannot gate its own output, and QA can only write the log and the disposition. Each agent's `tools:` line is the runtime enforcement.

## Client scaffold (every build)

```
engagements/<REF>/
├── CLAUDE.md                  purpose, schema, tokens, commands, IP rule
├── REGENERATE.md              exact rebuild prompt
├── data/
│   ├── source.json            embedded or referenced; SYNTHETIC flag if applicable
│   └── register.json          SP-1 output
├── tokens/<language>.css      one file
├── dashboard.html             single-file artifact (or dashboard.jsx)
└── .claude/skills/helm-dashboard/SKILL.md
```

`examples/helm-starter/` is a complete instance of this layout.

## Why the builder never gates

The SP-10 disposition is issued by `helm-qa` in a context that did not produce the artifact. A builder judging its own output collapses the fidelity check into the thing being checked. `/gate` spawns a fresh subagent by design.
