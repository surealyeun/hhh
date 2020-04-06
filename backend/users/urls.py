from django.urls import path
from .views import UserViewSet

<<<<<<< HEAD
from users import views

user_list = UserViewSet.as_view({"get": "list", "post": "create", "put": ""})

urlpatterns = [
    path("userList/", user_list, name="user-list"),
=======
user_list = UserViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = [
    path("", user_list, name="user-list"),
>>>>>>> ca75d17134016dc07f61d4a4c1fe226bba11ffd1
]
