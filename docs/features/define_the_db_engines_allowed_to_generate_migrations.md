Feature: define the DB engines allowed to generate migrations
=============================================================

You may want to allow only a few DB engines to generate migrations.
You can list them in your application main settings like this:

```python
BETTER_MIGRATIONS = {
    "ALLOW_ENGINES": [
        "postgresql",
        "sqlite",
    ]
}
```

The list of the available engines is: `mysql`, `oracle`, `postgresql`, `sqlite`.
