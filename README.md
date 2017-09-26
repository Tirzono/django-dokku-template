# Django Dokku Template

## Template

Using this template to create a new Django app is easy:

```bash
django-admin.py startproject --template=https://github.com/Tirzono/django-dokku-template/archive/master.zip --name=Procfile --name=README.md --name=settings_module.example --name=secrets.json.example --name=app.json {{ project_name }}
```

## Configuration

### Application

To create the app:

```bash
sudo dokku apps:create {{ project_name }}
```

Set your environment on the dokku server:

```bash
sudo dokku config:set {{ project_name }} DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
sudo dokku config:set {{ project_name }} SECRET_KEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
```

### Database

Install postgres and create a new database:

```bash
sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git postgres
sudo dokku postgres:create {{ project_name }}
sudo dokku postgres:link {{ project_name }} {{ project_name }}
```

### RabbitMQ

To create and couple RabbitMQ:

```bash
sudo dokku plugin:install https://github.com/dokku/dokku-rabbitmq.git rabbitmq
dokku rabbitmq:create {{ project_name }}
dokku rabbitmq:link {{ project_name }} {{ project_name }}
```
