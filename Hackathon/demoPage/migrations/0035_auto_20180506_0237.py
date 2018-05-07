# Generated by Django 2.0.5 on 2018-05-06 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0034_auto_20180506_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskdata',
            name='sarcopeniaRisk',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='healthdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 2, 37, 53, 128850), null=True),
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 2, 37, 53, 128850), null=True),
        ),
        migrations.AlterField(
            model_name='riskdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 6, 2, 37, 53, 128850), null=True),
        ),
    ]