# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_object(self, request, id):
        queryset = User.objects.get(pk=id)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
