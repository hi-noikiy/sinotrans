# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-19 14:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcing', '0032_auto_20171218_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinspection',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 19, 14, 34, 27, 223000, tzinfo=utc), verbose_name='Due Date'),
            preserve_default=False,
        ),
    ]