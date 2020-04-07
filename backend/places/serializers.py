from rest_framework import serializers
from .models import Store, Location, Review, Category


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store  # 모델 설정
        fields = "__all__"  # 필드 설정


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location  # 모델 설정
        fields = "__all__"  # 필드 설정


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # 모델 설정
        fields = "__all__"  # 필드 설정


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review  # 모델 설정
        fields = "__all__"  # 필드 설정
