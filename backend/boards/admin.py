from django.contrib import admin
from . import models


@admin.register(models.Board)
class BoradAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    class Media:
        js = ('jquery.js', 'inlines.js')

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    pass