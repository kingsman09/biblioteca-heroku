# Generated by Django 2.0.7 on 2018-08-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20180801_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='escolaridad',
            field=models.PositiveIntegerField(choices=[(0, 'None'), (1, 'Primaria'), (2, 'Basicos'), (3, 'Diversificado'), (4, 'Universidad'), (5, 'Maestria')], default=0, verbose_name='escolaridad'),
        ),
    ]
