# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
