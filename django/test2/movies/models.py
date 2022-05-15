from django.db import models

# Create your models here.

class moviesInfo(models.Model):
    title = models.CharField(max_length=20) # 电影的标题
    score = models.FloatField(default=0.0)  # 电影的评分
    number = models.IntegerField(default=0)  # 电影的评价人数
    image_path = models.CharField(max_length=255) # 电影的封面
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    def __str__(self):
        return self.title

class heroInfo(models.Model):
    attrs = models.CharField(max_length=20)  #导演
    startdata = models.CharField(max_length=255)  # 上映时间
    info = models.TextField()  # 剧情简介
    # case = models.CharField()  #获奖情况
    # 外键关联
    movies_id = models.ForeignKey('moviesInfo',on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    def __str__(self):   #类方法
        return self.attrs




class User(models.Model):
    # username = models.CharField(max_length=32)  # 用户名
    email = models.CharField(max_length=32)  # 邮箱
    password = models.CharField(max_length=50)  # 密码

    #
    # def __unicode__(self):
    #     return self.email

