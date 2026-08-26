---
name: lets-build-together
description: Collaboratively turn an early idea into a working, verified implementation through small feedback-driven increments. Use when the user says “let’s build,” wants to shape a solution together, or asks to remain involved in design and implementation decisions; do not use for ordinary requests that clearly ask for autonomous execution.
---

# Let's Build Together

Keep momentum while giving the user meaningful control over the result. Collaborate at decisions that materially affect behavior, scope, or experience; handle reversible implementation details autonomously.

## Start With Shared Intent

Inspect the available project context before asking questions. Briefly reflect back the desired outcome, the most important constraint, and any consequential assumption. Ask only when different answers would produce materially different work and the answer cannot be discovered locally.

For a multi-step or still-fluid build, copy and adapt [assets/build-together-template.md](assets/build-together-template.md) into a user-requested location. If no location is given, use `BUILD_TOGETHER.md` only when a durable working agreement would help; skip the file for small tasks.

## Build in Feedback-Sized Increments

1. Agree on the smallest end-to-end slice that will answer the current design question or produce visible value.
2. Implement that slice using the project's existing conventions and preserve unrelated work.
3. Verify the behavior in proportion to its risk. Prefer observable behavior over checks of implementation wording or structure.
4. Show the user the concrete result, tradeoffs discovered, and the next meaningful choice.
5. Fold feedback into the working agreement and continue with the next slice.

Do not turn every routine choice into a checkpoint. Pause when feedback can still change direction cheaply, especially before committing to a public interface, data model, destructive migration, paid service, or externally visible action.

## Keep the Collaboration Honest

- Distinguish decided requirements from proposals and assumptions.
- Keep the current slice small enough to revise without defending sunk work.
- Update or remove stale decisions in the working agreement as the build evolves.
- Surface constraints and failed approaches early, with evidence.
- Do not expand the product scope merely because adjacent improvements are possible.
- Treat “done” as user-visible behavior plus relevant verification, not merely code written.

Finish each useful increment with what now works, how it was checked, and the next decision or slice. When the agreed outcome is complete, provide a concise handoff instead of inventing more work.
