# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 23:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0008_auto_20161117_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='number',
            old_name='li',
            new_name='lis',
        ),
    ]
