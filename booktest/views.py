from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework import status

from .models import BookInfo
from .serializers import BookInfoSerializer


class BookViewSet(ReadOnlyModelViewSet):
    """查询的视图集"""

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def latest(self, request):
        """返回最新的图书信息"""

        book = BookInfo.objects.latest('id')
        serializer = BookInfoSerializer(book)
        return Response(serializer.data)

    def read(self, request, pk):
        """修改图书的阅读量数据"""
        book = self.get_object()
        book.read = request.data.get('bread')
        book.save()
        serializer = BookInfoSerializer(book)
        return Response(serializer.data)


#  class BookViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
#
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


# class BookViewSet(ViewSet):
#     """基本视图集"""
#
#     def list(self, request):
#         books = BookInfo.objects.all()
#         serializer = BookInfoSerializer(books, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = BookInfoSerializer(book)
#         return Response(serializer.data)


# class BookListAPIView(ListAPIView, CreateAPIView):
#     """书籍的列表视图"""
#
#     # 指定查询集(指定数据的来源)
#     queryset = BookInfo.objects.all()
#     # 指定序列化类(将来的数据转换或校验通过哪个序列化器)
#     serializer_class = BookInfoSerializer
#
#
# class BookDetailAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
#     """书籍的详情视图"""
#
#     # 指定查询集(指定数据的来源)
#     queryset = BookInfo.objects.all()
#     # 指定序列化类(将来的数据转换或校验通过哪个序列化器)
#     serializer_class = BookInfoSerializer


# class BookListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     """书籍的列表视图"""
#
#     # 指定查询集(指定数据的来源)
#     queryset = BookInfo.objects.all()
#     # 指定序列化类(将来的数据转换或校验通过哪个序列化器)
#     serializer_class = BookInfoSerializer
#
#     def get(self, request):
#         """获取所有图书"""
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class BookDetailAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     """书籍的详情视图"""
#
#     # 指定查询集(指定数据的来源)
#     queryset = BookInfo.objects.all()
#     # 指定序列化类(将来的数据转换或校验通过哪个序列化器)
#     serializer_class = BookInfoSerializer
#
#     def get(self, request, pk):
#         """查询单一图书数据"""
#         return self.retrieve(request)
#
#     def put(self, request, pk):
#         return self.update(request)
#
#     def delete(self, request, pk):
#         return self.destroy(request)


# class BookListAPIView(GenericAPIView):
#     """书籍的列表视图"""
#
#     # 指定查询集(指定数据的来源)
#     queryset = BookInfo.objects.all()
#     # 指定序列化类(将来的数据转换或校验通过哪个序列化器)
#     serializer_class = BookInfoSerializer
#
#     def get(self, request):
#         """获取所有图书"""
#
#         # 1.获取查询集
#         books = self.get_queryset()
#         # 2.获取序列化器对象
#         serializer = self.get_serializer(books, many=True)
#         # 3.响应
#         return Response(serializer.data)
#
#
# class BookDetailAPIView(GenericAPIView):
#     """书籍的详情视图"""
#
#     # 指定查询集(指定数据的来源)
#     queryset = BookInfo.objects.all()
#     # 指定序列化类(将来的数据转换或校验通过哪个序列化器)
#     serializer_class = BookInfoSerializer
#
#     def get(self, request, pk):
#         """查询单一图书数据"""
#
#         # 1.获取单一模型对象
#         book = self.get_object()
#         # 2.获取序列化器对象
#         serializer = self.get_serializer(book)
#         # 3.响应
#         return Response(serializer.data)


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
