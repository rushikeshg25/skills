# Overbuild Check: [Project or Feature]

> Checked: [YYYY-MM-DD]

## Verdict

**[Build as planned / Build the boring version first / Build as a capped learning project / Don't build]**

[One or two sentences on why.]

## Intent

[Learning / Product / Both, and what that means for this project.]

## Requirements

| Requirement | Value | Source |
| --- | --- | --- |
| Peak load | [e.g. 50 req/s] | [Measured / Estimate / Assumption] |
| Data volume and growth | [e.g. 20 GB, +2 GB/month] | [Measured / Estimate / Assumption] |
| Latency target | [e.g. p99 under 300 ms] | [Measured / Estimate / Assumption] |
| Durability and consistency | [e.g. no lost events, eventual consistency OK] | [Measured / Estimate / Assumption] |
| Ops time available | [e.g. 2 hours/week] | [Measured / Estimate / Assumption] |

## Components

| Component | Forced by | Boring alternative | Switch trigger | Monthly cost |
| --- | --- | --- | --- | --- |
| [Kafka] | [Requirement, or "nothing yet"] | [Postgres `SKIP LOCKED` queue] | [Measured threshold] | [$ or formula] |

## Cost

- **Expected scale:** [$ per month, with the formula or pricing source and date]
- **10x scale:** [$ per month]
- **Idle cost at zero traffic:** [$ per month and what drives it]
- **Ops time:** [hours per week]

## Outcome

[One measurable outcome with a date.]

## Kill Criteria

- [Cost ceiling, e.g. over $X/month for 2 months]
- [Outcome missed by date]
- [Ops time over N hours/week for a month]

## Exit Plan

- [Data export]
- [Infrastructure teardown command]
- [Portfolio evidence kept: README, architecture, benchmarks, demo recording, local run path]
