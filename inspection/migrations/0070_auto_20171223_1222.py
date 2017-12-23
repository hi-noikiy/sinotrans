# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-23 04:22
from __future__ import unicode_literals

from django.db import migrations, models
import inspection.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0069_auto_20171219_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter', models.CharField(max_length=30, verbose_name='reporter')),
                ('company_of_reporter', models.CharField(choices=[(b'SNT', 'SNT')], default=b'SNT', max_length=30, verbose_name='company of reporter')),
                ('department_of_reporter', models.CharField(choices=[(b'security', 'security'), (b'storage', 'storage'), (b'administration', 'administration')], default=b'storage', max_length=30, verbose_name='department of reporter')),
                ('report_content', models.TextField(max_length=500, verbose_name='report content')),
                ('area', models.CharField(choices=[(b'inwarehouse', 'in warehouse'), (b'outwarehouse', 'out warehouse')], default=b'inwarehouse', max_length=30, verbose_name='area')),
                ('category', models.CharField(choices=[(b'PI', 'PI')], default=b'PI', max_length=30, verbose_name='category')),
                ('risk', models.CharField(choices=[(b'H', b'H'), (b'M', b'M'), (b'L', b'L')], default=b'M', max_length=30, verbose_name='risk')),
                ('direct_reason', models.CharField(choices=[(b'unsafe_condition', 'unsafe condition')], default=b'unsafe_condition', max_length=30, verbose_name='direct reason')),
                ('root_cause', models.CharField(choices=[(b'MM', 'MM'), (b'EC', 'EC')], default=b'MM', max_length=30, verbose_name='root cause')),
                ('feedback_person', models.CharField(max_length=30, verbose_name='feedback person')),
                ('close_person', models.CharField(blank=True, max_length=30, null=True, verbose_name='close person')),
                ('rectification_measures', models.TextField(max_length=30, verbose_name='rectification measures')),
                ('rectification_status', models.CharField(choices=[(b'completed', 'Completed'), (b'uncompleted', 'Uncompleted')], default=b'uncompleted', max_length=30, verbose_name='rectification status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Inspection Created Date')),
                ('planned_complete_date', models.DateField(verbose_name='planned complete date')),
                ('completed_time', models.DateTimeField(blank=True, null=True, verbose_name='rectification completed time')),
                ('image_before', models.ImageField(upload_to=inspection.models.image_upload_to_pi, verbose_name='picture before rectification')),
                ('image_after', models.ImageField(blank=True, null=True, upload_to=inspection.models.image_upload_to_pi, verbose_name='picture after rectification')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WHPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter', models.CharField(max_length=30, verbose_name='reporter')),
                ('company_of_reporter', models.CharField(choices=[(b'SNT', 'SNT')], default=b'SNT', max_length=30, verbose_name='company of reporter')),
                ('department_of_reporter', models.CharField(choices=[(b'security', 'security'), (b'storage', 'storage'), (b'administration', 'administration')], default=b'storage', max_length=30, verbose_name='department of reporter')),
                ('report_content', models.TextField(max_length=500, verbose_name='report content')),
                ('area', models.CharField(choices=[(b'inwarehouse', 'in warehouse'), (b'outwarehouse', 'out warehouse')], default=b'inwarehouse', max_length=30, verbose_name='area')),
                ('category', models.CharField(choices=[(b'PI', 'PI')], default=b'PI', max_length=30, verbose_name='category')),
                ('risk', models.CharField(choices=[(b'H', b'H'), (b'M', b'M'), (b'L', b'L')], default=b'M', max_length=30, verbose_name='risk')),
                ('direct_reason', models.CharField(choices=[(b'unsafe_condition', 'unsafe condition')], default=b'unsafe_condition', max_length=30, verbose_name='direct reason')),
                ('root_cause', models.CharField(choices=[(b'MM', 'MM'), (b'EC', 'EC')], default=b'MM', max_length=30, verbose_name='root cause')),
                ('feedback_person', models.CharField(max_length=30, verbose_name='feedback person')),
                ('close_person', models.CharField(blank=True, max_length=30, null=True, verbose_name='close person')),
                ('rectification_measures', models.TextField(max_length=30, verbose_name='rectification measures')),
                ('rectification_status', models.CharField(choices=[(b'completed', 'Completed'), (b'uncompleted', 'Uncompleted')], default=b'uncompleted', max_length=30, verbose_name='rectification status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Inspection Created Date')),
                ('planned_complete_date', models.DateField(verbose_name='planned complete date')),
                ('completed_time', models.DateTimeField(blank=True, null=True, verbose_name='rectification completed time')),
                ('image_before', models.ImageField(upload_to=inspection.models.image_upload_to_pi, verbose_name='picture before rectification')),
                ('image_after', models.ImageField(blank=True, null=True, upload_to=inspection.models.image_upload_to_pi, verbose_name='picture after rectification')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='PI',
        ),
    ]
