# lets-build-together: Concrete feedback checkpoints

Status: proposed; available after this skill’s pull request merges.

Make each collaboration checkpoint answer a concrete question, distinguish prototypes from production, and preserve unanswered decisions.

## Research and adaptation

- [Matt Pocock prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md): a small prototype answers one design question.
- [Matt Pocock to-spec](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md): observable behavior and explicit scope.

Keep decisions and artifacts local unless publication is authorized; do not import tracker publishing or mandatory prototype branches. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Let’s build a retry settings UI together; first help me choose how the retry limit behaves.

**Expected behavior:** Show a small runnable slice and its checked behavior, then ask about the unresolved retry decision. Mark prototype shortcuts and keep a required unanswered choice open.

**Boundary request:** Fix this typo autonomously.

**Expected boundary:** Make the small edit without forcing a collaboration interview or prototype.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
