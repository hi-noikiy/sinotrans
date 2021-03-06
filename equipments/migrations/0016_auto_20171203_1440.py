# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-03 06:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0015_auto_20171203_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentinspection',
            name='completed_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='rectification completed time'),
        ),
        migrations.AddField(
            model_name='equipmentinspection',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 3, 6, 40, 29, 112000, tzinfo=utc), verbose_name='Due Date'),
            preserve_default=False,
        ),
    ]
