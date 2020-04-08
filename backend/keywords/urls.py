from django.urls import path
from .views import TagViewSet

tag_list = TagViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("", tag_list, name="tag-list"),
]
