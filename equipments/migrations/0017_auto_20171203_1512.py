# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-03 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0016_auto_20171203_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinspection',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Due Date'),
        ),
    ]
