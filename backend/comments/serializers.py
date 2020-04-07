from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  # 모델 설정
        fields = "__all__"  # 필드 설정
