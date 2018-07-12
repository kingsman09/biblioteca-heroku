# Generated by Django 2.0.7 on 2018-07-12 15:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0010_auto_20180712_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2018, 7, 20, 15, 12, 39, 297930, tzinfo=utc), verbose_name='fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(default=datetime.datetime(2018, 7, 12, 15, 12, 39, 297930, tzinfo=utc), verbose_name='fecha de prestamos'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='token',
            field=models.CharField(default='9Q9FBGTW2MPH1K7', max_length=50, unique=True),
        ),
    ]