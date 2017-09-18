# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0017_shelf_inspection_record_forecast_complete_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelf_inspection_record',
            name='gradient',
            field=models.DecimalField(null=True, verbose_name='Gradient', max_digits=20, decimal_places=1, blank=True),
        ),
    ]
