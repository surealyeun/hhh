from django.urls import path
from .views import (
    UserViewSet, user_search, user_search_by_id, user_update_and_delete, login, user_follow_feedlist, user_feedlist, recommend_location_list,
    wishlist_store, wishlist_location,store_detail,location_detail
)
urlpatterns = [
    path('wishlist/store/<store_id>/<username>/<score>', wishlist_store, name="wishlist_store"),
    path('wishlist/location/<location_id>/<username>/<score>', wishlist_location, name="wishlist_location"),
    path('users/detail/<username>/', user_search, name="user-search-by-name"),
    path('users/detail/id/<user_id>/', user_search_by_id, name="user_search_by_id"),
    path('users/update/delete/<username>/', user_update_and_delete, name="user-update-delete"),
    path('login/<username>/<password>', login, name="login"),
    path('feedlist/follow/<username>', user_follow_feedlist, name='user_follow_feedlist'),
    path('feedlist/user/<user_name>', user_feedlist, name='user_feedlist'),
    path('recommend/<area_gu>/<username>', recommend_location_list, name="recommend_location"),
    path('recommend/<area_gu>', recommend_location_list, name="recommend_location"),
    path('store/detail/<store_id>', store_detail, name="store_detail"),
    path('location/detail/<location_id>', location_detail, name="location_detail"),
]
