---
name: pipeline-forensics
description: Trace one record through a data pipeline (source database, CDC or change stream, message broker, consumer, sink database, report) to find the first hop where it goes missing, stale, duplicated, or wrong. Use when downstream data or reports do not match the source, updates are missed or arrive late, or a CDC, Kafka, queue, or ETL sync is suspected; do not use for single-service bugs with no data movement.
metadata:
  author: rushikesh
---

# Pipeline Forensics

Debug a data pipeline by following one concrete record through every hop, with evidence at each step. Aggregate symptoms like "reports are sometimes wrong" hide the failure; a single traced key shows exactly where the data stopped matching.

## Workflow

1. **Pin the symptom to keys.** Get 1 to 3 record IDs that have a known source value, the wrong or missing sink value, and the approximate time of the source change. If none are known, diff source against sink over a small time window (row counts, then per-key version or checksum) to find some.
2. **Map the hops before investigating.** Read the code and config and write the path down:
   - Capture: change stream, Debezium or logical replication, polling on a timestamp column, or application-level publish after save.
   - Broker: topic, partition count, partition key, retention and cleanup policy.
   - Consumer: group ID, commit strategy, batching, retries, dead-letter handling, concurrency model.
   - Transform: mapping and type conversion.
   - Sink write: the actual statement, conflict key, and any version guard.
   - Read path: views, row level security, timezone conversion, caches, materialized views.
3. **Trace each key hop by hop.** At every hop record when the record was seen, its value or version, and its position (oplog time, LSN, partition and offset). Keep a hop table as you go.
4. **Find the first divergent hop.** Everything before it is correct and everything after it is a consequence. Match the evidence against [references/failure-modes.md](references/failure-modes.md).
5. **Confirm the cause.** Find direct evidence, such as two events for one key on different partitions or an offset committed with no matching sink write, or reproduce it in a non-production environment. A plausible story is not a confirmed cause.
6. **Report** the hop table, the root cause with its evidence, fix options with tradeoffs, and a detection check so the same failure is caught next time.

## Hop Table

```markdown
| Hop | Evidence | Record state | Verdict |
| --- | --- | --- | --- |
| Source `orders` | `findOne({_id: "A17"})` at 10:02 IST | status=shipped, version=7 | OK |
| Topic `orders.cdc` | partition 3, offset 48122, 10:02:04 | status=shipped, version=7 | OK |
| Consumer `reporting-sync` | group committed 48130, no log line for key | not processed | **Diverges** |
| Sink `report.orders` | `SELECT ... WHERE id = 'A17'` | status=packed, version=6 | Stale |
```

## Report Format

- **Symptom:** what was wrong, for which keys, since when.
- **Hop table:** as above.
- **Root cause:** the first divergent hop, the failure mode, and the evidence that confirms it. Mark anything inferred as inference.
- **Fix options:** each with its tradeoff, for example a version-guarded upsert versus re-keying the topic.
- **Backfill:** how to repair records already affected, stated as a proposal.
- **Detection:** a reconciliation query, lag alert, or dead-letter alert that would have caught this.

## Safety Rules

- Stay read-only by default. Never reset consumer offsets, replay or delete topics, restart connectors, run backfills, or write to shared or production systems without explicit approval.
- Read topics without joining the real consumer group, for example with `kcat -C` and no `-G`, so investigation never moves production offsets.
- Timestamps from different systems come from different clocks and meanings (producer time versus broker append time, transaction start versus commit). Compare them with that in mind.
- Mask personal data from records in the report. Show keys and the fields that matter, not whole documents.
