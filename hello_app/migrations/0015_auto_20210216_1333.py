# Generated by Django 3.1.6 on 2021-02-16 04:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0014_auto_20210216_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='regdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 4, 33, 37, 42227, tzinfo=utc)),
        ),
    ]
