from django.urls import path
from .views import following_list, follower_list, follow, unfollow

urlpatterns = [
    path("following/<user_id>", following_list, name="following_list"),
    path("follower/<user_id>", follower_list, name="follower_list"),
    path("follow", follow, name="follow"),
    path("unfollow/<follower>/<followed>", unfollow, name="unfollow"),
]
