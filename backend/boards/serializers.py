from rest_framework import serializers
from .models import Board, Like


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board  # 모델 설정
        fields = "__all__"  # 필드 설정

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like  # 모델 설정
        fields = "__all__"  # 필드 설정
