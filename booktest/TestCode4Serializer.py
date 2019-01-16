from rest_framework import viewsets
# from .models import BookInfo
# from .serializers import BookModelSerializer
#
#
# class BookAPIViewSet(viewsets.ModelViewSet):
#     """定义模型视图集"""
#     # 1.指定查询集
#     queryset = BookInfo.objects.all()
#     # 2.指定序列化器(帮我们进行序列化或反序列化)
#     serializer_class = BookModelSerializer


from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
from booktest.models import BookInfo, HeroInfo

"""序列化单个模型对象"""
# book = BookInfo.objects.get(id=1)
# serializer = BookInfoSerializer(instance=book)
# serializer.data

"""序列化查询集"""
# 如果要序列化的是一个查询集时,要指定many=True
# books = BookInfo.objects.all()
# # instance除了可以传单个模型对象,查询集,还可以传字典
# # {'price': 20, 'books': books}
# serializer = BookInfoSerializer(instance=books, many=True)
# serializer.data


"""关联序列化"""
# hero = HeroInfo.objects.get(id=1)
# s = HeroInfoSerializer(hero)
# s.data


"""反序列化"""
"""
    1>获取前端传入的json数据
    2>创建序列化器对象进行反序列化操作 反序列化时创建序列化器对象需要给data参数传递数据, 要以关键字参数方法传递
    3>使用序列化对象调用is_valid() 方法做数据的校验
    4>如果校验后想拿到校验成功的数据用序列化器对象.validated_data
    5>如果要把校验后的数据存储到(新增和修改)数据用序列化器对象.save()方法
"""

# data_dict = {
#     'btitle': '小三国django',
#     'bpub_date': '1990-11-11'
# }
#
# book = BookInfo.objects.get(id=11)
#
# # raise_exception=True 如果在执行is_valid时校验出错直接抛出异常
# s = BookInfoSerializer(instance=book, data=data_dict)
# s.is_valid(raise_exception=True)
# # s.validated_data
# # 在调用序列化器的save时如果instance参数也传递了,就会调用序列化器的update操作
# # 如果调用序列化器的save时只传递了data,那么就会调用序列化器的create方法
# s.save()  # 有可能是新增操作,也有可能是修改操作
