from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view(), name='list_view'),  # 列表视图
    url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='detail_view'),  # 详情视图
]
