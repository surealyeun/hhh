from rest_framework import serializers
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow  # 모델 설정
        fields = "__all__"  # 필드 설정
