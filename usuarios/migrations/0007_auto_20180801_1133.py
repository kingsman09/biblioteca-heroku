# Generated by Django 2.0.7 on 2018-08-01 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20180801_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='celphone',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999999)]),
        ),
    ]
