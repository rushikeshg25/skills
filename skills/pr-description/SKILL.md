---
name: pr-description
description: Write or simplify pull request and merge request descriptions that explain the actual change, its purpose, and a useful example in plain language. Use when preparing or updating a PR/MR body, including during an authorized PR creation task. Not a code review or release-note workflow.
---

# PR Description

Help a reviewer understand what changes and why without reconstructing the diff. Deliver a ready-to-use description, not advice about writing one.

## Establish the facts

- Read applicable repository guidance and the PR/MR template. Preserve required sections; keep their contents concise.
- For an existing PR, inspect its actual base and head and the full current diff. For a new PR, establish the intended target branch and compare from its merge base. Do not assume the target is `main` or describe only the latest commit.
- Read the relevant implementation, callers, tests, and issue context needed to explain the behavior. Commit messages and the old description are clues, not proof.
- Separate local uncommitted work from the changes included in the PR. Include it only if the requested draft explicitly covers that work, and make its status clear.
- When only a supplied diff or summary is available, draft from that evidence. Identify material gaps without inventing motivation, test results, performance improvements, or compatibility guarantees.

## Write for the reviewer

Use the **easy-understanding** skill. In this collection, read [its instructions](../easy-understanding/SKILL.md); in another installation, resolve it through the available skill catalog. If unavailable, say so briefly outside the PR body and use this fallback: common words, active voice, one main idea per sentence, consistent terms, and preserved conditions and uncertainty.

1. Lead with the concrete outcome: what happens now, and who or what is affected. Explain the problem or purpose in the next sentence if it is not already clear.
2. Include only the implementation detail that explains the result or a meaningful tradeoff. Group related changes by behavior instead of listing files or commits. For a refactor, describe the internal change without inventing a user-visible improvement.
3. Add one small before/after example when it makes the change easier to understand. Use a request, response, command, UI action, or concrete input and output. Label hypothetical examples as illustrative; never present them as observed results.
4. State relevant validation and its actual outcome. Separate checks that passed from checks that failed, were skipped, or were not run. Keep logs out of the body; name the check and what it establishes. Do not turn a planned test into a passing result.
5. Include breaking changes, migration steps, rollout constraints, or important limitations when the evidence calls for them. Simpler writing must preserve exact API names, values, conditions, exceptions, and uncertainty.

For a small change, one short paragraph plus a validation sentence is usually enough. For a larger change, use a few focused paragraphs or the repository's required headings. An example, diagram, screenshot, or risk section is optional unless required by the repository or user. Do not impose a fixed word count.

Avoid vague claims such as “improves robustness,” process narration such as “addressed review feedback,” repeated summaries, and exhaustive file lists. Say what actually changes. Do not include unrelated work, private data, or unsupported issue-closing keywords.

## Check and deliver

Read the draft against the diff: can a reviewer identify the previous behavior, the resulting behavior, and why the change matters? For a new feature, explain what becomes possible. Remove claims that the evidence does not support.

When refreshing a description, describe the final PR as a whole. Preserve still-relevant human context and required template fields; remove obsolete scope and stale validation claims.

Return the description itself, ready to paste. Add a title only when requested or when creating the PR. Missing evidence that affects a claim belongs in the description; process notes belong outside it.

Drafting or rewriting does not authorize committing, pushing, creating a PR, or editing a remote body. When publication is already authorized, use the host's supported tool and verify the saved body. With `gh`, write Markdown to a temporary file and pass `--body-file` to preserve formatting. Do not merge as part of writing a description.

## Example

Illustrative facts: the export API previously ignored `status=paid`; this change applies the filter before generating CSV rows. The export regression test passed; browser checks were not run.

```markdown
Invoice exports now respect the selected status filter. Previously, exporting paid invoices also included unpaid invoices.

For example, `GET /invoices/export?status=paid` now returns CSV rows for paid invoices only. The API filters invoices before generating the CSV.

Validation: The export regression test passed. Browser checks were not run.
```

Keep the meaning and useful evidence of this example, not its exact wording or structure.
