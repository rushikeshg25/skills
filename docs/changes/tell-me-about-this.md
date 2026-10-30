# tell-me-about-this: Caller contracts and runtime evidence

Status: proposed; available after this skill’s pull request merges.

Document caller contracts, failure paths, source revision, and runtime verification limits; support hosts without exploration subagents.

## Research and adaptation

- [Matt Pocock codebase-design](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md): an interface includes invariants, error modes, ordering, and configuration.
- [Matt Pocock domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md): cross-check terminology and claims against code.

Describe existing contracts without refactoring modules or imposing another project’s glossary. Keep the guide’s existing output scope. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Document this repository’s request flow; no deployed environment is available.

**Expected behavior:** Record the source revision, trace successful and failure paths, explain caller obligations, and label runtime behavior unverified. Read directly if delegation is unavailable.

**Boundary request:** Just explain this one function in chat.

**Expected boundary:** Answer narrowly; do not invoke the six-file project-guide workflow.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
