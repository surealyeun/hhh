from django.urls import path
from .views import StoreViewSet, LocationViewSet, CategoryViewSet, ReviewViewSet

store_list = StoreViewSet.as_view({"get": "list", "post": "create"})
location_list = LocationViewSet.as_view({"get": "list", "post": "create"})
category_list = CategoryViewSet.as_view({"get": "list", "post": "create"})
review_list = ReviewViewSet.as_view({"get": "list", "post": "create"})


urlpatterns = [
    path("store", store_list, name="store-list"),
    path("location", location_list, name="location-list"),
    path("category", category_list, name="category-list"),
    path("review", review_list, name="review-list"),
]
