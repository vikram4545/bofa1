# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-19 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0014_auto_20161119_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holder',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boapp.Number'),
        ),
    ]