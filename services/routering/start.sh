#!/bin/bash

gunicorn app:api -c /code/gunicorn.py --reload