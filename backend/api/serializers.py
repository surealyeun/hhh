from .models import DiningStore
from rest_framework import serializers


class DiningStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningStore
        fields = [
            "id",
            "store_name",
            "branch",
            "area",
            "tel",
            "address",
            "latitude",
            "longitude",
            "category_list",
        ]
