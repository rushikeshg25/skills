---
name: tell-me-about-this
description: Explore a codebase and write a durable project guide under docs/project-guide/ covering the end-to-end runtime flow with diagrams, a folder and file map, the tech stack, the system architecture, and the non-obvious decisions behind them. Invoked only by the user with /tell-me-about-this.
disable-model-invocation: true
metadata:
  author: rushikesh
---

# Tell Me About This

Read a project the way a careful new maintainer would, then leave the understanding behind as files instead of letting it expire with the session.

The deliverable is six Markdown files in `docs/project-guide/`. Everything in them traces to code that was actually read.

## Workflow

1. **Scope the job.** Find the repository root, its size (`git ls-files | wc -l`), and its languages. Check whether `docs/project-guide/` already exists; if it does, this is an update, so read the existing files first and correct them rather than rewriting from scratch. Ask the user which package to document only when the repo is a monorepo and no single target is obvious.
2. **Map before reading.** Read the top-level tree, the README, package and build manifests, CI configuration, and any `docker-compose` or deployment files. From these, form an explicit hypothesis about the entry points and the main runtime path.
3. **Fan out when supported.** If delegation is available and useful for the repository size, launch 2–4 exploration subagents using the host's available tools, one per beat: entry points and the request or command lifecycle; data layer and external integrations; configuration, build, and deployment; tests and conventions. Give each the hypothesis from step 2 and ask for file paths with line anchors rather than prose summaries. Read directly when delegation is unavailable or the project is under roughly 50 tracked files; the same evidence requirements apply.
4. **Verify the spine yourself.** Read the files identified by your exploration or the subagents as the main path — entry point, router or dispatcher, core domain module, persistence — before writing the flow document. Subagent findings are leads; the traced path has to be read firsthand.
5. **Write the six files** from the matching section of [assets/project-guide-templates.md](assets/project-guide-templates.md).
6. **Check the result.** Confirm every cited path exists, every relative link resolves to a real file or heading, every `mermaid` block parses, and the main flow runs start to finish with no unexplained jumps. Unresolved gaps go in `Open questions` in the index, never into a confident sentence.

## Document contracts and the evidence boundary

Record the source revision and any relevant uncommitted changes in the guide index. State which runtime paths were traced and which were not inspected. For an update, start from changed entry points, interfaces, and their callers rather than rewriting unrelated sections.

For each important module, explain what callers must know beyond its function signatures: valid inputs, returned errors, ordering requirements, transaction boundaries, retries, and configuration read at startup versus runtime. Link the implementation and one relevant caller or test. Describe guarantees only when the evidence establishes them.

Trace one representative failure path as well as the successful path. Follow an error or timeout through handling, persistence, and the user-visible result; note where a retry could repeat a side effect. Keep inferred intent separate from observed behavior.

Source inspection establishes code behavior under stated conditions; it does not establish that a deployed service uses that revision or configuration. Label run commands as documented, inspected, or actually executed. Do not start services or access production merely to make the guide sound verified.

## Output

Write to `docs/project-guide/`:

| File | Contents |
| --- | --- |
| `README.md` | What the project is in three sentences, how to run it, a five-file tour of the source, the reading order for the other five files, and `Open questions`. |
| `01-architecture.md` | Components and their responsibilities, a component diagram, boundaries and contracts between them, the data model, state and persistence, deployment topology, and how the system fails and scales. |
| `02-flow.md` | The headline flow from process start to response, step by step with `file:line` anchors, plus the startup or bootstrap sequence and every other significant flow such as auth, background jobs, or the build. One diagram per flow. |
| `03-structure.md` | A high-level paragraph on what lives where, then a table per folder: file, responsibility, key exports, and who calls it. |
| `04-tech-stack.md` | Languages and runtimes with versions, frameworks and major libraries with what each is used for and where, datastores, infrastructure, and dev and CI tooling — each tied to the manifest line that pins it. |
| `05-decisions.md` | Non-obvious choices inferred from the code, with the evidence for each and the tradeoff it takes, plus a `Gotchas` section for the traps a newcomer hits first. |

Cover every significant source file in `03-structure.md`. Leave out generated output, vendored dependencies, lockfiles, and config boilerplate that says nothing about the design.

## Cross-links

The six files are one document at different altitudes, so let the reader move between them instead of searching.

- Every flow step in `02-flow.md` links to its source file and to the `03-structure.md` section that owns it.
- Every component in `01-architecture.md` links to the folder that implements it.
- Every table row naming a file links to that file.
- The index opens with a five-file tour: the shortest ordered path through real source files that builds a working mental model, each entry pointing at the guide section that explains it. Pick files that tell a story in sequence, not the five largest.

Use relative links so they resolve on GitHub and in a local preview. From inside `docs/project-guide/`, the repository root is `../../`, and a sibling document is a bare filename such as `03-structure.md`. Link to a heading with its GitHub anchor (lowercased, spaces to hyphens, punctuation dropped).

## Diagrams

Use Mermaid in ```mermaid fences so the diagrams render on GitHub.

- `flowchart` for request paths and data paths.
- `sequenceDiagram` for interactions across components or services.
- `erDiagram` for the data model.
- `graph` for deployment and infrastructure topology.

Keep each diagram under roughly 15 nodes and split a large one into stages instead of letting it sprawl. Label edges with what actually moves: the payload, the event, the call. Delete any diagram that only restates the paragraph above it.

## Rules

- Every claim traces to a file. Point at specific logic with a line anchor, such as `src/server.ts:42`.
- Never invent a component, a flow, or a rationale. Mark inference as inference and send unknowns to `Open questions`.
- Describe what the code does, not what the README claims it does. Note the drift where the two disagree.
- Never copy secrets, tokens, or `.env` values into the guide, even after reading them.
- Do not touch project code. This skill writes only inside `docs/project-guide/`.
- Write for someone who has never seen the repository and has to change it tomorrow.
