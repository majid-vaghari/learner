# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_photo', '0002_auto_20160618_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelednumber',
            name='label1',
            field=models.CharField(blank=True, default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='labelednumber',
            name='label2',
            field=models.CharField(blank=True, default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='labelednumber',
            name='label3',
            field=models.CharField(blank=True, default=None, max_length=1, null=True),
        ),
    ]