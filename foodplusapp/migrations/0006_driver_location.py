# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-09 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplusapp', '0005_auto_20190307_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
