# 定义子路由自己的所有路由
from django.conf.urls import url

from . import views

urlpatterns = [
    # url(url路径正则, 视图函数名)
    # url(r'^index/$', views.index),

    # 只在子路由中定义路由信息
    url(r'^users/index/$', views.index, name='index'),

    # 演示路由的匹配顺序: 自上而下的, 定义路由时,必须要有严格的开始^和结束符$
    # 定义路由时，通常以斜线/结尾, 好处是用户访问 index 或者 index/ 网址，均能访问到index视图
    # 虽然路由结尾带/能带来上述好处，但是却违背了HTTP中URL表示资源位置路径的设计理念。
    # 是否结尾带/以所属公司定义风格为准
    url(r'^users/say/$', views.say),
    url(r'^users/sayhello/$', views.say_hello),

]
