# Generated by Django 3.1.6 on 2021-02-09 04:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_auto_20210208_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 4, 21, 5, 761074, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 4, 21, 5, 760074, tzinfo=utc)),
        ),
    ]
