from django.db import models
from core import models as core_models

class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)

class Photo(core_models.TimeStampedModel):

    """ Photo Model Definitinon """

    image = models.ImageField(upload_to="boards")

    def __str__(self):
        return str(self.image)


class Like(models.Model):

    """ Like Model Definitinon """

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    board = models.ForeignKey("Board", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username + ' | ' + str(self.board.content)


class Board(core_models.TimeStampedModel):

    """ Board Model Definition """
    
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    address_gu = models.CharField(max_length=20, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    photo = models.ManyToManyField(Photo)
    store = models.ForeignKey("api.DiningStore", on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey("api.Location", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.writer) + ' | ' + self.address_gu +' | '+ self.content

    