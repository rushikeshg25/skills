# Changelog

User-visible changes to this skill collection. Dates record changes on `main` in Asia/Kolkata time; they are not versioned releases. Pending changes stay under **Unreleased** until merged. Routine commits and local decision logs are omitted.

## Unreleased

### Changed

- Reorganize the README around reader goals, with a complete skill catalog, invocation labels, and a shorter installation path.
- Rename `ste-writing` to **`easy-understanding`** for easier recall. The writing guidance and automatic invocation are unchanged. After updating your installed skills, use `$easy-understanding` in Codex or `/easy-understanding` in Claude Code. The old name is not an alias; remove an old installed `ste-writing` copy if your installer retains it. [PR #4](https://github.com/rushikeshg25/skills/pull/4)

### Added

- This changelog, with linked historical entries and migration guidance for renamed skills.
- A getting-started guide with example prompts, installation updates, decision-log setup, and troubleshooting.

## 2026-10-05

### Added

- Four independent explanation skills: `ste-writing` for automatic, ASD-STE100-inspired technical writing; `html-explainer` for interactive pages; `add-diagram` for Markdown and HTML diagrams; and `explainer-video` for rendered videos with optional narration. The latter three require user invocation. [PR #3](https://github.com/rushikeshg25/skills/pull/3)

## 2026-09-19

### Added

- `tell-me-about-this`, a user-invoked codebase tour that produces a linked project guide covering runtime flow, structure, stack, architecture, and decisions. [PR #2](https://github.com/rushikeshg25/skills/pull/2)

## 2026-09-14

### Added

- `decision-log` to record development decisions, `pipeline-forensics` to trace data across a pipeline, `learn-it-myself` for hands-on technical learning, and `overbuild-check` to assess infrastructure plans before building them. [PR #1](https://github.com/rushikeshg25/skills/pull/1)

## 2026-08-26

### Added

- The first implemented skills: `history-skill` for evidence-backed histories and `lets-build-together` for collaborative implementation in small increments. [Commit 55a3224](https://github.com/rushikeshg25/skills/commit/55a3224)
- Installation guidance for Claude Code and other compatible harnesses. [Commit 6fee1dc](https://github.com/rushikeshg25/skills/commit/6fee1dc)
