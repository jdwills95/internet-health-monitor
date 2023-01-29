#!/bin/bash

set -e

exec python3 internet_health_logger.py &
exec python3 main.py