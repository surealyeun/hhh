from django.db import models
from boards.models import Board
from places.models import Store, Location


class Tag(models.Model):
    """ Tag model Definition """

    tag = models.CharField(max_length=20, null=False, blank=False)
    board = models.ManyToManyField(Board)
    store = models.ForeignKey(Store, null=True)
    location = models.ForeignKey(Location, null=True)
