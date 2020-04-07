from django.db import models


class Follow(models.Model):

    """ Follow Model Definition """

    following = models.ManyToManyField("users.User", related_name="followed")
    followed = models.ManyToManyField("users.User", related_name="followers")
