# Generated by Django 2.0.7 on 2018-07-09 21:15

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20180705_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autores.Author'),
        ),
        migrations.AlterField(
            model_name='libros',
            name='fecha_registro',
            field=models.DateField(default=datetime.datetime(2018, 7, 9, 21, 15, 52, 219543, tzinfo=utc), verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='libros',
            name='tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='temas.Temas'),
        ),
    ]
