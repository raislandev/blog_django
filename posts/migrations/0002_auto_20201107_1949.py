# Generated by Django 3.1.3 on 2020-11-07 22:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 7, 22, 49, 53, 707163, tzinfo=utc)),
        ),
    ]
