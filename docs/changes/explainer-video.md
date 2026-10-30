# explainer-video: Reproducible chart and process motion

Status: proposed; available after this skill’s pull request merges.

Add truthful chart and process animation guidance and deterministic frame-based timing for reproducible exports.

## Research and adaptation

- [Remotion markup](https://github.com/remotion-dev/skills/blob/main/skills/remotion-markup/SKILL.md): drive motion from frame coordinates and frame rate, and inspect intermediate rendered frames.
- [Remotion best practices](https://github.com/remotion-dev/skills/blob/main/skills/remotion-best-practices/SKILL.md): separate preview and rendering responsibilities.
- [Remotion create](https://github.com/remotion-dev/skills/blob/main/skills/remotion-create/SKILL.md): inspect existing projects and make scene structure explicit.

Preserve this skill’s rendered-video deliverable, unlike the reference’s preview-first default. Frame-derived timing is a targeted production rule, not a dependency on Remotion. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Render a short video showing a value changing and a request splitting into parallel branches.

**Expected behavior:** Use one scene timeline, stable chart scales, concurrent branch states, and inspect an intermediate frame as well as endpoints.

**Boundary request:** Add animation to my HTML chart.

**Expected boundary:** Use the HTML workflow; do not invoke video production for a webpage animation.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
