from rest_framework import viewsets

from .models import BookInfo
from .serializers import BookModelSerializer


class BookAPIViewSet(viewsets.ModelViewSet):
    """定义模型视图集"""
    # 1.指定查询集
    queryset = BookInfo.objects.all()
    # 2.指定序列化器(帮我们进行序列化或反序列化)
    serializer_class = BookModelSerializer


from booktest.serializers import BookInfoSerializer
from booktest.models import BookInfo, HeroInfo


"""序列化单个模型对象"""
# book = BookInfo.objects.get(id=1)
# serializer = BookInfoSerializer(instance=book)
# serializer.data

"""序列化查询集"""
# 如果要序列化的是一个查询集时,要指定many=True
books = BookInfo.objects.all()
# instance除了可以传单个模型对象,查询集,还可以传字典
# {'price': 20, 'books': books}
serializer = BookInfoSerializer(instance=books, many=True)
serializer.data
