from django.conf.urls import url

from . import views


urlpatterns = [
    # url(路径, 函数名)
    # as_view --> 把方法变成函数
    #         --> 会找到指定类中的对应方法(根据本次请求方法动态去查找类中定义的方法)
    url(r'^demoview/$', views.DemoView.as_view())
]