from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from {{ project_name }}.settings import set_settings_module


set_settings_module()

app = Celery('{{ project_name }}')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
