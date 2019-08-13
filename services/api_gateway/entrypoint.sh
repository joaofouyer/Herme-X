#!/bin/bash

NUM_WORKERS=2
TIMEOUT=3600
python manage.py migrate

gunicorn --bind 0.0.0.0:8008 \
--workers $NUM_WORKERS \
--timeout $TIMEOUT \
--reload \
--log-level=DEBUG \
--worker-class gevent api_gateway.wsgi
