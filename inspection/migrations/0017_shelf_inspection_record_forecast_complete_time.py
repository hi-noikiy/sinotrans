# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0016_auto_20170828_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelf_inspection_record',
            name='forecast_complete_time',
            field=models.DateField(default=datetime.datetime(2017, 8, 28, 5, 33, 40, 926000, tzinfo=utc), verbose_name='Forecast Complete Time'),
            preserve_default=False,
        ),
    ]
