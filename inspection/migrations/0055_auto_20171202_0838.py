# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-02 00:38
from __future__ import unicode_literals

from django.db import migrations
import inspection.fields
import inspection.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0054_dailyinspection_inspector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyinspection',
            name='image_before',
            field=inspection.fields.ThumbnailImageField(null=True, upload_to=inspection.models.image_upload_to_dailyinspection, verbose_name='Picture before Rectification'),
        ),
    ]
