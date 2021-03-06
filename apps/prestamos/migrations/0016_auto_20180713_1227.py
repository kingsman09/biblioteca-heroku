# Generated by Django 2.0.6 on 2018-07-13 18:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0015_auto_20180712_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion',
            field=models.DateField(default=datetime.datetime(2018, 7, 21, 18, 26, 57, 846187, tzinfo=utc), verbose_name='fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(default=datetime.datetime(2018, 7, 13, 18, 26, 57, 846187, tzinfo=utc), verbose_name='fecha de prestamos'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libros.Libros'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='token',
            field=models.CharField(default='WM3KS6THFB68PZN', max_length=50, unique=True),
        ),
    ]
