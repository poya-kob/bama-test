# Generated by Django 3.2.9 on 2021-12-06 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20211205_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargallery',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_image', to='car.cars'),
        ),
    ]
