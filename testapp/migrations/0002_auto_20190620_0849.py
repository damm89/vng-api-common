# Generated by Django 2.2.1 on 2019-06-20 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("testapp", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.AddField(
            model_name="person",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="testapp.Group",
            ),
        ),
    ]
