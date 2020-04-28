from django.urls import path
from .views import following_list, follower_list

urlpatterns = [
    path("following/<user_id>", following_list, name="following_list"),
    path("follower/<user_id>", follower_list, name="follower_list"),
]
