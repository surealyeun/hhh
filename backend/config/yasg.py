from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi


schema_url_patterns = [
    path("users/", include("users.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="a202 Open API",
        default_version="v1",
        description="SSAFY 특화프로젝트 서울 2반 2조.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="opwer032@naver.com"),
        license=openapi.License(name="우리조 화이팅"),
    ),
    validators=["flex", "ssv"],
    public=True,
    permission_classes=(AllowAny,),
)
