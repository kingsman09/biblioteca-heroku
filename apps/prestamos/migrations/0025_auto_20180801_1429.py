# Generated by Django 2.0.7 on 2018-08-01 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0024_auto_20180801_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2018, 8, 9, 14, 29, 6, 142034), verbose_name='fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='token',
            field=models.CharField(default='XZU9XYAWVAUKEEX', max_length=50, unique=True),
        ),
    ]
