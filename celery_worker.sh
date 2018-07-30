#!/bin/bash

cd {{cookiecutter.project_slug}}
celery worker --beat --app {{cookiecutter.project_slug}} --loglevel info
