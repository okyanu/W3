#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
TIMEOUT=12000

/usr/local/bin/gunicorn moda.wsgi -t $TIMEOUT -w 4  -b 0.0.0.0:5000 --chdir=/app
exec "$@"