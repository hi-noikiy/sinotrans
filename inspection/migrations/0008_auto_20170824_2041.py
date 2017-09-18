# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import inspection.models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0007_dailyinspection_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='forklift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        ),
        migrations.CreateModel(
            name='forklift_annual_inspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('next_date', models.DateField(verbose_name='Next Inspection Date')),
            ],
        ),
        migrations.CreateModel(
            name='forklift_annual_inspection_image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'inspection/forklift_annual_inspection', null=True, verbose_name='image', blank=True)),
                ('forklift', models.ForeignKey(to='inspection.forklift_annual_inspection')),
            ],
        ),
        migrations.CreateModel(
            name='forklift_image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'inspection/forklift', null=True, verbose_name='image', blank=True)),
                ('forklift', models.ForeignKey(to='inspection.forklift')),
            ],
        ),
        migrations.CreateModel(
            name='forklift_maint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clean_forklift', models.CharField(default=b'no', max_length=30, verbose_name='clean forklift', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('clean_and_lubricate_chain', models.CharField(default=b'no', max_length=30, verbose_name='clean and lubricate chain', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('lubricate_gateshelf_and_lean_cylinder_bearing', models.CharField(default=b'no', max_length=30, verbose_name='lubricate gateshelf and lean cylinder bearing', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('lubricate_sideswayfork_and_check_work_status', models.CharField(default=b'no', max_length=30, verbose_name='lubricate sideswayfork and check work status', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('fastening_tyre_nut', models.CharField(default=b'no', max_length=30, verbose_name='fastening tyre nut', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_tyre_status', models.CharField(default=b'no', max_length=30, verbose_name='check tyre status', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_gear_oil_level_and_leak', models.CharField(default=b'no', max_length=30, verbose_name='check gear oil level and leak', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_hydraulic_oil_level', models.CharField(default=b'no', max_length=30, verbose_name='clean forklift', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('clean_all_motor_and_accessories', models.CharField(default=b'no', max_length=30, verbose_name='clean all motor and accessories', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_and_clean_motor_cooling_fan', models.CharField(default=b'no', max_length=30, verbose_name='check and clean motor cooling fan', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_all_cable_and_connection_status', models.CharField(default=b'no', max_length=30, verbose_name='check all cable and connection status', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_battery_electrolyte_liquidometer_ratio', models.CharField(default=b'no', max_length=30, verbose_name='check battery electrolyte liquidometer ratio', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_charger_status', models.CharField(default=b'no', max_length=30, verbose_name='check charger status', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_pipeline_fastening_and_leak', models.CharField(default=b'no', max_length=30, verbose_name='check pipeline fastening and leak', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_pallet_fork_and_pin_lock', models.CharField(default=b'no', max_length=30, verbose_name='check pallet fork and pin lock', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_lubricate_pedal_and_control_linkage', models.CharField(default=b'no', max_length=30, verbose_name='check lubricate pedal and control linkage', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_braking_device', models.CharField(default=b'no', max_length=30, verbose_name='check braking device', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_all_motor_carbon_brush', models.CharField(default=b'no', max_length=30, verbose_name='check all motor carbon brush', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_overhead_guard_and_counter_weight', models.CharField(default=b'no', max_length=30, verbose_name='check overhead guard and counter weight', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_steering_axle_and_drive_axle', models.CharField(default=b'no', max_length=30, verbose_name='check steering axle and drive axle', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_gateshelf_and_chain', models.CharField(default=b'no', max_length=30, verbose_name='check gateshelf and chain', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_hub_bearing', models.CharField(default=b'no', max_length=30, verbose_name='check hub bearing', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_steering_axle_bearing', models.CharField(default=b'no', max_length=30, verbose_name='check steering axle bearing', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('check_gateshlf_bearing', models.CharField(default=b'no', max_length=30, verbose_name='check gateshlf bearing', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('change_gear_oil', models.CharField(default=b'no', max_length=30, verbose_name='change gear oil', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('change_oil_suction_filter', models.CharField(default=b'no', max_length=30, verbose_name='change oil suction filter', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('change_ventilate_filter', models.CharField(default=b'no', max_length=30, verbose_name='change ventilate filter', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('change_hydraulic_oil', models.CharField(default=b'no', max_length=30, verbose_name='change hydraulic oil', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='forklift_repair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('damage_reason', models.CharField(max_length=30, verbose_name='Damage Reason', blank=True)),
                ('accessories_name', models.CharField(max_length=30, verbose_name='Accessories Name', blank=True)),
                ('accessories_num', models.DecimalField(verbose_name='Accessories Number', max_digits=20, decimal_places=0, blank=True)),
                ('description', models.TextField(max_length=30, verbose_name='Description')),
                ('repaired', models.CharField(default=b'no', max_length=30, verbose_name='Repaired', blank=True, choices=[(b'yes', b'Yes'), (b'no', b'No')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='shelf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=30, verbose_name='Damage Reason', blank=True)),
                ('warehouse', models.CharField(max_length=30, verbose_name='Warehouse', blank=True)),
                ('compartment', models.CharField(max_length=30, verbose_name='Compartment', blank=True)),
                ('warehouse_channel', models.CharField(max_length=30, verbose_name='Warehouse Channel', blank=True)),
                ('group', models.CharField(max_length=30, verbose_name='group', blank=True)),
                ('number', models.CharField(max_length=30, verbose_name='number', blank=True)),
                ('is_gradient_measurement_mandatory', models.BooleanField(verbose_name='Gradient Measurement Mandatory')),
            ],
        ),
        migrations.CreateModel(
            name='shelf_inspection_record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('use_condition', models.CharField(max_length=30, verbose_name='Use Condition', blank=True)),
                ('is_locked', models.BooleanField(verbose_name='Locked')),
                ('check_person', models.CharField(max_length=30, verbose_name='Check Person', blank=True)),
                ('gradient', models.DecimalField(verbose_name='Gradient', max_digits=20, decimal_places=1, blank=True)),
                ('comments', models.TextField(max_length=30, verbose_name='Comments')),
                ('shelf', models.ForeignKey(to='inspection.shelf')),
            ],
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='correct_status',
            field=models.CharField(default=b'uncompleted', max_length=30, verbose_name='correct status', choices=[(b'completed', 'Completed'), (b'uncompleted', 'Uncompleted')]),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='due_date',
            field=models.DateField(verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='image_after',
            field=models.ImageField(upload_to=inspection.models.image_upload_to_dailyinspection, null=True, verbose_name='image after', blank=True),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='image_before',
            field=models.ImageField(upload_to=inspection.models.image_upload_to_dailyinspection, null=True, verbose_name='image before', blank=True),
        ),
        migrations.AlterField(
            model_name='dailyinspection',
            name='impact',
            field=models.CharField(max_length=30, verbose_name='impact'),
        ),
    ]
