from rest_framework import serializers

from .models import BookInfo


# 定义序列化器
class BookModelSerializer(serializers.ModelSerializer):
    """定义序列化器类"""

    class Meta:
        model = BookInfo  # 将来序列化器中的字段从哪个模型中映射
        fields = '__all__'  # 映射模型中的哪些字段


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    # image = serializers.ImageField(label='图片', required=False)
