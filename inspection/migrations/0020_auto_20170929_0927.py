# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inspection.models
import inspection.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0019_auto_20170903_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyinspection',
            name='image_before',
            field=inspection.fields.ThumbnailImageField(null=True, upload_to=inspection.models.image_upload_to_dailyinspection, blank=True),
        ),
    ]
