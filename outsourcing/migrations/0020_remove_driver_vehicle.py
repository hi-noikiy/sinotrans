# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-04 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcing', '0019_auto_20171204_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='vehicle',
        ),
    ]
