---
name: postgres-query-plan
description: Diagnose a slow PostgreSQL query using EXPLAIN plans, representative parameters, schema, indexes, and workload evidence. Use for query-plan interpretation or SQL performance investigation; not for generic schema design, database provisioning, or cross-system record tracing.
metadata:
  author: rushikesh
---

# Postgres Query Plan

Find where a query spends work, explain why, and propose the smallest change supported by evidence. A sequential scan is not a defect by itself, and a new index is not a result until correctness and workload impact are checked.

## Establish the workload

Capture the query shape, parameter types and representative selectivities, PostgreSQL version, relevant table sizes, indexes, and the observed symptom. Distinguish one slow execution from high aggregate cost. Ask for an existing sanitized plan when database access is unavailable; do not invent row counts or timings.

Record the database role, search path, RLS context, prepared-statement behavior, and relevant session settings when they can affect the plan. Prefer targeted metadata and existing statistics over full-table scans or broad configuration dumps. Preserve secrets and sensitive parameter values outside reports.

Confirm whether the delay is execution, lock waiting, connection acquisition, or result transfer. A fast server plan does not rule out pool waits, application N+1 queries, or a large result being serialized and sent to the client.

## Collect the right plan safely

Start with supplied evidence or plain `EXPLAIN` for estimates. Cost units are planner estimates, not milliseconds. Use the server version's documentation to interpret available fields.

`EXPLAIN ANALYZE` executes the statement. Treat it as workload execution, even for a SELECT that invokes functions or locks rows. Only run it when that workload and environment are authorized, with bounded statement and lock timeouts appropriate to the task. Prefer a representative local or staging copy for expensive or effectful statements. Wrapping a statement in a rollback does not undo every possible effect, such as sequence advancement or external function effects.

When actual execution is appropriate, `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)` or the text equivalent provides runtime evidence. `TIMING OFF` can reduce per-node timing overhead when row counts and overall execution time are enough. Do not enable extensions, run maintenance, change planner settings globally, or build indexes as part of read-only diagnosis.

## Read the work, not just the top node

Follow the data from scans through joins, aggregation, sorting, and limits. Locate the first material mismatch between estimated and actual rows and explain how it affects later work.

- Account for `loops`: reported actual row counts and node times are generally per-loop averages. Do not sum inclusive parent and child times as independent costs. Parallel nodes need worker-aware interpretation.
- Compare index conditions with residual filters and rows removed. Check selectivity, type casts, expression matching, partial-index predicates, and index column order against the actual query.
- Inspect sort method, temporary I/O, hash batches, buffer activity, and heap fetches for index-only scans. A shared-buffer read is not proof of physical disk I/O because the operating system may cache it.
- Check join fan-out and repeated inner scans. Preserve duplicate, NULL, ordering, and limit semantics before suggesting a rewrite.
- For parameter-sensitive queries, compare a small, typical, and large match set when evidence permits. A custom plan for one literal does not prove that the application's generic prepared plan will behave the same way.

A sequential scan can be appropriate for a small table or a query reading much of it. Planner switches are diagnostic experiments, not permanent fixes. A proposed index must account for storage, write cost, overlapping indexes, and deployment constraints.

## Test a specific explanation

State the suspected mechanism and a result that could disprove it. Examples: a cardinality error due to correlated predicates, a nonmatching expression index, or repeated probes caused by unexpected join fan-out. Prefer the next measurement that separates plausible explanations.

When implementation is requested, make one candidate change in the authorized environment and compare the same query contract, parameters, role, data distribution, and relevant settings. Check equivalent results including duplicates and NULLs. Compare repeated measurements with cache state and concurrency noted; do not claim a speedup from one noisy sample or an empty fixture.

If statistics maintenance, index creation, or a schema change is needed, present the exact proposal and its operational cost. Implementation permission for local code does not authorize production DDL or global configuration changes.

## Report and stop

Return the observed bottleneck, decisive plan fields, confirmed versus inferred cause, and the smallest proposed or tested fix. Include before/after evidence when available, semantic checks, tradeoffs, and remaining uncertainty. With an estimate-only plan, explicitly leave runtime performance unverified.

Stop when the measured requirement is met or the next missing observation is identified. Do not keep adding indexes or infrastructure to improve a synthetic number.
