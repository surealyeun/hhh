from django.urls import path
from .views import (
    UserViewSet, user_search, user_update_and_delete, login
)
urlpatterns = [
    path('users/detail/<username>/', user_search, name="user-search-by-name"),
    path('users/update/delete/<username>/', user_update_and_delete, name="user-update-delete"),
    path('login/<username>/<password>', login, name="login")
]
