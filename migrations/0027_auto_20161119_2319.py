# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-20 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0026_holder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holder',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]