#!/bin/bash

NUM_WORKERS=2
TIMEOUT=3600
#python manage.py migrate
yarn --modules-folder ./application/static/assets
gunicorn --bind 0.0.0.0:8000 \
--workers $NUM_WORKERS \
--timeout $TIMEOUT \
--reload \
--log-level=warning \
--worker-class gevent client.wsgi
