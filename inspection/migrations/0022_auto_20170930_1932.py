# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0021_auto_20170930_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyinspection',
            name='category',
            field=models.CharField(default=b'device', max_length=30, verbose_name='Category', choices=[(b'people', 'People'), (b'device', 'Device'), (b'machine', 'Machine'), (b'method', 'Method'), (b'environment', 'Environment')]),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='rectification_status',
            field=models.CharField(default=b'uncompleted', max_length=30, verbose_name='Rectification Status', choices=[(b'completed', 'Completed'), (b'uncompleted', 'Uncompleted')]),
        ),
    ]
