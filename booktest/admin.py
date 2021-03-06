from django.contrib import admin

from .models import BookInfo, HeroInfo


# Register your models here.


class HeroInfoStackInline(admin.TabularInline):
    # class HeroInfoStackInline(admin.StackedInline):
    """关联显示数据"""
    model = HeroInfo  # 关联查询那个模型的数据
    # extra = 1  # 额外的编辑页面
    extra = 2  # 额外的编辑页面


# 定义模型站点管理类(管理模型数据在admin界面的展示)
class BookInfoAdmin(admin.ModelAdmin):
    # 修改每页显示的数据条数
    list_per_page = 2

    # 底部操作选项框
    actions_on_bottom = True

    list_display = ['btitle', 'id', 'bread', 'format_pub_date']

    # fields = ['btitle', 'bpub_date']  # 编辑界面可以修改字段

    fieldsets = [
        ['基础', {'fields': ['btitle', 'bpub_date', 'image']}],
        ['高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ['collapse']
        }]
    ]

    inlines = [HeroInfoStackInline]  # 关联数据展示'一关联显示多'


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    # list_per_page = 10

    list_display = ['id', 'hname', 'hcomment', 'hgender', 'is_delete', 'hbook', 'book_read']

    list_filter = ['hbook', 'hgender']  # 列表界面右边显示的过滤器

    search_fields = ['id', 'hname']  # 顶部搜索框


# 把要在admin界面中展示的模型添加/注册到admin站点
admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(HeroInfo)


admin.site.site_header = '传智书城'  # 首页头部标题
admin.site.site_title = '传智书城MIS'  # 标签页标题  首页欢迎页|标签页标题
admin.site.index_title = '欢迎使用传智书城MIS'  # 显示在头部标题下面的索引标题
