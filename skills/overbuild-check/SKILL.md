---
name: overbuild-check
description: Pressure-test an infrastructure-heavy plan before building it by separating learning goals from product goals, naming the boring alternative for each component, estimating running cost, setting one measurable outcome, and writing kill criteria. Use before adding or proposing distributed or infrastructure components (Kafka, Kubernetes, queues, caches, microservices, custom databases, vector stores, GPU serving), when starting a side project with a complex architecture, or when the user asks whether something is overkill; skip small, reversible changes.
metadata:
  author: rushikesh
---

# Overbuild Check

Complex systems are fine when they earn their place. Decide what "earning it" means before the first component is deployed, while changing course is still cheap.

## Workflow

1. **Classify the intent.** This changes the verdict more than any other input, so ask when it is unclear.
   - *Learning:* the complexity is the point. Cap the time and money instead of removing it.
   - *Product:* every component must pay for itself in user-visible value or required scale.
   - *Both:* build the product on the boring default and isolate the learning component where it cannot take the product down.
2. **Pin requirements to numbers.** Users, peak requests per second, data volume and growth, latency targets, durability and consistency needs, and ops hours available per week. Label anything unknown as an assumption with an estimate. Never invent traffic to justify a design.
3. **Challenge each component.** For every piece of infrastructure, write which requirement forces it, the boring alternative that meets today's numbers, and the measurable trigger for switching later. State thresholds as estimates and say how to measure them.
4. **Estimate monthly cost** at expected scale and at 10x. Include always-on costs that exist at zero traffic, such as managed control planes, minimum broker or node counts, load balancers, NAT gateways, and idle GPUs, plus ops hours. Use current pricing pages when available; otherwise leave the formula with placeholders. Never make up prices.
5. **Set one measurable outcome with a date.** Product example: "10 external teams sending logs weekly by 2026-12-01". Learning example: "demo a consumer group rebalance under injected broker failure and explain every log line".
6. **Write kill criteria and an exit plan.** Decide in advance what stops or pauses the project: a cost ceiling, a missed outcome date, or ops time above a limit. Plan a cheap shutdown that keeps the project's value: export data, tear down infrastructure as code, and keep a README with the architecture, benchmark numbers, a recorded demo, and a local run path (for example Docker Compose) so it stays demoable at zero cost.

## Common Boring Alternatives

| Proposed | Boring alternative | Switch when (measure it) |
| --- | --- | --- |
| Kafka or RabbitMQ | PostgreSQL job table with `FOR UPDATE SKIP LOCKED`, or Redis Streams if Redis already runs | Throughput, fan-out, or replay needs exceed what the table handles |
| Kubernetes | One VM with Docker Compose or systemd, or a managed container service | Many services need independent scaling or multi-node scheduling |
| Microservices | Modules with clear boundaries in one deployable | Parts need separate deploy cadence, scaling, or ownership |
| Redis cache | Better indexes, an in-process cache, or a materialized view | Measured database load or shared cache across instances |
| Dedicated vector database | `pgvector` in the existing PostgreSQL | Measured index size or query latency outgrows it |
| Custom storage engine | PostgreSQL or SQLite | The engine itself is the product or the learning goal |
| Workflow engine | Cron plus idempotent jobs and a status table | Long multi-step workflows with complex retries and compensation |
| Dedicated GPU serving | A hosted endpoint, scale-to-zero GPU, or local inference while prototyping | Sustained utilization makes dedicated hardware cheaper, or data must stay in-house |

## Output

Produce a short report from [assets/overbuild-check-template.md](assets/overbuild-check-template.md) with one of four verdicts:

- **Build as planned:** every component is forced by a requirement.
- **Build the boring version first:** ship on the alternatives and record the switch triggers.
- **Build as a capped learning project:** keep the complexity and enforce the time and cost caps.
- **Don't build:** the outcome does not justify the cost or effort.

Present the report in the conversation. Save it as a file only when the user asks, defaulting to `OVERBUILD_CHECK.md`. If the `decision-log` skill is active, log the verdict there.

## Rules

- Do not argue against learning projects. Cap them.
- Recommend; the user decides.
- Skip the check for small, reversible choices that are cheap to undo.
- Keep the report concrete and short. Numbers and triggers, not opinions about technology.
