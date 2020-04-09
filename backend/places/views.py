# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    StoreSerializer,
    CategorySerializer,
    LocationSerializer,
    ReviewSerializer,
)
from .models import Store, Category, Location, Review


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
