# add-diagram: Optional motion with renderer-aware fallback

Status: proposed; available after this skill’s pull request merges.

Support optional, accessible animation in HTML diagrams while preserving static Markdown rendering and truthful chart comparisons.

## Research and adaptation

- [Nico Bailon visual-explainer](https://github.com/nicobailon/visual-explainer/blob/main/plugins/visual-explainer/SKILL.md): figure-first explanations, named process steps, and motion only when it explains change. Keep this repo’s optional motion, portable HTML, and renderer-aware Markdown boundaries instead of adopting its rendering kit.
- [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): meaningful user-driven motion and accessible visual hierarchy.

Adapt motion to document capabilities rather than importing a webpage workflow into Markdown. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Add a retry flowchart to an HTML document with step-by-step playback.

**Expected behavior:** Keep topology visible, label retry conditions, expose the current step in text, and support reduced motion and reset. Concurrent branches remain concurrent.

**Boundary request:** Add a retry flowchart to a GitHub Markdown document.

**Expected boundary:** Use static Mermaid compatible with GitHub; do not inject scripts or create an unrequested HTML companion.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
