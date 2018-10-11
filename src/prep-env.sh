#!/bin/bash

pipenv run pip install pip==18.0
pipenv install

pipenv run python manage.py makemigrations
python manage.py runserver && gunicorn fagottino.wsgi -b 0.0.0.0:8000

