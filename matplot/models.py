from django.db import models

# Create your models here.
from django.db import models

#定义图书模型类BookInfo
class PartInfo(models.Model):
    #btitle = models.CharField(max_length=20)#名称
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)


#定义英雄模型类HeroInfo
class ManInfo(models.Model):
    name = models.CharField(max_length=20)
    yeji = models.FloatField()
    huikuan = models.FloatField()
    hetong = models.FloatField()
    sex = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    #hcomment = models.CharField(max_length=200, null=True, blank=False) #hcomment对应的数据库中的字段可以为空，但通过后台管理页面添加信息时hcomment对应的输入框不能为空
    mpart = models.ForeignKey('PartInfo')#英雄与图书表的关系为一对多，所以属性定义在英雄模型类中