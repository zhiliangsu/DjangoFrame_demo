from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BookInfo
from .serializers import BookInfoSerializer


class BookListAPIView(GenericAPIView):
    """书籍的列表视图"""

    # 指定查询集(指定数据的来源)
    queryset = BookInfo.objects.all()
    # 指定序列化类(将来的数据转换或校验通过哪个序列化器)
    serializer_class = BookInfoSerializer

    def get(self, request):
        """获取所有图书"""

        # 1.获取查询集
        books = self.get_queryset()
        # 2.获取序列化器对象
        serializer = self.get_serializer(books, many=True)
        # 3.响应
        return Response(serializer.data)

# class BookListAPIView(APIView):
#     """使用APIView实现查询所有书籍接口"""
#
#     def get(self, request):
#         # 1.获取查询集
#         books = BookInfo.objects.all()
#         # 2.创建序列化器进行序列化
#         serializer = BookInfoSerializer(books, many=True)
#         # 3.响应
#         return Response(serializer.data)
