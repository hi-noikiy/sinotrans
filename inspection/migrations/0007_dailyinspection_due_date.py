# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0006_dailyinspection'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyinspection',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2017, 8, 14, 15, 32, 6, 294000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
