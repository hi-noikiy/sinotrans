# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-27 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forklift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_car_number', models.CharField(max_length=30, verbose_name='Inner Car Number')),
                ('internal_plate_number', models.CharField(max_length=30, verbose_name='Inner Plate Number')),
                ('model', models.CharField(max_length=30, verbose_name='Forklift Model')),
                ('sn', models.CharField(max_length=30, verbose_name='SN')),
                ('category', models.CharField(max_length=30, verbose_name='Forklift Category')),
                ('manufacturer', models.CharField(max_length=30, verbose_name='Manufacturer')),
                ('tip_height', models.CharField(max_length=30, verbose_name='Tip Height')),
                ('carrying_capacity', models.CharField(max_length=30, verbose_name='Carrying Capacity')),
                ('self_weight', models.CharField(max_length=30, verbose_name='Self Weight')),
                ('turning_radius', models.CharField(max_length=30, verbose_name='Turning Radius')),
                ('front_tyre_size', models.CharField(max_length=30, verbose_name='Front Tyre Size')),
                ('back_tyre_size', models.CharField(max_length=30, verbose_name='Back Tyre Size')),
                ('width', models.CharField(max_length=30, verbose_name='Forklift Width')),
                ('length', models.CharField(max_length=30, verbose_name='Forklift Length')),
                ('fork_length', models.CharField(max_length=30, verbose_name='Fork Length')),
                ('maximum_velocity', models.CharField(max_length=30, verbose_name='Maximum Velocity')),
            ],
            options={
                'verbose_name': 'forklift',
                'verbose_name_plural': 'forklift',
            },
        ),
        migrations.CreateModel(
            name='ForkliftAnnualInspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Annual Inspection Date')),
                ('next_date', models.DateField(verbose_name='Next Inspection Date')),
            ],
            options={
                'verbose_name': 'forklift annual inspection',
                'verbose_name_plural': 'forklift annual inspection',
            },
        ),
        migrations.CreateModel(
            name='ForkliftAnnualInspectionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='inspection/forklift_annual_inspection', verbose_name='image')),
                ('forklift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outsourcing.ForkliftAnnualInspection')),
            ],
            options={
                'verbose_name': 'forklift annual inspection image',
                'verbose_name_plural': 'forklift annual inspection image',
            },
        ),
        migrations.CreateModel(
            name='ForkliftImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='inspection/forklift', verbose_name='image')),
                ('forklift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outsourcing.Forklift')),
            ],
            options={
                'verbose_name': 'forklift image',
                'verbose_name_plural': 'forklift image',
            },
        ),
        migrations.CreateModel(
            name='ForkliftMaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clean_forklift', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='clean forklift')),
                ('clean_and_lubricate_chain', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='clean and lubricate chain')),
                ('lubricate_gateshelf_and_lean_cylinder_bearing', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='lubricate gateshelf and lean cylinder bearing')),
                ('lubricate_sideswayfork_and_check_work_status', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='lubricate sideswayfork and check work status')),
                ('fastening_tyre_nut', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='fastening tyre nut')),
                ('check_tyre_status', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check tyre status')),
                ('check_gear_oil_level_and_leak', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check gear oil level and leak')),
                ('check_hydraulic_oil_level', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check hydraulic oil level')),
                ('clean_all_motor_and_accessories', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='clean all motor and accessories')),
                ('check_and_clean_motor_cooling_fan', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check and clean motor cooling fan')),
                ('check_all_cable_and_connection_status', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check all cable and connection status')),
                ('check_battery_electrolyte_liquidometer_ratio', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check battery electrolyte liquidometer ratio')),
                ('check_charger_status', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check charger status')),
                ('check_pipeline_fastening_and_leak', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check pipeline fastening and leak')),
                ('check_pallet_fork_and_pin_lock', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check pallet fork and pin lock')),
                ('check_lubricate_pedal_and_control_linkage', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check lubricate pedal and control linkage')),
                ('check_braking_device', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check braking device')),
                ('check_all_motor_carbon_brush', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check all motor carbon brush')),
                ('check_overhead_guard_and_counter_weight', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check overhead guard and counter weight')),
                ('check_steering_axle_and_drive_axle', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check steering axle and drive axle')),
                ('check_gateshelf_and_chain', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check gateshelf and chain')),
                ('check_hub_bearing', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check hub bearing')),
                ('check_steering_axle_bearing', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check steering axle bearing')),
                ('check_gateshlf_bearing', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='check gateshlf bearing')),
                ('change_gear_oil', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='change gear oil')),
                ('change_oil_suction_filter', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='change oil suction filter')),
                ('change_ventilate_filter', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='change ventilate filter')),
                ('change_hydraulic_oil', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='change hydraulic oil')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'forklift maintenance',
                'verbose_name_plural': 'forklift maintenance',
            },
        ),
        migrations.CreateModel(
            name='ForkliftRepair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage_reason', models.CharField(blank=True, max_length=30, verbose_name='Damage Reason')),
                ('accessories_name', models.CharField(blank=True, max_length=30, verbose_name='Accessories Name')),
                ('accessories_num', models.DecimalField(blank=True, decimal_places=0, max_digits=20, verbose_name='Accessories Number')),
                ('description', models.TextField(max_length=30, verbose_name='Description')),
                ('repaired', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=30, verbose_name='Repaired')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'forklift repair',
                'verbose_name_plural': 'forklift repair',
            },
        ),
    ]