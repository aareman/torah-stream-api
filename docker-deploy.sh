#!/usr/bin/env bash

poetry install

. .venv/bin/activate

python manage.py migrate --noinput

python manage.py collectstatic --noinput

gunicorn app.wsgi:application -c gunicorn.conf.py
