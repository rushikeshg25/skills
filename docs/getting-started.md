# Getting started

Install one skill, try it on a small task, and inspect the result before adding more. The [README catalog](../README.md#choose-a-skill) lists every skill and its invocation mode.

## Install the skills you need

Use the interactive installer to choose both skills and agents:

```bash
npx skills@latest add rushikeshg25/skills
```

For a specific skill, choose the agent explicitly:

```bash
npx skills@latest add rushikeshg25/skills --agent codex --skill easy-understanding
npx skills@latest add rushikeshg25/skills --agent claude-code --skill add-diagram
```

These are alternatives for different agents and skills; you do not need both. Add `-g` to install for your user across projects. For the complete collection in Claude Code, use:

```bash
npx skills@latest add rushikeshg25/skills --agent claude-code --skill '*'
```

To install every skill for every harness supported by the installer:

```bash
npx skills@latest add rushikeshg25/skills --all
```

Use the installer's reported destination to confirm what was installed. Start a new agent session if the skills do not appear in the current session. A clone of this repository alone does not make its skills discoverable to every agent.

## Try a concrete request

These examples use Codex's `$skill-name` syntax. For Claude Code, start the request with `/skill-name` instead.

| Goal | Example prompt | Expected result |
| --- | --- | --- |
| Understand a repository | “Use $tell-me-about-this to explain this repository.” | A linked guide under `docs/project-guide/`, grounded in the code. |
| Build collaboratively | “Use $lets-build-together to build a small habit tracker. Keep me involved in the design.” | Small implementation steps with feedback and verification. |
| Learn by doing | “Use $learn-it-myself to teach me a hash table. Let me write the core operations.” | Exercises and checks while you implement the logic. |
| Investigate a pipeline | “Use $pipeline-forensics to find why order 123 is stale in the report.” | A traced record and the first hop where evidence diverges, or explicit evidence gaps. |
| Assess a plan | “Use $overbuild-check to assess whether this side project needs Kafka.” | Alternatives, costs, a measurable outcome, and stopping criteria. |
| Explain clearly | “Use $easy-understanding to explain replication lag to a new engineer.” | Direct technical prose with necessary terms and qualifications preserved. |
| Explore interactively | “Use $html-explainer to explain compound interest with an adjustable rate.” | An HTML file with a working example and useful controls. |
| Add a visual | “Use $add-diagram to add the retry sequence to docs/design.md.” | An edited document with a diagram compatible with its renderer. |
| Make a video | “Use $explainer-video to make a 60-second dot-product explanation with local narration.” | A playable video and source, or a precise production blocker. |
| Reconstruct history | “Use $history-skill to reconstruct the authentication migration from Git history.” | A chronology with evidence and uncertainty clearly identified. |

Use real files and records that you can inspect. A prompt does not supply unavailable repository, database, or service access; the agent should identify missing evidence rather than invent a result.

## Make decision logging a standing practice

Install the skill in the project where decisions should be recorded:

```bash
npx skills@latest add rushikeshg25/skills --skill decision-log
```

Add this instruction to the project's `AGENTS.md` for Codex, `CLAUDE.md` for Claude Code, or the equivalent instructions file for your harness:

```markdown
During nontrivial development work, use the decision-log skill. Append an entry
to logs/YYYY-MM-DD.md after each design choice, choice between approaches,
bug-fix strategy, or blocker. Record the decision and the alternatives considered.
```

Run a task that involves a real choice and look for a dated entry in `logs/`. The helper needs Bash and write access to the project. Follow your agent's normal approval flow if it requests permission to run the helper.

Decision logs describe the work as it happens. The [project changelog](../CHANGELOG.md) describes changes users should know about. The skill does not commit logs or change `.gitignore`; decide separately whether your project should version those files.

## Update an installation

Read the [changelog](../CHANGELOG.md), especially rename and removal notes. Review any edits you made to your installed copies before updating:

```bash
npx skills@latest update
```

Follow the installer's output to confirm which copies changed. After a rename, check for an old copy that could still appear in your agent. `ste-writing` became `easy-understanding`; the old command is not an alias.

## When something does not work

| Symptom | Check |
| --- | --- |
| The agent cannot find the skill | Confirm the installed location and target agent, then try a fresh session. Reading the README does not install skills. |
| A skill does not run automatically | It may be user-invoked. Check the catalog and invoke it explicitly. Automatic selection is contextual. |
| A skill runs when you did not request it | Check the installed invocation metadata and whether the harness supports it. Check for stale or duplicate installed copies. |
| A diagram appears as source text | The Markdown renderer may not support Mermaid. Request a supported SVG or PNG asset instead. |
| A video cannot be produced | Check for a working renderer and encoder. Narration also needs a speech engine or an authorized provider. |
| A tool or service is unavailable | The skills provide instructions, not credentials or bundled runtime tools. Use the reported blocker to supply the missing capability. |

If the instructions themselves are wrong, report the skill name, agent, request, expected result, and observed behavior. Remove secrets and private data from examples.
