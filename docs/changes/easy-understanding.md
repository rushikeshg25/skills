# easy-understanding: Task-shaped explanations with preserved meaning

Status: proposed; available after this skill’s pull request merges.

Match explanation depth to the reader task and protect command semantics, compound conditions, and uncertainty during rewrites.

## Research and adaptation

- [Matt Pocock writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md): clear information hierarchy and explicit completion criteria.

Adapt clarity principles to the reader’s task; do not adopt agent-specific coined terminology or claim formal STE compliance. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Simplify: Retry only if the request is idempotent and the failure is transient.

**Expected behavior:** Keep both conditions necessary. A suitable rewrite is: Retry the request only when both conditions are true: the request is idempotent, and the failure is transient.

**Boundary request:** Rewrite this quoted poem in the author’s original voice.

**Expected boundary:** Preserve the requested creative voice rather than imposing controlled technical prose.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
