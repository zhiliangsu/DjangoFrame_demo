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
try:
    BookInfo.objects.get(pk=30)
except BookInfo.DoesNotExist as e:
    print("Test:", e)
# booktest.models.DoesNotExist: BookInfo matching query does not exist.

BookInfo.objects.all()
BookInfo.objects.all().count()
