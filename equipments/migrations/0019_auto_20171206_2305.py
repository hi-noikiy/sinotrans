# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-06 15:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0018_auto_20171203_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='SprayWarehouseInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(help_text='Use the following format: < YYYY >', validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2017)], verbose_name='year')),
                ('month', models.CharField(choices=[(b'01', 'January'), (b'02', 'February'), (b'03', 'March'), (b'04', 'April'), (b'05', 'May'), (b'06', 'June'), (b'07', 'July'), (b'08', 'August'), (b'09', 'September'), (b'10', 'October'), (b'11', 'November'), (b'12', 'December')], max_length=30, verbose_name='Month')),
                ('valve_normal', models.BooleanField(default=False, verbose_name='valve normal')),
                ('valve_open_signal_transmission_normal', models.BooleanField(default=False, verbose_name='valve open signal transmission normal ')),
                ('valve_no_corrosion', models.BooleanField(default=False, verbose_name='valve no corrosion')),
                ('water_testing_normal', models.BooleanField(default=False, verbose_name='water testing normal')),
                ('valve_switch_in_close_status', models.BooleanField(default=False, verbose_name='valve switch in close status')),
                ('pipe_network_pressure_normal', models.BooleanField(default=False, verbose_name='pipe network pressure normal')),
                ('pipe_valve_in_open_status', models.BooleanField(default=False, verbose_name='pipe valve in open status')),
                ('pipe_connection_no_leakage', models.BooleanField(default=False, verbose_name='pipe connection no leakage')),
                ('spray_head_no_leakage', models.BooleanField(default=False, verbose_name='spray head no leakage')),
                ('inspector', models.CharField(max_length=30, verbose_name='Inspector')),
                ('date_of_inspection', models.DateField(auto_now_add=True, verbose_name='Date of Inspection')),
            ],
            options={
                'ordering': ('month',),
                'verbose_name': 'Spray Warehouse Inspection',
                'verbose_name_plural': 'Spray Warehouse Inspection',
            },
        ),
        migrations.AlterUniqueTogether(
            name='spraywarehouseinspection',
            unique_together=set([('month', 'year')]),
        ),
    ]
