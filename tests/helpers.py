import shutil


def cleanup_migrations():
    shutil.rmtree("tests/example_app/migrations/", ignore_errors=True)
