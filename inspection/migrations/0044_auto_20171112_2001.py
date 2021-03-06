# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-12 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0043_auto_20171112_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShelfAnnualInspectionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'inspection/shelf_annual_inspection', verbose_name='image')),
            ],
            options={
                'verbose_name': 'shelf annual inspection image',
            },
        ),
        migrations.RemoveField(
            model_name='shelf_annual_inspection_image',
            name='shelf_annual_inspection',
        ),
        migrations.AlterField(
            model_name='shelfannualinspection',
            name='shelf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.shelf', verbose_name='Shelf'),
        ),
        migrations.DeleteModel(
            name='shelf_annual_inspection',
        ),
        migrations.DeleteModel(
            name='shelf_annual_inspection_image',
        ),
        migrations.AddField(
            model_name='shelfannualinspectionimage',
            name='shelf_annual_inspection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.ShelfAnnualInspection', verbose_name=b'shelf annual inspection'),
        ),
    ]
