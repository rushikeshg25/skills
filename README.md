# Skills

A collection of reusable agent skills by Rushikesh

## Installation

Install interactively and let the Skills CLI detect your available agent harnesses:

```bash
npx skills@latest add rushikeshg25/skills
```

Install all skills for Claude Code:

```bash
npx skills@latest add rushikeshg25/skills --agent claude-code --skill '*'
```

Install all skills for every harness supported by the CLI:

```bash
npx skills@latest add rushikeshg25/skills --all
```

## Compatibility

The shared `SKILL.md` instructions and bundled templates follow the portable Agent Skills layout used by Claude Code, Codex, and other compatible harnesses. The optional `agents/openai.yaml` files add OpenAI-specific interface metadata and can be ignored safely by other harnesses.

## Structure

Each skill lives in its own folder under `skills/` and contains a `SKILL.md` file.

## Available skills

- `history-skill`: reconstruct and maintain evidence-backed histories and timelines.
- `lets-build-together`: turn an idea into verified, feedback-sized increments with the user.
- `decision-log`: keep an append-only, dated log of decisions, alternatives, and blockers while working.
- `pipeline-forensics`: trace one record through a CDC, Kafka, or ETL pipeline to find the first hop where it goes missing or stale.
- `learn-it-myself`: learn a concept by implementing it yourself while the agent explains, sets checks, and reviews.
- `overbuild-check`: pressure-test an infrastructure-heavy plan for need, cost, a measurable outcome, and kill criteria before building it.

## Setting up decision-log

`decision-log` is meant to run on its own during development work, so the agent has to be able to find it. Agents do not read this repository or any index file to discover skills. Claude Code finds skills by location, `.claude/skills/` in a project or `~/.claude/skills/` for your user, and shows the model each skill's name and description so it can decide when to load one.

1. Install the skill into the project you want logged:

   ```bash
   npx skills@latest add rushikeshg25/skills --agent claude-code --skill decision-log
   ```

   Add `-g` to install it for all your projects. Omit `--agent` to pick other harnesses interactively.

2. Tell the agent to use it on every nontrivial task. The skill description already asks for proactive use, but a standing instruction makes it reliable. Add this to the project's `CLAUDE.md` (or `~/.claude/CLAUDE.md` for a global install, or `AGENTS.md` for Codex and other harnesses):

   ```markdown
   ## Decision log

   During any nontrivial coding, debugging, or refactoring task, use the `decision-log` skill: append an entry to `logs/YYYY-MM-DD.md` after each design choice, choice between approaches, bug fix strategy, or blocker.
   ```

3. Start a new session and ask for a change that involves a real choice. An entry should appear in `logs/` under today's date. If Claude Code asks for permission to run `scripts/log-entry.sh`, allow it so later entries do not interrupt the work.

4. Decide whether logs belong in version control. The skill never commits log files or edits `.gitignore`, so add `logs/` to `.gitignore` if you want to keep them local.
