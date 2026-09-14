---
name: decision-log
description: Use proactively, without being asked, for any nontrivial coding, debugging, refactoring, or other development task in this project, and keep using it until the task is done. Maintains an append-only, dated decision log at logs/YYYY-MM-DD.md, adding a short entry after each design choice, choice between approaches, bug fix strategy, or blocker, with the alternatives passed over and why. Skip trivial questions and edits that involve no real decision.
allowed-tools: Bash(bash ${CLAUDE_SKILL_DIR}/scripts/log-entry.sh *)
metadata:
  author: rushikesh
---

# Decision Log

Keep a running record of the decisions made while working, so a future reader can see what was chosen, what was passed over, and why. These are standing instructions for the rest of the session: log as the work happens, without waiting to be asked and without saving entries up for the end.

## Workflow

1. When starting a task, read today's log if one exists, so new entries continue the record instead of repeating it.
2. After each meaningful step, append one entry with the script below.
3. Before reporting a task as done, check that every meaningful step since the last entry has been logged, and append any that are missing.

## What Counts as a Meaningful Step

- A design or architecture choice, such as a data model, interface, or new dependency.
- Picking one approach over another viable one.
- Fixing a bug in a particular way, especially when other fixes were possible.
- Hitting a blocker. Log it once it is resolved, or log it as unresolved if you have to move on or stop.
- Reversing or revising an earlier decision.

Skip steps with no real choice in them, such as reading code, renaming, formatting, running a passing test suite, or following an established project convention.

## Appending an Entry

Run the bundled script with a short step label and the entry bullets on stdin:

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/log-entry.sh "Rate limiter strategy" <<'EOF'
- **Decision:** Token bucket per API key stored in Redis, because limits must hold across every app instance.
- **Alternatives:** Fixed window counter (allows 2x bursts at window edges); in-process limiter (each instance would enforce its own limit).
- **Blocker:** `EVALSHA` is disabled on the managed Redis tier; switched to `EVAL` with the script inline.
EOF
```

`${CLAUDE_SKILL_DIR}` is this skill's directory; in harnesses that do not substitute it, use that directory's path. The script takes the local date and time from the system, writes to `logs/YYYY-MM-DD.md` under the repository root (or the current directory outside git), creates the file with a `# Session Log — YYYY-MM-DD` header when it does not exist, and appends the entry under a `## HH:MM - label` heading. Keep the quoted `'EOF'` so backticks and `$` are written literally.

If the script cannot run, follow the same rules by hand: take the date and time from the system, create the file with exactly that header, and append to the end with `>>` or an edit after the last line.

## Log Rules

- The file is append-only. Never overwrite, reorder, or edit existing entries, including your own, and never use a whole-file write on an existing log.
- To correct or revisit an earlier entry, append a new one that refers to it by its time and label.
- Work that crosses midnight continues in the new day's file.
- Do not commit log files or change `.gitignore` for them unless the user asks.

## Entry Format

Each entry has these bullets, a few lines in total:

- **Decision:** What was decided or done, and the main reason for it.
- **Alternatives:** The options actually considered and why each was passed over. If only one option was viable, say why in a few words.
- **Blocker:** What got in the way and how it was resolved. Omit this bullet when there was no blocker. If it is still open, write `Unresolved:` with the current state, then append a follow-up entry once it is resolved.

## Writing Rules

- Point to files, commits, or errors by name instead of pasting code or logs.
- Record the reasoning that actually drove the choice. Do not invent alternatives after the fact to fill the format.
- Never include secrets, credentials, tokens, or private personal data.
- Log without asking permission for each entry and without interrupting the task.
