from django.db import DEFAULT_DB_ALIAS, connections
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.writer import MigrationWriter

from .config import get_setting


# Safety check to ensure we actually can patch MigrationWriter correctly
if "as_string" not in dir(MigrationWriter):
    raise ValueError(
        "This patch is not compatible with your version of Django: "
        "'django.db.migrations.writer.MigrationWriter' has no method 'as_string()'"
    )


# Patch writer's as_string() method to add comments in the resulting file
def as_string_with_sql_annotations(self, *args, **kwargs):
    connection = connections[DEFAULT_DB_ALIAS]

    # check allowed engines in settings
    allowed_engines = get_setting("ALLOW_ENGINES")
    if allowed_engines and connection.vendor not in allowed_engines:
        raise Exception(
            "You are not allowed to generate migrations files "
            "with the DB engine '%s'. Please use an engine among "
            "the following list: %s" % (
                connection.vendor,
                ", ".join(allowed_engines),
            )
        )

    content = self._original_as_string(*args, **kwargs)
    assert "\nclass Migration" in content, "couldn't find 'class Migration' in migration content"

    # write migration un-processed so the executor can find/read it
    with open(self.path, "w") as f:
        f.write(content)

    # get SQL code
    executor = MigrationExecutor(connection)
    app_label = self.migration.app_label
    mirgation_name = self.migration.name
    plan = [(executor.loader.graph.nodes[(app_label, mirgation_name)], False)]
    sql_statements = executor.collect_sql(plan)

    # amend content that will be written to disk
    comment = "\n".join("# %s" % stmt for stmt in sql_statements)
    comment = "# Generated SQL code (%s):\n#\n%s\n#\n" % (connection.vendor, comment)

    # check rules
    rules = get_setting("RULES")
    check_results = []
    for rule in rules:
        status = rule().process(self.migration, sql_statements)
        out = (status, rule.title)
        check_results.append(out)

    if check_results:
        comment += "\n# Check results:\n"
    for res in check_results:
        comment += "# CHECK %s: %s\n" % (res[0], res[1])

    content = content.replace(
        "\nclass Migration",
        "\n%sclass Migration" % comment,
    )

    return content


MigrationWriter._original_as_string = MigrationWriter.as_string
MigrationWriter.as_string = as_string_with_sql_annotations
