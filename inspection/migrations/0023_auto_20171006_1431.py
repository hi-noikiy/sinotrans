# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0022_auto_20170930_1932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyinspection',
            options={'ordering': ['-created'], 'verbose_name': 'Daily Inspection', 'verbose_name_plural': 'Daily Inspection'},
        ),
        migrations.AlterModelOptions(
            name='extinguisher',
            options={'verbose_name': 'extinguisher'},
        ),
        migrations.AlterModelOptions(
            name='extinguisher_inspection',
            options={'verbose_name': 'extinguisher inspection'},
        ),
        migrations.AlterModelOptions(
            name='forklift',
            options={'verbose_name': 'forklift', 'verbose_name_plural': 'forklift'},
        ),
        migrations.AlterModelOptions(
            name='forklift_annual_inspection',
            options={'verbose_name': 'forklift annual inspection', 'verbose_name_plural': 'forklift annual inspection'},
        ),
        migrations.AlterModelOptions(
            name='forklift_annual_inspection_image',
            options={'verbose_name': 'forklift annual inspection image', 'verbose_name_plural': 'forklift annual inspection image'},
        ),
        migrations.AlterModelOptions(
            name='forklift_image',
            options={'verbose_name': 'forklift image', 'verbose_name_plural': 'forklift image'},
        ),
        migrations.AlterModelOptions(
            name='forklift_maint',
            options={'verbose_name': 'forklift maintenance', 'verbose_name_plural': 'forklift maintenance'},
        ),
        migrations.AlterModelOptions(
            name='forklift_repair',
            options={'verbose_name': 'forklift repair', 'verbose_name_plural': 'forklift repair'},
        ),
        migrations.AlterModelOptions(
            name='hydrant',
            options={'verbose_name': 'hydrant'},
        ),
        migrations.AlterModelOptions(
            name='hydrant_inspection',
            options={'verbose_name': 'hydrant inspection'},
        ),
        migrations.AlterModelOptions(
            name='rehearsal',
            options={'verbose_name': 'rehearsal'},
        ),
        migrations.AlterModelOptions(
            name='shelf',
            options={'verbose_name': 'Shelf', 'verbose_name_plural': 'Shelf'},
        ),
        migrations.AlterModelOptions(
            name='shelf_annual_inspection',
            options={'verbose_name': 'shelf annual inspection'},
        ),
        migrations.AlterModelOptions(
            name='shelf_annual_inspection_image',
            options={'verbose_name': 'shelf annual inspection image'},
        ),
        migrations.AlterModelOptions(
            name='shelf_inspection',
            options={'verbose_name': 'shelf inspection', 'verbose_name_plural': 'shelf inspection'},
        ),
        migrations.AlterModelOptions(
            name='shelf_inspection_record',
            options={'verbose_name': 'shelf inspection record', 'verbose_name_plural': 'shelf inspection record'},
        ),
    ]
