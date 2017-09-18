# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0002_officeinspection_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='officeinspection',
            name='power',
            field=models.CharField(default=b'no', max_length=30, verbose_name='power', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')]),
        ),
    ]
