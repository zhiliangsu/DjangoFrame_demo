from django.conf.urls import url
from rest_framework.routers import DefaultRouter

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
    url(r'^books/$', views.BookViewSet.as_view({'get': 'list'})),
    url(r'^books/(?P<pk>\d+)/$', views.BookViewSet.as_view({'get': 'retrieve'})),
]

# router = DefaultRouter()  # 创建路由器对象
# router.register(r'books', views.BookAPIViewSet)
# urlpatterns += router.urls
