# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcing', '0004_forkliftrepair_repaire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forkliftrepair',
            name='repaire_date',
            field=models.DateField(verbose_name='Repaire Date'),
        ),
    ]
