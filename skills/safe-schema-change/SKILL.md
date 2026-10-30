---
name: safe-schema-change
description: Plan or implement a database schema change that must preserve live data and compatibility across application versions. Use for column or constraint changes, index rollouts, backfills, and expand-contract migrations. Not for designing a new empty database, generic SQL tuning, or applying production migrations without authorization.
metadata:
  author: rushikesh
---

# Safe Schema Change

Make each migration phase compatible, bounded, and verifiable. An executable migration file does not prove that a change is safe under live traffic.

## Establish the contract and target

Inspect the database engine and version, migration runner, transaction behavior, existing schema, data scale, and deployment order. Find affected readers and writers: old application versions, workers, reports, CDC consumers, external clients, and restore or rollback paths. Use the actual project's migration conventions.

State the invariant to preserve, such as no lost writes, unique identifiers, or old and new binaries both reading correctly during rollout. Identify malformed values, duplicates, NULLs, and conversion failures with bounded read-only checks before choosing a transformation. Exact full-table counts can themselves be expensive.

A planning request produces a concrete plan or reviewable SQL, not database mutations. An implementation request permits preparing files and appropriate local checks; applying changes to shared or production data requires authorization for that target. Reuse authorization already granted within that scope.

## Choose the smallest safe sequence

For a small empty table or a genuinely compatible additive change, a direct migration may be enough. Do not impose a multi-release process without a compatibility or operational reason.

When old and new code must coexist, separate these phases:

1. **Expand:** introduce a compatible schema shape. State how old code behaves before it knows about the new field or constraint.
2. **Coordinate writers:** define the source of truth and how every writer keeps the new representation current. Application dual writes alone do not cover older binaries or out-of-band writers. Check atomicity and partial failures; do not assume two successful-looking calls form a transaction.
3. **Backfill:** migrate historical data in bounded, restartable batches while preserving newer concurrent writes. Use a stable key or keyset cursor, a durable checkpoint when needed, and an idempotent update predicate. Do not overwrite fresh values with an older snapshot.
4. **Verify and switch:** reconcile the relevant values, constraints, and read results. Row counts alone do not establish equivalence. Define the observation period and the metric that permits new reads to become authoritative.
5. **Contract:** remove old fields or compatibility code only after old readers and writers are retired, lagging consumers have caught up, and the rollback window has closed. Keep this a separate deployment when those conditions cannot be established now.

For each phase, name its prerequisite, change, success check, stop condition, and recovery action. If a phase remains a proposal, label it clearly.

## Account for engine and runner behavior

Use version-specific official documentation for lock level, rewrite or scan behavior, transaction restrictions, and failure states. An ORM's small diff can still request a blocking operation.

For PostgreSQL, consider these distinctions when applicable:

- Many ALTER TABLE operations require strong locks even when they avoid a table rewrite. Long transactions can delay lock acquisition; queued DDL can also delay later work. Bound lock waits and stop instead of retrying indefinitely.
- `CREATE INDEX CONCURRENTLY` reduces write blocking but is not free or instantaneous, cannot run inside a transaction block, and can leave an invalid index after failure. Check runner transaction wrapping and index validity before retrying. Do not treat “index already exists” as proof of a successful build.
- `NOT VALID` followed by `VALIDATE CONSTRAINT` is available for supported constraint types, not as a universal option for every constraint. Check existing-data validation separately from enforcement on new writes.
- Defaults, type changes, partitioned objects, and uniqueness checks have version- and operation-specific behavior. Do not label a migration “zero downtime” without evidence for its workload and deployment path.

Backfills need bounded batches, throttling based on observed load, and stop thresholds for lock waits, replication lag, or error rate. Keep transactions short enough for the actual workload. Specify how to resume without skipping or duplicating logical work.

## Plan recovery before execution

Separate application rollback, schema rollback, and data recovery. Recreating a dropped column or table does not restore its contents, indexes, constraints, grants, or later writes. State which steps are irreversible and whether a forward fix is safer than a down migration.

For a consequential mutation, record the exact target, schema pre-state, expected post-state, verification query, and stop condition. Establish an appropriate tested restore or recovery path before destructive steps; a backup job's existence alone does not prove recoverability. Never delete data or persistent volumes to make a migration test pass.

## Verify and hand off

In an authorized local or staging environment, test the relevant old/new application combinations, conversion edge cases, an interrupted batch followed by resume, and concurrent writes during the backfill when that risk exists. Check the resulting schema and data, not merely the migration runner's exit status.

Deliver the plan or migration files, phase order, exact checks run, remaining rollout gates, and recovery limitations. Distinguish generated SQL, local execution, staging rehearsal, and production verification. Stop at the authorized boundary; do not apply the rollout just because the files are complete.
