# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-06 10:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0037_auto_20180506_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 10, 45, 22, 210439), null=True),
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 10, 45, 22, 209664), null=True),
        ),
        migrations.AlterField(
            model_name='riskdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 10, 45, 22, 211120), null=True),
        ),
    ]
