# Generated by Django 2.0.7 on 2018-07-17 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0017_auto_20180717_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 17, 10, 11, 54, 430512), verbose_name='fecha de registro'),
        ),
    ]
