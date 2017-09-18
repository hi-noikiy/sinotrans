# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0009_auto_20170826_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyinspection',
            name='category',
            field=models.CharField(default=b'people', max_length=30, verbose_name='Category', choices=[(b'people', 'People'), (b'device', 'Device'), (b'machine', 'Machine'), (b'method', 'Method'), (b'environment', 'Environment')]),
        ),
        migrations.AddField(
            model_name='dailyinspection',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 6, 38, 16, 712000, tzinfo=utc), verbose_name='Inspection Created Date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyinspection',
            name='inspection_content',
            field=models.CharField(default='', max_length=30, verbose_name='Inspection Content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyinspection',
            name='location',
            field=models.CharField(default=b'1', max_length=30, verbose_name='Location', choices=[(b'1', 'Storage Area')]),
        ),
        migrations.AddField(
            model_name='dailyinspection',
            name='rectification_measures',
            field=models.TextField(default='', max_length=30, verbose_name='Rectification Measures'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyinspection',
            name='rectification_status',
            field=models.CharField(default=b'uncompleted', max_length=30, verbose_name='Rectification Status', choices=[(b'completed', 'Completed'), (b'uncompleted', 'Uncompleted')]),
        ),
        migrations.AddField(
            model_name='dailyinspection',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 6, 38, 38, 328000, tzinfo=utc), verbose_name='Inspection Updated Date', auto_now=True),
            preserve_default=False,
        ),
    ]
