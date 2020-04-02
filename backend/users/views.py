from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


@api_view(["GET"])
def user_list(request):
    Users = User.objects.all()
    context = {
        "users": Users,
    }
    # return render() -> .html 페이지를 응답으로 보내주기
    serializer = UserSerializer(Users, many=True)
    return Response(serializer.data)
