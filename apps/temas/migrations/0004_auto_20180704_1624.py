# Generated by Django 2.0.7 on 2018-07-04 22:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0003_auto_20180704_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temas',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2018, 7, 4, 22, 24, 18, 615968, tzinfo=utc), verbose_name='fecha_ingreso'),
        ),
    ]
