<!-- DERIVED copy of prompts/sp-08-accessibility-fidelity-qa.md by tools/sync_prompts.py. Edit the source in prompts/. -->

# SP-08: Accessibility & Fidelity QA

*Prove the dashboard is readable, truthful, and clean before it leaves the lab.*

## Goal

Log every finding with severity. No silent fixes. A fixed finding still appears in the log with its resolution.

## Inputs

| Input | Form |
|---|---|
| SP-6 artifact | The file under test |
| SP-1 Data Register | Source of truth for every rendered value |
| SP-5 tokens | Every text and background pair |
| IP checklist | Below |

## Procedure

1. Contrast: run `python3 tools/contrast.py <slug>` and test every text/background pair the artifact actually uses against WCAG 2.1 AA (4.5:1 body, 3:1 large text and UI components). Record ratios. Any pair below floor is a finding; fix or log an exception with client approval.
2. Fidelity: spot-check a minimum of ten rendered values and every headline metric against the Data Register. Record expected, rendered, and match.
3. Alert states: confirm each is distinguishable without color (shape, label, or position).
4. Keyboard: tab through every interactive element; confirm order, focus visibility, escape behavior.
5. Reduced motion: emulate and confirm boot and ambient motion are off.
6. IP checklist: no franchise names; no logos; no licensed or fan-recreation fonts; no glyph systems from any property; no frames traceable to a specific screen; no reference numbers without meaning.
7. Decorative audit: every `data-decorative` element is in the Stream zone and visually subordinate.

## Output contract

- **QA Log**: Check | Result | Severity (critical / major / minor) | Action | Status
- **Contrast matrix**: Pair | Ratio | Floor | Result
- **Fidelity spot-check**: Field | Expected | Rendered | Match
- **IP checklist**: Item | Pass/Fail | Note
- **Exceptions register**: any approved sub-floor pair with approver and date

## Gates

- Zero open critical findings before SP-10.
- Every headline metric appears in the fidelity table.
- Every IP item is a pass.

## Claude Code handoff

Subagent: `helm-qa` (see `.claude/agents/helm-qa.md`). Command: `/helm qa dashboard.html`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
