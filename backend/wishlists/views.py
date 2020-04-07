from rest_framework import viewsets
from .serializers import WishlistSerializer
from .models import WishList


class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishlistSerializer
