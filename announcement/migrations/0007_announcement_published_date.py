# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0006_auto_20160615_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
