# Generated by Django 2.0.7 on 2018-07-12 16:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0014_auto_20180712_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2018, 7, 20, 16, 38, 53, 251051, tzinfo=utc), verbose_name='fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(default=datetime.datetime(2018, 7, 12, 16, 38, 53, 251051, tzinfo=utc), verbose_name='fecha de prestamos'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='token',
            field=models.CharField(default='1MRN4112SKV3NZ6', max_length=50, unique=True),
        ),
    ]
