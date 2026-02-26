release: python manage.py collectstatic --noinput --verbosity 3
web: gunicorn hackathon_main.wsgi:application --bind 0.0.0.0:$PORT --workers 3
