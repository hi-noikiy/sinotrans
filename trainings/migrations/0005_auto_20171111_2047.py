# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-11 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0004_auto_20171111_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingrecord',
            name='annual_trainning_pan',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trainings.AnnualTraningPlan', verbose_name='annual training plan'),
        ),
    ]