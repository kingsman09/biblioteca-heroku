# Generated by Django 2.0.7 on 2018-07-26 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0019_auto_20180725_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 26, 12, 29, 58, 505832), verbose_name='fecha de registro'),
        ),
    ]
