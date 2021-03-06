import json

from django.forms import model_to_dict
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
        # 1.提取前端传入要新增的数据
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        json_dict = json.loads(json_str)

        # 除了自己的数据可以不用验证,其他人给的所有数据在使用之前必须校验
        # 2.把数据存储到表中
        book = BookInfo.objects.create(
            btitle=json_dict.get('btitle'),
            bpub_date=json_dict.get('bpub_date')
        )

        # 3.把模型转换成字典
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'is_delete': book.is_delete,
            'image': book.image.url if book.image else ''
        }

        # 返回
        return JsonResponse(book_dict, status=201)


class BookDetailView(View):
    """详情视图: 带pk"""

    def get(self, request, pk):
        """查询某本书籍"""

        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'message': 'pk不存在'}, status=404)
        # 查出指定pk的数据
        # querySet如何转成字典对象?
        # book = BookInfo.objects.filter(id=pk)
        # if not book:
        #     return HttpResponse({'message': 'pk不存在'}, status=404)

        # 字典转换模型
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'is_delete': book.is_delete,
            'image': book.image.url if book.image else ''
        }
        # 响应
        return JsonResponse(book_dict)

    def put(self, request, pk):
        """修改指定的某本书籍"""
        # 提取前端请求数据
        json_str_bytes = request.body
        json_str = json_str_bytes.decode()
        json_dict = json.loads(json_str)
        # 获取到要修改的模型对象
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'message': 'pk不存在'}, status=404)

        # 修改模型对象
        book.btitle = json_dict.get('btitle')
        book.bpub_date = json_dict.get('bpub_date')
        book.save()

        # 字典转换模型
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'is_delete': book.is_delete,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(book_dict, status=200)

    def delete(self, request, pk):
        """删除指定的某本书籍"""
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'message': 'pk不存在'}, status=404)

        # 删除指定数据
        book.delete()

        # 响应
        return HttpResponse(status=204)
