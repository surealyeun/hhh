from django.urls import path
from .views import board_like_post, board_like_delete

urlpatterns = [
    path('board/like/post/<username>/<boardno>', board_like_post, name="board_like_post"),
    path('board/like/delete/<username>/<boardno>', board_like_delete, name="board_like_delete"),
]
