from rest_framework import viewsets
from .serializers import FollowSerializer
from .models import Follow


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
