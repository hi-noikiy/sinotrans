# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0018_auto_20170828_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf',
            name='number',
            field=models.CharField(max_length=30, verbose_name='Shelf Number', blank=True),
        ),
    ]
