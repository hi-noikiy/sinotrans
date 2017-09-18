# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import crowdfundings.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crowdfunding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=45, choices=[(b'health', b'Health'), (b'school', b'School')])),
                ('title', models.CharField(max_length=120)),
                ('detail', models.TextField(null=True, blank=True)),
                ('is_favorite', models.BooleanField(default=False, help_text='Designates whether this is favorite.', verbose_name='favorite status')),
                ('image', models.ImageField(upload_to=crowdfundings.models.image_upload_to)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
