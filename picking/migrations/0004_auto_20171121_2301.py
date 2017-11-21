# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-21 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picking', '0003_auto_20171121_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickingbill',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=20, verbose_name='volume'),
        ),
        migrations.AlterField(
            model_name='waybill',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=20, verbose_name='volume'),
        ),
    ]
