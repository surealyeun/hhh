from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter(trailing_slash=False)
router.register(r"stores", views.DiningStoreViewSet, basename="stores")

urlpatterns = router.urls
