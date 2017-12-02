# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-02 00:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inspection', '0053_auto_20171202_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyinspection',
            name='inspector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Inspector'),
        ),
    ]
