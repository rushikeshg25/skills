# Skills

Reusable agent skills by Rushikesh for understanding code, building with feedback, investigating data problems, and explaining technical ideas.

Each skill handles a specific job. Install the ones you need, read their instructions, and adapt them to your workflow. You can use each skill independently.

[Choose a skill](#choose-a-skill) · [Install](#install) · [Invocation](#invocation) · [Changelog](CHANGELOG.md)

## Start here

| What you want to do | Start with |
| --- | --- |
| Understand an unfamiliar repository | [`tell-me-about-this`](skills/tell-me-about-this/SKILL.md) |
| Shape and build an idea with the agent | [`lets-build-together`](skills/lets-build-together/SKILL.md) |
| Learn by writing the core logic yourself | [`learn-it-myself`](skills/learn-it-myself/SKILL.md) |
| Find where data went missing or stale | [`pipeline-forensics`](skills/pipeline-forensics/SKILL.md) |
| Make a technical explanation easier to read | [`easy-understanding`](skills/easy-understanding/SKILL.md) |

## Install

Choose skills and let the installer detect your agent:

```bash
npx skills@latest add rushikeshg25/skills
```

Or install one skill for a specific agent:

```bash
npx skills@latest add rushikeshg25/skills --agent codex --skill easy-understanding
```

Replace `codex` with `claude-code` for Claude Code. Add `-g` for a user-wide installation instead of a project installation. The installer requires Node.js and npm; the skills themselves do not require a Node.js runtime unless their task needs one.

## Choose a skill

**Model-invoked** means the agent may select the skill when the request fits. You can also invoke it explicitly. **User-invoked** means you choose when it runs.

### Understand and build

| Skill | Use it to | Invocation |
| --- | --- | --- |
| [`tell-me-about-this`](skills/tell-me-about-this/SKILL.md) | Produce a linked codebase guide covering runtime flow, architecture, files, and decisions. | User |
| [`lets-build-together`](skills/lets-build-together/SKILL.md) | Turn an idea into verified increments while staying involved in decisions. | Model or user |
| [`learn-it-myself`](skills/learn-it-myself/SKILL.md) | Learn a concept by implementing the core logic yourself, with tutoring and checks. | Model or user |
| [`overbuild-check`](skills/overbuild-check/SKILL.md) | Assess an infrastructure plan's need, cost, success measure, and stopping criteria. | Model or user |
| [`pipeline-forensics`](skills/pipeline-forensics/SKILL.md) | Trace one record across a data pipeline to locate the first incorrect hop. | Model or user |

### Explain and visualize

| Skill | Output | Invocation |
| --- | --- | --- |
| [`easy-understanding`](skills/easy-understanding/SKILL.md) | Clear technical prose inspired by ASD-STE100, with meaning and qualifications preserved. | Model or user |
| [`html-explainer`](skills/html-explainer/SKILL.md) | An HTML page with visuals and interactions that explain a topic. | User |
| [`add-diagram`](skills/add-diagram/SKILL.md) | A diagram integrated into an existing Markdown or HTML document. | User |
| [`explainer-video`](skills/explainer-video/SKILL.md) | A rendered video, editable source, transcript, and optional synchronized narration. | User |

Choose prose for a direct explanation, a diagram for relationships, HTML for exploration, and video for a paced visual lesson. The writing skill uses a practical simplified style; it does not certify ASD-STE100 compliance.

### Keep a useful record

| Skill | Output | Invocation |
| --- | --- | --- |
| [`decision-log`](skills/decision-log/SKILL.md) | A local, append-only log of decisions, alternatives, and blockers during development. | Model or user |
| [`history-skill`](skills/history-skill/SKILL.md) | An evidence-backed history reconstructed from source material. | Model or user |

## Invocation

In **Codex**, use `$skill-name`. In **Claude Code**, use `/skill-name`:

```text
Use $html-explainer to explain compound interest with an adjustable interest rate.
```

```text
/add-diagram Add the retry sequence to docs/design.md.
```

Automatic selection depends on the agent and the request; it does not guarantee that a skill runs on every turn. To make `decision-log` a standing practice, install it and add its instruction to the project's `AGENTS.md` or `CLAUDE.md`.

## Compatibility and requirements

Skills use the portable `SKILL.md` layout. Codex reads additional interface and invocation settings from `agents/openai.yaml`; Claude Code uses frontmatter settings in `SKILL.md`. Other harnesses may interpret invocation controls differently.

The repository provides instructions, templates, and a decision-log helper. It does not bundle browser renderers, video encoders, or speech engines. HTML and diagram verification need a compatible preview tool. Video production needs a renderer and encoder; narration also needs local speech tools or an authorized provider.

## Project

- [Changelog](CHANGELOG.md): additions, behavior changes, and rename migration notes.
- [Skill source](skills/): one folder per skill, with supporting files only where needed.
- [MIT license](LICENSE): use and adapt the collection under its terms.

The task-focused catalog and explicit invocation labels take inspiration from [Matt Pocock's skills collection](https://github.com/mattpocock/skills).
