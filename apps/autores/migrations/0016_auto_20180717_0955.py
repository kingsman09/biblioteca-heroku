# Generated by Django 2.0.7 on 2018-07-17 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0015_auto_20180713_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 17, 9, 54, 59, 554699), verbose_name='fecha de registro'),
        ),
    ]
