#!/usr/bin/env bash

# Fail hard and fast
set -eo pipefail

# Start supervisord
exec "$@"
