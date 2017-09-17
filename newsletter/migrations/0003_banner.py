# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newsletter.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_userwechat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=newsletter.models.image_upload_to_banner)),
                ('title', models.CharField(max_length=120, null=True, blank=True)),
                ('text', models.CharField(max_length=220, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
