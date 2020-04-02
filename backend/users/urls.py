from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import views

schema_view = get_schema_view(openapi.Info(title="User API", default_version="v1",))

app_name = "users"

url_patterns = [
    path("userList/", views.user_list, name="user_list"),
]
