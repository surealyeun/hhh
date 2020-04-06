from rest_framework import serializers
from .models import Location, Store


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location  # 모델 설정
        fields = "__all__"  # 필드 설정


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__alll__"
