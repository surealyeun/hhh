from django.urls import path
from .views import BoardViewSet

board_list = BoardViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("", board_list, name="board-list"),
]
