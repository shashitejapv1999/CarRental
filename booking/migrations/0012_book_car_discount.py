# Generated by Django 4.1.1 on 2022-12-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0011_book_car_session_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="book_car",
            name="discount",
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
