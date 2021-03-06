# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forkliftannualinspection',
            name='forklift',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='outsourcing.Forklift', verbose_name='forklift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forkliftmaint',
            name='forklift',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='outsourcing.Forklift', verbose_name='forklift'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forkliftrepair',
            name='forklift',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='outsourcing.Forklift', verbose_name='forklift'),
            preserve_default=False,
        ),
    ]
