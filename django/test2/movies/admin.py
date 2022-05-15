from django.contrib import admin
from .models import moviesInfo,heroInfo
# Register your models here.

class moviesInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','score','number','image_path',"isDelete"]

# 命名 ： 模型名字 + Admin
class heroInfoAdmin(admin.ModelAdmin):
    list_display = ['attrs',"startdata","info",'movies_id',"isDelete"]
# "case"
# 注册模型类
admin.site.register(moviesInfo,moviesInfoAdmin)  # 1.8.2
admin.site.register(heroInfo,heroInfoAdmin)
