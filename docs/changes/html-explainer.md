# html-explainer: Static charts by default

The animation guidance introduced in PR #5 is being rolled back after user feedback.

Keep charts and flowcharts static unless the user explicitly asks for animation. Controls may update values immediately. Remove the separate animation reference while retaining chart labels, layout guidance, dark-theme support, and accessibility checks.

## Original research

- [Nico Bailon visual-explainer](https://github.com/nicobailon/visual-explainer/blob/main/plugins/visual-explainer/SKILL.md): figure-first explanations, named process steps, and motion only when it explains change. Keep this repo’s optional motion, portable HTML, and renderer-aware Markdown boundaries instead of adopting its rendering kit.
- [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): subject-specific layout and motion that responds to an action.
- [Anthropic web-artifacts-builder](https://github.com/anthropics/skills/blob/main/skills/web-artifacts-builder/SKILL.md): portable HTML delivery and an explicit distinction between simple and complex artifacts.

Retain standalone inline SVG/JavaScript for small explainers instead of adopting the reference’s React scaffolding. Keep browser verification required by this skill. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Explain compound interest in HTML with an adjustable rate.

**Expected behavior:** Keep a labelled static chart. Changing the rate updates the curve immediately, with no animation or playback controls. Preserve the dark theme and verify chart contrast.

**Boundary request:** Explain compound interest in two sentences.

**Expected boundary:** Return prose; do not invoke the HTML skill or create a page.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
