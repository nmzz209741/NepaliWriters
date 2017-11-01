# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 10:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20171101_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 16, 8, 17, 538806)),
        ),
        migrations.AlterField(
            model_name='posttoreview',
            name='status',
            field=models.TextField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')]),
        ),
    ]