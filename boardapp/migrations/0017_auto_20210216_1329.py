# Generated by Django 3.1.6 on 2021-02-16 04:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0016_auto_20210216_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 4, 29, 31, 230388, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 16, 4, 29, 31, 228388, tzinfo=utc)),
        ),
    ]
