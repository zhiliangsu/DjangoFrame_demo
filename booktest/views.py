from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import BookInfo, HeroInfo

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
        # 1.先把所有书籍查出来
        books = BookInfo.objects.all()

        # 2.把查询集中的模型对象转换成一个一个的字段
        book_list = []
        for book in books if books else []:
            book_dict = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'is_delete': book.is_delete,
                'image': book.image.url if book.image else ''
            }
            book_list.append(book_dict)

        # 注意返回的是一个字典,需要设置safe=True
        return JsonResponse(book_list, safe=False)

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
