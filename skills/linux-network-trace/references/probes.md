# Bounded Linux connection probes

Choose only the probe that answers the current question. Run it from the affected host or existing container when authorized. These examples use placeholders, not discovered infrastructure. Set values from trusted incident evidence and pass them as quoted arguments; do not paste arbitrary incident text into executable commands.

## Resolver and route

```bash
# NAME is the affected hostname. timeout is a GNU coreutils command;
# check availability or use the host tool's supported timeout mechanism.
timeout 5s getent ahosts "$NAME"
dig +time=2 +tries=1 "$NAME" A
dig +time=2 +tries=1 "$NAME" AAAA

# ADDRESS is one observed destination IP; select the matching family.
ip -4 route get "$ADDRESS"
# For an IPv6 address instead:
ip -6 route get "$ADDRESS"
```

`getent` follows the host's name-service configuration; `dig` queries DNS and can bypass NSS behavior such as hosts-file mappings. Neither proves that a particular application uses the same resolver or cache. Note resolver scope, TTL, and the actual address used by the failing connection.

Route lookup reports the kernel's selected path in the current namespace. For a proxied connection, the first network peer may be the proxy rather than the URL's hostname. Do not inspect only the direct origin route and conclude the proxied path is healthy.

## Socket and port

```bash
# Filter results to the relevant port; process details may require permissions.
ss -ltn "sport = :$PORT"
ss -tn "dport = :$PORT"

# Confirm this host's nc variant supports these options before using them.
timeout 5s nc -z -w 3 "$NAME" "$PORT"
```

A listener check belongs on the serving host or namespace. A successful TCP probe confirms transport establishment, not TLS identity or application behavior. Preserve IPv4/IPv6 distinctions when comparing probes. Do not use port ranges or broad scans for a single-service incident.

## HTTP timing

Use a known, non-mutating endpoint within the authorized target. Keep authentication out of command text and output. Avoid verbose traces and response headers unless needed and safely redacted.

```bash
# URL is the actual affected http:// or https:// URL with no embedded secrets.
curl --silent --show-error --output /dev/null \
  --connect-timeout 5 --max-time 15 \
  --write-out 'status=%{http_code} dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} first_byte=%{time_starttransfer} total=%{time_total}\n' \
  --url "$URL"
```

Inspect the exit status as well as the HTTP status. An HTTP error can still produce a successful curl process exit without a fail option. A status of `000` does not identify a unique cause. No redirect following is enabled in this example; inspect a redirect before contacting another destination.

These timing values are cumulative. For a fresh direct HTTPS connection, approximate intervals are TCP = connect minus DNS, TLS = tls minus connect, and post-handshake first-byte wait = first_byte minus tls. For plain HTTP, `time_appconnect` is normally zero, so use the connect milestone instead. Proxies, connection reuse, and protocol differences change that interpretation; do not apply the subtraction mechanically to every run.

To isolate DNS while preserving HTTPS SNI and certificate hostname validation, a supported curl can use `--resolve "$NAME:$PORT:$ADDRESS"` with the original hostname URL. Format IPv6 addresses according to the installed curl version. Use only a trusted observed address. With proxies, name resolution and connection paths can differ, so this may not isolate origin DNS. Do not use `-k` or silently bypass an established proxy.

## Namespace and tool limits

Use an existing authorized container execution mechanism to run the same bounded checks. First verify its target identity and network namespace. Missing tools inside an image are a limitation, not permission to install packages, run a privileged container, or inspect unrelated processes.

For packet evidence, agree on a narrow capture filter and time/count limit first. Headers and payloads can contain credentials and private data even when the diagnostic goal is only TCP behavior. Prefer existing sanitized traces when they answer the question.
