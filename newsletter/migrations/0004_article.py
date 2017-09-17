# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import newsletter.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name=b'title')),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'content')),
                ('publishtime', models.DateTimeField(auto_now_add=True)),
                ('abstract', models.TextField()),
                ('image', models.ImageField(upload_to=newsletter.models.image_upload_to_banner)),
            ],
        ),
    ]
