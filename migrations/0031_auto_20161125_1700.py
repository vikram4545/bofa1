# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-25 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0030_number_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='Addressp',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='number',
            name='address',
            field=models.TextField(default=' ', max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='number',
            name='anumber',
            field=models.CharField(default=0, max_length=12),
        ),
        migrations.AlterField(
            model_name='number',
            name='upload',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]