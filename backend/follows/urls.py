from django.urls import path
from .views import FollowViewSet

follow_list = FollowViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("", follow_list, name="follow-list"),
]
