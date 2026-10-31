# PR Description

`pr-description` writes PR and MR bodies in plain language using `easy-understanding`. It explains the actual change, adds an example when useful, and distinguishes verified results from missing evidence. Repository templates take precedence over its suggested shape.

Example request: `Use $pr-description to explain this branch's changes for a reviewer.`

Expected artifact: a Markdown PR body ready to paste. Drafting needs the relevant diff or change evidence; local Git and an authenticated host CLI or connector help inspect an existing PR. Remote access is needed only when inspecting remote information or publishing an authorized update.

## Design sources

Inspected on 2026-10-31:

- [Sentry's pr-writer](https://github.com/getsentry/skills/blob/main/skills/pr-writer/SKILL.md): behavior-first cover notes, full-branch evidence, and structure proportional to the change. This skill retains relevant validation and repository-required headings instead of applying Sentry's default omissions.
- [Matt Pocock's pr skill](https://github.com/mattpocock/skills/blob/main/skills/engineering/pr/SKILL.md): concrete before/after evidence and small reviewer aids. This skill makes visuals and risk sections conditional instead of requiring a visual-first template.
- [Easy Understanding](../../skills/easy-understanding/SKILL.md): plain language that preserves technical meaning, conditions, and uncertainty.

The resulting instructions are tailored to this collection. They do not require either external skill or runtime access to these sources.
