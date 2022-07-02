#! /bin/bash
#python manage.py makemigrations --settings=app.base
#python manage.py migrate --settings=app.base
python3 manage.py collectstatic 
python3 manage.py runserver 0.0.0.0:8000 
#daphne -b 0.0.0.0 -p 8000 app.asgi:application