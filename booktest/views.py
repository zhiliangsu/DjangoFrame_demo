from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BookInfo
from .serializers import BookInfoSerializer


class BookListAPIView(APIView):
    """使用APIView实现查询所有书籍接口"""

    def get(self, request):
        # 1.获取查询集
        books = BookInfo.objects.all()
        # 2.创建序列化器进行序列化
        serializer = BookInfoSerializer(books, many=True)
        # 3.响应
        return Response(serializer.data)
