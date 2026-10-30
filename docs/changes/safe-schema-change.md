# New skill: safe-schema-change

You work with PostgreSQL, services, and data pipelines. Migration correctness depends on old/new consumers and concurrent writes, not only valid SQL.

Automatic selection is enabled for matching tasks; invoke it explicitly with `$safe-schema-change`. No additional skill, service, or connector is required. Use existing tools and access; missing runtime prerequisites remain explicit limitations.

## Research and scope

- [Database migration](https://github.com/wshobson/agents/blob/main/plugins/framework-migration/skills/database-migration/SKILL.md): staged schema transformations and recovery planning; replace unbounded updates and destructive restore examples with bounded, evidence-led phases.
- [PostgreSQL ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html): lock and constraint-validation behavior.
- [PostgreSQL CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html): concurrent index restrictions and failure states.

Sources inspected on 2026-10-30. This skill uses original wording and a narrower workflow; it does not vendor or install the referenced skills.

## Review examples

**Representative request:** Plan only: rename a populated column while old and new application versions both run.

**Expected behavior:** Keep old writers in the compatibility plan, define the authoritative value and concurrent-write guard, backfill in resumable batches, and defer dropping the old column. Do not execute SQL.

**Boundary request:** Create a new empty table for a throwaway local demo.

**Expected boundary:** Use a simple direct migration when appropriate; do not impose a multi-release expand-contract rollout.

These examples were checked manually.

## Independent scenario check

An independent agent planned a populated-column rename with overlapping old/new binaries. It preserved an authoritative field for old writers, chose a compatibility bridge, separated the resumable backfill from transaction-wrapped DDL, and deferred destructive contraction until the rollback window closed. Version-specific implementation details remained an explicit gate.

This was a read-only synthetic scenario evaluation, not a live database migration, query benchmark, or Linux network test.
