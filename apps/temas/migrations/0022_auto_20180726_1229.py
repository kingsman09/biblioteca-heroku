# Generated by Django 2.0.7 on 2018-07-26 18:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0021_auto_20180725_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temas',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2018, 7, 26, 18, 29, 58, 505832, tzinfo=utc), verbose_name='fecha_ingreso'),
        ),
    ]
