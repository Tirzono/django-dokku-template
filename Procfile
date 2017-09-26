web: gunicorn --pythonpath {{ project_name }} {{ project_name }}.wsgi
worker: celery worker --beat --app {{ project_name }} --loglevel info
