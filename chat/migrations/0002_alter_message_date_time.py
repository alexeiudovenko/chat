# Generated by Django 3.2.7 on 2021-09-19 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 18, 45, 51, 869776), verbose_name='Date and time'),
        ),
    ]
