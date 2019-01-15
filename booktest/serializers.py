from rest_framework import serializers

from .models import BookInfo


# 定义序列化器
class BookModelSerializer(serializers.ModelSerializer):
    """定义序列化器类"""
    class Meta:
        model = BookInfo  # 将来序列化器中的字段从哪个模型中映射
        fields = '__all__'  # 映射模型中的哪些字段
