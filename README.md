Django Dokku Template
=====================

Using this template to create a new Django app is easy:

```bash
$ django-admin.py startproject --template=https://github.com/Tirzono/django-dokku-template/archive/master.zip --name=Procfile --name=README.md --name=settings_module.example --name=secrets.json.example {{ project_name }}
```

Install postgres and create a new database:

```bash
$ sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git postgres
$ sudo dokku postgres:create {{ project_name }}
$ sudo dokku postgres:link {{ project_name }} {{ project_name }}
```

Set your environment on the dokku server:

```bash
$ sudo dokku config:set {{ project_name }} DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
```
