# Project Guide Templates

One skeleton per output file. Copy the matching section into `docs/project-guide/`, fill every bracket, and delete any heading that adds nothing for this project.

---

## `README.md`

````markdown
# [Project] Project Guide

> Generated: [YYYY-MM-DD] from commit [short SHA]

## What this is

[Three sentences: the problem it solves, who uses it, and what shape it takes — service, CLI, library, app.]

## Run it

```bash
[install]
[run]
[test]
```

[Prerequisites and required environment variables, named but never valued.]

## The five-file tour

The shortest path to a working mental model. Read these source files in this order.

| # | File | Why this one | Then look at |
| --- | --- | --- | --- |
| 1 | [`path/to/entry.ext`](../../path/to/entry.ext) | [The entry point: where the process starts.] | [02-flow.md](02-flow.md#startup) |
| 2 | [`path/to/file.ext`](../../path/to/file.ext) | [What it establishes for everything after it.] | [01-architecture.md](01-architecture.md#components) |
| 3 | [`path/to/file.ext`](../../path/to/file.ext) | [Why it is next.] | [03-structure.md](03-structure.md) |
| 4 | [`path/to/file.ext`](../../path/to/file.ext) | [Why it is next.] | [05-decisions.md](05-decisions.md) |
| 5 | [`path/to/file.ext`](../../path/to/file.ext) | [What it ties together.] | [02-flow.md](02-flow.md) |

## Reading order for this guide

1. [01-architecture.md](01-architecture.md) — the shape of the system.
2. [02-flow.md](02-flow.md) — what happens when it runs.
3. [03-structure.md](03-structure.md) — what lives where.
4. [04-tech-stack.md](04-tech-stack.md) — what it is built on.
5. [05-decisions.md](05-decisions.md) — why it looks like this.

## Open questions

- [A gap, a contradiction, or something the code does not explain.]
````

---

## `01-architecture.md`

````markdown
# Architecture

## Overview

[How the system is organized in one paragraph, and the single idea that explains the layout.]

```mermaid
[Component diagram: the major parts and what flows between them.]
```

## Components

| Component | Responsibility | Lives in | Talks to |
| --- | --- | --- | --- |
| [Name] | [What it owns] | [`path/`](03-structure.md#folder) | [Other components] |

## Boundaries and contracts

- **[Boundary]:** [The interface, the format crossing it, and what each side may assume.]

## Data model

```mermaid
[erDiagram of the core entities and their relationships.]
```

| Entity | Stored in | Key fields | Defined at |
| --- | --- | --- | --- |
| [Name] | [Table, collection, or file] | [Fields that matter] | [path:line] |

## State and persistence

[What is durable, what is cached, what is in memory, and what is lost on restart.]

## Deployment

```mermaid
[Deployment topology: processes, hosts, managed services.]
```

[How it is built, where it runs, and how configuration reaches it.]

## Failure and scale

- **[Failure mode]:** [What happens, and what the code does about it — retries, timeouts, fallbacks.]
- **Scaling:** [What scales horizontally, what is a single point, and what the bottleneck is.]
````

---

## `02-flow.md`

````markdown
# Flow

## [Headline flow, e.g. HTTP request lifecycle]

```mermaid
[flowchart or sequenceDiagram of this flow.]
```

1. **[Step]** — [What happens and why.] [`file.ext:line`](../../path/to/file.ext) · [structure](03-structure.md#folder)
2. **[Step]** — [What happens and why.] [`file.ext:line`](../../path/to/file.ext) · [structure](03-structure.md#folder)

[Where it can branch, short-circuit, or error out.]

## Startup

```mermaid
[Bootstrap sequence from process start to ready.]
```

1. **[Step]** — [Config loaded, connections opened, routes registered.] [`file.ext:line`](../../path/to/file.ext) · [structure](03-structure.md#folder)

## [Other significant flow, e.g. auth, background job, build]

```mermaid
[Diagram.]
```

1. **[Step]** — [What happens.] [`file.ext:line`](../../path/to/file.ext) · [structure](03-structure.md#folder)
````

---

## `03-structure.md`

````markdown
# Structure

## What lives where

[One paragraph orienting the reader: the organizing principle, and the two or three folders that carry most of the weight.]

```text
[Top-level tree, annotated with a few words per entry.]
```

## `[folder/]`

[What this folder is for, in one or two sentences.]

| File | Responsibility | Key exports | Called by |
| --- | --- | --- | --- |
| [`file.ext`](../../folder/file.ext) | [What it does] | [Functions, types, classes] | [Callers] |

## Excluded

[Generated output, vendored code, and boilerplate left out of the tables, so the omission is not mistaken for a gap.]
````

---

## `04-tech-stack.md`

````markdown
# Tech Stack

## Languages and runtimes

| Language or runtime | Version | Pinned at |
| --- | --- | --- |
| [Name] | [Version] | [path:line] |

## Frameworks and major libraries

| Library | Version | Used for | Used in |
| --- | --- | --- | --- |
| [Name] | [Version] | [What it does here] | [path/] |

## Data and infrastructure

| Service | Role | Configured at |
| --- | --- | --- |
| [Postgres, Redis, S3, queue] | [What it holds or moves] | [path:line] |

## Tooling

| Tool | Role | Configured at |
| --- | --- | --- |
| [Build, lint, format, test, CI, deploy] | [When it runs] | [path:line] |

## Notes

- [Anything unusual: a pinned or patched dependency, a library used against its grain, a version that constrains the design.]
````

---

## `05-decisions.md`

````markdown
# Decisions

Choices inferred from the code. Each one names its evidence; nothing here is a guess dressed as a fact.

## [Decision]

- **What:** [The choice that was made.]
- **Evidence:** [path:line, and what it shows.]
- **Why, apparently:** [The rationale the code supports. Say "inferred" when it is not written down anywhere.]
- **Tradeoff:** [What this buys and what it costs.]
- **Confidence:** [Confirmed by a comment or doc / inferred from the code / uncertain.]

## Gotchas

- **[Trap]:** [What looks wrong but is not, or what breaks in a non-obvious way.] `path:line`

## Conventions

- [A pattern the codebase follows consistently that a newcomer should match.]
````
