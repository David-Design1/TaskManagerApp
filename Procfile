web: python manage.py collectstatic --noinput && gunicorn task_manager.wsgi --log-level debug
worker: celery -A task_manager worker -l info
beat: celery -A task_manager beat -l info