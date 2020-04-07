from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag  # 모델 설정
        fields = "__all__"  # 필드 설정
