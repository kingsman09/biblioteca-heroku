# Generated by Django 2.0.7 on 2018-08-02 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0025_auto_20180801_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2018, 8, 10, 9, 13, 0, 155084), verbose_name='fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='token',
            field=models.CharField(default='14DSD6MY665B8WD', max_length=50, unique=True),
        ),
    ]
