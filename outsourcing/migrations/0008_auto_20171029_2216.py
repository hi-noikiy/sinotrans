# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-29 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcing', '0007_auto_20171027_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forkliftrepair',
            name='description',
            field=models.TextField(max_length=130, verbose_name='Breakdown Description'),
        ),
    ]
