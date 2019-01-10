from django.conf.urls import url

from . import views

urlpatterns = [
    # 演示利用正则组提取url路径参数:位置参数
    url(r'^weather1/([a-z]+)/(\d{4})/$', views.weather1),
    # 演示利用正则组起别名提取url路径参数:关键字参数
    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),
    # 演示提取查询字符串
    url(r'^query_params/$', views.query_params),
    # 演示提取请求体表单数据
    url(r'^get_body_form/$', views.get_body_form),
    # 演示提取请求体非表单(JSON)数据
    url(r'^get_body_non_form/$', views.get_body_non_form),


    # 演示响应对象基本操作
    url(r'^response_demo/$', views.response_demo),
    # 演示响应JSON数据
    url(r'^json_response_demo/$', views.json_response_demo, name='index'),
    # 演示重定向及反向解析
    url(r'^redirect_demo/$', views.redirect_demo),
    # 演示cookie读写
    url(r'^cookie_demo/$', views.cookie_demo),
    # 演示session读写
    url(r'^session_demo/$', views.session_demo),
]