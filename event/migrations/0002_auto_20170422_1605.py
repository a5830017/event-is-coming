# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pcount',
            field=models.IntegerField(default=0),
        ),
    ]
