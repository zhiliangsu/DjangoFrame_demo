from django.shortcuts import render

# Create your views here.
from booktest.models import BookInfo, HeroInfo

# 新增一本书
# book = BookInfo()
# book.btitle = '西游记'
# book.bpub_date = '1991-11-11'
# book.save()

book = BookInfo(
    btitle='西游记',
    bpub_date='1991-11-11'
)
book.save()


# 用create创建的时候,不用再调用save,创建的同时直接保存
hero = HeroInfo.objects.create(
    hname='白骨精',
    hbook=book,
    # hbook_id=book.id,
)
