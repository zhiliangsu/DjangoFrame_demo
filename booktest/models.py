# Create your models here.
from django.db import models


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    """
    ImageField: 
        1.可以帮我们在admin站点生成上传文件的表单界面
        2.上传图片的功能
    upload_to: 上传的文件存储在MEDIA_ROOT指定路径中的子目录
    null=True: 如果模型字段是后追加的必须给它设置默认值,或设置可以为null,否则迁移会报错
    """
    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle

    def format_pub_date(self):  # 1990-1-1
        return self.bpub_date.strftime('%Y-%m-%d')

    format_pub_date.short_description = '发布日期'  # 修改方法名字在站点列表界面的显示名称
    format_pub_date.admin_order_field = 'bpub_date'  # 指定此方法中的数据依据哪个字段进行排序


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    def book_read(self):
        return self.hbook.bread

    book_read.short_description = '图书阅读量'
    book_read.admin_order_field = 'hbook__bread'

