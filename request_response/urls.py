from django.conf.urls import url

from . import views

urlpatterns = [
    # 演示利用正则组提取url路径参数:位置参数
    url(r'^weather1/([a-z]+)/(\d{4})/$', views.weather1),

    # 演示利用正则组起别名提取url路径参数:关键字参数
    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),

    # 演示提取查询字符串
    url(r'^query_params/$', views.query_params),
]