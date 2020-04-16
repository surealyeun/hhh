from api import models, serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class DiningStoreViewSet(viewsets.ModelViewSet):
    queryset = models.DiningStore.objects.all()
    serializer_class = serializers.DiningStoreSerializer
    pagination_class = SmallPagination

class DiningReviewViewSet(viewsets.ModelViewSet):
    queryset = models.DiningReview.objects.all()
    serializer_class = serializers.DiningReviewSerializer
    pagination_class = SmallPagination

class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    pagination_class = SmallPagination