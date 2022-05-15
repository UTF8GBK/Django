
from django.urls import path,include,re_path
from movies import views

urlpatterns = [
    path('',views.index),  # 匹配视图函数
    re_path('^(\d+)/$',views.detail),  # 匹配视图函数

    path('cookie_set/',views.cookie_set),# 设置cookie
    path('cookie_get/',views.cookie_get), # 获取cookie
    path('cookie_del/',views.cookie_del),# 删除cookie

    path('session_set/', views.session_set),  # 设置session
    path('session_get/', views.session_get),  # 获取session
    path('session_del/', views.session_del),  # 删除session

    path('login/', views.login,name='login'), #登录页面
    path('check_login/', views.check_login),

    # path('zhuce/',views.zhuce,name = 'zhuce'),
    path('register/', views.register),        #注册页面
    path('pasword_reset/', views.pasword_reset,name='login'),


]
