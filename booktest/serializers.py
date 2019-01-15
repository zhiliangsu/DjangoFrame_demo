from rest_framework import serializers

from .models import BookInfo


# 定义序列化器
class BookModelSerializer(serializers.ModelSerializer):
    """定义序列化器类"""

    class Meta:
        model = BookInfo  # 将来序列化器中的字段从哪个模型中映射
        fields = '__all__'  # 映射模型中的哪些字段


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )

    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    # hbook = serializers.PrimaryKeyRelatedField(label='书籍', read_only=True)  # 只会序列化关联对象的主键
    # hbook = serializers.PrimaryKeyRelatedField(label='书籍', queryset=BookInfo.objects.all())
    # hbook = serializers.StringRelatedField(label='书籍')  # 序列化关联对象的__str__的返回值
    # hbook = BookInfoSerializer()  # 指定关联序列化器实例对象


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    # image = serializers.ImageField(label='图片', required=False)
    heroinfo_set = HeroInfoSerializer(many=True)
