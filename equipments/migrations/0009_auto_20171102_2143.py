# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-02 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0008_auto_20171102_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spraypumproominspection',
            name='date_of_inspection',
            field=models.DateField(verbose_name='Date of Inspection'),
        ),
    ]