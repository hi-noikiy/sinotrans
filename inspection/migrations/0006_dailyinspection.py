# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inspection.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0005_officeinspection_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyInspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cateory', models.CharField(default=b'people', max_length=30, verbose_name='cateory', choices=[(b'people', b'People'), (b'device', b'Device'), (b'machine', b'Machine'), (b'method', b'Method'), (b'environment', b'Environment')])),
                ('item', models.CharField(max_length=30, verbose_name='item')),
                ('impact', models.TextField(max_length=30, verbose_name='impact')),
                ('correct', models.TextField(max_length=30, verbose_name='correct')),
                ('correct_status', models.CharField(default=b'notcomplete', max_length=30, verbose_name='correct status', choices=[(b'complete', b'Complete'), (b'notcomplete', b'Not Complete')])),
                ('owner', models.CharField(max_length=30, verbose_name='owner')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image_before', models.ImageField(null=True, upload_to=inspection.models.image_upload_to, blank=True)),
                ('image_after', models.ImageField(null=True, upload_to=inspection.models.image_upload_to, blank=True)),
                ('warehouse', models.CharField(default=b'3#', max_length=30, verbose_name='warehouse', choices=[(b'3', b'3#'), (b'5', b'5#')])),
            ],
        ),
    ]
