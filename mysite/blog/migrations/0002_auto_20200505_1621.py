# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-05 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 16, 21, 31, 774773, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 5, 16, 21, 31, 773852, tzinfo=utc)),
        ),
    ]
