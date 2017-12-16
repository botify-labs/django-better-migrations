import os
import unittest

from freezegun import freeze_time
from django.core.management import call_command

from tests.helpers import cleanup_migrations


class TestMakemigrationsAddsSql(unittest.TestCase):
    def tearDown(self):
        cleanup_migrations()

    @freeze_time("2017-12-01")
    def test_makemigrations_adds_a_migration_file(self):
        call_command("makemigrations", "example_app")
        assert os.path.isfile("tests/example_app/migrations/0001_initial.py")

        content = open("tests/example_app/migrations/0001_initial.py").read()
        content.should.match_snapshot("migrations__0001_initial.py")
