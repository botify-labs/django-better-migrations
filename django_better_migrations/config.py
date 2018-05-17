from django.apps import AppConfig
from django.conf import settings

import django_better_migrations.rules as rules


class MigrationsConfig(AppConfig):
    name = "django_better_migrations"

    def ready(self):
        """
        This method allows importing our patches only once the django app is loaded.
        See docs: https://docs.djangoproject.com/en/dev/ref/applications/#django.apps.AppConfig.ready
        """
        import django_better_migrations.migration_writer_patch  # noqa


DEFAULT_CONFIGURATION = {
    "RULES": [
        rules.NoAddColumnNonNull,
    ],
    "ALLOW_ENGINES": [],
}


def get_setting(key):
    app_setting = getattr(settings, "BETTER_MIGRATIONS", {})

    if key in app_setting:
        return app_setting[key]

    return DEFAULT_CONFIGURATION[key]
