# Generated by Django 2.0.7 on 2018-07-09 21:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0005_auto_20180705_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 9, 21, 15, 52, 219543, tzinfo=utc), verbose_name='fecha de registro'),
        ),
    ]
