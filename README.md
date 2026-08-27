# Skills

A collection of reusable agent skills by Rushikesh

## Installation

Install interactively and let the Skills CLI detect your available agent harnesses:

```bash
npx skills@latest add rushikeshg25/skills
```

Install both skills for Claude Code:

```bash
npx skills@latest add rushikeshg25/skills --agent claude-code --skill '*'
```

Install both skills for every harness supported by the CLI:

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
