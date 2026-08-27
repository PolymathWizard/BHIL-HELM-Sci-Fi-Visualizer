# Regeneration prompt

Paste into Claude Code from this directory to rebuild `dashboard.html` from the register and tokens.

```
Rebuild dashboard.html as a single-file HTML artifact.
Language: tactical-hud. Link tokens/tactical-hud.css. Use only CSS custom properties from that file for color, type, radius, glow, and motion.
Reader: operations director on a wall display, 3 to 5 seconds. Purpose sentence: the screen exists so that the ops director can decide whether to reallocate carriers before the 14:00 cutoff.
Data: embed data/source.json as the constant HELM_DATA. Bind every rendered number with data-field and data-evidence attributes matching data/register.json. Render the evidence label inside any component whose tier is STATED, INFERENCE, or UNCORROBORATED.
Zones: Prime holds a Ring Gauge for on_time_rate with the STATED target as a tick mark. Support holds four Headline Metrics with Sparklines for orders_in_flight, carrier_capacity, avg_dock_wait, exceptions_open. Context holds a Trend Chart of on_time_rate_daily with a 7d/14d/30d Filter Rail. Status Rail holds five Status Pills for hub_state, each distinguishable by shape as well as color. Stream holds an Ambient Ticker marked data-decorative="true".
One renderState(state) function re-renders everything.
Motion: boot sequence at or below --motion-boot, skippable, off under prefers-reduced-motion; arrivals at --motion-arrival; critical state changes immediate.
Dependencies: Chart.js 4.4.1 from cdnjs, pinned. Inline SVG fallback if Chart is undefined, with a console warning. No localStorage or sessionStorage. No other external calls.
Accessibility: visible focus states, keyboard reachable filter and metrics, escape clears focus, aria labels on zones.
Header shows a SYNTHETIC DATA badge because every row is generated.
```
