# Generated by Django 2.0.4 on 2018-05-16 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0008_rpsprepare_tradedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rps',
            name='tradedate',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 16, 34, 29, 173377), verbose_name='交易日期'),
        ),
        migrations.AlterField(
            model_name='rpsprepare',
            name='tradedate',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 16, 34, 29, 177226), verbose_name='交易日期'),
        ),
    ]