# Generated by Django 2.0.7 on 2018-08-02 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0021_auto_20180727_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 8, 2, 9, 35, 31, 443218), verbose_name='fecha de registro'),
        ),
    ]
