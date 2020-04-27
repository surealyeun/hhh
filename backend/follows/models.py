from django.db import models


class Follow(models.Model):

    """ Follow Model Definition """

    following = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="followed", null=True)
    followed = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="following", null=True)

    def __str__(self):
        return self.following.username + ' ------> ' + self.followed.username
