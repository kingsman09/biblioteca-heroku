# Generated by Django 2.0.7 on 2018-07-27 22:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0022_auto_20180726_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temas',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2018, 7, 27, 22, 44, 19, 609460, tzinfo=utc), verbose_name='fecha_ingreso'),
        ),
    ]
