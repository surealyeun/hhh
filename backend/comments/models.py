from django.db import models
from core import models as core_models


class Comment(core_models.TimeStampedModel):

    """ Comment Model Definition """

    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=120)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    board = models.ForeignKey("boards.Board", on_delete=models.CASCADE)

    def __str__(self):
        return self.board.content+' | '+ self.writer.username + ' | '+self.text