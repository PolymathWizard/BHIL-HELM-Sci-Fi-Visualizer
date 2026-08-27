---
description: Run HELM (brief | profile | intent | style | layout | components | build | motion | qa | snapshot | gate)
argument-hint: <stage> [options]
---
Load `.claude/skills/helm/SKILL.md` and run stage `$ARGUMENTS`.

Stage to prompt and agent map:
- brief: prompts/00-master.md, orchestrate all four agents in order (profiler, stylist, builder, qa)
- profile, intent: helm-profiler
- style, layout: helm-stylist
- components, build, motion, snapshot: helm-builder
- qa, gate: helm-qa in a fresh subagent context

Confirm the six intake values if this is a new engagement. Work only inside `engagements/<REF>/`. After the stage completes, ask whether to continue to the next stage or refine this one.
