# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-30 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0077_auto_20171223_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extinguisherinspection',
            name='check_result',
            field=models.CharField(choices=[(b'normal', 'Normal'), (b'breakdown', 'Breakdown')], default=b'normal', max_length=30, verbose_name='Check Result'),
        ),
        migrations.AlterField(
            model_name='hydrantinspection',
            name='check_result',
            field=models.CharField(choices=[(b'normal', 'Normal'), (b'breakdown', 'Breakdown')], default=b'normal', max_length=30, verbose_name='Check Result'),
        ),
    ]
