from django.db import models

# Create your models here.
class BookInfo(models.Model):
    # 书本名字
    btitle  = models.CharField(max_length=20)
#    发布日期
    bpub_data=models.DateField()

class HeroInfo(models.Model):
    hname =models.CharField(max_length=20)  #英雄名称
    hgender = models.BooleanField()   #英雄的性别
    hcomment=models.CharField(max_length=100)   #英雄的介绍
    #  to ： 你需要关联的表，no_delete :你更改数据的时候我应该干嘛
    hbook=models.ForeignKey('BookInfo',on_delete=models.CASCADE)

