from django.urls import path
from api import views

from .views import (
    review_search
)
urlpatterns = [
    path('reviews/<store_id>/', review_search, name="review-search")
]
