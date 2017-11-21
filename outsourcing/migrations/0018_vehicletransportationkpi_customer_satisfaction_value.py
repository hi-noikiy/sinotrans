# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-11 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outsourcing', '0017_remove_vehicletransportationkpi_customer_satisfaction_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicletransportationkpi',
            name='customer_satisfaction_value',
            field=models.DecimalField(decimal_places=1, default=8.5, max_digits=2, verbose_name='customer satisfaction rate'),
            preserve_default=False,
        ),
    ]