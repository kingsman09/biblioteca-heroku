# Generated by Django 2.0.7 on 2018-07-25 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0018_auto_20180717_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 25, 11, 36, 54, 109384), verbose_name='fecha de registro'),
        ),
    ]