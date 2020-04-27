from django.db import models
from users.models import User


class Category(models.Model):
    """" 가게 유형 """

    type = models.CharField(max_length=20, verbose_name="가게 유형")


class Store(models.Model):

    """ 특정 건물을 규정 """

    name = models.CharField(max_length=100, verbose_name="가게명")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Location(models.Model):
    """ 특정 장소를 규정 """

    name = models.CharField(max_length=100, verbose_name="장소명")
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Review(models.Model):
    """ 평가 모델 """

    score = models.IntegerField(default=0)
    store = models.ForeignKey("api.DiningStore", on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey("api.Location", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    
    def __str__(self):
        if self.store is None:
            return self.user.username+' | '+self.location.location_name+' | '+str(self.score)
        else :
            return self.user.username+' | '+self.store.store_name+' | '+str(self.score)
