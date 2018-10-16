#!/bin/bash

python manage.py migrate; gunicorn fagottino.wsgi -b 0.0.0.0:8000