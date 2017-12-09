# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-09 03:42
from __future__ import unicode_literals

from django.db import migrations
import inspection.fields
import newsletter.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_auto_20171202_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=inspection.fields.ThumbnailImageField(upload_to=newsletter.models.image_upload_to_article, verbose_name='image'),
        ),
    ]
