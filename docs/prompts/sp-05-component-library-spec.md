<!-- DERIVED copy of prompts/sp-05-component-library-spec.md by tools/sync_prompts.py. Edit the source in prompts/. -->

# SP-05: Component Library Spec

*Define the tokens and components once, so every panel is consistent and the client can add panels later.*

## Goal

Tokens are the contract between the style and the build. Components are the contract between the build and every future add-panel command.

## Inputs

| Input | Form |
|---|---|
| SP-3 selected language | Token set from `tokens/<slug>.css` |
| SP-4 zone map | Which components each zone needs |
| Component contract | `data/canonical/components.json` |

## Procedure

1. Emit design tokens as CSS custom properties from the language token file: background layers (void, panel, panel-raised), text (primary, secondary, muted), accent (primary, secondary), state colors (nominal, caution, critical, offline), type stack (display, body, mono), spacing scale, radius, border weights, glow, motion durations and easings.
2. Apply brand-color overrides from SP-3 as token overrides, never as inline values.
3. Select the components the zone map requires from the fourteen in the contract. For each: purpose, required data shape, props, states, and the language-specific treatment.
4. Mark decorative-only components. Ambient Ticker is always decorative and always carries `data-decorative="true"`.
5. Specify the Headline Metric evidence badge: the class label renders inside the component for any tier that requires an on-screen label.
6. Write the `renderState()` contract: one function, one state object, every component re-renders from it.

## Output contract

- **tokens.css** block (or reference to the generated token file plus overrides)
- **Component contract table**: Component | Zone | Data shape | Props | States | Language treatment
- **Decorative-only note**
- **renderState() signature** and the state object schema

## Gates

- No hex value appears outside the token block.
- Every component that renders a number has an `evidence` prop.
- Radius, glow, and border weight come from the language, not the component.

## Claude Code handoff

Subagent: `helm-builder` (see `.claude/agents/helm-builder.md`). Command: `/helm components`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
