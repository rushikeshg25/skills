# pipeline-forensics: Evidence-bounded divergence diagnosis

Status: proposed; available after this skill’s pull request merges.

Correct overconfident hop attribution and distinguish missing logs, committed offsets, version mismatches, and proven sink outcomes.

## Research and adaptation

- [Matt Pocock diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md): a discriminating signal and falsifiable competing explanations.

Keep production probes read-only and allow a precise evidence gap as an honest result; do not import forced reproduction or instrumentation in production. Research inspected on 2026-10-30; upstream links may evolve. The changes use original wording.

## Review examples

**Representative request:** Source version 7 is present at partition 3 offset 48122. The group committed 48130, logs are missing, and the sink has version 6.

**Expected behavior:** Mark the consumer outcome unknown. The divergence lies after the observed broker event and before the observed stale sink state; probe durable sink writes and version ordering instead of declaring a skip.

**Boundary request:** A single-service parser throws on an invalid string; there is no pipeline.

**Expected boundary:** Use ordinary debugging rather than inventing source/broker/sink stages.

These are manual instruction walkthroughs, not independent model evaluations or rendered-output tests. Metadata checks cannot establish that a generated artifact works.
