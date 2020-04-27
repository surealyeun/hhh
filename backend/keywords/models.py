from django.db import models
from boards.models import Board


class Tag(models.Model):
    """ Tag model Definition """

    tag = models.CharField(max_length=20, null=False, blank=False)
    board = models.ManyToManyField(Board)
    store = models.ForeignKey("api.DiningStore", null=True, on_delete=models.CASCADE, blank=True)
    location = models.ForeignKey("api.Location", null=True, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.tag
