# Generated by Django 2.0.7 on 2018-07-12 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0008_auto_20180710_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 12, 15, 2, 28, 294485, tzinfo=utc), verbose_name='Fecha de ingreso'),
        ),
    ]
