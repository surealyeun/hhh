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

    # 한줄평.
    contents = models.CharField(max_length=100, help_text="최대 100자 까지 입력 가능합니다.")
    rating = models.IntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
