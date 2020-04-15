from django.utils import timezone
from django.db import models

class DiningStore(models.Model):
    id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20, null=True)
    area = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(max_length=10, null=True)
    longitude = models.FloatField(max_length=10, null=True)
    category = models.CharField(max_length=200, null=True)

    @property
    def category_list(self):
        return self.category.split("|") if self.category else []

class DiningReview(models.Model):
    review_id = models.IntegerField(null=True)
    store = models.ForeignKey("DiningStore", on_delete=models.CASCADE, null=True)
    dining_user = models.IntegerField(null=True)
    score = models.IntegerField(null=True)
    content = models.TextField(null=True)
    reg_time = models.DateTimeField(null=True)

    class Meta:
        unique_together = (('store', 'review_id'),)
