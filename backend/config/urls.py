"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import users.views

router = routers.DefaultRouter()
router.register("users", users.views.UserViewSet)

schema_url_v1_patterns = [
    url("users/", include("users.urls", namespace="user_api")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="a202",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dlehfud22@naver.com"),
        license=openapi.License(name="BSD License"),
    ),
    validators=["flex", "ssv"],
    public=True,
    permission_classes=(AllowAny,),
)

# prefix = movies , viewset = MovieViewSet

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(router.urls)),
    url(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
