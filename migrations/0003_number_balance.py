# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0002_auto_20161116_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]