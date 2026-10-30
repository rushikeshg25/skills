# learn-it-myself: Calibrated practice and retention

Status: proposed; available after this skill’s pull request merges.

Calibrate exercises with a small prediction, distinguish tooling failures from learning gaps, and check retention without taking over core logic.

## Research and adaptation

- [Matt Pocock teach](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md): retrieval practice, scoped lessons, and durable understanding.

Reuse the gaps ledger instead of creating an entire teaching workspace. Passing checks and copied code alone do not establish retention. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Teach me a hash table. I want to implement collision handling myself.

**Expected behavior:** Ask for one concrete prediction, prepare a small behavioral check, and leave collision handling to the user. In a later lesson, use a fresh collision example before revealing a solution.

**Boundary request:** Ship a production-ready hash table implementation for me.

**Expected boundary:** Use normal implementation mode, not tutoring; do not withhold requested code.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
