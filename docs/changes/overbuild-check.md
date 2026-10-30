# overbuild-check: Compare guarantees before cost

Status: proposed; available after this skill’s pull request merges.

Check alternatives against delivery and durability guarantees, expose decision-changing evidence, and account for migration and safe exit costs.

## Research and adaptation

- [Matt Pocock prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md): choose an experiment that answers the actual design question.
- [Matt Pocock grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): resolve decision dependencies and discover facts before asking.

Use targeted evidence rather than an exhaustive interview. An exit plan is not permission to tear down data or services. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Plan only: replace Kafka with a job table; three independent consumers need seven-day replay.

**Expected behavior:** Compare independent consumption and retention guarantees before calling a job table equivalent. Propose a bounded check and state unknowns; do not run infrastructure experiments.

**Boundary request:** I want to learn Kafka consumer rebalancing as a weekend exercise.

**Expected boundary:** Preserve the learning goal and set cost/time caps; do not reject Kafka merely because a table is simpler.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
