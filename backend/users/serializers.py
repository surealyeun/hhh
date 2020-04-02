from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = User  # 모델 설정
        fields = "__all__"  # 필드 설정
=======
        model = User
        fields = ("id", "password", "gender")
>>>>>>> d8e1b59a880684829564f5620ddd4324becd2b14
