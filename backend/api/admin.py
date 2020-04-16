from django.contrib import admin
from . import models

@admin.register(models.DiningStore)
class DiningStoreAdmin(admin.ModelAdmin):
    pass

@admin.register(models.DiningReview)
class DiningReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    pass