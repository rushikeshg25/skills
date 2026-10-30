# New skill: linux-network-trace

You use Linux, containers, networking, and backend services, while the agent may run on macOS. This skill makes the diagnostic vantage point explicit.

Automatic selection is enabled for matching tasks; invoke it explicitly with `$linux-network-trace`. No additional skill, service, or connector is required. Use existing tools and access; missing runtime prerequisites remain explicit limitations.

## Research and scope

- [Connectivity triage](https://github.com/wshobson/agents/blob/main/plugins/incident-response/skills/connectivity-triage/SKILL.md): bounded probes and separation of observed evidence from inferred fault domains; adapt the macOS workflow to Linux namespaces.
- [curl manual](https://curl.se/docs/manpage.html): bounded requests, cumulative timing, hostname-preserving address tests.
- [ip-route manual](https://man7.org/linux/man-pages/man8/ip-route.8.html): route lookup semantics.

Sources inspected on 2026-10-30. This skill uses original wording and a narrower workflow; it does not vendor or install the referenced skills.

## Review examples

**Representative request:** An API works from my laptop but times out in a Linux container. Diagnose it without changes.

**Expected behavior:** Establish the container vantage point, compare its resolver, route, proxy, and TCP behavior, and leave inaccessible boundaries unknown. Do not disable firewall rules or infer that laptop success proves container connectivity.

**Boundary request:** The connection is healthy, but a parser returns the wrong business value.

**Expected boundary:** Use application debugging; do not run network probes without a network symptom.

These examples were checked manually.

## Independent scenario check

An independent agent handled laptop-success/container-timeout evidence without Linux access. It declined to attribute the failure to a firewall, requested a bounded probe from the affected container, preserved proxy and hostname behavior, and proposed no configuration change.

This was a read-only synthetic scenario evaluation, not a live database migration, query benchmark, or Linux network test.
