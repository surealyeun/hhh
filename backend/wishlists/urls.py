from django.urls import path
from .views import WishlistViewSet

wishlist_list = WishlistViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("", wishlist_list, name="wishlist-list"),
]
