# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0012_extinguisher_inspection_hydrant_inspection'),
    ]

    operations = [
        migrations.CreateModel(
            name='shelf_inspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_date', models.DateField(verbose_name='Check Date')),
                ('comments', models.TextField(max_length=30, verbose_name='Comments')),
            ],
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='category',
            field=models.CharField(default='People', max_length=30, verbose_name='Category', choices=[(b'people', 'People'), (b'device', 'Device'), (b'machine', 'Machine'), (b'method', 'Method'), (b'environment', 'Environment')]),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='rectification_status',
            field=models.CharField(default='Uncompleted', max_length=30, verbose_name='Rectification Status', choices=[(b'completed', 'Completed'), (b'uncompleted', 'Uncompleted')]),
        ),
    ]
