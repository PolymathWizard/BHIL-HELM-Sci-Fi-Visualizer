# SP-10: Terminal Gate

*Non-optional. Issue the SHIP / HOLD / REWORK disposition.*

## Goal

The gate is a checklist, not a judgment call. Failures on the first, third, and seventh checks are HOLD. Two or more failures on the rest are REWORK.

## Inputs

| Input | Form |
|---|---|
| SP-8 QA log | Complete |
| SP-6 artifact and scaffold | On disk |
| Appendix B | Withheld elements list |

## Procedure

Verify in order:

1. Every headline metric is VERIFIED or CORROBORATED, or the STATED / INFERENCE / UNCORROBORATED label is visible on screen.
2. The SP-8 QA log has no open critical findings.
3. The IP checklist passes on every item.
4. The artifact runs from a clean directory with only cdnjs dependencies.
5. The Claude Code scaffold regenerates the artifact.
6. Appendix B lists every element withheld and why.
7. No reader could mistake an ambient zone for signal.

Disposition rule: any failure on 1, 3, or 7 is HOLD. Two or more failures on 2, 4, 5, or 6 is REWORK. Otherwise SHIP.

## Output contract

- **Disposition**: SHIP / HOLD / REWORK with the failing check numbers
- **Release note**: version, language, reader, headline metric, evidence summary
- **Handoff checklist**: files delivered, commands available, first three things the client's Claude Code should run

## Gates

- The gate is run by `helm-qa`, never by the builder that produced the artifact.
- A HOLD returns to SP-3 or SP-8 as the failing check dictates. A REWORK returns to SP-6.

## Claude Code handoff

Subagent: `helm-qa` (see `.claude/agents/helm-qa.md`). Command: `/helm gate`. The subagent receives only the inputs listed above and returns only the output contract; it cannot write outside its declared paths.

---

*HELM. Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.*
