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
4. **Find the first evidenced divergence.** Compare the same key and logical version at adjacent hops. If a hop lacks evidence, mark it unknown and report the interval where divergence could have occurred; do not claim that everything before it is correct. Match the evidence against [references/failure-modes.md](references/failure-modes.md).
5. **Confirm the cause.** Find direct evidence of the mechanism, such as a stale event overwriting a newer sink version, or reproduce it in a non-production environment. Events on different partitions and advanced offsets are leads; connect them to the incorrect outcome before naming a cause. A plausible story is not a confirmed cause.
6. **Report** the hop table, the root cause with its evidence, fix options with tradeoffs, and a detection check so the same failure is caught next time.

## Hop Table

```markdown
| Hop | Evidence | Record state | Verdict |
| --- | --- | --- | --- |
| Source `orders` | `findOne({_id: "A17"})` at 10:02 IST | status=shipped, version=7 | OK |
| Topic `orders.cdc` | partition 3, offset 48122, 10:02:04 | status=shipped, version=7 | OK |
| Consumer `reporting-sync` | partition 3 committed next offset 48130; no retained log for key | processing outcome unknown | **Unknown** |
| Sink `report.orders` | `SELECT ... WHERE id = 'A17'` | status=packed, version=6 | Stale |
```

## Separate missing data from missing evidence

Record the observation time and scope of each probe. Match source version, event identity, partition/offset, transform result, and sink version before comparing values. A current source read can be newer than the captured event; retention or compaction may have removed an older event.

A missing log line does not prove a record was skipped. A committed Kafka offset normally identifies the next record to consume in that partition; it does not independently prove a particular sink transaction succeeded. Check the commit strategy and durable write evidence. Lag reaching zero is also not proof of source/sink equality.

Keep competing explanations explicit, such as capture loss, delayed processing, stale overwrite, or a read filter. Choose the smallest read-only probe that distinguishes them and state what each possible result would imply. Use a narrow key/time window and bounded reads; broaden only when the evidence requires it.

Stop at a confirmed cause or a precisely located evidence gap. The report should identify the missing observation needed to continue instead of upgrading a plausible explanation into a root cause.

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
