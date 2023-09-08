#!/bin/sh

# clean data in database
#python manage.py flush --no-input

# migration to application
python app_django.py makemigrations
python app_django.py migrate
# collect static files
python app_django.py collectstatic --no-input --clear

# create superuser for postgres
# python manage.py createsuperuser --email=admin@admin.com --noinput

python app_django.py runserver 0.0.0.0:8000