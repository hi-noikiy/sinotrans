# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 12:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0037_auto_20171026_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forklift_annual_inspection_image',
            name='forklift',
        ),
        migrations.RemoveField(
            model_name='forklift_image',
            name='forklift',
        ),
        migrations.DeleteModel(
            name='forklift_maint',
        ),
        migrations.DeleteModel(
            name='forklift_repair',
        ),
        migrations.DeleteModel(
            name='forklift',
        ),
        migrations.DeleteModel(
            name='forklift_annual_inspection',
        ),
        migrations.DeleteModel(
            name='forklift_annual_inspection_image',
        ),
        migrations.DeleteModel(
            name='forklift_image',
        ),
    ]
