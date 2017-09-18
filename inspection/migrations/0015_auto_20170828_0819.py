# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc

class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0014_delete_shelf_inspection'),
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
        migrations.AddField(
            model_name='shelf_inspection_record',
            name='shelf_inspection',
            field=models.ForeignKey(default=None, to='inspection.shelf_inspection'),
        ),
        migrations.AlterField(
            model_name='shelf_inspection_record',
            name='use_condition',
            field=models.CharField(blank=True, max_length=30, verbose_name='Use Condition', choices=[(b'1', 'Normal'), (b'2', 'Breakdown')]),
        ),          
    ]
