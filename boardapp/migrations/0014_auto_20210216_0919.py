# Generated by Django 3.1.6 on 2021-02-16 00:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0013_auto_20210215_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 0, 19, 14, 856321, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 0, 19, 14, 854322, tzinfo=utc)),
        ),
    ]
