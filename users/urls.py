# 定义子路由自己的所有路由
from django.conf.urls import url

from . import views

urlpatterns = [
    # url(url路径正则, 视图函数名)
    # url(r'^index/$', views.index),

    # 只在子路由中定义路由信息
    url(r'^users/index/$', views.index),

]
