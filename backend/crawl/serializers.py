from rest_framework import serializers
from .models import StoreImg, LocationImg


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 모델 설정
        fields = "__all__"  # 필드 설정
