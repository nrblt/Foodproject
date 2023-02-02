#!/bin/sh/

set -e 

python manage.py wait_for_db
python manage.py collecstatic --noinput
python manage.py migrate

uwgsi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
