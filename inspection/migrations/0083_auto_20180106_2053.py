# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-06 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0082_auto_20180102_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf_inspection_record',
            name='use_condition',
            field=models.CharField(blank=True, choices=[(b'normal', 'Normal'), (b'breakdown', 'Breakdown')], max_length=30, verbose_name='Use Condition'),
        ),
    ]
