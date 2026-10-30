# New skill: postgres-query-plan

You work with PostgreSQL and backend performance. This skill connects plan interpretation to application behavior and avoids speculative index changes.

Automatic selection is enabled for matching tasks; invoke it explicitly with `$postgres-query-plan`. No additional skill, service, or connector is required. Use existing tools and access; missing runtime prerequisites remain explicit limitations.

## Research and scope

- [Supabase Postgres best practices](https://github.com/supabase/agent-skills/blob/main/skills/supabase-postgres-best-practices/SKILL.md): targeted query, index, locking, and diagnostic guidance.
- [SQL optimization patterns](https://github.com/wshobson/agents/blob/main/plugins/developer-essentials/skills/sql-optimization-patterns/SKILL.md): plan-first investigation; do not adopt blanket index-good/scan-bad heuristics.
- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html): execution semantics and measurement options.

Sources inspected on 2026-10-30. This skill uses original wording and a narrower workflow; it does not vendor or install the referenced skills.

## Review examples

**Representative request:** Use $postgres-query-plan on this estimated plan: Seq Scan on a 30-row table; no runtime measurements are available.

**Expected behavior:** Do not call the scan a defect or invent latency. Request representative runtime evidence only if needed and authorized. Leave performance unverified.

**Boundary request:** Design a new customer table without a performance symptom.

**Expected boundary:** Use ordinary schema design; do not force query-plan diagnosis.

These examples were checked manually.

## Independent scenario check

An independent agent applied the skill to an estimate-only sequential-scan plan. It distinguished planner cost from time and estimated output rows from table size, refused to promise an index speedup, and requested workload evidence without executing production SQL.

This was a read-only synthetic scenario evaluation, not a live database migration, query benchmark, or Linux network test.
