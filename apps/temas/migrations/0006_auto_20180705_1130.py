# Generated by Django 2.0.7 on 2018-07-05 17:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0005_auto_20180704_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temas',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2018, 7, 5, 17, 30, 54, 696121, tzinfo=utc), verbose_name='fecha_ingreso'),
        ),
    ]