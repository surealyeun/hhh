from django.urls import path
from .views import board_like_post, board_like_delete, board_delete, board_post, comment_post
urlpatterns = [
    path('comment/post/<boardno>/<userid>/<text>', comment_post, name="comment_post"),
    path('board/post', board_post, name="board_post"),
    path('board/like/post/<username>/<boardno>', board_like_post, name="board_like_post"),
    path('board/like/delete/<username>/<boardno>', board_like_delete, name="board_like_delete"),
    path('boards/delete/<boardno>', board_delete, name="board_delete"),
]
