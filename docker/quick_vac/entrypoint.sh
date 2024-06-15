#!/bin/bash
# Stop on any error
set -e
set -o pipefail

if [[ "$RUN_MIGRATIONS" == "true" ]] || [[ "$RUN_MIGRATIONS" == "True" ]]; then
  alembic upgrade heads
fi

exec "$@"
