# Generated by Django 2.0.7 on 2018-08-02 15:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0023_auto_20180727_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temas',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2018, 8, 2, 15, 35, 31, 442221, tzinfo=utc), verbose_name='fecha_ingreso'),
        ),
    ]
