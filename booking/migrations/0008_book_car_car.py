# Generated by Django 4.1.1 on 2022-12-06 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("owner", "0009_cars_cost_of_vehicle_cars_rent_per_hour_and_more"),
        ("booking", "0007_remove_book_car_car"),
    ]

    operations = [
        migrations.AddField(
            model_name="book_car",
            name="car",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="owner.cars"
            ),
        ),
    ]
