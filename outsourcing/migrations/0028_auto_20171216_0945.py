# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-16 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcing', '0027_auto_20171209_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forklift',
            name='forklift_length',
            field=models.CharField(max_length=30, verbose_name='Fork Length'),
        ),
        migrations.AlterField(
            model_name='forkliftannualinspectionimage',
            name='image',
            field=models.ImageField(default=1, upload_to='inspection/forklift_annual_inspection', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forkliftmaint',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='forkliftmaint',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Latest Update'),
        ),
        migrations.AlterField(
            model_name='vehicletransportationkpi',
            name='transportation_project',
            field=models.CharField(choices=[('01', 'shuttle bus'), ('02', 'general cargo shanghai'), ('03', 'general cargo zhejiang'), ('04', 'scattered oil (land-and-water coordinated transport)'), ('05', 'Scattered oil (road)'), ('06', 'hazardous article'), ('07', 'water transport')], max_length=130, verbose_name='transportation project'),
        ),
    ]