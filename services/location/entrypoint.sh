#!/bin/bash

NUM_WORKERS=2
TIMEOUT=3600

gunicorn --bind 0.0.0.0:5050 \
--workers $NUM_WORKERS \
--timeout $TIMEOUT \
--reload \
--log-level=DEBUG