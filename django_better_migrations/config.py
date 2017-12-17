from django.apps import AppConfig


class MigrationsConfig(AppConfig):
    name = "django_better_migrations"

    def ready(self):
        """
        This method allows importing our patches only once the django app is loaded.
        See docs: https://docs.djangoproject.com/en/dev/ref/applications/#django.apps.AppConfig.ready
        """
        import django_better_migrations.migration_writer_patch  # noqa
