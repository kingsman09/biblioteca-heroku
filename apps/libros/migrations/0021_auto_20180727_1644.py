# Generated by Django 2.0.7 on 2018-07-27 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0020_auto_20180726_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 27, 16, 44, 19, 640709), verbose_name='Fecha de ingreso'),
        ),
    ]
