# Generated by Django 2.0.7 on 2018-07-12 15:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0011_auto_20180712_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temas',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2018, 7, 12, 15, 11, 28, 474338, tzinfo=utc), verbose_name='fecha_ingreso'),
        ),
    ]
