Installation
============

Install the lib with:

    pip install django-better-migrations

(or any other tool you use for dependency management)

Then add `django_better_migrations` in `INSTALLED_APPS` in your settings:

```python
INSTALLED_APPS = [
    ...
    "django_better_migrations",
]
```

It doesn't matter much where the app is added. Since the main job is
to override some django default behavior, the lib will not interfer
with other apps unless they override the same parts of Django...


After doing this, the library will be enabled with its default
configuration. Next step is configuring it to your needs, you'll
learn this in the [Configuration section](./configuration.md).
