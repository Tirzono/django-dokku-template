# Django Dokku Template

## Template

Using this template to create a new Django app is easy:

```bash
django-admin.py startproject --template=https://github.com/Tirzono/django-dokku-template/archive/master.zip -e py,md,example,json,sh -n Procfile {{cookiecutter.project_slug}} .
```

## Configuration

### Application

To create the app:

```bash
sudo dokku apps:create {{cookiecutter.project_slug}}
```

Set your environment on the dokku server:

```bash
sudo dokku config:set {{cookiecutter.project_slug}} DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.production
sudo dokku config:set {{cookiecutter.project_slug}} SECRET_KEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
```

### Database

Install postgres and create a new database:

```bash
sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git postgres
sudo dokku postgres:create {{cookiecutter.project_slug}}
sudo dokku postgres:link {{cookiecutter.project_slug}} {{cookiecutter.project_slug}}
```

### RabbitMQ

To create and couple RabbitMQ:

```bash
sudo dokku plugin:install https://github.com/dokku/dokku-rabbitmq.git rabbitmq
dokku rabbitmq:create {{cookiecutter.project_slug}}
dokku rabbitmq:link {{cookiecutter.project_slug}} {{cookiecutter.project_slug}}
```
