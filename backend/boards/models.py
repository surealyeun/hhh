from django.db import models
from core import models as core_models


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definitinon """

    image = models.ImageField(upload_to="boards")

    def __str__(self):
        return str(self.created)


class Like(models.Model):

    """ Photo Model Definitinon """

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Board(core_models.TimeStampedModel):

    """ Board Model Definition """
    
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    address_gu = models.CharField(max_length=20, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    photo = models.ManyToManyField(Photo)
    like = models.ManyToManyField(Like, null=True, blank=True)

    def __str__(self):
        return str(self.writer) + ' | ' + self.address_gu +' | '+ self.content

    