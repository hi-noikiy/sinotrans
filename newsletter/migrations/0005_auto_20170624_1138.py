# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newsletter.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=newsletter.models.image_upload_to_article),
        ),
    ]
