# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-23 05:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0070_auto_20171223_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extinguisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Name')),
                ('capacity', models.CharField(blank=True, max_length=30, verbose_name='Capacity')),
            ],
            options={
                'verbose_name': 'extinguisher',
                'verbose_name_plural': 'extinguisher',
            },
        ),
        migrations.CreateModel(
            name='ExtinguisherInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_person', models.CharField(blank=True, max_length=30, verbose_name='Check Person')),
                ('check_result', models.CharField(blank=True, max_length=30, verbose_name='Check Result')),
                ('check_date', models.DateField(verbose_name='Check Date')),
                ('extinguisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.Extinguisher', verbose_name='extinguisher')),
            ],
            options={
                'verbose_name': 'extinguisher inspection',
                'verbose_name_plural': 'extinguisher inspection',
            },
        ),
        migrations.CreateModel(
            name='Hydrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Name')),
                ('accessories', models.CharField(blank=True, max_length=30, verbose_name='Accessories')),
            ],
            options={
                'verbose_name': 'hydrant',
                'verbose_name_plural': 'hydrant',
            },
        ),
        migrations.CreateModel(
            name='HydrantInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_person', models.CharField(blank=True, max_length=30, verbose_name='Check Person')),
                ('check_result', models.CharField(blank=True, max_length=30, verbose_name='Check Result')),
                ('check_date', models.DateField(verbose_name='Check Date')),
                ('extinguisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.Hydrant', verbose_name='hydrant')),
            ],
            options={
                'verbose_name': 'hydrant inspection',
                'verbose_name_plural': 'hydrant inspection',
            },
        ),
        migrations.AlterModelOptions(
            name='rtpi',
            options={'verbose_name': 'RTPI', 'verbose_name_plural': 'RTPI'},
        ),
        migrations.AlterModelOptions(
            name='whpi',
            options={'verbose_name': 'WHPI', 'verbose_name_plural': 'WHPI'},
        ),
    ]