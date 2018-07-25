# Generated by Django 2.0.7 on 2018-07-17 16:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0018_auto_20180717_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2018, 7, 25, 16, 11, 54, 430512, tzinfo=utc), verbose_name='fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(default=datetime.datetime(2018, 7, 17, 16, 11, 54, 430512, tzinfo=utc), verbose_name='fecha de prestamos'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='token',
            field=models.CharField(default='4VQEX2DVCU1BSDC', max_length=50, unique=True),
        ),
    ]