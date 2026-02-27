#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
readme_file="${README_FILE:-${repo_root}/README.md}"
username="${USERNAME:-${GITHUB_REPOSITORY_OWNER:-}}"

if [[ -z "${username}" ]]; then
  echo "USERNAME or GITHUB_REPOSITORY_OWNER is required."
  exit 1
fi

cache_bust="$(date -u +%Y%m%d)"

stats_block="$(cat <<EOF
<!-- GH_STATS_START -->
<img src="https://github-readme-streak-stats.herokuapp.com/?user=${username}&theme=tokyonight&hide_border=true&background=00000000&cache_bust=${cache_bust}" alt="GitHub Streak" />
<br />
<br />
<!-- GH_STATS_END -->
EOF
)"

if grep -q '<!-- GH_STATS_START -->' "${readme_file}" && grep -q '<!-- GH_STATS_END -->' "${readme_file}"; then
  BLOCK="${stats_block}" perl -0777 -i -pe 's/<!-- GH_STATS_START -->.*?<!-- GH_STATS_END -->/$ENV{BLOCK}/s' "${readme_file}"
else
  printf '\n%s\n' "${stats_block}" >> "${readme_file}"
fi

echo "Updated ${readme_file} streak block cache_bust=${cache_bust}"
