# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20170422_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_numset',
            field=models.IntegerField(default=0),
        ),
    ]
