# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-03 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0014_auto_20171121_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentinspection',
            name='owner',
            field=models.CharField(default='', max_length=30, verbose_name='Owner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipmentinspection',
            name='date_of_inspection',
            field=models.DateField(auto_now_add=True, verbose_name='Date of Inspection'),
        ),
        migrations.AlterField(
            model_name='equipmentinspection',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]