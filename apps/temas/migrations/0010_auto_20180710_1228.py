# Generated by Django 2.0.7 on 2018-07-10 18:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0009_auto_20180710_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temas',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2018, 7, 10, 18, 28, 32, 459280, tzinfo=utc), verbose_name='fecha_ingreso'),
        ),
    ]
