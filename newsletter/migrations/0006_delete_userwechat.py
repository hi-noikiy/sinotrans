# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20170624_1138'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserWechat',
        ),
    ]
