# Contributing

Improve a skill around a real task it should handle. Include the request, the observed result, and what should change. Small examples are more useful than broad claims that a skill is too vague or too strict.

## Change a skill

1. Read its `SKILL.md` and the supporting files relevant to your change. Preserve existing user intent and invocation mode unless changing those is the purpose of the PR.
2. Keep the entrypoint focused on decisions the agent would otherwise get wrong. Put substantial conditional guidance in a linked reference. Add scripts or assets only when they support a concrete workflow.
3. Update the folder name, frontmatter `name`, interface prompt, and README together when renaming a skill. Explain the old and new invocation names in the changelog.
4. Try a representative request and one nearby request that should not trigger the skill. Report what you actually ran and any unavailable tools. Metadata checks cannot prove useful behavior.
5. Run the repository checks below and document any remaining limitations in the PR.

Each skill lives under `skills/<name>/`. The name uses lowercase letters, digits, and single hyphens. `SKILL.md` needs a clear `name` and `description`; the folder and frontmatter names must match.

This collection also supplies `agents/openai.yaml` for every skill. Keep its display name, short description, and `$skill-name` default prompt consistent with the entrypoint.

## Choose invocation deliberately

Default to model selection for reusable guidance that applies when a task fits. A user-only skill needs both controls:

```yaml
# SKILL.md frontmatter, for Claude Code
disable-model-invocation: true
```

```yaml
# agents/openai.yaml, for Codex
policy:
  allow_implicit_invocation: false
```

State the intended trigger in the description as well. Do not rely on that prose alone to enforce user-only behavior. Other harnesses may not support these controls.

## Check locally

Use Python 3.11 or newer in a project-local environment:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
.venv/bin/python -m unittest discover -s tests -v
git diff --check
```

The validator checks metadata, invocation consistency, README coverage, and local inline Markdown link targets. It ignores example code blocks and does not check remote URLs or heading fragments. Its purpose is repository integrity; visual output and model behavior still need task-specific verification. No provider credentials are needed for these checks.

The [GitHub Actions workflow](.github/workflows/validate.yml) runs the same validator and regression tests on pull requests and pushes to `main`, with read-only repository permissions.

When adding a helper script, exercise its observable behavior. When changing a prompt, describe a realistic before/after result instead of asserting that a particular sentence or heading exists.

## Maintain the changelog

Add user-visible changes to [CHANGELOG.md](CHANGELOG.md) under **Unreleased**, grouped as **Added**, **Changed**, **Fixed**, or **Removed** as needed. Describe what a user gains or needs to do. Link a relevant PR or commit when available; avoid speculative versions and future dates.

Renames, removals, and invocation changes need migration guidance. Internal refactoring with no effect on users can omit a changelog entry; explain that in the PR.

When recording a batch already merged to `main`, move only those entries into its merge-date section in Asia/Kolkata time. Preserve links and leave other pending entries under Unreleased. Historical dates describe availability on `main`, not the author's local commit time. This project currently uses dated changes rather than package releases.

## Keep the patch focused

Leave local decision logs, installed skill copies, virtual environments, generated media, and credentials out of commits. Do not copy a runtime dependency into every skill when an optional production path is enough.

For a new skill, add it to the README catalog and include an example request, expected artifact, and required tools in the PR. For a bug report, include the agent, skill name, request, expected behavior, and observed behavior with private data removed.

Contributions use this repository's [MIT license](LICENSE).
