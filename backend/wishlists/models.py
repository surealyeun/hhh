from django.db import models
from core import models as core_models


class WishList(core_models.TimeStampedModel):

    """ WishList Model Definition """

    store = models.ForeignKey("places.Store", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store}, {self.user}"
