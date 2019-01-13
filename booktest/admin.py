from django.contrib import admin

from .models import BookInfo, HeroInfo
# Register your models here.

# 把要在admin界面中展示的模型添加/注册到admin站点
admin.site.register(BookInfo)
admin.site.register(HeroInfo)


admin.site.site_header = '传智书城'  # 首页头部标题
admin.site.site_title = '传智书城MIS'  # 标签页标题  首页欢迎页|标签页标题
admin.site.index_title = '欢迎使用传智书城MIS'  # 显示在头部标题下面的索引标题
