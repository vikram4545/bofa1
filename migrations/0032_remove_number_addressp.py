# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-25 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0031_auto_20161125_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='number',
            name='Addressp',
        ),
    ]