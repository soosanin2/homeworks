from django.db import models
from user.models import User

class PublishingHouse(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)

    class Meta:
        db_table = 'publishing_house'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField(null=False)
    price = models.CharField(max_length=10)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'
