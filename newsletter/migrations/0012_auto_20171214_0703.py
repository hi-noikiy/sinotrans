# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-13 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_auto_20171209_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[(b'news', 'news'), (b'hot', 'hot'), (b'regulations', 'regulations'), (b'policy_and_information', 'policy and information'), (b'organization_and_position_responsibility', 'organization and position responsibility'), (b'road_risk_map', 'road risk map'), (b'activities', 'activities')], default=b'news', max_length=150, verbose_name='category'),
        ),
    ]
