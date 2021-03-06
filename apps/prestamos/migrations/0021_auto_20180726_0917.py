# Generated by Django 2.0.7 on 2018-07-26 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0020_auto_20180725_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2018, 8, 3, 9, 17, 12, 90648), verbose_name='fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(default=datetime.datetime(2018, 7, 26, 9, 17, 12, 90648), verbose_name='fecha de prestamos'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='token',
            field=models.CharField(default='9PU9RD93FDN9YHH', max_length=50, unique=True),
        ),
    ]
