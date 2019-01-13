from django.views import View
from django.http import HttpResponse, JsonResponse

"""
GET     /books/         提供所有记录
POST    /books/         新增一条记录
GET     /books/<pk>/    提供指定id的记录
PUT     /books/<pk>/    修改指定id的记录
DELETE  /books/<pk>/    删除指定id的记录

响应数据    JSON
"""


class BookListView(View):
    """列表视图: 不带pk"""

    def get(self, request):
        """查询所有书籍"""
        pass

    def post(self, request):
        """新增一本书籍"""
        pass


class BookDetailView(View):
    """详情视图: 带pk"""

    def get(self, request, pk):
        """查询某本书籍"""
        pass

    def put(self, request, pk):
        """修改指定的某本书籍"""
        pass

    def delete(self, request, pk):
        """删除指定的某本书籍"""
        pass
