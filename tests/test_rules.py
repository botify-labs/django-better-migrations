import unittest

from django_better_migrations.rules import NoAddColumnNonNull


class TestAddColumnNonNullRules(unittest.TestCase):
    def test_add_not_null_column(self):
        statements = (
            'ALTER TABLE "auth_user" ALTER COLUMN "username" NOT NULL;',
        )
        return_code = NoAddColumnNonNull().process(
            None,
            statements)
        self.assertEquals(return_code, "ERROR")

    def test_drop_not_null_column(self):
        statements = (
            'ALTER TABLE "auth_user" ALTER COLUMN "username" DROP NOT NULL;',
        )
        return_code = NoAddColumnNonNull().process(
            None,
            statements)
        self.assertEquals(return_code, "OK")
