# Operating principles

Seven rules every HELM build obeys. They are restated in `CLAUDE.md`, the skill file, and each subagent, so a session cannot drift away from them.

## 1. The dashboard serves a decision, not a mood

Every build starts with the reader, the seconds they have, and the decision the screen must move. Style is selected after that, never before. SP-1 and SP-2 run before SP-3 without exception.

## 2. Lineage, not reproduction

The catalog records what each fictional interface did (palette relationships, hierarchy, motion, sound) so the build can carry the feel. No franchise names, logos, wordmarks, glyph systems, licensed fonts, or copied frames appear in any deliverable. The test suite greps shipped files for property names and fails the build if one appears.

## 3. Pay the narrative tax knowingly

Every sci-fi trope trades usability for storytelling. HELM makes each trade explicit in the [Narrative Tax Register](../reference/narrative-tax.md) and dials density, transparency, and motion back to what the reader can use.

## 4. Real data or labeled placeholders

A mockup binds to client data or to rows marked SYNTHETIC. Decorative noise lives only in zones marked `data-decorative="true"` and never where a reader would mistake it for signal.

## 5. Claude Code is the deployment target

Every build ships a single-file artifact plus `CLAUDE.md`, a skill, and a regeneration prompt so the client's own Claude Code can extend, restyle, and re-bind without HELM in the loop.

## 6. Evidence classification is non-optional

Every rendered data claim and every lineage claim carries one of five tiers. Client KPIs and targets enter as STATED until reconciled. Typeface attributions from fan sources enter as UNCORROBORATED. See [Evidence tiers](../reference/evidence-tiers.md).

## 7. No silent correction

Gaps, contradictions, contrast failures, and withheld IP elements surface in the QA log, never quietly fixed. A fixed finding still appears with its resolution.

## Two design lessons that shaped the framework

**Explicit beats derived.** Thresholds, zone assignments, and evidence classes are stated in the register, not inferred at render time. Inference from limited data produced false findings in earlier BHIL builds.

**Defaults require counterweights.** Suppressing glow pushes a build toward density; suppressing density pushes it toward motion. The Narrative Tax Register sets a default on all twelve tropes at once so no single suppression reaches for another.
