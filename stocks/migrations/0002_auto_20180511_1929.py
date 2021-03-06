# Generated by Django 2.0.4 on 2018-05-11 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BKDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(default='', max_length=250, verbose_name='备注')),
                ('isactived', models.BooleanField(choices=[(True, '是'), (False, '否')], verbose_name='有效')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='StockDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='开盘价')),
                ('close', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='收盘价')),
                ('high', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='最高价')),
                ('low', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='最低价')),
                ('volumn', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='vol')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=9, null=True, verbose_name='金额')),
                ('tradedate', models.DateField(db_index=True, verbose_name='日期')),
            ],
        ),
        migrations.RemoveField(
            model_name='zxg',
            name='bkname',
        ),
        migrations.RemoveField(
            model_name='zxg',
            name='code',
        ),
        migrations.RenameField(
            model_name='bk',
            old_name='remark',
            new_name='remarks',
        ),
        migrations.RenameField(
            model_name='stockcode',
            old_name='update',
            new_name='timeToMarket',
        ),
        migrations.RemoveField(
            model_name='stockcode',
            name='isindex',
        ),
        migrations.AddField(
            model_name='bk',
            name='code',
            field=models.CharField(db_index=True, default='', max_length=18, verbose_name='编码'),
        ),
        migrations.AddField(
            model_name='bk',
            name='value1',
            field=models.CharField(default='', max_length=50, verbose_name='预留1'),
        ),
        migrations.AddField(
            model_name='bk',
            name='value2',
            field=models.CharField(default='', max_length=50, verbose_name='预留2'),
        ),
        migrations.AddField(
            model_name='bk',
            name='value3',
            field=models.CharField(default='', max_length=50, verbose_name='预留3'),
        ),
        migrations.AddField(
            model_name='stockcode',
            name='category',
            field=models.SmallIntegerField(choices=[(10, '股票'), (11, '指数'), (12, '分级基金'), (13, '债券'), (14, '逆回购')], default=10, verbose_name='交易类别'),
        ),
        migrations.AddField(
            model_name='stockcode',
            name='decimalpoint',
            field=models.SmallIntegerField(default=2, verbose_name='价格小数位数'),
        ),
        migrations.AddField(
            model_name='stockcode',
            name='shortcut',
            field=models.CharField(default='', max_length=8, verbose_name='快捷键'),
        ),
        migrations.AddField(
            model_name='stockcode',
            name='volunit',
            field=models.IntegerField(default=100, verbose_name='每次交易最小成交单位'),
        ),
        migrations.AlterField(
            model_name='bk',
            name='isactived',
            field=models.BooleanField(choices=[(True, '是'), (False, '否')], default=True, verbose_name='有效'),
        ),
        migrations.AlterField(
            model_name='stockcode',
            name='isdelisted',
            field=models.SmallIntegerField(choices=[(True, '是'), (False, '否')], default=False, verbose_name='是否退市'),
        ),
        migrations.DeleteModel(
            name='ZXG',
        ),
        migrations.AddField(
            model_name='stockday',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.Stockcode', verbose_name='代码'),
        ),
        migrations.AddField(
            model_name='bkdetail',
            name='bkname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.BK'),
        ),
        migrations.AddField(
            model_name='bkdetail',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stocks.Stockcode', verbose_name='代码'),
        ),
    ]
