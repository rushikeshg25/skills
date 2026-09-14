# Pipeline Failure Modes

Grouped by the hop where the record first diverges. Each entry lists the symptom and how to check it. Commands are examples; adapt names, and keep every check read-only.

## Capture

**Change stream history lost.** A consumer was down longer than the oplog window, so its resume token no longer exists. Updates in the gap are never emitted.
- Check the oplog window with `rs.printReplicationInfo()` and compare it to consumer downtime.
- Search connector or consumer logs for `ChangeStreamHistoryLost` or resume token errors, and look for a restart that began from "now".

**Partial update events.** A MongoDB change stream opened without `fullDocument: 'updateLookup'` emits only `updateDescription` for updates. A consumer that treats the event as a whole document drops or nulls the other fields. With `updateLookup`, the document is looked up later and can be newer than the event, or null if deleted.
- Inspect a raw update event for the key and compare its fields with what the consumer writes.

**Timestamp polling misses rows.** Polling `updated_at > last_watermark` skips rows that share the watermark timestamp, and rows from long transactions. In PostgreSQL `now()` is the transaction start time, so a row committed after the poll can carry an earlier timestamp.
- Look for sink-missing rows whose `updated_at` equals a batch boundary or falls just before one.
- Check how long the writing transactions run.

**Writes bypass capture.** With application-level publishing, direct database edits, migrations, and bulk scripts never produce events. With dual writes, the database commit can succeed while the publish fails.
- Find who wrote the missing change: the application, a script, or a migration.
- Search for publish errors near the change time. An outbox table fixes the dual-write case.

**Replication slot lost or lagging.** For Debezium or logical replication on PostgreSQL, a dropped slot or removed WAL means a gap, and a lagging slot means delay.
- Run `SELECT slot_name, active, wal_status, pg_wal_lsn_diff(pg_current_wal_lsn(), confirmed_flush_lsn) AS lag_bytes FROM pg_replication_slots;`

## Broker

**Partition key is not the entity ID.** Updates for one entity land on different partitions and are consumed out of order, so an older state can be applied last.
- List every event for the key with its partition and offset: `kcat -b $BROKER -C -t $TOPIC -o s@$START_MS -o e@$END_MS -f '%p %o %T %k\n' | grep $KEY`
- Events for one key on more than one partition confirm it. Check the producer's key setting.

**Events expired before consumption.** A lagging consumer falls behind `retention.ms`. Its offset goes out of range and `auto.offset.reset=latest` silently skips ahead.
- Check topic config with `kafka-configs.sh --bootstrap-server $BROKER --entity-type topics --entity-name $TOPIC --describe --all`.
- Search consumer logs for offset reset or out-of-range messages.

**Produce failures swallowed.** Send errors are not checked, or a record exceeds the size limit (`RecordTooLargeException`, `MESSAGE_TOO_LARGE`).
- Search producer logs near the change time and confirm whether send results are awaited.

## Consumer

**Offset committed before processing.** Auto-commit, or a commit issued before the sink write finishes, loses the batch on a crash or error. In kafka-go, `Reader.ReadMessage` commits automatically when `GroupID` is set; `FetchMessage` followed by `CommitMessages` after the write is the safe pattern.
- Find where commits happen relative to the sink write, then look for crashes or deploys near the change time.

**Errors logged and skipped.** A failed message is logged and its offset committed anyway, or it goes to a dead-letter topic nobody reads.
- Search consumer logs for the key and inspect the dead-letter topic.

**Lag.** Updates arrive late rather than never.
- Run `kafka-consumer-groups.sh --bootstrap-server $BROKER --describe --group $GROUP` and compare `LAG` over time.

**Rebalance loops.** Processing a batch takes longer than `max.poll.interval.ms`, so the consumer is removed from the group, work is redone, and lag grows.
- Search for rebalance and "leaving group" messages and compare batch processing time with the setting.

**Concurrency breaks ordering.** A worker pool processes messages from one partition in parallel, so per-key order is lost even with correct keys.
- Read the dispatch code. Routing work to workers by key hash preserves per-key order.

**Poison message.** One record fails on every retry and blocks its partition, so everything behind it stalls.
- Look for a partition whose committed offset stops moving while others advance.

**Duplicates.** Delivery is at least once, so redelivered events create duplicate rows when the sink insert is not idempotent.
- Count sink rows per key. Make the write an upsert on a natural key.

## Sink

**Upsert without a version guard.** Arrival order wins, so a stale or reordered event overwrites a newer row.
- Check the statement for a guard, for example `INSERT INTO orders AS t (...) VALUES (...) ON CONFLICT (id) DO UPDATE SET ... WHERE t.version < EXCLUDED.version`.

**Batch rolled back after offsets committed.** One bad row fails the whole transaction, the error is handled, and the offsets are committed anyway.
- Match sink transaction errors with commit timing.

**Type and shape conversion.** ObjectId to string, Decimal128 to float precision loss, dates as ISO strings versus epoch milliseconds, and a missing field written as `NULL` over an existing value.
- Compare the raw event field by field with the written row.

**Deletes not applied.** Delete events carry only the key, and Debezium follows a delete with a tombstone whose value is null. A consumer that ignores or crashes on these never removes rows.
- Check that delete events and null values are handled.

## Read Path

**Timezone conversion.** For a `timestamp without time zone` column holding UTC, the correct conversion is `(ts AT TIME ZONE 'UTC') AT TIME ZONE 'Asia/Kolkata'`; a single `AT TIME ZONE` shifts the wrong way. For `timestamptz`, the session `TimeZone` setting changes `::date` results, so day boundaries differ between IST and UTC reports.
- Compare `pg_typeof(ts)`, the session timezone, and the report query's conversion for an affected row.

**Row level security or view filters hide rows.** The report role sees fewer rows than the sync role. Policies may depend on settings such as `current_setting('app.include_drafts', true)`. Superusers and roles with `BYPASSRLS` skip policies, and table owners skip them unless `FORCE ROW LEVEL SECURITY` is set.
- Read `SELECT * FROM pg_policies WHERE tablename = '$TABLE';`
- Run the report query in a session with `SET ROLE $REPORT_ROLE;`.

**Stale cache or materialized view.** The sink row is correct but the report reads an old copy.
- Query the base table directly, then check the cache TTL or the `REFRESH MATERIALIZED VIEW` schedule.
