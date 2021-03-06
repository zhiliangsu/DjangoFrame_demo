from django.shortcuts import render

# Create your views here.
from booktest.models import BookInfo, HeroInfo
from django.db.models import F, Q, Sum

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


"""
F对象和Q对象
    如果需要做两个字段进行比较就要用F --> F(属性名)
    Q对象可以做逻辑运算符 and  or  not  可以做基本查询 也可以 or 或 not --> Q(属性名__运算符=值)
"""
# F对象
# 1.查询阅读量大于评论量的书籍
BookInfo.objects.filter(bread__gt=F('bcomment'))

# 2.查询阅读量大于2倍评论量的书籍
BookInfo.objects.filter(bread__gt=F('bcomment') * 2)

# Q对象
# BookInfo.objects.filter(bread__gt=20, id__lte=3)  # and表示两个条件都满足的菜肴
# BookInfo.objects.filter(Q(bread__gt=20), Q(id__lte=3))
# BookInfo.objects.filter(bread__gt=20).filter(id__lte=3)

# 1.查询阅读量大于20，或编号小于3的图书
BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))  # or满足其中一个条件的就要

# 2.查询编号不等于3的书籍
BookInfo.objects.filter(~Q(id=3))


"""
基础关联查询:
    一查多: 用book去查hero
        第一步先拿到一: book
        第二步完成一查多: 一的模型实例对象.多的模型名字小写_set --> book.heroinfo_set
        <只要给多的一方指定外键,那么在一的一方就会隐式生成一个隐藏字段: 多的一方模型名小写_set -->heroinfo_set>
    多查一:
        第一步先拿到多的这一方的某个模型对象: hero
        第二步 --> hero.hbook
"""
# 1.一查多：查询编号为1的图书中所有人物信息
# book = BookInfo.objects.get(id=1)
# book.heroinfo_set.all()

# 2.多查一：查询编号为1的英雄出自的书籍
# hero = HeroInfo.objects.get(id=1)
# hero.hbook


"""关联过滤/内联查询"""
# 一查多: 查谁就是谁的模型类对象开头.objects.filter(外键名__属性名__运算符=值)
# HeroInfo.objects.filter(hbook__btitle="天龙八部")
"""
在关联过滤查询时多的一方当条件时,只用写多的一方模型名小写就可以了,不用再加_set
_set是在关联基本查询时,用一查多才需要用
"""
# 多查一: 用一这方的模型对象.objects.filter(多的那一方的模型名小写__属性名__运算符=值)
# BookInfo.objects.filter(heroinfo__hcomment__contains='降龙')

# 关联过滤查询
# 1.多查一：查询书籍中人物的描述包含"降龙"的书籍
BookInfo.objects.filter(heroinfo__hcomment__contains="降龙")

# 2.一查多：查询书名为"天龙八部"的所有人物信息
# HeroInfo.objects.filter(hbook__btitle__exact="天龙八部")
HeroInfo.objects.filter(hbook__btitle="天龙八部")


"""聚合函数和排序"""
# 只能对QuerySet类型的东西进行排序
BookInfo.objects.all().order_by('bread')  # 默认升序
BookInfo.objects.all().order_by('-bread')  # 降序

BookInfo.objects.aggregate(Sum('bread'))


"""数据修改"""
# book = BookInfo.objects.get(btitle='西游记')
# book.btitle = '西游记<后传>'
# book.save()

# BookInfo.objects.filter(id=5).update(btitle='西游记<起源>')


"""数据删除"""
book = BookInfo.objects.get(id=5)
book.delete()

HeroInfo.objects.filter(id=18).delete()

qs = BookInfo.objects.all()
# qs1 = BookInfo.objects.all()
