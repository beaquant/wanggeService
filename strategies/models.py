from django.db import models


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True


class StrategyType(BaseModel):
    code = models.CharField(verbose_name='编号', max_length=10, unique=True, db_index=True)
    name = models.CharField(verbose_name='名称', max_length=8)
    remark = models.CharField(verbose_name='备注', max_length=255)

    def __str__(self):
        return "{}-{}".format(self.code, self.name)


class Strategy(BaseModel):
    code = models.CharField(verbose_name='编号', max_length=10, unique=True, db_index=True)
    name = models.CharField(verbose_name='名称', max_length=8)
    strategytype = models.ForeignKey(StrategyType, on_delete=models.PROTECT)
    remark = models.CharField(verbose_name='备注', max_length=255)
    deleted = models.BooleanField('已删除', default= False)

    def __str__(self):
        return "{}-{}".format(self.code, self.name)


class StrategyDetail(BaseModel):
    strategy = models.ForeignKey(Strategy, on_delete=models.PROTECT)
    orderid = models.SmallIntegerField(verbose_name='序号', null=False)
    # 设置最多允许的值： 99,999,999 ,999 .9999
    num = models.DecimalField('数量', max_digits=15, decimal_places=4, default=0)
    expressions = models.CharField('表达式', max_length=255, default='')
