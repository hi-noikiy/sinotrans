# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-08 01:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0024_emergency_exit_door'),
    ]

    operations = [
        migrations.DeleteModel(
            name='emergency_exit_door',
        ),
    ]
