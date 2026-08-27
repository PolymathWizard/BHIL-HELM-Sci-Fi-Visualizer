# The prompt system

Eleven prompts. The master runs all ten stages in one pass; each supporting prompt deepens one stage. Every prompt file in `prompts/` has the same shape: goal, inputs, procedure, output contract, gates, Claude Code handoff.

| Prompt | Name | Stage | Agent |
|---|---|---|---|
| [Master](00-master.md) | HELM Dashboard Brief and Mockup | All | Orchestrator |
| [SP-1](sp-01-data-input-deconstruction.md) | Data and Input Deconstruction | Profile | helm-profiler |
| [SP-2](sp-02-narrative-intent-mapping.md) | Narrative Intent Mapping | Intent | helm-profiler |
| [SP-3](sp-03-style-language-selector.md) | Style Language Selector | Style | helm-stylist |
| [SP-4](sp-04-information-architecture-layout-grid.md) | Information Architecture and Layout Grid | Layout | helm-stylist |
| [SP-5](sp-05-component-library-spec.md) | Component Library Spec | Components | helm-builder |
| [SP-6](sp-06-functional-mockup-build.md) | Functional Mockup Build | Build | helm-builder |
| [SP-7](sp-07-interaction-motion-layer.md) | Interaction and Motion Layer | Motion | helm-builder |
| [SP-8](sp-08-accessibility-fidelity-qa.md) | Accessibility and Fidelity QA | QA | helm-qa |
| [SP-9](sp-09-helm-snapshot.md) | HELM Snapshot | Door-opener | helm-builder |
| [SP-10](sp-10-terminal-gate.md) | Terminal Gate | Gate | helm-qa |

## How prompts feed each other

```
DATA SOURCES
    │
    ▼
SP-1 Data Register ──► data shape
    │
    ▼
SP-2 Decision Map ──► density budget, alert hierarchy
    │
    ▼
SP-3 Language + Narrative Tax ──► lineage card, tokens
    │
    ▼
SP-4 Zone map ──► SP-5 Component contract
                        │
                        ▼
                  SP-6 Artifact + scaffold ──► SP-7 Motion
                                                  │
                                                  ▼
                                            SP-8 QA log
                                                  │
                                                  ▼
                                            SP-10 SHIP / HOLD / REWORK

SP-9 Snapshot runs SP-1 (summary), SP-3, and a reduced SP-6 on its own.
```

## Intake variables

| Variable | Description |
|---|---|
| `[Client / Engagement]` | Who the dashboard is for and the REF code |
| `[Data Sources]` | Files, APIs, or a narrative of what exists |
| `[Reader and Decision]` | Who looks, in what setting, and what they decide |
| `[Style Intent]` | A catalog language, a mood, or "recommend" |
| `[Deployment Target]` | Artifact preview, standalone HTML, React in a repo, or Claude Code scaffold |
| `[Constraints]` | Brand colors that must survive, accessibility level, motion tolerance, screen size |

## Tips for best results

- **Profile before styling.** Half of failed sci-fi dashboards are styled around data that could never support the drama.
- **One language per screen.** Blending takes palette and type from one and hierarchy device from the other, never motion from both.
- **The wall test.** At three meters the Prime zone holds one number and one state.
- **Ambient is honest ambient.** A ticker is fine if it scrolls real events. Mark it decorative if it does not.
- **Ship the scaffold.** A dashboard the client cannot regenerate is a screenshot.
- **Study the source, ship the grammar.** Analysts watch the lineage; builders never open a franchise screenshot next to the editor.
