from django.db import migrations, models

# Generated SQL code (sqlite):
#
# --
# -- Create model Person
# --
# CREATE TABLE "example_app_person" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
#
# Check results:
# CHECK OK: No ALTER TABLE ADD COLUMN with non-NULL constraint
class Migration(migrations.Migration):
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
