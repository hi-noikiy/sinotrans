# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0003_officeinspection_power'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeinspection',
            name='location',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
