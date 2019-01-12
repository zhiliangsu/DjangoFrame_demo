from django.shortcuts import render

# Create your views here.
from booktest.models import BookInfo, HeroInfo

# 新增一本书
# book = BookInfo()
# book.btitle = '西游记'
# book.bpub_date = '1991-11-11'
# book.save()

# book = BookInfo(
#     btitle='西游记',
#     bpub_date='1991-11-11'
# )
# book.save()
#
#
# # 用create创建的时候,不用再调用save,创建的同时直接保存
# hero = HeroInfo.objects.create(
#     hname='白骨精',
#     hbook=book,
#     # hbook_id=book.id,
# )


"""
基本查询:
    get 查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
    all 查询多个结果。
    count 查询结果数量。
"""
# book = BookInfo.objects.get(id=5)
# book = BookInfo.objects.get(pk=3)
# try:
#     BookInfo.objects.get(pk=30)
# except BookInfo.DoesNotExist as e:
#     print("Test:", e)
# booktest.models.DoesNotExist: BookInfo matching query does not exist.

# BookInfo.objects.all()
# BookInfo.objects.all().count()


"""
过滤查询:
    实现SQL中的where功能，包括:
        filter 过滤出多个结果
        exclude 排除掉符合条件剩下的结果
        get 过滤单一结果
    对于过滤条件的使用，上述三个方法相同，故仅以filter进行讲解。

过滤条件的表达语法如下：
    属性名称__比较运算符=值
    # 属性名称和比较运算符间使用两个下划线，所以属性名不能包括多个下划线

"""
# 1.查询id为1的书籍
# BookInfo.objects.filter(id__exact=1)
BookInfo.objects.filter(id=1)

# 2.查询书名包含‘湖’的书籍
BookInfo.objects.filter(btitle__contains='湖')

# 3.查询书名以‘部’结尾的书籍 （endswith 、startswith）
BookInfo.objects.filter(btitle__endswith='部')

# 4.查询书名不为空的书籍
BookInfo.objects.filter(btitle__isnull=False)

# 5.查询编号为2和4的书籍
BookInfo.objects.filter(id__in=[2, 4])

# 6.查询编号大于2的书籍
# gt: >  gte: >=  lt: <  lte: <=
BookInfo.objects.filter(id__gt=2)

# 7.查询id不等于3的书籍
BookInfo.objects.exclude(id=3)

# 8.查询1980年发表的书籍
BookInfo.objects.filter(bpub_date__year=1980)

# 9.查询1990年1月1日后发表的书籍
BookInfo.objects.filter(bpub_date__gt='1990-1-1')
