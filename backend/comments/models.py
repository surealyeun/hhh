from django.db import models
from core import models as core_models


class Comment(core_models.TimeStampedModel):

    """ Comment Model Definition """

    comment = models.CharField(max_length=120)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    board = models.ForeignKey("boards.Board", on_delete=models.CASCADE)
    like = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )
