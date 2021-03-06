# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-04 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import inspection.utils


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcing', '0011_auto_20171104_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicletransportationkpi',
            name='vehicle_qualification_rate',
            field=inspection.utils.PercentageField(max_length=30, verbose_name='vehicle qualification rate'),
        ),
        migrations.AlterField(
            model_name='vehicletransportationkpi',
            name='yearly_plan_executing_rate',
            field=models.CharField(max_length=30, validators=[inspection.utils.valid_percentage], verbose_name='yearly plan executing rate'),
        ),
    ]
