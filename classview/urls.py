from django.conf.urls import url

from . import views


urlpatterns = [
    # url(路径, 函数名)
    url(r'^demoview/$', views.DemoView.as_view())
]