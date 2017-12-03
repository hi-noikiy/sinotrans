# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-02 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0052_dailyinspection_inspector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyinspection',
            name='inspector',
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='completed_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='rectification completed time'),
        ),
        migrations.AlterField(
            model_name='shelf_inspection',
            name='check_date',
            field=models.DateField(auto_now_add=True, verbose_name='Check Date'),
        ),
    ]