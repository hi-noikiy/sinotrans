# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-22 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricalequipmentinspection',
            name='comments',
            field=models.TextField(blank=True, max_length=130, verbose_name='Comments'),
        ),
    ]
