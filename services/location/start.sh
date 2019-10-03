#!/bin/bash

gunicorn app:api -c /code/settings/gunicorn.py --reload