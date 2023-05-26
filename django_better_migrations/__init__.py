import django

from .apps import DEFAULT_CONFIGURATION

__version__ = "0.0.4"

if django.VERSION < (3, 2):
    default_app_config = "django_better_migrations.apps.MigrationsConfig"

__all__ = ["DEFAULT_CONFIGURATION"]
