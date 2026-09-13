---
name: history-skill
description: Reconstruct and maintain an evidence-backed history of a project, decision, incident, or body of work. Use when the user asks for a history, chronology, timeline, retrospective record, or an update to an existing history document.
metadata:
  author: rushikesh
---

# History

Create a chronology that helps a future reader understand what happened, when it happened, and why it mattered.

## Workflow

1. Establish the subject, time range, audience, and requested output. Infer these from available context when the choice is low-risk.
2. Gather the strongest available evidence. Prefer primary sources such as version-control history, source files, decision records, issue or pull-request discussions, release notes, and dated artifacts.
3. Normalize dates and ordering. State the timezone when it affects interpretation, and label approximate dates rather than implying false precision.
4. Separate confirmed facts from interpretations. When sources conflict, preserve the disagreement and explain which source appears more reliable.
5. Write or update the history with the structure in [assets/history-template.md](assets/history-template.md). Adapt the template to the subject and remove sections that add no value.
6. Verify every material claim against its cited evidence. Check that links, commit IDs, paths, names, dates, and event order are accurate.

## Working With Existing Histories

Preserve useful prose and the author's voice. Add new events in the appropriate chronological position, reconcile duplicates, and change prior claims only when stronger evidence supports the correction. Make corrections visible when silently rewriting the record could mislead readers.

## Evidence Rules

- Never invent missing events, motives, dates, quotations, or sources.
- Cite evidence close to the claim it supports. Use stable links or repository-relative paths when possible.
- Mark inference explicitly and include an honest confidence level when uncertainty matters.
- Exclude credentials, private personal data, and irrelevant sensitive material even when they appear in source history.
- Put unresolved gaps in `Open questions` instead of smoothing them over.

Use `HISTORY.md` as the default filename only when the user wants a durable project document and has not specified another location.
