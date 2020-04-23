from django.db import models
from core import models as core_models


class WishList(core_models.TimeStampedModel):

    """ WishList Model Definition """

    diningstore = models.ForeignKey("api.DiningStore", on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey("api.Location", on_delete=models.CASCADE, null=True, blank=True)    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}" + f"/{self.diningstore}" + f"/{self.location}"
