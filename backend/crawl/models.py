from django.db import models
from backend.api import models as api

# Create your models here.
class Sense(models.Model):
    
    """ 소셜 트랜드 분석 """
    FEEL_POSITIVE = "긍정"
    FEEL_NEUTRAL = "중립"
    FEEL_NEGATIVE = "부정"

    FEEL_CHOICES = (
        (FEEL_POSITIVE, "긍정"),
        (FEEL_NEUTRAL, "중립"),
        (FEEL_NEGATIVE, "부정"),
    )

    ftype = models.CharField(choice = FEEL_CHOICES, max_length=10, null=False, blank=False)
    word = models.TextField()
    rank = models.IntegerField()
    store = models.ForeignKey("api.DiningStore", verbose_name=(""), on_delete=models.CASCADE)

    def __str__(self):
        return self


class StoreImg(models.Model):

    """ 이미지 저장 모델 """

    #location ..?
    store = models.ForeignKey("api.DiningStore", on_delete=models.CASCADE)
    src = models.TextField()


class LocationImg(models.Model):

    location = models.ForeignKey("api.DiningLocation", on_delete=models.CASCADE)
    src = models.TextField()