from django.db import models

# Create your models here.
class StoreSense(models.Model):
    
    """ 소셜 트랜드 분석 """
    # FEEL_POSITIVE = "긍정"
    # FEEL_NEUTRAL = "중립"
    # FEEL_NEGATIVE = "부정"

    # FEEL_CHOICES = (
    #     (FEEL_POSITIVE, "긍정"),
    #     (FEEL_NEUTRAL, "중립"),
    #     (FEEL_NEGATIVE, "부정"),
    # )

    ftype = models.CharField(max_length=10, null=False, blank=False)
    word = models.CharField(max_length=100)
    rank = models.IntegerField()
    store = models.ForeignKey("api.DiningStore", verbose_name=(""), on_delete=models.CASCADE)

    def __str__(self):
        return self


class LocationSense(models.Model):

    ftype = models.CharField(max_length=10, null=False, blank=False)
    word = models.CharField(max_length=100)
    rank = models.IntegerField()
    location = models.ForeignKey("api.Location", verbose_name=(""), on_delete=models.CASCADE)


class DistrctSense(models.Model):

    ftype = models.CharField(max_length=10, null=False, blank=False)
    word = models.CharField(max_length=100)
    rank = models.IntegerField()
    district = models.CharField(max_length=20, null=False, blank=False)


class StoreImg(models.Model):

    """ 이미지 저장 모델 """

    #location ..?
    store = models.ForeignKey("api.DiningStore", on_delete=models.CASCADE)
    src = models.TextField()


class LocationImg(models.Model):

    location = models.ForeignKey("api.Location", on_delete=models.CASCADE)
    src = models.TextField()