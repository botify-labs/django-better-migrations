import shutil


def cleanup_migrations():
    shutil.rmtree("tests/example_app/migrations/")
