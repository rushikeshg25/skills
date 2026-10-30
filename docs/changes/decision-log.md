# decision-log: Decision status without violating read-only scope

Status: proposed; available after this skill’s pull request merges.

Respect read-only tasks and distinguish proposed, accepted, and superseded decisions with evidence and revisit conditions.

## Research and adaptation

- [Matt Pocock domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md): record consequential tradeoffs without creating an ADR for every small choice.

Link an existing ADR instead of turning the session log into a second specification. Keep the append-only helper unchanged. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Review only: compare a queue table with Kafka; make no file changes.

**Expected behavior:** Keep the recommendation and decision status in chat. Do not append a log file. For authorized development later, append accepted or provisional choices and link superseded entries.

**Boundary request:** What is 2 + 2?

**Expected boundary:** Answer directly; do not log a routine question.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
