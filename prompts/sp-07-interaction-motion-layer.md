# SP-07: Interaction & Motion Layer

*Add the motion that makes the language feel alive without paying more narrative tax than the reader can afford.*

## Goal

Motion is a language property. Boot, arrival, state change, and ambient each get one grammar, and reduced motion removes everything that is not a state change.

## Inputs

| Input | Form |
|---|---|
| SP-3 motion grammar and sound cue | From the lineage card |
| SP-5 component list | Which components are interactive |
| `[Constraints]` | Motion tolerance, sound in scope |

## Procedure

1. Specify interactions per component: hover (reveal secondary value), click (drill to detail panel), keyboard (tab order, arrow navigation within grids, escape closes), filter (time range, segment).
2. Specify motion in the language's grammar: boot sequence at or below 1.2 s and skippable; data-arrival transitions 200 to 400 ms; state changes immediate for critical, eased for nominal; ambient motion low amplitude only.
3. Implement `prefers-reduced-motion`: disable boot and ambient motion; keep state changes instant.
4. If sound is in scope: one distinct cue per system event, default off, mute control visible. Never reuse a cue across events.
5. Confirm every interactive element has a visible focus state using the accent token.

## Output contract

- **Interaction table**: Component | Hover | Click | Keyboard | Filter
- **Motion spec**: Event | Duration | Easing | Reduced-motion behavior
- **Reduced-motion fallback list**
- **Sound-cue map** (optional): Event | Cue | Default state

## Gates

- No motion exceeds the language's `--motion-boot` or `--motion-arrival` token.
- Critical state changes are never eased.
- Sound is opt-in.

## Claude Code handoff

Subagent: `helm-builder` (see `.claude/agents/helm-builder.md`). Command: `/helm motion`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
