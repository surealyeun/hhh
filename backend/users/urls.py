from django.urls import path
from django.conf.urls import url

from users import views

urlpatterns = [
    url(r"", views.UserViewSet.as_view({"get": "list"}), name="movies"),
]
