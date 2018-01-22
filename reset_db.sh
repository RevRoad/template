#!/bin/bash

if [ "$1" == "makemigrations" ]; then
  rm <app_name>/migrations/00*.py
  python manage.py makemigrations
fi
mysql -uroot -e "DROP DATABASE <app_name>"
mysql -uroot -e "CREATE DATABASE <app_name>"
python manage.py migrate
# python manage.py loaddata initial