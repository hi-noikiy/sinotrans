# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-21 14:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0021_auto_20171221_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinspection',
            name='comments',
            field=models.TextField(blank=True, max_length=130, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='equipmentinspection',
            name='owner',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='hssekpi',
            name='year',
            field=models.PositiveIntegerField(help_text='Use the following format: < YYYY >', validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2018)], verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='spraywarehouseinspection',
            name='year',
            field=models.PositiveIntegerField(help_text='Use the following format: < YYYY >', validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2018)], verbose_name='year'),
        ),
    ]
