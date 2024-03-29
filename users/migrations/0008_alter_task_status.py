# Generated by Django 5.0.1 on 2024-02-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_alter_task_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("done", "DONE"),
                    ("processing", "PROCESSING"),
                    ("no work", "NO WORK"),
                ],
                default="no work",
                max_length=63,
            ),
        ),
    ]
