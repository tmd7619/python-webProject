# Generated by Django 3.1.6 on 2021-02-09 05:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0006_auto_20210209_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='regdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 5, 49, 32, 967720, tzinfo=utc)),
        ),
    ]
