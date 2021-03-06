from django.conf.urls import url
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view(), name='list_view'),  # 列表视图
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='detail_view'),  # 详情视图

    # 演示APIView
    # url(r'^books/$', views.BookListAPIView.as_view()),

    # 演示GenericAPIView列表视图
    # url(r'^books/$', views.BookListAPIView.as_view()),
    #
    # # 演示GenericAPIView详情视图
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailAPIView.as_view()),

    # 使用ViewSet视图集
    # url(r'^books/$', views.BookViewSet.as_view({'get': 'list'})),
    # url(r'^books/(?P<pk>\d+)/$', views.BookViewSet.as_view({'get': 'retrieve'})),

    # 使用GenericViewSet视图集
    # url(r'^books/$', views.BookViewSet.as_view({'get': 'list'})),
    # url(r'^books/(?P<pk>\d+)/$', views.BookViewSet.as_view({'get': 'retrieve'})),

    # 使用ReadOnlyModelViewSet视图集
    # url(r'^books/$', views.BookViewSet.as_view({'get': 'list'})),
    # url(r'^books/(?P<pk>\d+)/$', views.BookViewSet.as_view({'get': 'retrieve'})),
    # # 以下两个路由是额外追加的行为
    # url(r'^books/latest$', views.BookViewSet.as_view({'get': 'latest'})),
    # url(r'^books/(?P<pk>\d+)/read$', views.BookViewSet.as_view({'put': 'read'})),
]

# 路由器只能配置视图集使用
# SimpleRouter和DefaultRouter只有一个区别: DefaultRouter会多配置一个根路由
router = SimpleRouter()
router.register(r'books', views.BookViewSet)
urlpatterns += router.urls

# router = DefaultRouter()  # 创建路由器对象
# router.register(r'books', views.BookAPIViewSet)
# urlpatterns += router.urls
