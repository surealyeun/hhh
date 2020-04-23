from api import models, serializers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import DiningReviewSerializer


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



@api_view(['GET'])
def review_search(request, store_id):
    reviews = models.DiningReview.objects.filter(store_id=store_id)
    review_serializer = DiningReviewSerializer(reviews, many=True)
    return Response(review_serializer.data)