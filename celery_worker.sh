#!/bin/bash

cd {{ project_name }}
celery worker --beat --app {{ project_name }} --loglevel info
