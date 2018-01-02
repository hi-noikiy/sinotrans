# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-01 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0024_auto_20180101_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipmentinspection',
            old_name='created',
            new_name='check_date',
        ),
        migrations.RenameField(
            model_name='spraypumproominspection',
            old_name='created',
            new_name='check_date',
        ),
        migrations.RenameField(
            model_name='spraywarehouseinspection',
            old_name='created',
            new_name='check_date',
        ),
        migrations.AlterField(
            model_name='hssekpi',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of Inspection'),
        ),
    ]
