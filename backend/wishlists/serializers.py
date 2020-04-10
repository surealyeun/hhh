from rest_framework import serializers
from .models import WishList


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = "__all__"
