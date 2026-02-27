#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
readme_file="${README_FILE:-${repo_root}/README.md}"
username="${USERNAME:-${GITHUB_REPOSITORY_OWNER:-}}"

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "GITHUB_TOKEN is required."
  exit 1
fi

if [[ -z "${username}" ]]; then
  echo "USERNAME or GITHUB_REPOSITORY_OWNER is required."
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required."
  exit 1
fi

export GH_TOKEN="${GITHUB_TOKEN}"

created_at="$(gh api graphql \
  -f query='query($login:String!){user(login:$login){createdAt}}' \
  -f login="${username}" \
  --jq '.data.user.createdAt')"

if [[ -z "${created_at}" || "${created_at}" == "null" ]]; then
  echo "Unable to read createdAt for user ${username}."
  exit 1
fi

start_year="$(date -u -d "${created_at}" +%Y)"
end_year="$(date -u +%Y)"
now_iso="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

total_contributions=0

for year in $(seq "${start_year}" "${end_year}"); do
  from="${year}-01-01T00:00:00Z"
  to="${year}-12-31T23:59:59Z"

  if [[ "${year}" == "${start_year}" ]] && [[ "${created_at}" > "${from}" ]]; then
    from="${created_at}"
  fi

  if [[ "${year}" == "${end_year}" ]]; then
    to="${now_iso}"
  fi

  year_total="$(gh api graphql \
    -f query='query($login:String!,$from:DateTime!,$to:DateTime!){user(login:$login){contributionsCollection(from:$from,to:$to){contributionCalendar{totalContributions}}}}' \
    -f login="${username}" \
    -f from="${from}" \
    -f to="${to}" \
    --jq '.data.user.contributionsCollection.contributionCalendar.totalContributions')"

  if [[ -z "${year_total}" || "${year_total}" == "null" ]]; then
    year_total=0
  fi

  total_contributions=$((total_contributions + year_total))
done

stats_block="$(cat <<EOF
<!-- GH_STATS_START -->
### Contribution Snapshot
- Total contributions (all years): **${total_contributions}**
<!-- GH_STATS_END -->
EOF
)"

if grep -q '<!-- GH_STATS_START -->' "${readme_file}" && grep -q '<!-- GH_STATS_END -->' "${readme_file}"; then
  BLOCK="${stats_block}" perl -0777 -i -pe 's/<!-- GH_STATS_START -->.*?<!-- GH_STATS_END -->/$ENV{BLOCK}/s' "${readme_file}"
else
  printf '\n%s\n' "${stats_block}" >> "${readme_file}"
fi

echo "Updated ${readme_file} with total contributions: ${total_contributions}"
