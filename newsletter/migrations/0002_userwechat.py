# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWechat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=120, null=True, blank=True)),
                ('unionid', models.CharField(max_length=120, null=True, blank=True)),
                ('city', models.CharField(max_length=120, null=True, blank=True)),
                ('country', models.CharField(max_length=120, null=True, blank=True)),
                ('headimgurl', models.CharField(max_length=120, null=True, blank=True)),
                ('language', models.CharField(max_length=120, null=True, blank=True)),
                ('sex', models.CharField(max_length=120, null=True, blank=True)),
                ('privilege', models.CharField(max_length=120, null=True, blank=True)),
                ('nickname', models.CharField(max_length=120, null=True, blank=True)),
            ],
        ),
    ]
