# Generated by Django 3.0.8 on 2020-08-17 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_auto_20200813_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacton',
            name='time_of_transaction',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 1, 29, 40, 700437)),
        ),
    ]
