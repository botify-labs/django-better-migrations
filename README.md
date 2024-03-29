Django Better Migrations
========================

[![Deployed to PyPI](https://img.shields.io/pypi/pyversions/django-better-migrations?logo=pypi&logoColor=white)](https://pypi.org/pypi/django-better-migrations)
[![GitHub Repository](https://img.shields.io/github/stars/botify-labs/django-better-migrations?logo=github)](https://github.com/botify-labs/django-better-migrations/)
[![Continuous Integration](https://img.shields.io/github/actions/workflow/status/botify-labs/django-better-migrations/ci.yml?logo=github)](https://github.com/botify-labs/django-better-migrations/actions?workflow=CI)
[![MIT License](https://img.shields.io/github/license/botify-labs/django-better-migrations?logo=open-source-initiative&logoColor=white)](https://github.com/botify-labs/django-better-migrations/blob/main/LICENSE)

This project aims at providing improvements to Django's default migration system.


More informations in the documentation, see "docs/" folder.


Example
-------

See below migration, generated automatically via `manage.py makemigrations`:
```python
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-01 00:00
from __future__ import unicode_literals

from django.db import migrations, models


# Generated SQL code (sqlite):
#
# --
# -- Create model Person
# --
# CREATE TABLE "example_app_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
#

# Check results:
# CHECK OK: No ALTER TABLE ADD COLUMN with non-NULL constraint
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
```


License
-------

MIT, see `LICENSE` file.
