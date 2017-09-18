# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0011_auto_20170826_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='extinguisher_inspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_person', models.CharField(max_length=30, verbose_name='Check Person', blank=True)),
                ('check_result', models.CharField(max_length=30, verbose_name='Check Result', blank=True)),
                ('check_date', models.DateField(verbose_name='Check Date')),
                ('extinguisher', models.ForeignKey(to='inspection.extinguisher')),
            ],
        ),
        migrations.CreateModel(
            name='hydrant_inspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_person', models.CharField(max_length=30, verbose_name='Check Person', blank=True)),
                ('check_result', models.CharField(max_length=30, verbose_name='Check Result', blank=True)),
                ('check_date', models.DateField(verbose_name='Check Date')),
                ('extinguisher', models.ForeignKey(to='inspection.hydrant')),
            ],
        ),
    ]
