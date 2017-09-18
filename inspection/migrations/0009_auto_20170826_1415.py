# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inspection.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0008_auto_20170824_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyinspection',
            name='cateory',
        ),
        migrations.RemoveField(
            model_name='dailyinspection',
            name='correct',
        ),
        migrations.RemoveField(
            model_name='dailyinspection',
            name='correct_status',
        ),
        migrations.RemoveField(
            model_name='dailyinspection',
            name='created',
        ),
        migrations.RemoveField(
            model_name='dailyinspection',
            name='item',
        ),
        migrations.RemoveField(
            model_name='dailyinspection',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='dailyinspection',
            name='warehouse',
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='due_date',
            field=models.DateField(verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='image_after',
            field=models.ImageField(upload_to=inspection.models.image_upload_to_dailyinspection, null=True, verbose_name='Picture after Rectification', blank=True),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='image_before',
            field=models.ImageField(upload_to=inspection.models.image_upload_to_dailyinspection, null=True, verbose_name='Picture before Rectification', blank=True),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='impact',
            field=models.CharField(max_length=30, verbose_name='Impact'),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='owner',
            field=models.CharField(max_length=30, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='forklift_annual_inspection',
            name='date',
            field=models.DateField(verbose_name='Annual Inspection Date'),
        ),
        migrations.AlterField(
            model_name='forklift_maint',
            name='check_hydraulic_oil_level',
            field=models.CharField(default=b'no', max_length=30, verbose_name='check hydraulic oil level', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')]),
        ),
    ]
