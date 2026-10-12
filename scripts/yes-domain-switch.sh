#!/bin/sh
# Point the Yes site's canonical URLs, share tags and structured data at
# yesmcpasd.org. Run once, after yesmcpasd.org is a custom domain on the
# Pages project, then set YES_DOMAIN_LIVE=1 (Pages > Settings > Variables)
# so openseatsmcpasd.org/yes/... 301s to the new domain.
set -e
cd "$(dirname "$0")/.."
find yes -name '*.html' -exec sed -i 's#https://openseatsmcpasd.org/yes/#https://yesmcpasd.org/#g' {} +
grep -rl 'openseatsmcpasd.org/yes' yes && { echo "leftover openseatsmcpasd.org/yes references above"; exit 1; } || true
echo "Done. Commit, push to main, then set YES_DOMAIN_LIVE=1 and redeploy."
