# Generated by Django 4.1.1 on 2022-12-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cars",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_name", models.CharField(max_length=20)),
                ("color", models.CharField(max_length=10)),
                ("capacity", models.CharField(max_length=2)),
                ("is_available", models.BooleanField(default=True)),
                ("description", models.CharField(max_length=100)),
            ],
        ),
    ]
