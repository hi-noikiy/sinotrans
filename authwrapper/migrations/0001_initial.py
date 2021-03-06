# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import authwrapper.fields
import authwrapper.models
import authwrapper.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[authwrapper.validators.ASCIIUsernameValidator()], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('phone', authwrapper.fields.PhoneNumberNullField(error_messages={'unique': 'A user with that phone number already exists.'}, max_length=30, blank=True, help_text='Required. digits and + only.', unique=True, verbose_name='phone')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', authwrapper.fields.EmailNullField(max_length=255, unique=True, null=True, verbose_name='email address', blank=True)),
                ('sex', models.CharField(default='male', max_length=30, verbose_name='sex', blank=True, choices=[('male', 'Male'), ('female', 'Female')])),
                ('birthday', models.DateField(null=True, verbose_name='birthday', blank=True)),
                ('nickname', models.CharField(max_length=30, verbose_name='nickname', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('account_type', models.CharField(default='username', max_length=50, null=True, blank=True, choices=[('username', 'Username'), ('mail', 'Mail'), ('wechat', 'Wechat'), ('phone', 'Phone')])),
                ('image', models.ImageField(null=True, upload_to=authwrapper.models.image_upload_to, blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', authwrapper.models.MyUserManager()),
            ],
        ),
    ]
