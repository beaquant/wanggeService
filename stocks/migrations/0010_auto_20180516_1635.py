# Generated by Django 2.0.4 on 2018-05-16 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0009_auto_20180516_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rps',
            name='tradedate',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 16, 35, 52, 730950), verbose_name='交易日期'),
        ),
        migrations.AlterField(
            model_name='rpsprepare',
            name='tradedate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='交易日期'),
        ),
    ]
