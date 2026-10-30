---
name: linux-network-trace
description: Diagnose a Linux host or container connection failure across resolver, route, TCP, TLS, proxy, and application boundaries. Use for timeouts, connection refusals, DNS failures, or host-versus-container connectivity differences. Not for broad network scanning, changing firewall rules, or general application bugs with a healthy connection.
metadata:
  author: rushikesh
---

# Linux Network Trace

Trace the actual failing connection from the affected process's environment. Success from a laptop or a different container does not prove that path works.

## Pin down the connection

Record the source host, process or container, destination hostname and port, protocol, exact failure, approximate time, and whether it is intermittent. Identify proxies, VPNs, load balancers, and namespaces only as evidence establishes them.

Verify the host executing commands separately from the host under investigation. If the agent runs on macOS and the failing service runs on Linux, use authorized access to the Linux target or provide targeted commands for that host. Do not treat macOS output as Linux evidence.

Start with existing error messages and configuration fields relevant to the connection. Proxy URLs, environment variables, request headers, and packet captures can contain credentials; inspect only required fields and redact before output. Do not dump a process's full environment or entire request bodies.

## Follow the first uncertain boundary

Choose the next probe to distinguish explanations; do not run every command as a checklist. Read [references/probes.md](references/probes.md) when choosing Linux commands or HTTP timing probes.

1. **Resolver:** compare the application's resolver path with the observed A/AAAA results. Name-service configuration, split DNS, search suffixes, and application caches can differ. `dig` and `getent` answer different questions.
2. **Route and namespace:** check the route to an observed destination address from the affected namespace. Account for IPv4 versus IPv6, policy routing, interfaces, and proxy routing. A route lookup does not prove end-to-end reachability.
3. **TCP:** distinguish refusal, timeout, and established connection. Inspect the expected listener on the server when access permits. A refusal may come from a listener absence or an active rejection; a timeout alone does not locate a firewall.
4. **TLS:** preserve the hostname for SNI and certificate validation when testing an address. Check the certificate name, chain, time validity, and relevant trust store. Disabling validation does not fix or verify TLS.
5. **HTTP or other application protocol:** record the status or protocol error after transport succeeds. A 401 or 403 establishes a responding component, not successful authorization or necessarily a healthy origin. Check whether the response came from a proxy, load balancer, or the application.

Compare with a known-good connection only when it differs in one useful dimension, such as the same endpoint from the host and container. Keep request method, hostname, address family, proxy use, and credentials comparable; explain differences that remain.

## Interpret probes conservatively

Failed ping can mean ICMP filtering; successful ping does not prove the service port works. Silent traceroute hops are not proof of packet loss at those routers. TCP success does not establish TLS or application success.

HTTP timing fields are cumulative milestones. Separate connect, TLS, and first-byte intervals before attributing delay. Time to first byte includes server work and may include proxy effects; it is not a pure network-latency measurement. Compare fresh and reused connections deliberately.

For intermittent failures, capture a small timestamped sample with endpoint address, namespace, failure stage, and relevant timeout. Look for changing DNS answers, family selection, reconnects, saturation, or proxy differences. Keep probe count and duration bounded; do not launch a load test to diagnose one connection.

## Preserve the diagnostic state

Use read-only inspection and bounded requests to an authorized, non-mutating endpoint. Do not flush DNS, restart services, alter routes, disable TLS checks, modify firewall/VPN rules, or create privileged debug containers merely to get a green probe.

Entering an existing namespace or accessing another host must be within granted permissions. Use installed tools when possible; report missing capabilities instead of silently installing packages or escalating privileges. Packet capture is a separate step: establish its interface, filter, duration, permissions, and sensitive-data handling before using it.

## Report and stop

Return the connection tuple and vantage point, a compact list of observations by boundary, the narrowest supported failure domain, and the next check or proposed fix. Mark hypotheses and unavailable evidence explicitly. Include the exact sanitized commands and their outcomes when useful.

Stop when the failure boundary is established or a specific access/evidence gap prevents narrowing it further. A repair request can authorize a later change, but verify that repair from the original failing vantage point, not only from the agent's machine.
