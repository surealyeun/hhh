from django.db import models
from boards.models import Board

# Create your models here.
class Tag(models.Model):

    """ Tag model Definition """

    tag = models.CharField(max_length=20, null=False, blank=False)
    board = models.ManyToManyField(Board)
