# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfundings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crowdfunding',
            name='amount',
            field=models.DecimalField(default=100, max_digits=50, decimal_places=0),
        ),
        migrations.AddField(
            model_name='crowdfunding',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='deadline'),
        ),
    ]
