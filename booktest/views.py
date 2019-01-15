from rest_framework import viewsets

from .models import BookInfo
from .serializers import BookModelSerializer


class BookAPIViewSet(viewsets.ModelViewSet):
    """定义模型视图集"""
    # 1.指定查询集
    queryset = BookInfo.objects.all()
    # 2.指定序列化器(帮我们进行序列化或反序列化)
    serializer_class = BookModelSerializer
