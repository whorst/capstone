# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 19:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0004_remove_announcement_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='description',
            field=models.TextField(default=datetime.datetime(2016, 6, 15, 19, 17, 9, 353833, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
