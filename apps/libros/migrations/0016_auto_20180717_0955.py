# Generated by Django 2.0.7 on 2018-07-17 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0015_auto_20180713_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 17, 15, 54, 59, 571656, tzinfo=utc), verbose_name='Fecha de ingreso'),
        ),
    ]
