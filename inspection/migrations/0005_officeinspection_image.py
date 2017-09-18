# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inspection.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0004_auto_20170810_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='officeinspection',
            name='image',
            field=models.ImageField(null=True, upload_to=inspection.models.image_upload_to, blank=True),
        ),
    ]
