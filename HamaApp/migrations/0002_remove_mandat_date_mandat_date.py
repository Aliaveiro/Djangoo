# Generated by Django 4.0.5 on 2022-07-08 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HamaApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mandat',
            name='Date',
        ),
        migrations.AddField(
            model_name='mandat',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
