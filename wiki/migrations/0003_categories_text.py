# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20160820_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
