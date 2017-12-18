class BaseRule(object):
    pass


class NoAddColumnNonNull(BaseRule):
    title = "No ALTER TABLE ADD COLUMN with non-NULL constraint"

    def process(self, migration, statements):
        if any(self._incorrect(stmt) for stmt in statements):
            return "ERROR"
        return "OK"

    def _incorrect(self, stmt):
        return stmt.startswith("ALTER TABLE") and "NOT NULL" in stmt
