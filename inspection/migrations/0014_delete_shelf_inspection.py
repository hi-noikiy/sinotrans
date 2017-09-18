# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0013_auto_20170827_2203'),
    ]

    operations = [
        migrations.DeleteModel(
            name='shelf_inspection',
        ),
    ]
