# Generated by Django 2.0.5 on 2018-05-05 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoPage', '0014_auto_20180505_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logindata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 18, 31, 46, 252237), null=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='inputTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 5, 18, 31, 46, 252237), null=True),
        ),
    ]
