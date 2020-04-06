from django.urls import path
from django.conf.urls import url
from .views import LocationViewSet, StoreViewSet

from locations import views

location_list = LocationViewSet.as_view({"get": "list", "post": "create", "put": ""})

urlpatterns = [
    path("locationList/", location_list, name="location-list"),
]
