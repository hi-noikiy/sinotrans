# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0015_auto_20170828_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf_inspection',
            name='comments',
            field=models.TextField(max_length=30, null=True, verbose_name='Comments', blank=True),
        ),
        migrations.AlterField(
            model_name='shelf_inspection_record',
            name='comments',
            field=models.TextField(max_length=30, null=True, verbose_name='Comments', blank=True),
        ),
    ]
