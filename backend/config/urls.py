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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .yasg import schema_view
<<<<<<< HEAD

from users.views import UserViewSet
from locations.views import LocationViewSet


router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"locations", LocationViewSet)
=======
from users.views import UserViewSet
from boards.views import BoardViewSet
from follows.views import FollowViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("boards", BoardViewSet)
router.register("follows", FollowViewSet)
>>>>>>> ca75d17134016dc07f61d4a4c1fe226bba11ffd1

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    url(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
