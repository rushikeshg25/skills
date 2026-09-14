#!/usr/bin/env bash
# Append one entry to today's decision log, creating the file with its header if needed.
#
# Usage:
#   bash log-entry.sh "Short step label" <<'EOF'
#   - **Decision:** ...
#   - **Alternatives:** ...
#   EOF
#
# Writes to logs/YYYY-MM-DD.md under the git repository root, or under the
# current directory outside git. Prints the log path on success.
set -euo pipefail

label=${1:-}
if [ -z "$label" ]; then
  echo 'usage: log-entry.sh "Short step label" < entry-body' >&2
  exit 2
fi

body=$(cat)
if [ -z "${body//[[:space:]]/}" ]; then
  echo "log-entry.sh: entry body on stdin is empty" >&2
  exit 2
fi

root=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
now=$(date '+%F %H:%M')
day=${now% *}
time=${now#* }
log="$root/logs/$day.md"

mkdir -p "$root/logs"
[ -f "$log" ] || printf '# Session Log — %s\n' "$day" > "$log"
printf '\n## %s - %s\n\n%s\n' "$time" "$label" "$body" >> "$log"
echo "$log"
