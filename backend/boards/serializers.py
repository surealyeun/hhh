from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board  # 모델 설정
        fields = "__all__"  # 필드 설정
